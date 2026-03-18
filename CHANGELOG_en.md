# Changelog - CSV Documentation Generator

All notable version updates are documented here.

## [1.0.0] - 2026-03-18

### Added

#### Core Features
- **9 Validation Document Templates** (VP, URS, FS, TS, RA, IQ, OQ, PQ, VSR)
- **Professional GMP-Style Word Generator**
  - Header color: Steel blue (#4682B4) + white text
  - Priority markers: `[必须]`, `[应该]`, `[Pass]`, `[Fail]`
  - Cover page + approval signature table
  - Alternating row colors
- **Bilingual Chinese/English Support**

#### AI Agent Intelligent Requirements Tracking System
- **Agent Mode Detection** (`scripts/agent.py`)
  - Auto-detect OpenClaw/OpenCode/Codex agent types
  - Support `interactive` (semi-auto) and `autonomous` (full-auto) modes
  - Environment variable priority: `CSV_DOCS_MODE` > Agent env vars > Git config > Project config

- **Requirements Parser** (`scripts/requirements/parser.py`)
  - Parse requirements from code comments: `@req`, `@requirement`, `# URS-001`
  - Auto-detect electronic signature requirements (21 CFR Part 11)
  - Keywords: 签名, 审核, 审批, sign, approve, etc.

- **Risk Analyzer** (`scripts/requirements/risk_analyzer.py`)
  - RPN/FMEA methodology
  - Auto severity/likelihood/detectability assessment
  - GAMP Category-based risk calculation
  - Standard mitigation suggestions

- **Git Linker** (`scripts/requirements/linker.py`)
  - Auto-parse requirement IDs from commit messages
  - Requirements ↔ Commit traceability matrix

- **Test Results Parser** (`scripts/tests/parser.py`)
  - Support JUnit XML, pytest JSON, NUnit XML formats
  - Auto-link requirements to test status
  - Test coverage statistics

- **Document Auto-Filler** (`scripts/fill/filler.py`)
  - Auto-fill template variables from requirements database
  - Document completeness validation

- **Audit Log** (`scripts/audit/log.py`)
  - Complete record of all operations
  - Export to PDF (text format)
  - Filter by operation type and mode

#### CLI Unified Entry Point (`scripts/cli.py`)

```bash
csv-docs init              # Initialize project config
csv-docs agent             # Detect agent mode
csv-docs agent --set autonomous  # Set to autonomous mode
csv-docs parse ./src       # Parse code for requirements
csv-docs status            # Show status
csv-docs add "description" # Add requirement
csv-docs risk              # Run risk analysis
csv-docs test --results ./ # Parse test results
csv-docs generate vp       # Generate document
csv-docs audit            # Show audit log
```

#### Compliance Support
- **GAMP 5 Second Edition** validation lifecycle
- **21 CFR Part 11** Electronic Records and Signatures
- **EU Annex 11** Computerized Systems
- **ALCOA+** Data Integrity Principles

### Configuration

#### Project Config (`.csv-docs-config.json`)
```json
{
  "agent": {
    "default_mode": "interactive",
    "auto_detect": true
  },
  "autonomous": {
    "on_duplicate": "overwrite"
  },
  "compliance": {
    "gamp_category": null,
    "auto_esig_detection": true,
    "auto_ra": true,
    "esig_keywords": ["签名", "审核", "审批", "sign", "approve"]
  }
}
```

#### Requirements Database (`requirements.json`)
- Stores all requirements, risks, test results, commit links

#### Audit Log (`audit-log.json`)
- Complete audit trail of all operations

---

## [0.1.0] - Initial Version

### Added
- Basic document templates
- Word generator
- Excel generator
- GAMP 5 reference documents
- 21 CFR Part 11 reference documents
- EU Annex 11 reference documents
- Data integrity reference documents

---

## Version Format

Version format follows [Semantic Versioning](https://semver.org/):
- **MAJOR**: Incompatible API changes
- **MINOR**: Backward-compatible new features
- **PATCH**: Backward-compatible bug fixes
