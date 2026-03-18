# 安装确认 / Installation Qualification (IQ)

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

本文档验证 {SYSTEM_NAME} 系统的硬件、软件和网络环境已正确安装和配置，满足预定的规格要求。

This document verifies that the hardware, software, and network environment for {SYSTEM_NAME} have been properly installed and configured according to specifications.

## 2. 范围 / Scope

IQ 确认范围包括:

- 硬件安装确认
- 软件安装确认
- 网络配置确认
- 系统环境确认
- 第三方组件确认

## 3. 参考文档 / Reference Documents

| 文档 / Document | 文档编号 / Document ID | 版本 / Version |
|---------------|---------------------|---------------|
| 技术规格 / TS | | |
| 风险评估 / RA | | |

## 4. 硬件确认 / Hardware Qualification

### 4.1 服务器硬件 / Server Hardware

| 序号 / No. | 检查项目 / Check Item | 预期结果 / Expected Result | 实际结果 / Actual Result | 状态 / Status | 备注 / Notes |
|-----------|---------------------|--------------------------|------------------------|--------------|-------------|
| IQ-001 | 服务器型号 / Server Model | | | Pass/Fail | |
| IQ-002 | CPU 规格 / CPU Specification | | | Pass/Fail | |
| IQ-003 | 内存容量 / Memory Capacity | | | Pass/Fail | |
| IQ-004 | 硬盘容量 / Storage Capacity | | | Pass/Fail | |
| IQ-005 | 网卡配置 / Network Card Configuration | | | Pass/Fail | |

### 4.2 存储设备 / Storage Devices

| 序号 / No. | 检查项目 / Check Item | 预期结果 / Expected Result | 实际结果 / Actual Result | 状态 / Status | 备注 / Notes |
|-----------|---------------------|--------------------------|------------------------|--------------|-------------|
| IQ-010 | 存储设备型号 / Storage Model | | | Pass/Fail | |
| IQ-011 | 存储容量 / Storage Capacity | | | Pass/Fail | |
| IQ-012 | RAID 配置 / RAID Configuration | | | Pass/Fail | |

## 5. 软件确认 / Software Qualification

### 5.1 操作系统 / Operating System

| 序号 / No. | 检查项目 / Check Item | 预期结果 / Expected Result | 实际结果 / Actual Result | 状态 / Status | 备注 / Notes |
|-----------|---------------------|--------------------------|------------------------|--------------|-------------|
| IQ-020 | 操作系统类型 / OS Type | | | Pass/Fail | |
| IQ-021 | 操作系统版本 / OS Version | | | Pass/Fail | |
| IQ-022 | 操作系统补丁 / OS Patches | | | Pass/Fail | |
| IQ-023 | 系统主机名 / Hostname | | | Pass/Fail | |
| IQ-024 | IP 地址 / IP Address | | | Pass/Fail | |

### 5.2 中间件 / Middleware

| 序号 / No. | 检查项目 / Check Item | 预期结果 / Expected Result | 实际结果 / Actual Result | 状态 / Status | 备注 / Notes |
|-----------|---------------------|--------------------------|------------------------|--------------|-------------|
| IQ-030 | 中间件类型 / Middleware Type | | | Pass/Fail | |
| IQ-031 | 中间件版本 / Middleware Version | | | Pass/Fail | |

### 5.3 数据库 / Database

| 序号 / No. | 检查项目 / Check Item | 预期结果 / Expected Result | 实际结果 / Actual Result | 状态 / Status | 备注 / Notes |
|-----------|---------------------|--------------------------|------------------------|--------------|-------------|
| IQ-040 | 数据库类型 / Database Type | | | Pass/Fail | |
| IQ-041 | 数据库版本 / Database Version | | | Pass/Fail | |
| IQ-042 | 数据库字符集 / Database Charset | | | Pass/Fail | |

### 5.4 应用程序 / Application

| 序号 / No. | 检查项目 / Check Item | 预期结果 / Expected Result | 实际结果 / Actual Result | 状态 / Status | 备注 / Notes |
|-----------|---------------------|--------------------------|------------------------|--------------|-------------|
| IQ-050 | 应用程序版本 / Application Version | | | Pass/Fail | |
| IQ-051 | 安装路径 / Installation Path | | | Pass/Fail | |
| IQ-052 | 文件完整性 / File Integrity | | | Pass/Fail | |

## 6. 网络配置确认 / Network Configuration

| 序号 / No. | 检查项目 / Check Item | 预期结果 / Expected Result | 实际结果 / Actual Result | 状态 / Status | 备注 / Notes |
|-----------|---------------------|--------------------------|------------------------|--------------|-------------|
| IQ-060 | 防火墙规则 / Firewall Rules | | | Pass/Fail | |
| IQ-061 | 端口开放 / Port Opening | | | Pass/Fail | |
| IQ-062 | DNS 配置 / DNS Configuration | | | Pass/Fail | |
| IQ-063 | 网络连通性 / Network Connectivity | | | Pass/Fail | |

## 7. 第三方组件确认 / Third-Party Components

| 序号 / No. | 组件名称 / Component Name | 版本 / Version | 供应商 / Vendor | 状态 / Status | 备注 / Notes |
|-----------|------------------------|---------------|----------------|--------------|-------------|
| IQ-070 | | | | Pass/Fail | |
| IQ-071 | | | | Pass/Fail | |

## 8. 环境要求确认 / Environment Requirements

| 序号 / No. | 检查项目 / Check Item | 规格要求 / Specification | 实际值 / Actual | 状态 / Status |
|-----------|---------------------|---------------------|---------------|--------------|
| IQ-080 | 机房温度 / Server Room Temperature | 18-25°C | | Pass/Fail |
| IQ-081 | 机房湿度 / Server Room Humidity | 40-70% | | Pass/Fail |
| IQ-082 | 电源供应 / Power Supply | UPS 保护 | | Pass/Fail |

## 9. IQ 总结 / IQ Summary

### 9.1 测试结果统计 / Test Results Summary

| 项目 / Item | 总数 / Total | 通过 / Pass | 失败 / Fail | 通过率 / Pass Rate |
|------------|-------------|------------|------------|-------------------|
| 硬件 / Hardware | | | | |
| 软件 / Software | | | | |
| 网络 / Network | | | | |
| **总计 / Total** | | | | |

### 9.2 偏差记录 / Deviation Records

| 偏差编号 / Deviation ID | 描述 / Description | 影响评估 / Impact Assessment | 纠正措施 / Corrective Action | 状态 / Status |
|----------------------|-------------------|--------------------------|---------------------------|--------------|
| | | | | Open/Closed |

## 10. 结论 / Conclusion

| 结论 / Conclusion | |
|------------------|---|
| IQ 测试完成日期 / IQ Completion Date | |
| IQ 测试结果 / IQ Result | 通过 Pass / 失败 Fail / 有条件通过 Conditional Pass |
| 系统是否可以进入 OQ / System Proceed to OQ | 是 Yes / 否 No |

## 11. 批准 / Approval

| 角色 / Role | 签名 / Signature | 日期 / Date |
|-------------|-----------------|-------------|
| 测试工程师 / Test Engineer | | |
| IT 负责人 / IT Lead | | |
| 系统负责人 / System Owner | | |
| QA 审核员 / QA Reviewer | | |
