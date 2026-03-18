"""Requirements parsing module for CSV Documentation Generator

Parses source code to extract requirements, detects electronic signature needs,
and manages the requirements database.
"""

import os
import re
import json
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class Requirement:
    """Represents a single requirement"""

    id: str
    type: str  # URS, FS, TS
    description: str
    priority: str  # 必须, 应该, 可以
    source_file: Optional[str] = None
    source_line: Optional[int] = None
    esig_required: bool = False
    esig_category: Optional[str] = None
    tags: List[str] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    status: str = "draft"  # draft, verified, failed

    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if not self.created_at:
            self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()


class RequirementsParser:
    """Parse source code to extract requirements"""

    # Comment patterns for requirement markers
    COMMENT_PATTERNS = [
        r"@req\s+(?:(\w+-\d+)\s+)?(.+)",  # @req URS-001 description
        r"@requirement\s+(?:(\w+-\d+)\s+)?(.+)",  # @requirement
        r"#\s*(\w+-\d+)[:\s]+(.+)",  # URS-001: description
        r"#\s*\[(\w+-\d+)\]\s*(.+)",  # [URS-001] description
        r"<!--\s*(\w+-\d+)\s+(.+)-->",  # HTML comment style
    ]

    # Priority keywords
    PRIORITY_KEYWORDS = {
        "必须": "必须",
        "must": "必须",
        "required": "必须",
        "应该": "应该",
        "should": "应该",
        "建议": "应该",
        "可以": "可以",
        "could": "可以",
        "may": "可以",
    }

    # eSignature related keywords (configurable)
    ESIG_KEYWORDS = [
        # Chinese
        "签名",
        "签字",
        "签署",
        "电子签名",
        "签章",
        "审核",
        "审批",
        "批准",
        "核验",
        "确认",
        "电子记录",
        "record",
        "approval",
        # English
        "sign",
        "signature",
        "signing",
        "review",
        "approve",
        "authorize",
        "electronic signature",
        "e-sign",
        "digital signature",
        "certified",
    ]

    # eSignature categories
    ESIG_CATEGORIES = {
        "workflow_approval": ["审核", "审批", "批准", "review", "approve", "authorize"],
        "document_signing": ["签名", "sign", "signature", "签署"],
        "record_confirmation": ["确认", "核验", "confirm", "verify"],
        "data_certification": ["认证", "证明", "certify", "certificate"],
    }

    def __init__(
        self, project_path: Optional[Path] = None, config: Optional[Dict] = None
    ):
        self.project_path = project_path or Path.cwd()
        self.config = config or {}
        self.requirements_db = self._load_requirements_db()
        self._load_esig_keywords()

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration"""
        config_path = self.project_path / ".csv-docs-config.json"
        if config_path.exists():
            with open(config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def _load_esig_keywords(self):
        """Load eSignature keywords from config"""
        compliance_config = self.config.get("compliance", {})
        configured_keywords = compliance_config.get("esig_keywords", [])
        if configured_keywords:
            self.ESIG_KEYWORDS = configured_keywords

    def _load_requirements_db(self) -> Dict[str, Any]:
        """Load requirements database"""
        db_path = self.project_path / "requirements.json"
        if db_path.exists():
            with open(db_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {
            "version": "1.0",
            "requirements": [],
            "risks": [],
            "test_results": [],
            "commit_links": [],
        }

    def _save_requirements_db(self):
        """Save requirements database"""
        db_path = self.project_path / "requirements.json"
        with open(db_path, "w", encoding="utf-8") as f:
            json.dump(self.requirements_db, f, indent=2, ensure_ascii=False)

    def _generate_id(self, req_type: str) -> str:
        """Generate next available ID for requirement type"""
        existing = [
            r
            for r in self.requirements_db.get("requirements", [])
            if r.get("id", "").startswith(f"{req_type}-")
        ]

        max_num = 0
        for r in existing:
            try:
                num = int(r["id"].split("-")[1])
                max_num = max(max_num, num)
            except (ValueError, IndexError):
                continue

        return f"{req_type}-{max_num + 1:03d}"

    def _detect_esig(self, text: str) -> Tuple[bool, Optional[str]]:
        """Detect if text relates to electronic signature"""
        text_lower = text.lower()
        for category, keywords in self.ESIG_CATEGORIES.items():
            for keyword in keywords:
                if keyword.lower() in text_lower:
                    return True, category
        return False, None

    def _extract_priority(self, text: str) -> str:
        """Extract priority from text"""
        text_lower = text.lower()
        for keyword, priority in self.PRIORITY_KEYWORDS.items():
            if keyword.lower() in text_lower:
                return priority
        return "应该"  # Default

    def _parse_requirement_from_match(
        self, match: re.Match, file_path: str, line_num: int
    ) -> Optional[Requirement]:
        """Parse a requirement from regex match"""
        groups = match.groups()

        # Try to extract ID and description
        if len(groups) == 2:
            req_id = groups[0]
            description = groups[1]
        elif len(groups) == 1:
            req_id = None
            description = groups[0]
        else:
            return None

        if not description or len(description.strip()) < 3:
            return None

        # Determine type from ID or file analysis
        req_type = "URS"  # Default
        if req_id:
            prefix = req_id.split("-")[0] if "-" in req_id else req_id[:3]
            if prefix.upper() in ["URS", "FS", "TS"]:
                req_type = prefix.upper()
        else:
            # Infer from file path
            path_lower = file_path.lower()
            if "test" in path_lower or "_test" in path_lower:
                req_type = "TS"
            elif "spec" in path_lower or "feature" in path_lower:
                req_type = "FS"

        # Generate ID if not provided
        if not req_id:
            req_id = self._generate_id(req_type)

        # Extract priority
        priority = self._extract_priority(description)

        # Detect eSignature requirement
        esig_required, esig_category = self._detect_esig(description)

        return Requirement(
            id=req_id,
            type=req_type,
            description=description.strip(),
            priority=priority,
            source_file=file_path,
            source_line=line_num,
            esig_required=esig_required,
            esig_category=esig_category,
            status="draft",
        )

    def parse_file(self, file_path: Path) -> List[Requirement]:
        """Parse a single file for requirements"""
        requirements = []

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except (UnicodeDecodeError, IOError):
            return requirements

        for line_num, line in enumerate(lines, 1):
            for pattern in self.COMMENT_PATTERNS:
                matches = re.finditer(pattern, line, re.IGNORECASE)
                for match in matches:
                    req = self._parse_requirement_from_match(
                        match, str(file_path), line_num
                    )
                    if req:
                        requirements.append(req)
                        break  # One match per line is enough

        return requirements

    def parse_directory(
        self, directory: Path, extensions: List[str] = None
    ) -> List[Requirement]:
        """Parse all files in a directory"""
        if extensions is None:
            extensions = [".py", ".js", ".ts", ".java", ".cs", ".go", ".rs"]

        all_requirements = []

        for ext in extensions:
            for file_path in directory.rglob(f"*{ext}"):
                # Skip common non-source directories
                skip_dirs = [
                    "node_modules",
                    ".venv",
                    "venv",
                    "__pycache__",
                    ".git",
                    "test",
                    "tests",
                ]
                if any(skip in file_path.parts for skip in skip_dirs):
                    continue

                requirements = self.parse_file(file_path)
                all_requirements.extend(requirements)

        return all_requirements

    def add_requirement(
        self,
        description: str,
        req_type: str = "URS",
        priority: str = None,
        source_file: str = None,
        source_line: int = None,
    ) -> Requirement:
        """Manually add a requirement"""
        esig_required, esig_category = self._detect_esig(description)

        if not priority:
            priority = self._extract_priority(description)

        req_id = self._generate_id(req_type)

        requirement = Requirement(
            id=req_id,
            type=req_type,
            description=description,
            priority=priority,
            source_file=source_file,
            source_line=source_line,
            esig_required=esig_required,
            esig_category=esig_category,
            status="draft",
        )

        self.requirements_db.setdefault("requirements", []).append(asdict(requirement))
        self._save_requirements_db()

        return requirement

    def get_requirements(
        self,
        req_type: Optional[str] = None,
        esig_only: bool = False,
        status: Optional[str] = None,
    ) -> List[Requirement]:
        """Get requirements with optional filters"""
        requirements = [
            Requirement(**r) for r in self.requirements_db.get("requirements", [])
        ]

        if req_type:
            requirements = [r for r in requirements if r.type == req_type]

        if esig_only:
            requirements = [r for r in requirements if r.esig_required]

        if status:
            requirements = [r for r in requirements if r.status == status]

        return requirements

    def update_requirement(self, req_id: str, **kwargs) -> bool:
        """Update a requirement by ID"""
        for req in self.requirements_db.get("requirements", []):
            if req.get("id") == req_id:
                req.update(kwargs)
                req["updated_at"] = datetime.now().isoformat()
                self._save_requirements_db()
                return True
        return False

    def delete_requirement(self, req_id: str) -> bool:
        """Delete a requirement by ID"""
        requirements = self.requirements_db.get("requirements", [])
        for i, req in enumerate(requirements):
            if req.get("id") == req_id:
                requirements.pop(i)
                self._save_requirements_db()
                return True
        return False

    def get_esig_requirements(self) -> List[Requirement]:
        """Get all requirements that require electronic signature"""
        return self.get_requirements(esig_only=True)

    def get_next_id(self, req_type: str = "URS") -> str:
        """Get the next available ID for a requirement type"""
        return self._generate_id(req_type)
