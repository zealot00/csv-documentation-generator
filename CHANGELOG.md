# Changelog - CSV 文档生成器

所有重要的版本更新都会记录在此文件中。

**[English Version](CHANGELOG_en.md)**

## [1.0.0] - 2026-03-18

### Added

#### 核心功能
- **9 种验证文档模板** (VP, URS, FS, TS, RA, IQ, OQ, PQ, VSR)
- **专业 GMP 样式 Word 生成器**
  - 表头颜色: 钢蓝色 (#4682B4) + 白色文字
  - 优先级标记: `[必须]`, `[应该]`, `[Pass]`, `[Fail]`
  - 封面页 + 审批签字表
  - 交替行颜色
- **中英双语支持**

#### AI Agent 智能需求追踪系统
- **Agent 模式检测** (`scripts/agent.py`)
  - 自动检测 OpenClaw/OpenCode/Codex 等 Agent 类型
  - 支持 `interactive` (半自动) 和 `autonomous` (全自动) 模式
  - 环境变量优先级: `CSV_DOCS_MODE` > Agent 环境变量 > Git 配置 > 项目配置

- **需求解析器** (`scripts/requirements/parser.py`)
  - 从代码注释解析需求: `@req`, `@requirement`, `# URS-001`
  - 自动识别电子签名需求 (21 CFR Part 11)
  - 关键词: 签名、审核、审批、sign、approve 等

- **风险评估器** (`scripts/requirements/risk_analyzer.py`)
  - RPN/FMEA 方法论
  - 自动严重性/可能性/可检测性评估
  - 基于 GAMP Category 的风险计算
  - 标准缓解措施建议

- **Git 关联器** (`scripts/requirements/linker.py`)
  - 自动解析提交信息中的需求 ID
  - 需求 ↔ 提交 可追溯性矩阵

- **测试结果解析器** (`scripts/tests/parser.py`)
  - 支持 JUnit XML、pytest JSON、NUnit XML 格式
  - 自动关联需求与测试状态
  - 测试覆盖率统计

- **文档自动填充器** (`scripts/fill/filler.py`)
  - 从需求数据库自动填充模板变量
  - 文档完整性验证

- **审计日志** (`scripts/audit/log.py`)
  - 所有操作完整记录
  - 支持导出为 PDF (文本格式)
  - 按操作类型、模式筛选

#### CLI 统一入口 (`scripts/cli.py`)

```bash
csv-docs init              # 初始化项目配置
csv-docs agent             # 检测 Agent 模式
csv-docs agent --set autonomous  # 设置为全自动模式
csv-docs parse ./src       # 解析代码需求
csv-docs status            # 查看状态
csv-docs add "描述"        # 添加需求
csv-docs risk              # 运行风险分析
csv-docs test --results ./ # 解析测试结果
csv-docs generate vp       # 生成文档
csv-docs audit            # 查看审计日志
```

#### 合规支持
- **GAMP 5 Second Edition** 验证生命周期
- **21 CFR Part 11** 电子记录与电子签名
- **EU Annex 11** 计算机化系统
- **ALCOA+** 数据完整性原则

### Configuration

#### 项目配置 (`.csv-docs-config.json`)
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

#### 需求数据库 (`requirements.json`)
- 存储所有需求、风险、测试结果、提交关联

#### 审计日志 (`audit-log.json`)
- 所有操作的完整审计轨迹

---

## [0.1.0] - 初始版本

### Added
- 基础文档模板
- Word 生成器
- Excel 生成器
- GAMP 5 参考文档
- 21 CFR Part 11 参考文档
- EU Annex 11 参考文档
- 数据完整性参考文档

---

## 版本格式

版本格式遵循 [Semantic Versioning](https://semver.org/):
- **MAJOR**: 不兼容的 API 变更
- **MINOR**: 向后兼容的功能新增
- **PATCH**: 向后兼容的问题修复
