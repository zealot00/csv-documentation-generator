# 风险评估 / Risk Assessment

| 属性 / Attribute | 内容 / Content |
|-----------------|----------------|
| 文档编号 / Document ID | {DOC_ID} |
| 版本 / Version | {VERSION} |
| 日期 / Date | {DATE} |
| 作者 / Author | {AUTHOR} |
| 审核 / Reviewer | {REVIEWER} |
| 批准 / Approver | {APPROVER} |
| 系统名称 / System Name | {SYSTEM_NAME} |
| GAMP 分类 / GAMP Category | Category {GAMP_CATEGORY} |

---

## 1. 目的 / Purpose

本文档对 {SYSTEM_NAME} 系统进行风险评估，识别潜在风险，评估风险等级，并制定风险缓解措施。

This document presents the risk assessment for {SYSTEM_NAME}, identifying potential risks, evaluating risk levels, and defining risk mitigation measures.

## 2. 范围 / Scope

### 2.1 关键功能 / Critical Functions

本风险评估涵盖以下关键功能:

{CRITICAL_FUNCTIONS:-数据录入, 审计追踪, 权限控制, 数据存储, 报告生成}

### 2.2 评估方法 / Assessment Method

采用 FMEA (Failure Mode and Effects Analysis) 方法进行风险评估。

## 3. 风险评估标准 / Risk Assessment Criteria

### 3.1 严重性等级 / Severity Levels

| 等级 / Level | 描述 / Description | 影响 / Impact |
|-------------|-------------------|--------------|
| 严重 / Critical (5) | 系统故障导致产品召回或严重合规问题 | 严重 |
| 高 / High (4) | 系统故障导致主要功能丧失 | 重大 |
| 中 / Medium (3) | 系统故障导致部分功能受影响 | 中等 |
| 低 / Low (2) | 系统故障导致次要功能受影响 | 轻微 |
| 可忽略 / Negligible (1) | 几乎无影响 | 极小 |

### 3.2 可能性等级 / Likelihood Levels

| 等级 / Level | 描述 / Description | 发生频率 / Frequency |
|-------------|-------------------|---------------------|
| 频繁 / Frequent (5) | 几乎每次使用都发生 | > 1/天 |
| 可能 / Probable (4) | 经常发生 | 1/周 - 1/天 |
| 偶尔 / Occasional (3) | 偶尔发生 | 1/月 - 1/周 |
| 罕见 / Remote (2) | 很少发生 | 1/年 - 1/月 |
| 不可能 / Improbable (1) | 几乎不可能 | < 1/年 |

### 3.3 可检测性等级 / Detectability Levels

| 等级 / Level | 描述 / Description |
|-------------|-------------------|
| 几乎不可能 / Almost Impossible (5) | 风险几乎不可能被发现 |
| 困难 / Difficult (4) | 需要专门工具或方法检测 |
| 一般 / Moderate (3) | 标准测试可以检测 |
| 容易 / Easy (2) | 日常监控可以检测 |
| 几乎肯定 / Almost Certain (1) | 立即可检测 |

### 3.4 风险优先级 / Risk Priority Number (RPN)

RPN = 严重性 × 可能性 × 可检测性

| RPN 范围 | 风险等级 | 行动要求 |
|----------|----------|----------|
| 1-25 | 低风险 / Low | 接受，可不采取行动 |
| 26-50 | 中风险 / Medium | 需要关注，制定缓解措施 |
| 51-75 | 高风险 / High | 必须采取缓解措施 |
| 76-125 | 严重风险 / Critical | 立即采取行动，暂停上线 |

## 4. 风险评估 / Risk Assessment

### 4.1 数据完整性风险 / Data Integrity Risks

| ID | 风险描述 / Risk Description | 严重性 | 可能性 | 可检测性 | RPN | 风险等级 | 缓解措施 / Mitigation |
|----|---------------------------|--------|--------|----------|-----|----------|---------------------|
| RA-DI-001 | 数据意外删除导致信息丢失 | 4 | 2 | 3 | 24 | 低 | 定期备份,回收站功能 |
| RA-DI-002 | 数据未同步导致不一致 | 3 | 2 | 2 | 12 | 低 | 事务机制,一致性检查 |
| RA-DI-003 | 审计追踪被篡改 | 5 | 1 | 3 | 15 | 低 | 只读存储,完整性校验 |

### 4.2 系统可用性风险 / System Availability Risks

| ID | 风险描述 / Risk Description | 严重性 | 可能性 | 可检测性 | RPN | 风险等级 | 缓解措施 / Mitigation |
|----|---------------------------|--------|--------|----------|-----|----------|---------------------|
| RA-AV-001 | 服务器故障导致系统不可用 | 4 | 2 | 2 | 16 | 低 | HA 集群,故障转移 |
| RA-AV-002 | 网络中断导致无法访问 | 3 | 2 | 2 | 12 | 低 | 冗余网络,离线模式 |

### 4.3 安全性风险 / Security Risks

| ID | 风险描述 / Risk Description | 严重性 | 可能性 | 可检测性 | RPN | 风险等级 | 缓解措施 / Mitigation |
|----|---------------------------|--------|--------|----------|-----|----------|---------------------|
| RA-SC-001 | 未授权访问导致数据泄露 | 5 | 2 | 3 | 30 | 中 | 强密码策略,多因素认证 |
| RA-SC-002 | 权限控制不当导致越权操作 | 4 | 2 | 3 | 24 | 低 | RBAC,权限审计 |
| RA-SC-003 | 敏感数据未加密导致泄露 | 5 | 2 | 3 | 30 | 中 | 数据加密,脱敏处理 |

### 4.4 合规性风险 / Compliance Risks

| ID | 风险描述 / Risk Description | 严重性 | 可能性 | 可检测性 | RPN | 风险等级 | 缓解措施 / Mitigation |
|----|---------------------------|--------|--------|----------|-----|----------|---------------------|
| RA-CP-001 | 21 CFR Part 11 不合规 | 5 | 2 | 3 | 30 | 中 | Part 11 合规性验证 |
| RA-CP-002 | 数据保留不符合法规要求 | 4 | 2 | 2 | 16 | 低 | 数据保留策略,自动归档 |

## 5. 风险缓解措施 / Risk Mitigation

### 5.1 已采取的措施 / Implemented Mitigations

| 风险 ID / Risk ID | 缓解措施 / Mitigation | 责任部门 / Owner | 完成日期 / Completion Date |
|------------------|---------------------|-----------------|--------------------------|
| | | | |

### 5.2 残余风险 / Residual Risks

| 风险 ID / Risk ID | 残余风险描述 / Residual Risk | RPN (缓解后) | 接受决定 / Acceptance Decision |
|------------------|----------------------------|-------------|------------------------------|
| | | | QA 批准 / QA Approval |

## 6. 风险评估总结 / Risk Assessment Summary

| 风险类别 / Risk Category | 总风险数 | 高风险 | 中风险 | 低风险 |
|------------------------|---------|--------|--------|--------|
| 数据完整性 / Data Integrity | | | | |
| 系统可用性 / Availability | | | | |
| 安全性 / Security | | | | |
| 合规性 / Compliance | | | | |
| **总计 / Total** | | | | |

## 7. 批准 / Approval

| 角色 / Role | 签名 / Signature | 日期 / Date |
|-------------|-----------------|-------------|
| 系统负责人 / System Owner | | |
| IT 负责人 / IT Lead | | |
| QA 负责人 / QA Lead | | |
| 质量总监 / Quality Director | | |
