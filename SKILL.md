---
name: csv-documentation-generator
description: Use when generating computer system validation (CSV) documentation for pharmaceutical and medical device industries, including validation plans, URS, FS, IQ/OQ/PQ documents, and traceability matrices.
triggers:
  - "Generate CSV documentation"
  - "创建 GMP 验证文档"
  - "计算机化系统验证"
  - "IQ OQ PQ protocol"
  - "URS FS RA 追溯矩阵"
  - "GAMP 5 validation"
  - "GxP"
  - "21 CFR Part 11"
  - "电子签名"
  - "电子记录"
  - "EDC"
  - "CTMS"
  - "eTMF"
  - "LIMS"
  - "医疗器械"
category: gxp-compliance
version: "1.4.0"
author: zealot00
homepage: https://github.com/zealot00/csv-documentation-generator
repository: https://github.com/zealot00/csv-documentation-generator
bugs: https://github.com/zealot00/csv-documentation-generator/issues
createdAt: "2026-03-18"
lastReviewedAt: "2026-03-18"
validationStatus: "beta"
compatibility:
  openclaw: ">=1.0.0"
  python: ">=3.10"
requiredTools:
  - exec
  - write
inputSchema:
  type: object
  required: [project, system]
  properties:
    docType:
      type: string
      enum: [vp, urs, fs, ra, iq, oq, pq, rtm, vsr, checklist, test-case, all]
    project:
      type: string
      description: "项目名称 / Project name"
    system:
      type: string
      description: "系统名称及版本 / System name and version"
    category:
      type: integer
      enum: [1, 2, 3, 4, 5]
      description: "GAMP category (1-5)"
    bilingual:
      type: boolean
      default: true
    output:
      type: string
      default: "./output"
outputSchema:
  type: object
  properties:
    docx:
      type: array
      items:
        type: string
      description: "Generated Word documents"
    xlsx:
      type: array
      items:
        type: string
      description: "Generated Excel documents"
---

# CSV Documentation Generator

Generate Computerized System Validation (CSV) documentation for pharmaceutical and medical device industries. Supports bilingual (Chinese/English) templates and multiple output formats (Word/Excel).

## When to Use

Use this skill when:
- Creating validation documentation for GMP-regulated systems
- Generating User Requirements Specification (URS) with regulatory compliance checks
- Preparing IQ/OQ/PQ protocols for system qualification
- Creating traceability matrices linking requirements to test cases
- Conducting risk assessments for computerised systems
- Need documentation templates that comply with GAMP 5, 21 CFR Part 11, EU Annex 11

### Supported Systems

| System Type | GAMP Category | Documents |
|-------------|---------------|-----------|
| EDC (Electronic Data Capture) | Category 4/5 | All 12 documents |
| CTMS (Clinical Trial Management) | Category 4 | VP, URS, FS, RA, IQ, OQ, RTM |
| LIMS (Laboratory Information Management) | Category 4/5 | All 12 documents |
| MES (Manufacturing Execution System) | Category 4 | All 12 documents |
| ERP (Enterprise Resource Planning) | Category 4 | VP, URS, RA, IQ, OQ |
| SCADA/DCS | Category 2/3 | VP, URS, IQ, OQ, PQ |
| Custom Software | Category 3/4 | VP, URS, RA, IQ, OQ |

## Quick Start

```bash
# Navigate to skill directory
cd <SKILL_DIR>/csv-documentation-generator

# Run script - will automatically create virtual environment on first run
python3 scripts/generate.py vp --project "XX系统" --system "EDC v1.0" --output ./output/

# Note: If --category is not specified, interactive GAMP category selection will be prompted
# The script provides bilingual (Chinese/English) guidance based on GAMP 5 Second Edition

# Generate Validation Plan (with category specified)
python3 scripts/generate.py vp --project "XX系统" --system "EDC v1.0" --category 4 --output ./output/

# Generate full validation package
python3 scripts/generate.py all --project "XX系统" --system "MES" --category 4 --output ./validation/
```

### Parse Requirements from Code (pre-generation)

```bash
# Navigate to skill directory
cd <SKILL_DIR>/csv-documentation-generator

# Parse source code for requirements (extracts @URS, @TEST, @FS, @TS markers)
python3 scripts/cli.py parse ./src

# Review extracted requirements
cat requirements.json
```

### Auto Environment Setup

This skill automatically handles environment setup:
1. **First run**: Automatically creates `.venv` virtual environment in skill directory
2. **Dependencies**: Automatically installs required packages (python-docx, openpyxl, etc.)
3. **Subsequent runs**: Use the already-created virtual environment

This ensures consistent behavior and avoids dependency conflicts.

### Interactive GAMP Category Selection

If `--category` is not specified, the script will prompt with bilingual (Chinese/English) guidance:

```
GAMP 5 (Second Edition) Category Selection:
  [1] Infrastructure Software - 基础设施软件
  [2] Firmware - 固件
  [3] Commercial Off-The-Shelf (COTS) - Non-configured - 商用现货软件 (不可配置)
  [4] Configured COTS - 配置型 COTS 软件 (e.g., EDC, CTMS, LIMS, MES)
  [5] Custom / Critical Application - 定制/关键应用
```

AI agents should guide users to select the appropriate category based on GAMP 5 Second Edition principles.

## Available Commands

| Command | Description | Output Format |
|---------|-------------|---------------|
| `generate.py vp` | Validation Plan | .docx |
| `generate.py urs` | User Requirements Specification | .docx |
| `generate.py fs` | Functional Specification | .docx |
| `generate.py ts` | Technical Specification | .docx |
| `generate.py ra` | Risk Assessment (FMEA) | .docx |
| `generate.py iq` | Installation Qualification | .docx |
| `generate.py oq` | Operational Qualification | .docx |
| `generate.py pq` | Performance Qualification | .docx |
| `generate.py rtm` | Traceability Matrix | .xlsx |
| `generate.py vsr` | Validation Summary Report | .docx |
| `generate.py checklist` | Validation Checklist | .xlsx |
| `generate.py test-case` | Test Case Template | .xlsx |
| `generate.py all` | Full validation package | .docx / .xlsx |

## Command Options

| Option | Description | Required |
|--------|-------------|----------|
| `--project` | Project name | Yes |
| `--system` | System name and version | Yes |
| `--category` | GAMP category (1-5). If not specified, interactive selection will be prompted with bilingual GAMP 5 guidance. | No (will prompt) |
| `--bilingual` | Generate bilingual templates (default: true) | No |
| `--output` | Output directory | Yes |
| `--format` | Output format: docx, xlsx, or both (default: both) | No |

## Output Format Standards

All generated documents follow consistent naming and formatting rules:

### Document Naming Convention

| Document Type | Format | Example |
|--------------|--------|---------|
| Validation Plan | `{TYPE}_{PROJECT}.{ext}` | VP_XX系统.docx |
| User Requirements | `{TYPE}_{PROJECT}.{ext}` | URS_XX系统.docx |
| Functional Specification | `{TYPE}_{PROJECT}.{ext}` | FS_XX系统.docx |
| Traceability Matrix | `RTM_{PROJECT}.{ext}` | RTM_XX系统.xlsx |

### Output Directory Structure

```
{output_dir}/
├── VP_项目名.docx
├── URS_项目名.docx
├── FS_项目名.docx
├── TS_项目名.docx
├── RA_项目名.docx
├── IQ_项目名.docx
├── OQ_项目名.docx
├── PQ_项目名.docx
├── VSR_项目名.docx
├── RTM_项目名.xlsx
└── CHECKLIST_项目名.xlsx
```

### Document Styling Standards

**Fonts:**
- Chinese text: SimSun (宋体)
- English text: Arial

**Colors:**
- Table headers: #2563EB (Royal Blue) with white text
- Priority markers: [必须] (red), [应该] (amber), [可以] (green)
- Test results: [通过] (green), [失败] (red), [待测] (amber)

## Template Variables

Common variables used in templates:

| Variable | Description | Example |
|----------|-------------|---------|
| `{PROJECT_NAME}` | Project name | 临床试验系统 |
| `{SYSTEM_NAME}` | System name | EDC v1.0 |
| `{SYSTEM_VERSION}` | System version | 1.0 |
| `{GAMP_CATEGORY}` | GAMP category | 4 |
| `{DOC_ID}` | Document ID | URS-001 |
| `{DATE}` | Document date | 2024-01-01 |
| `{AUTHOR}` | Document author | 张三 |
| `{REVIEWER}` | Reviewer name | 李四 |
| `{APPROVER}` | Approver name | 王五 |

## Regulatory Compliance

### GAMP 5 Categories

| Category | Description | Validation Approach |
|----------|-------------|-------------------|
| 1 | Operating System | Legacy |
| 2 | Firmware | Simplified |
| 3 | Commercial-off-the-shelf (COTS) | Risk-based |
| 4 | Configured COTS | Risk-based |
| 5 | Custom/Critical | Full validation |

### Key Regulatory Requirements

This skill includes compliance checks for:

- **21 CFR Part 11**: Electronic Records and Signatures
  - Audit trail requirements
  - Electronic signature requirements
  - System access controls

- **EU Annex 11**: Computerised Systems
  - Validation requirements
  - Data integrity
  - Change control

- **ALCOA+**: Data Integrity
  - Attributable
  - Legible
  - Contemporaneous
  - Original
  - Accurate (+ Complete, Consistent, Enduring)

## GAMP 5 Second Edition - Critical Thinking Constraints

> **GAMP 5 M12 Critical Thinking**: AI agents MUST apply critical thinking principles per GAMP 5 Second Edition Appendix M12. Do NOT use rigid templates or "tick-in-the-box" approaches. Scale validation effort proportionally to system risk and complexity.

### M12.1 Validation Planning Constraints

When generating VP documents, AI agents MUST:

1. **Conduct Business Process Analysis**
   - Identify the business process the system supports
   - Create or reference business process flow diagrams
   - Understand data flow to identify GxP-regulated data

2. **Identify GxP Scope**
   - Determine which data are GxP records requiring audit trails
   - NOT all data requires audit trails - apply context-based judgment
   - Consider data that directly impacts patient safety or product quality

3. **Avoid One-Size-Fits-All Approaches**
   - Higher risk systems require more rigorous validation
   - Lower risk systems can use simplified approaches
   - Justify the chosen validation approach

### M12.2 Requirements Development Constraints

When generating URS documents, AI agents MUST:

1. **Apply Context-Based Audit Trail Requirements**
   ```
   WRONG: "All data modifications require audit trails"
   RIGHT: "GxP-regulated records require audit trails. 
           Non-GxP data (e.g., user preferences) do not require audit trails."
   ```

2. **Identify Primary Records**
   - Identify which records are the "authoritative copy" (primary record)
   - Data may flow through multiple systems - identify where compliance is maintained

3. **Use Risk-Based Prioritization**
   - Critical requirements (patient safety, data integrity) are [必须]
   - Less critical requirements are [应该] or [可以]
   - Higher risk requirements require more rigorous testing

### M12.3 Risk Assessment Constraints (Hierarchical Risk)

When generating RA documents, AI agents MUST:

1. **Apply Hierarchical Risk Structure**
   ```
   Parent Function Risk (Major) → determines testing rigor
           ↓
   Subsidiary Functions (Children) → risk cannot exceed parent
   ```

2. **Follow Risk Recursion Rules**
   - A subsidiary function CANNOT have higher risk than its parent
   - If a subsidiary appears high-risk, reconsider the parent assessment
   - Rationale: If overall function is acceptable risk, subsidiary issues may be acceptable

3. **Avoid Over-Testing Low-Risk Functions**
   - Low-risk parent function → subsidiary functions don't need detailed assessment
   - High-risk parent function → more granular assessment justified
   - Use risk recursion to scale effort appropriately

### M12.4 Testing Constraints

When generating test cases, AI agents MUST:

1. **Differentiate Proving vs Non-Proving Steps**
   - Proving steps: Demonstrate requirement fulfillment (evidence needed)
   - Non-proving steps: Setup activities (no evidence needed)

2. **Scale Evidence to Risk**
   - High-risk functions: Detailed evidence, screenshots
   - Low-risk functions: Summary evidence acceptable
   - Avoid excessive documentation for low-risk items

### M12.5 Supplier Assessment Constraints

When generating supplier assessment content:

1. **Leverage Supplier Documentation**
   - Use supplier audits, SOC 2 reports, ISO certifications
   - Avoid duplicating supplier testing efforts

2. **Assess Based on System Category**
   - Category 3/4: Leverage supplier validation
   - Category 5: Full in-house validation required

### Constraint Violation Examples

| WRONG Approach | GAMP 5 M12 Correct Approach |
|---------------|---------------------------|
| "Enable audit trail for all data" | "Enable audit trail for GxP records only" |
| "Test all functions equally" | "Scale testing rigor to risk level" |
| "Detailed testing for all subsidiaries" | "Subsidiary risk ≤ parent risk" |
| "Maximum documentation for all systems" | "Proportionate to system complexity/risk" |

## Document Generation Triggering Conditions

### VP (Validation Plan)

**Trigger Keywords:**
- "验证计划", "validation plan", "VP"
- "项目启动", "project start"
- "系统上线", "system launch"

**Pre-fill Data (from context or user):**
- `{PROJECT_NAME}`, `{SYSTEM_NAME}`
- `{GAMP_CATEGORY}` - If not specified, prompt user with GAMP category selection
- `{CHANGE_DESCRIPTION}` - If change project, auto-fill from change request

**AI填充规则:**
1. 如果是**变更项目**：自动生成变更说明章节，从`{CHANGE_DESCRIPTION}`提取关键风险
2. 如果是**新项目**：生成完整规划章节
3. 基于`{GAMP_CATEGORY}`自动调整验证生命周期范围

### URS (User Requirements Specification)

**Trigger Keywords:**
- "用户需求", "URS", "user requirements"
- "需求规格", "requirements specification"

**Pre-fill Data:**
- `{SYSTEM_NAME}`, `{SYSTEM_VERSION}`
- `{GAMP_CATEGORY}`
- Business process description (from user or discovery)
- GxP records identification (from VP business process analysis)

**AI填充规则:**
1. 首先询问系统的业务背景和数据流
2. 识别GxP记录范围（与用户确认）
3. 基于GxP范围自动确定审计追踪需求
4. 按结构填充需求，每个需求追溯到FS

### FS (Functional Specification)

**Trigger Keywords:**
- "功能规格", "FS", "functional specification"
- "设计规格", "design specification"

**Pre-fill Data:**
- URS requirements (auto-linked by ID)
- System architecture (from TS or user description)
- GxP scope (from URS)

**AI填充规则:**
1. 自动从URS追溯到FS需求ID
2. 每个FS功能必须追溯到至少一个URS-ID
3. 区分配置项(COTS)和定制项

### RA (Risk Assessment)

**Trigger Keywords:**
- "风险评估", "RA", "risk assessment"
- "风险分析", "risk analysis"

**Pre-fill Data:**
- `{CHANGE_DESCRIPTION}` - If change project
- URS requirements (for risk identification)
- GxP scope (from URS)

**AI填充规则:**
1. 如果有`{CHANGE_DESCRIPTION}`，自动生成变更风险评估
2. 追溯URS优先级到RA风险等级
3. 应用层级风险规则：子功能风险≤父功能风险

### IQ/OQ/PQ (Qualification Protocols)

**Trigger Keywords:**
- "安装确认", "IQ", "installation qualification"
- "操作确认", "OQ", "operational qualification"
- "性能确认", "PQ", "performance qualification"

**Pre-fill Data:**
- System configuration (from TS)
- Risk assessment results (from RA)

**AI填充规则:**
1. 根据RA中的风险等级调整测试范围
2. 高风险功能→完整IQ/OQ/PQ
3. 低风险功能→简化测试

### VSR (Validation Summary Report)

**Trigger Keywords:**
- "验证总结", "VSR", "validation summary"
- "验证报告", "validation report"

**Pre-fill Data:**
- All test results (from IQ/OQ/PQ)
- Requirements traceability (from RTM)
- Deviation records (from testing)

**AI填充规则:**
1. 自动汇总所有测试结果
2. 自动生成Lessons Learned章节
3. 自动生成Periodic Review计划

## Content Fill Prompt Library

### URS需求填充Prompt

When generating URS, AI SHOULD follow this structure:

```
1. 首先了解业务背景:
   - 询问系统的业务类型和用途
   - 识别系统的用户群体
   - 了解数据的生命周期

2. 识别GxP记录范围:
   - 哪些数据影响患者安全?
   - 哪些数据需要审计追踪?
   - 主记录(Primary Record)是什么?

3. 填充需求格式:
   | ID | 需求描述 | 优先级 | 验证方法 |
   |----|---------|--------|---------|
   | URS-{SEQ} | 系统应[功能]+[对象]+[条件] | [{必须}/{应该}/{可以}] | [{测试}/{审查}] |

4. 需求描述规则:
   - 正确: "系统应在用户登录失败5次后锁定账户30分钟"
   - 错误: "系统应该安全"
```

### FS功能填充Prompt

When generating FS, AI SHOULD follow this structure:

```
1. 追溯到URS:
   - 每个FS功能必须引用对应的URS-ID
   - 使用追溯表总览

2. 功能描述格式:
   - 描述系统如何实现URS需求
   - 包含用户界面、业务流程、边界条件

3. 配置项vs定制项:
   - COTS标准配置: 标记为"配置"
   - 需要二次开发: 标记为"定制"
```

### RA风险填充Prompt

When generating RA, AI SHOULD follow this structure:

```
1. 层级风险评估:
   - 首先评估主要功能(Major/Parent)的风险
   - 子功能(Subsidiary)风险不得高于父功能

2. RPN计算:
   RPN = 严重性(S) × 可能性(L) × 可检测性(D)
   
   | RPN范围 | 风险等级 | 行动 |
   |---------|---------|------|
   | 1-25 | 低 | 接受 |
   | 26-50 | 中 | 缓解措施 |
   | 51-75 | 高 | 必须缓解 |
   | 76-125 | 严重 | 暂停上线 |

3. 追溯到URS优先级:
   - URS [必须] + 安全/合规 → 高风险
   - URS [应该] → 中风险
   - URS [可以] → 低风险
```

## Data Flow Definitions

### Document Interdependencies

```
┌─────────────────────────────────────────────────────────────────┐
│                        数据流动链                                 │
└─────────────────────────────────────────────────────────────────┘

[用户/AI 填写 VP 变更描述]
        │
        ▼
[RA 自动生成变更风险评估]
        │
        ▼ (追溯)
[FS 基于URS风险调整测试范围]
        │
        ▼
[IQ/OQ/PQ 测试范围自动调整]
        │
        ▼
[VSR 自动汇总变更影响]
```

### Specific Data Mappings

| 源文档 | 数据项 | 目标文档 | 填充位置 |
|--------|--------|----------|----------|
| VP | `{CHANGE_DESCRIPTION}` | RA | 1.5 变更说明 |
| URS | GxP记录识别 | FS | 审计追踪需求 |
| URS | 需求优先级 | RA | 风险等级基准 |
| FS | URS追溯表 | RTM | 追溯矩阵 |
| RA | 风险等级 | IQ/OQ/PQ | 测试范围 |
| IQ/OQ/PQ | 测试结果 | VSR | 4.验证结果汇总 |

### Automatic Traceability建立规则

1. **URS → FS**: AI在填充FS时必须引用URS-ID
2. **FS → TS**: 技术规格支持功能规格
3. **URS → RA**: 风险等级基于URS优先级
4. **RA → Test**: 测试范围基于风险等级
5. **All → RTM**: 追溯矩阵自动汇总

## Reference Documents

Reference materials included in `references/` folder:

| File | Description |
|------|-------------|
| `gamp-5.md` | GAMP 5 quick reference guide |
| `21cfr-part11.md` | 21 CFR Part 11 key requirements |
| `annex-11.md` | EU Annex 11 requirements |
| `data-integrity.md` | ALCOA+ data integrity principles |

## Example Templates

Complete fill examples are provided in `templates/examples/` directory:

| Example File | Description |
|--------------|-------------|
| `urs-example.md` | URS with complete requirement examples |
| `fs-example.md` | FS with traceability examples |
| `ra-example.md` | RA with hierarchical risk examples |
| `iq-example.md` | IQ with qualification check examples |

AI agents SHOULD reference these examples for content style guidance when filling templates.

## Bilingual Format

All templates support Chinese/English bilingual output:

```markdown
## 1. 目的 / Purpose

本文档定义了... / This document defines...
```

Tables use dual-language headers:

| 中文 | English |
|------|---------|
| 验证计划 | Validation Plan |
| 用户需求 | User Requirements |

## Requirements Traceability

This skill supports **GAMP 5 compliant requirements traceability** across the entire validation lifecycle.

### Automated Traceability Chain

```
代码注释 (@URS[module]) 
    ↓
requirements.json (需求解析)
    ↓
URS 模板 (自动同步章节)
    ↓
FS/TS 文档 (引用需求ID)
    ↓
测试用例 (关联需求ID)
    ↓
测试结果 (解析需求ID)
    ↓
RTM (追溯矩阵自动生成)
```

### Code Comment Standards (AI Agent Must Follow)

When generating code, **AI agents MUST include requirement markers** for automatic traceability. Use the standardized `@REQ` format:

```python
# @REQ URS-001 - 系统应支持基于角色的访问控制 (RBAC)
# @REQ URS-002 - 用户密码必须满足复杂度要求（至少8位）
# @FS FS-001
# @TS TS-001
# @TEST[OQ-UM-001] - 验证用户角色分配功能
# @RISK H  # High risk module

def assign_role(user_id: str, role: str) -> bool:
    '''
    @REQ URS-001 - Role-based access control required
    @TEST[OQ-UM-001] - Test role assignment
    '''
    # Implementation...
```

**Standard comment formats:**

| Pattern | Example | Description |
|---------|---------|-------------|
| `// @REQ URS-xxx` | `// @REQ URS-001 - 系统应支持RBAC` | Requirement with ID and description |
| `# @REQ` | `# @REQ URS-001 - 描述` | Python-style comment |
| `/* @REQ */` | `/* @REQ URS-001 - 描述 */` | Multi-line comment |
| `// @TEST[type-id]` | `// @TEST[OQ-UM-001] - 验证` | Test case link |
| `// @FS` | `// @FS FS-001` | FS reference |
| `// @TS` | `// @TS TS-001` | TS reference |
| `// @RISK [H/M/L]` | `// @RISK H` | Risk level (High/Medium/Low) |

**Risk levels:**
- `H` (High): Security, compliance, electronic signature, audit trail related
- `M` (Medium): Default for most requirements
- `L` (Low): Simple features, documentation, reports

### Standard Modules

| Module ID | 中文名 | English Name | Test Prefix |
|-----------|--------|--------------|-------------|
| `user_mgmt` | 用户管理 | User Management | UM |
| `audit_trail` | 审计追踪 | Audit Trail | AT |
| `data_mgmt` | 数据管理 | Data Management | DM |
| `business_func` | 业务功能 | Business Functions | BF |
| `reporting` | 报告功能 | Reporting | RP |
| `integration` | 接口集成 | Integration | INT |
| `security` | 安全 | Security | SEC |
| `compliance` | 合规 | Compliance | CMP |

**注意**: 章节号（4.X）是动态分配的，基于模板中已有的章节。同步时会自动为新模块分配下一个可用编号。

### Test Case ID Format

Test case IDs follow the format: `{IQ|OQ|PQ}-{ModulePrefix}-{Number}`

| Type | Example | Description |
|------|---------|-------------|
| IQ | `IQ-UM-001` | Installation Qualification test |
| OQ | `OQ-UM-001` | Operational Qualification test |
| PQ | `PQ-UM-001` | Performance Qualification test |

### Auto-Sync Feature

Before generating documents, use `--sync` to automatically update templates with new requirements:

```bash
# Generate URS and sync requirements to template
python3 scripts/generate.py urs --sync \
  --project "临床系统" \
  --system "EDC v1.0" \
  --category 4 \
  --output ./validation/

# Generate full validation package with sync
python3 scripts/generate.py all --sync \
  --project "XX系统" \
  --system "MES" \
  --category 4 \
  --output ./validation/
```

**What `--sync` does:**
1. Reads `requirements.json` for all requirements
2. Groups requirements by module
3. Checks if each module section exists in template
4. Auto-appends new module sections if missing
5. Backs up original template before modification

### Sync Template to Database

Use `--sync-template-to-db` to extract requirements from templates and add them to `requirements.json`:

```bash
# Extract requirements from urs.md template to requirements.json
python3 scripts/generate.py urs --sync-template-to-db \
  --project "临床系统" \
  --system "EDC v1.0" \
  --category 4 \
  --output ./validation/
```

**What `--sync-template-to-db` does:**
1. Reads the template (e.g., urs.md)
2. Extracts all requirements in `| URS-xxx | description |` format
3. Loads existing requirements.json (if exists)
4. Adds new requirements that don't already exist
5. Preserves existing requirements and test results

### Interactive Mode

For interactive step-by-step document generation with confirmation prompts:

```bash
python3 scripts/generate.py all --interactive \
  --project "临床系统" \
  --system "EDC v1.0" \
  --category 4 \
  --output ./validation/
```

**Interactive workflow:**
```
[1/11] 解析代码注释...
  → 按 Enter 继续，'s' 跳过，'q' 退出:

[2/11] 同步需求到数据库...
  → 按 Enter 继续，'s' 跳过，'q' 退出:

[3/11] 生成 URS...
  → 按 Enter 继续，'s' 跳过，'q' 退出:
  ✓ ./output/URS_临床系统.docx
...
```

**Options:**
- `Enter` - Execute this step
- `s` - Skip this step
- `q` - Quit (already generated files are preserved)

### Compliance Check

Run GAMP 5 compliance validation to check requirements coverage and test coverage:

```bash
# Run compliance check (text output)
python3 scripts/generate.py check \
  --requirements requirements.json \
  --test-results test_results.json

# Run compliance check (JSON output for CI/CD)
python3 scripts/generate.py check \
  --requirements requirements.json \
  --test-results test_results.json \
  --output-format json
```

**Compliance checks performed:**
- Requirement coverage (ensures all code requirements are documented)
- High-risk module verification (IQ/OQ/PQ tests for critical modules)
- Test coverage threshold (default 80%)

**Exit codes:**
- `0` - All checks passed
- `1` - Warnings present
- `2` - Errors found

### Incremental Update (Smart Rebuild)

Use `--diff-only` to skip regeneration when requirements haven't changed:

```bash
# Only regenerate RTM if requirements changed
python3 scripts/generate.py rtm --diff-only \
  --project "临床系统" \
  --system "EDC v1.0" \
  --category 4 \
  --output ./validation/
```

**How it works:**
1. Computes SHA256 hash of requirements after each generation
2. Stores hash in `.requirements.hash` in output directory
3. On subsequent runs, compares current hash against stored hash
4. Skips generation if hash matches (requirements unchanged)

### Git Hooks (Automated Compliance)

Install post-commit hooks to automatically run compliance checks after code commits:

```bash
# Install hooks locally (per-project)
./scripts/git-hooks/install.sh --local

# Install hooks globally (all projects)
./scripts/git-hooks/install.sh --global

# Uninstall hooks
./scripts/git-hooks/install.sh --uninstall
```

**What the hook does:**
- Detects commits with code or requirements changes
- Runs compliance check (non-blocking)
- Outputs warnings to stderr without blocking commit

### Bidirectional Sync

Use `--sync` for bidirectional sync between template and requirements.json:

```bash
# Full bidirectional sync (both directions)
python3 scripts/generate.py urs --sync \
  --project "临床系统" \
  --system "EDC v1.0" \
  --category 4

# Only sync template → JSON
python3 scripts/generate.py urs --sync --sync-direction to-json

# Only sync JSON → template
python3 scripts/generate.py urs --sync --sync-direction to-template
```

**Conflict resolution:**
```bash
# Keep template descriptions on conflict
python3 scripts/generate.py urs --sync --conflict-resolution template

# Keep JSON descriptions on conflict
python3 scripts/generate.py urs --sync --conflict-resolution json

# Keep newer version based on updated_at
python3 scripts/generate.py urs --sync --conflict-resolution newer
```

**Section numbering behavior:**
- Sync automatically creates module sections with `### 4.X` headers
- Section numbers are dynamically assigned based on existing sections in the template
- Only modules with requirements in `requirements.json` will have sections created
- Custom modules (e.g., `pm_query`, `multi_lock`) are supported and will be assigned the next available section number

### Monorepo Support

For projects with multiple subprojects (monorepo structure):

```bash
# Auto-detect monorepo root
python3 scripts/generate.py rtm --project "临床系统" --system "EDC v1.0"

# Explicitly specify monorepo root
python3 scripts/generate.py rtm --project "临床系统" --system "EDC v1.0" \
  --project-root /path/to/monorepo
```

**Detected monorepo layouts:**
- `apps/`, `packages/`, `projects/`, `modules/`, `services/` directories
- Each subproject with its own `requirements.json`

### Template Versioning

Templates are versioned for compatibility tracking:

```bash
# Check compatibility (automatic on generate)
python3 scripts/generate.py rtm --project "系统" --system "v1.0" --category 4

# Specify template version
python3 scripts/generate.py rtm --template-version 1.2.0 \
  --project "系统" --system "v1.0" --category 4
```

**Automatic migrations:**
- Templates are automatically migrated to current version
- Version checks prevent incompatible generator/template combinations

### CI/CD Integration

Use provided CI/CD templates for automated documentation generation:

**GitHub Actions** (`templates/ci/github-actions.yml`):
```yaml
- uses: actions/checkout@v4
- uses: actions/setup-python@v5
  with:
    python-version: '3.11'
- run: pip install -r requirements.txt
- run: python scripts/generate.py check --output-format json
- run: python scripts/generate.py all --diff-only
```

**GitLab CI** (`templates/ci/gitlab-ci.yml`):
```yaml
generate:rtm:
  extends: .csv-docs-base
  script:
    - python scripts/generate.py rtm --diff-only
  artifacts:
    paths:
      - validation/RTM*.xlsx
```

### Important Notes

#### Template Requirements Are Examples
The URS/FS/TS IDs and descriptions in templates are **examples only**. For actual projects:
1. Review and modify template requirements based on real system needs
2. Delete or replace example requirements as appropriate
3. Use `--sync-template-to-db` to populate initial requirements, then customize

#### Change-Driven Risk Assessment (GxP)
Per GxP requirements, any system change requires a risk assessment. When generating RA documents, include the change description:

```bash
python3 scripts/generate.py ra \
  --project "临床系统" \
  --system "EDC v1.0" \
  --change-description "升级数据库从 v12 到 v14" \
  --output ./validation/
```

### Parsing Requirements from Code

```bash
# Navigate to skill directory
cd <SKILL_DIR>/csv-documentation-generator

# Parse source code for requirements using csv-docs CLI
python3 scripts/cli.py parse ./src

# View extracted requirements
cat requirements.json
```

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| python-docx not installed | Run: `pip install -r requirements.txt` |
| Encoding errors | Ensure UTF-8 encoding in your terminal |
| Template not found | Check you are in the correct directory |

### Getting Help

Run with verbose output:
```bash
python3 scripts/generate.py --help
```

## Examples

### Example 1: Generate URS for CTMS

```bash
python3 scripts/generate.py urs \
  --project "临床试验管理系统" \
  --system "CTMS v2.0" \
  --category 4 \
  --bilingual true \
  --output ./validation/
```

### Example 2: Generate Risk Assessment

```bash
python3 scripts/generate.py ra \
  --project "质量管理系统" \
  --system "QMS v1.5" \
  --category 4 \
  --critical-functions "数据录入,审计追踪,权限控制" \
  --output ./validation/
```

### Example 3: Generate Traceability Matrix

```bash
python3 scripts/generate.py rtm \
  --project "实验室系统" \
  --system "LIMS v3.0" \
  --category 4 \
  --urs-file ./URS-001.md \
  --fs-file ./FS-001.md \
  --output ./validation/
```
