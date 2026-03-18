# CSV 文档生成器 (CSV Documentation Generator)

计算机化系统验证 (Computerized System Validation, CSV) 文档自动生成工具。支持中英双语模板，适用于制药、医疗器械行业的验证文档编制。

## 概述

本工具提供 12 种验证文档模板，支持：
- **中英双语** (Chinese/English)
- **Word/Excel** 格式输出
- **GAMP 5** 分类验证策略
- **21 CFR Part 11** 合规检查
- **ALCOA+** 数据完整性原则

## 支持的系统类型

| 系统类型 | GAMP 分类 | 适用文档 |
|----------|-----------|----------|
| EDC (电子数据采集) | Category 4/5 | 全部 12 种 |
| CTMS (临床试验管理系统) | Category 4 | VP, URS, FS, RA, IQ, OQ, RTM |
| LIMS (实验室信息管理系统) | Category 4/5 | 全部 12 种 |
| MES (制造执行系统) | Category 4 | 全部 12 种 |
| ERP (企业资源计划) | Category 4 | VP, URS, RA, IQ, OQ |
| SCADA/DCS | Category 2/3 | VP, URS, IQ, OQ, PQ |
| 自研软件 | Category 3/4 | VP, URS, RA, IQ, OQ |

## 快速开始

### 安装

```bash
# 克隆或下载本工具
cd ~/Code/skills/csv-documentation-generator

# 安装 Python 依赖
pip install -r requirements.txt

# 验证安装
python3 scripts/generate.py --help
```

### 基本用法

```bash
# 生成验证计划 (Validation Plan)
python3 scripts/generate.py vp \
  --project "XX临床系统" \
  --system "EDC v1.0" \
  --category 4 \
  --output ./output/

# 生成用户需求规格 (URS)
python3 scripts/generate.py urs \
  --project "XX临床系统" \
  --system "CTMS v2.0" \
  --category 4 \
  --bilingual true \
  --output ./output/

# 生成完整验证包
python3 scripts/generate.py all \
  --project "XX系统" \
  --system "MES v1.0" \
  --category 4 \
  --output ./validation/
```

## 命令参考

### 可用命令

| 命令 | 说明 | 输出格式 |
|------|------|----------|
| `generate.py vp` | 验证计划 | .docx |
| `generate.py urs` | 用户需求规格 | .docx |
| `generate.py fs` | 功能规格 | .docx |
| `generate.py ts` | 技术规格 | .docx |
| `generate.py ra` | 风险评估 (FMEA) | .docx |
| `generate.py iq` | 安装确认 | .docx |
| `generate.py oq` | 操作确认 | .docx |
| `generate.py pq` | 性能确认 | .docx |
| `generate.py rtm` | 追溯矩阵 | .xlsx |
| `generate.py vsr` | 验证总结报告 | .docx |
| `generate.py checklist` | 验证检查清单 | .xlsx |
| `generate.py test-case` | 测试用例模板 | .xlsx |
| `generate.py all` | 完整验证包 | .docx / .xlsx |

### 命令选项

| 选项 | 说明 | 必填 |
|------|------|------|
| `--project` | 项目名称 | 是 |
| `--system` | 系统名称和版本 | 是 |
| `--category` | GAMP 分类 (1-5) | 是 |
| `--bilingual` | 双语模板 (默认: true) | 否 |
| `--output` | 输出目录 | 是 |
| `--format` | 输出格式: docx, xlsx, both (默认: both) | 否 |

### 示例

#### 示例 1: 生成 CTMS 用户需求

```bash
python3 scripts/generate.py urs \
  --project "临床试验管理系统" \
  --system "CTMS v2.0" \
  --category 4 \
  --bilingual true \
  --output ./validation/
```

#### 示例 2: 生成风险评估

```bash
python3 scripts/generate.py ra \
  --project "质量管理系统" \
  --system "QMS v1.5" \
  --category 4 \
  --critical-functions "数据录入,审计追踪,权限控制" \
  --output ./validation/
```

#### 示例 3: 生成追溯矩阵

```bash
python3 scripts/generate.py rtm \
  --project "实验室系统" \
  --system "LIMS v3.0" \
  --category 4 \
  --urs-file ./URS-001.md \
  --fs-file ./FS-001.md \
  --output ./validation/
```

## 模板变量

常用变量说明：

| 变量 | 说明 | 示例 |
|------|------|------|
| `{PROJECT_NAME}` | 项目名称 | 临床试验系统 |
| `{SYSTEM_NAME}` | 系统名称 | EDC v1.0 |
| `{SYSTEM_VERSION}` | 系统版本 | 1.0 |
| `{GAMP_CATEGORY}` | GAMP 分类 | 4 |
| `{DOC_ID}` | 文档编号 | URS-001 |
| `{DATE}` | 文档日期 | 2024-01-01 |
| `{AUTHOR}` | 文档作者 | 张三 |
| `{REVIEWER}` | 审核人 | 李四 |
| `{APPROVER}` | 批准人 | 王五 |

## 法规合规

### GAMP 5 分类

| 分类 | 说明 | 验证策略 |
|------|------|----------|
| 1 | 操作系统 | 遗留系统 |
| 2 | 固件 | 简化验证 |
| 3 | 商用现货 (COTS) | 基于风险 |
| 4 | 配置型 COTS | 基于风险 |
| 5 | 定制/关键系统 | 完整验证 |

### 关键法规

本工具包含以下法规合规检查：

- **21 CFR Part 11**: 电子记录与电子签名
  - 审计追踪要求
  - 电子签名要求
  - 系统访问控制

- **EU Annex 11**: 计算机化系统
  - 验证要求
  - 数据完整性
  - 变更控制

- **ALCOA+**: 数据完整性原则
  - Attributable (可归属)
  - Legible (可读)
  - Contemporaneous (同步)
  - Original (原始)
  - Accurate (准确) + Complete, Consistent, Enduring

## 文件结构

```
csv-documentation-generator/
├── SKILL.md                           # 主技能文件
├── README.md                          # 说明文档
├── requirements.txt                   # Python 依赖
├── scripts/
│   ├── __init__.py
│   ├── generate.py                   # 主入口脚本
│   ├── config.py                     # 配置管理
│   ├── word_generator.py             # Word 生成器
│   ├── excel_generator.py            # Excel 生成器
│   └── template_loader.py            # 模板加载器
├── templates/
│   ├── vp.md                        # 验证计划模板
│   ├── urs.md                       # 用户需求模板
│   ├── fs.md                        # 功能规格模板
│   ├── ts.md                        # 技术规格模板
│   ├── ra.md                        # 风险评估模板
│   ├── iq.md                        # 安装确认模板
│   ├── oq.md                        # 操作确认模板
│   ├── pq.md                        # 性能确认模板
│   ├── vsr.md                       # 验证总结模板
│   ├── test-case.xlsx               # 测试用例模板
│   └── checklist.xlsx                # 检查清单模板
└── references/
    ├── gamp-5.md                   # GAMP 5 参考
    ├── 21cfr-part11.md            # Part 11 参考
    ├── annex-11.md                # Annex 11 参考
    └── data-integrity.md          # 数据完整性参考
```

## 常见问题

### 问题 1: python-docx 未安装

**解决**:
```bash
pip install python-docx openpyxl
```

### 问题 2: 编码错误

**解决**: 确保终端使用 UTF-8 编码

### 问题 3: 模板未找到

**解决**: 确认在正确的目录下运行命令

## 参考文档

参考文档位于 `references/` 文件夹：

| 文件 | 说明 |
|------|------|
| `gamp-5.md` | GAMP 5 快速参考指南 |
| `21cfr-part11.md` | 21 CFR Part 11 关键要求 |
| `annex-11.md` | EU Annex 11 要求 |
| `data-integrity.md` | ALCOA+ 数据完整性原则 |

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！
