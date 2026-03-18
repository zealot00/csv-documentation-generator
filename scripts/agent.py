"""Agent detection module for CSV Documentation Generator

Detects the current AI agent type and determines the appropriate mode:
- interactive: Semi-automatic mode (for OpenCode, Codex, Cursor, etc.)
- autonomous: Full automatic mode (for OpenClaw, etc.)
"""

import os
import json
import subprocess
from pathlib import Path
from typing import Optional, Dict, Any
from dataclasses import dataclass


@dataclass
class AgentInfo:
    name: str
    mode: str
    confidence: float
    source: str


class AgentDetector:
    """Detect AI agent type and determine operating mode"""

    # Known agent environment variables and their default modes
    AGENT_ENV_VARS = {
        "OPENCLAW_MODE": "autonomous",
        "OPENCODE_MODE": "interactive",
        "CODEX_MODE": "interactive",
        "CURSOR_MODE": "interactive",
        "AGENT_MODE": None,  # Generic, needs value
        "CSV_DOCS_MODE": None,  # Explicit override
    }

    # Known agent process names
    AGENT_PROCESS_NAMES = {
        "openclaw": "autonomous",
        "claude": "interactive",
        "codex": "interactive",
        "opencode": "interactive",
        "cursor": "interactive",
        "copilot": "interactive",
    }

    # Known agent git config patterns
    AGENT_GIT_CONFIG_PATTERNS = {
        "agent.openclaw.mode": "autonomous",
        "agent.opencode.mode": "interactive",
        "csv-docs.mode": None,  # Explicit
    }

    def __init__(self, project_path: Optional[Path] = None):
        self.project_path = project_path or Path.cwd()
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load project configuration"""
        config_path = self.project_path / ".csv-docs-config.json"
        if config_path.exists():
            with open(config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def _get_env_mode(self) -> Optional[str]:
        """Check environment variables for mode setting"""
        # CSV_DOCS_MODE takes highest priority (explicit override)
        explicit_mode = os.getenv("CSV_DOCS_MODE")
        if explicit_mode:
            return explicit_mode

        # Check other known agent variables
        for var, default_mode in self.AGENT_ENV_VARS.items():
            if var == "CSV_DOCS_MODE":
                continue
            value = os.getenv(var)
            if value:
                if default_mode:
                    return default_mode
                return value

        return None

    def _get_process_mode(self) -> Optional[str]:
        """Detect mode from parent process name"""
        try:
            import psutil

            current_process = psutil.Process()
            parent = current_process.parent()
            if parent:
                parent_name = parent.name().lower()
                for name, mode in self.AGENT_PROCESS_NAMES.items():
                    if name in parent_name:
                        return mode
        except (ImportError, Exception):
            pass

        return None

    def _get_git_config_mode(self) -> Optional[str]:
        """Check git config for agent mode setting"""
        try:
            for pattern in self.AGENT_GIT_CONFIG_PATTERNS.keys():
                result = subprocess.run(
                    ["git", "config", "--get", pattern],
                    capture_output=True,
                    text=True,
                    cwd=self.project_path,
                )
                if result.returncode == 0 and result.stdout.strip():
                    value = result.stdout.strip()
                    if pattern == "csv-docs.mode":
                        return value
                    return self.AGENT_GIT_CONFIG_PATTERNS.get(pattern)
        except Exception:
            pass

        return None

    def _get_config_mode(self) -> Optional[str]:
        """Get mode from project config file"""
        return self.config.get("agent", {}).get("default_mode")

    def detect(self) -> AgentInfo:
        """Detect agent type and determine mode based on configuration priority"""
        detection_order = self.config.get("agent", {}).get(
            "detection_order", ["env", "process", "git", "config"]
        )

        # If auto_detect is disabled, use config default
        if not self.config.get("agent", {}).get("auto_detect", True):
            mode = self._get_config_mode() or "interactive"
            return AgentInfo(
                name="Unknown",
                mode=mode,
                confidence=1.0,
                source="config (auto_detect=false)",
            )

        mode = None
        source = None
        confidence = 0.0

        for step in detection_order:
            if step == "env":
                detected = self._get_env_mode()
                if detected:
                    mode = detected
                    source = "environment_variable"
                    confidence = 1.0
                    break
            elif step == "process":
                detected = self._get_process_mode()
                if detected:
                    mode = detected
                    source = "process_detection"
                    confidence = 0.8
                    break
            elif step == "git":
                detected = self._get_git_config_mode()
                if detected:
                    mode = detected
                    source = "git_config"
                    confidence = 0.9
                    break
            elif step == "config":
                detected = self._get_config_mode()
                if detected:
                    mode = detected
                    source = "project_config"
                    confidence = 0.7
                    break

        # Fallback to interactive
        if not mode:
            mode = "interactive"
            source = "default_fallback"
            confidence = 1.0

        return AgentInfo(
            name="Auto-detected",
            mode=mode,
            confidence=confidence,
            source=source or "unknown",
        )

    def set_mode(self, mode: str, target: str = "config") -> bool:
        """Manually set the mode

        Args:
            mode: "interactive" or "autonomous"
            target: Where to save ("config", "git", "env")
        """
        if mode not in ("interactive", "autonomous"):
            raise ValueError(
                f"Invalid mode: {mode}. Must be 'interactive' or 'autonomous'"
            )

        if target == "config":
            config_path = self.project_path / ".csv-docs-config.json"
            if config_path.exists():
                with open(config_path, "r", encoding="utf-8") as f:
                    config = json.load(f)
            else:
                config = {"agent": {}}

            config["agent"]["default_mode"] = mode
            config["agent"]["auto_detect"] = False

            with open(config_path, "w", encoding="utf-8") as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            return True

        elif target == "git":
            try:
                subprocess.run(
                    ["git", "config", "--global", "csv-docs.mode", mode], check=True
                )
                return True
            except subprocess.CalledProcessError:
                return False

        elif target == "env":
            # This only affects current session
            os.environ["CSV_DOCS_MODE"] = mode
            return True

        return False


def get_agent_mode(project_path: Optional[Path] = None) -> AgentInfo:
    """Convenience function to detect agent mode"""
    detector = AgentDetector(project_path)
    return detector.detect()


def set_agent_mode(
    mode: str, target: str = "config", project_path: Optional[Path] = None
) -> bool:
    """Convenience function to set agent mode"""
    detector = AgentDetector(project_path)
    return detector.set_mode(mode, target)
