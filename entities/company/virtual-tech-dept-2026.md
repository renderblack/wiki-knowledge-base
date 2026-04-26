---
title: 虚拟技术部
created: 2026-04-19
updated: 2026-04-25
type: entity
tags: [company, product]
sources: []
related: [[entities/company/construction-progress-viz|兴土智瞰]], [[entities/company/unityplate|UnityPlate]], [[projects/enterprise-software-implementation/PROGRESS|集成平台]]
---

# 虚拟技术部

浙江兴土桥梁专用装备制造有限公司旗下虚拟技术部，成立于2025年，由Bolt老大负责。

## 两大核心产品

| 产品 | 版本 | 状态 | 定位 |
|------|------|------|------|
| [[entities/company/construction-progress-viz|兴土智瞰]] | V1.8 | ✅ 已交付 | 施工进度「看得见/预警/追溯/精细化」，软硬件协同 |
| [[entities/company/unityplate|UnityPlate]] | V1.3 | ✅ 已交付 | 交通工程三维可视化，标前协同+数据资产+无人机管理 |

**兴土智瞰**侧重施工过程管理，**UnityPlate**侧重标前协同+GIS+航测，两者可联动。

## 技术栈

| 产品 | 技术栈 |
|------|--------|
| 兴土智瞰 | Java + SQL Server + Tomcat + 微信小程序 + 3D可视化 |
| UnityPlate | Spring Boot + SQL Server + Redis + Mars3D + MinIO |

## 战略方向

- **集成平台**：整合兴土智瞰和UnityPlate能力，构建统一数据底座（参考 [[projects/enterprise-software-implementation/PROGRESS|集成平台战略执行平台]]）
- **AI赋能**：CAD智能化（图纸识别/生成）、AI Agent生态
- **3DGS**：三维重建、航拍图像处理、524国道项目

## 当前挑战

- 公司数据治理基础薄弱，主数据未统一
- 集成平台需要的多项硬条件尚未就绪（MDM/事件总线/统一身份）
- 差序格局文化下，系统落地面临组织阻力
