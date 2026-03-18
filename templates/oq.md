# 操作确认 / Operational Qualification (OQ)

| 属性 / Attribute | 内容 / Content |
|-----------------|----------------|
| 文档编号 / Document ID | {DOC_ID} |
| 版本 / Version | {VERSION} |
| 日期 / Date | {DATE} |
| 作者 / Author | {AUTHOR} |
| 审核 / Reviewer | {REVIEWER} |
| 批准 / Approver | {APPROVER} |
| 系统名称 / System Name | {SYSTEM_NAME} |
| 系统版本 / System Version | {SYSTEM_VERSION} |
| GAMP 分类 / GAMP Category | Category {GAMP_CATEGORY} |

---

## 1. 目的 / Purpose

本文档验证 {SYSTEM_NAME} 系统的各项功能按照用户需求规格 (URS) 和功能规格 (FS) 正确运行，满足预定的操作要求。

This document verifies that {SYSTEM_NAME} functions operate correctly according to URS and FS, meeting the specified operational requirements.

## 2. 范围 / Scope

OQ 确认范围包括:

- 系统功能测试
- 用户界面测试
- 数据处理测试
- 接口功能测试
- 权限控制测试
- 审计追踪测试
- 备份恢复测试

## 3. 参考文档 / Reference Documents

| 文档 / Document | 文档编号 / Document ID | 版本 / Version |
|---------------|---------------------|---------------|
| 用户需求规格 / URS | | |
| 功能规格 / FS | | |
| 风险评估 / RA | | |
| 安装确认 / IQ | | |

## 4. OQ 测试用例 / OQ Test Cases

### 4.1 用户管理测试 / User Management Tests

| 用例 ID / Test Case ID | 测试描述 / Test Description | 预置条件 / Pre-condition | 测试步骤 / Test Steps | 预期结果 / Expected Result | 实际结果 / Actual Result | 状态 / Status |
|------------------------|--------------------------|------------------------|---------------------|-------------------------|-----------------------|--------------|
| OQ-UM-001 | 用户登录测试 / User Login Test | 系统正常运行 | 1. 输入用户名和密码 2. 点击登录 | 成功登录系统 | | Pass/Fail |
| OQ-UM-002 | 密码复杂度验证 / Password Complexity | 系统正常运行 | 输入不符合复杂度要求的密码 | 系统拒绝并提示错误 | | Pass/Fail |
| OQ-UM-003 | 账户锁定测试 / Account Lockout | 系统正常运行 | 连续输入错误密码5次 | 账户被锁定 | | Pass/Fail |
| OQ-UM-004 | 角色权限测试 / Role Permission | 已配置角色和权限 | 使用不同角色登录系统 | 各角色功能权限正确 | | Pass/Fail |

### 4.2 审计追踪测试 / Audit Trail Tests

| 用例 ID / Test Case ID | 测试描述 / Test Description | 预置条件 / Pre-condition | 测试步骤 / Test Steps | 预期结果 / Expected Result | 实际结果 / Actual Result | 状态 / Status |
|------------------------|--------------------------|------------------------|---------------------|-------------------------|-----------------------|--------------|
| OQ-AT-001 | 数据创建审计 / Data Creation Audit | 系统正常运行 | 创建一条记录 | 审计记录自动生成 | | Pass/Fail |
| OQ-AT-002 | 数据修改审计 / Data Modification Audit | 系统正常运行 | 修改一条记录 | 审计记录记录修改内容 | | Pass/Fail |
| OQ-AT-003 | 数据删除审计 / Data Deletion Audit | 系统正常运行 | 删除一条记录 | 审计记录不可被删除 | | Pass/Fail |
| OQ-AT-004 | 审计记录导出 / Audit Export | 系统正常运行 | 导出审计记录 | 导出成功且格式正确 | | Pass/Fail |

### 4.3 数据管理测试 / Data Management Tests

| 用例 ID / Test Case ID | 测试描述 / Test Description | 预置条件 / Pre-condition | 测试步骤 / Test Steps | 预期结果 / Expected Result | 实际结果 / Actual Result | 状态 / Status |
|------------------------|--------------------------|------------------------|---------------------|-------------------------|-----------------------|--------------|
| OQ-DM-001 | 数据备份测试 / Data Backup | 系统正常运行 | 执行数据备份 | 备份成功生成备份文件 | | Pass/Fail |
| OQ-DM-002 | 数据恢复测试 / Data Recovery | 已完成数据备份 | 执行数据恢复 | 数据成功恢复到备份点 | | Pass/Fail |
| OQ-DM-003 | 数据导入测试 / Data Import | 准备导入文件 | 执行数据导入 | 数据成功导入系统 | | Pass/Fail |
| OQ-DM-004 | 数据导出测试 / Data Export | 系统有数据 | 执行数据导出 | 数据成功导出为指定格式 | | Pass/Fail |

### 4.4 权限控制测试 / Access Control Tests

| 用例 ID / Test Case ID | 测试描述 / Test Description | 预置条件 / Pre-condition | 测试步骤 / Test Steps | 预期结果 / Expected Result | 实际结果 / Actual Result | 状态 / Status |
|------------------------|--------------------------|------------------------|---------------------|-------------------------|-----------------------|--------------|
| OQ-AC-001 | 未授权访问测试 / Unauthorized Access | 未登录状态 | 尝试直接访问系统页面 | 页面重定向到登录页 | | Pass/Fail |
| OQ-AC-002 | 越权操作测试 / Privilege Escalation | 普通用户登录 | 尝试访问管理员功能 | 访问被拒绝 | | Pass/Fail |
| OQ-AC-003 | 会话超时测试 / Session Timeout | 用户已登录 | 30分钟无操作 | 自动登出系统 | | Pass/Fail |

### 4.5 接口测试 / Interface Tests

| 用例 ID / Test Case ID | 测试描述 / Test Description | 预置条件 / Pre-condition | 测试步骤 / Test Steps | 预期结果 / Expected Result | 实际结果 / Actual Result | 状态 / Status |
|------------------------|--------------------------|------------------------|---------------------|-------------------------|-----------------------|--------------|
| OQ-API-001 | API 接口测试 / API Test | 接口服务正常运行 | 调用系统 API | 返回正确响应 | | Pass/Fail |
| OQ-API-002 | 接口错误处理 / Error Handling | 接口服务正常运行 | 发送错误请求 | 返回正确错误信息 | | Pass/Fail |

## 5. OQ 测试结果统计 / OQ Test Results Summary

| 测试类别 / Test Category | 总用例数 / Total | 通过 / Pass | 失败 / Fail | 通过率 / Pass Rate |
|------------------------|-----------------|------------|------------|-------------------|
| 用户管理 / User Management | | | | |
| 审计追踪 / Audit Trail | | | | |
| 数据管理 / Data Management | | | | |
| 权限控制 / Access Control | | | | |
| 接口测试 / Interfaces | | | | |
| **总计 / Total** | | | | |

## 6. 偏差记录 / Deviation Records

| 偏差编号 / Deviation ID | 测试用例 / Test Case | 描述 / Description | 影响评估 / Impact | 纠正措施 / Corrective Action | 状态 / Status |
|----------------------|-------------------|-------------------|------------------|---------------------------|--------------|
| | | | | | Open/Closed |

## 7. 结论 / Conclusion

| 结论 / Conclusion | |
|------------------|---|
| OQ 测试完成日期 / OQ Completion Date | |
| OQ 测试结果 / OQ Result | 通过 Pass / 失败 Fail / 有条件通过 Conditional Pass |
| 系统是否可以进入 PQ / System Proceed to PQ | 是 Yes / 否 No |

## 8. 批准 / Approval

| 角色 / Role | 签名 / Signature | 日期 / Date |
|-------------|-----------------|-------------|
| 测试工程师 / Test Engineer | | |
| 系统负责人 / System Owner | | |
| IT 负责人 / IT Lead | | |
| QA 审核员 / QA Reviewer | | |
| QA 批准人 / QA Approver | | |
