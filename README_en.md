# CSV Documentation Generator v1.1.3

[![Version](https://img.shields.io/badge/version-1.1.3-blue.svg)](CHANGELOG.md)
[![GAMP 5](https://img.shields.io/badge/GAMP-5%20Second%20Edition-green.svg)](references/gamp-5.md)
[![21 CFR Part 11](https://img.shields.io/badge/21%20CFR%20Part%2011-Compliant-orange.svg)](references/21cfr-part11.md)
[![Status](https://img.shields.io/badge/status-beta-yellow.svg)]

Automated documentation generator for Computerized System Validation (CSV). Supports bilingual Chinese/English templates, designed for pharmaceutical and medical device industry validation documentation.

**[Changelog](CHANGELOG.md)** | **[中文版](README.md)**

**[中文更新日志](CHANGELOG_en.md)**

---

## AI Agent Installation

This skill can be used by the following AI Agent systems:

### OpenCode

```bash
# Method 1: Link to skills directory
ln -s ~/Code/skills/csv-documentation-generator ~/.agents/skills/csv-documentation-generator

# Method 2: Copy to skills directory
cp -r ~/Code/skills/csv-documentation-generator ~/.agents/skills/
```

### Claude Code

```bash
ln -s ~/Code/skills/csv-documentation-generator ~/.claude/skills/csv-documentation-generator
```

### Cursor

Cursor supports loading external skills. Link or copy this directory to Cursor's skills search path.

### Other AI Agents

Ensure the skill directory is in the AI's search path. AI can be triggered by:

> **Trigger Keywords**: validation plan, URS, FS, IQ, OQ, PQ, risk assessment, GAMP, GxP, 21 CFR Part 11, electronic signature, electronic record, EDC, CTMS, eTMF, LIMS, medical device, etc.

### AI Usage Example

When user requests CSV documentation generation:

1. **Understand user requirements** - System type, document type, project info
2. **Invoke generation script** - Use `scripts/generate.py`
3. **Wait for GAMP category confirmation** - If not specified, script shows interactive prompt
4. **Fill parameters** - Set project name, system name, etc.

```
User: Generate a validation plan for a CTMS system
AI: Using CSV Documentation Skill to generate validation plan...

Note: System will prompt for GAMP category selection:
- Category 3: Commercial off-the-shelf (non-configurable)
- Category 4: Configured COTS (e.g., EDC, CTMS, LIMS)
- Category 5: Custom/critical application

Invoke: python3 scripts/generate.py vp --project "XX Project" --system "CTMS v2.0" --output ./validation/
```

---

## Overview

This tool provides 12 validation document templates supporting:
- **Bilingual Chinese/English**
- **Word/Excel** output formats
- **GAMP 5** validation strategy
- **21 CFR Part 11** compliance
- **ALCOA+** data integrity principles
- **Requirements Traceability** - Code comment auto-parsing, complete URS/FS/TS/Test case traceability chain

## Supported System Types

| System Type | GAMP Category | Applicable Documents |
|------------|--------------|---------------------|
| EDC (Electronic Data Capture) | Category 4/5 | All 12 |
| CTMS (Clinical Trial Management) | Category 4 | VP, URS, FS, RA, IQ, OQ, RTM |
| LIMS (Laboratory Information Management) | Category 4/5 | All 12 |
| MES (Manufacturing Execution System) | Category 4 | All 12 |
| ERP (Enterprise Resource Planning) | Category 4 | VP, URS, RA, IQ, OQ |
| SCADA/DCS | Category 2/3 | VP, URS, IQ, OQ, PQ |
| Custom Software | Category 3/4 | VP, URS, RA, IQ, OQ |

## Quick Start

### Auto Environment Setup

The tool automatically detects and creates virtual environment:

1. First run creates `.venv` in skill directory automatically
2. Installs dependencies (`python-docx`, `openpyxl`, etc.)
3. Subsequent runs use the existing virtual environment

### Basic Usage

```bash
# Enter skill directory
cd ~/Code/skills/csv-documentation-generator

# Run script - first run creates virtual environment automatically
python3 scripts/generate.py vp --project "Clinical System" --system "EDC v1.0" --output ./output/

# Note: If --category not specified, GAMP category prompt will appear
python3 scripts/generate.py vp --project "Clinical System" --system "EDC v1.0" --category 4 --output ./output/
```

## Command Reference

### Available Commands

| Command | Description | Output |
|---------|-------------|--------|
| `generate.py vp` | Validation Plan | .docx |
| `generate.py urs` | User Requirements Specification | .docx |
| `generate.py fs` | Functional Specification | .docx |
| `generate.py ts` | Technical Specification | .docx |
| `generate.py ra` | Risk Assessment (FMEA) | .docx |
| `generate.py iq` | Installation Qualification | .docx |
| `generate.py oq` | Operational Qualification | .docx |
| `generate.py pq` | Performance Qualification | .docx |
| `generate.py rtm` | Requirements Traceability Matrix | .xlsx |
| `generate.py vsr` | Validation Summary Report | .docx |
| `generate.py checklist` | Validation Checklist | .xlsx |
| `generate.py test-case` | Test Case Template | .xlsx |
| `generate.py all` | Complete Validation Package | .docx / .xlsx |

### Command Options

| Option | Description | Required |
|--------|-------------|----------|
| `--project` | Project name | Yes |
| `--system` | System name and version | Yes |
| `--category` | GAMP category (1-5) | Yes |
| `--bilingual` | Bilingual template (default: true) | No |
| `--output` | Output directory | Yes |
| `--format` | Output format: docx, xlsx, both (default: both) | No |

### Examples

#### Example 1: Generate CTMS User Requirements

```bash
python3 scripts/generate.py urs \
  --project "Clinical Trial Management System" \
  --system "CTMS v2.0" \
  --category 4 \
  --bilingual true \
  --output ./validation/
```

#### Example 2: Generate Risk Assessment

```bash
python3 scripts/generate.py ra \
  --project "Quality Management System" \
  --system "QMS v1.5" \
  --category 4 \
  --critical-functions "Data Entry,Audit Trail,Access Control" \
  --output ./validation/
```

#### Example 3: Generate Traceability Matrix

```bash
python3 scripts/generate.py rtm \
  --project "Laboratory System" \
  --system "LIMS v3.0" \
  --category 4 \
  --urs-file ./URS-001.md \
  --fs-file ./FS-001.md \
  --output ./validation/
```

## Template Variables

Common variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `{PROJECT_NAME}` | Project name | Clinical Trial System |
| `{SYSTEM_NAME}` | System name | EDC v1.0 |
| `{SYSTEM_VERSION}` | System version | 1.0 |
| `{GAMP_CATEGORY}` | GAMP category | 4 |
| `{DOC_ID}` | Document ID | URS-001 |
| `{DATE}` | Document date | 2024-01-01 |
| `{AUTHOR}` | Document author | John Doe |
| `{REVIEWER}` | Reviewer | Jane Smith |
| `{APPROVER}` | Approver | Bob Wilson |

## Regulatory Compliance

### GAMP 5 Categories

| Category | Description | Validation Strategy |
|----------|-------------|-------------------|
| 1 | Operating Systems | Legacy System |
| 2 | Firmware | Simplified Validation |
| 3 | Commercial COTS | Risk-Based |
| 4 | Configured COTS | Risk-Based |
| 5 | Custom/Critical Systems | Full Validation |

### Key Regulations

This tool includes compliance checks for:

- **21 CFR Part 11**: Electronic Records and Signatures
  - Audit trail requirements
  - Electronic signature requirements
  - System access control

- **EU Annex 11**: Computerized Systems
  - Validation requirements
  - Data integrity
  - Change control

- **ALCOA+**: Data Integrity Principles
  - Attributable
  - Legible
  - Contemporaneous
  - Original
  - Accurate + Complete, Consistent, Enduring

## File Structure

```
csv-documentation-generator/
├── SKILL.md                           # Main skill file
├── README.md                          # Chinese documentation
├── README_en.md                      # English documentation
├── CHANGELOG.md                      # Chinese changelog
├── CHANGELOG_en.md                   # English changelog
├── requirements.txt                   # Python dependencies
├── .csv-docs-config.json             # Project config (AI Agent)
├── requirements.json                  # Requirements database (AI Agent)
├── audit-log.json                    # Audit log (AI Agent)
├── scripts/
│   ├── cli.py                        # Unified CLI (csv-docs)
│   ├── generate.py                   # Document generator
│   ├── agent.py                      # Agent mode detection
│   ├── config.py                     # Configuration management
│   ├── word_generator.py             # Word generator
│   ├── excel_generator.py            # Excel generator
│   ├── template_loader.py            # Template loader
│   ├── requirements/                 # Requirements tracking
│   │   ├── parser.py                 # Parser + eSig detection
│   │   ├── risk_analyzer.py          # RPN/FMEA risk assessment
│   │   └── linker.py                 # Git commit linking
│   ├── tests/                        # Test results
│   │   └── parser.py                 # JUnit/pytest parser
│   ├── fill/                         # Document filler
│   │   └── filler.py                 # Auto-fill variables
│   └── audit/                        # Audit log
│       └── log.py                    # Audit log + PDF export
├── templates/
│   ├── vp.md, urs.md, fs.md, ts.md
│   ├── ra.md, iq.md, oq.md, pq.md
│   ├── vsr.md
│   ├── test-case.xlsx
│   └── checklist.xlsx
└── references/
    ├── gamp-5.md
    ├── 21cfr-part11.md
    ├── annex-11.md
    └── data-integrity.md
```

## AI Agent Commands

```bash
# Initialize project
csv-docs init

# Check agent mode
csv-docs agent

# Set autonomous mode (for OpenClaw)
csv-docs agent --set autonomous

# Parse code for requirements
csv-docs parse ./src

# Show status
csv-docs status

# Add requirement manually
csv-docs add "User login functionality"

# Run risk analysis
csv-docs risk

# Add test results
csv-docs test --results ./test-results/

# Generate document
csv-docs generate vp --auto-fill

# Show audit log
csv-docs audit
```

## FAQ

### Q1: python-docx not installed

**Solution**:
```bash
pip install -r requirements.txt
```

### Q2: Encoding errors

**Solution**: Ensure terminal uses UTF-8 encoding

### Q3: Template not found

**Solution**: Confirm running in correct directory

## License

MIT License

## Contributing

Issues and Pull Requests are welcome!
