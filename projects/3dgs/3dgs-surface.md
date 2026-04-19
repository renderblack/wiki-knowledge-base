---
title: 3DGS 表面重建
created: 2026-04-19
updated: 2026-04-19
type: project
tags: [3dgs, surface-reconstruction, mesh, computer-vision]
sources: []
---

# 3DGS 表面重建

## 概述

3DGS 用高斯椭球表示体积云，**不适合直接提取精确几何面**。表面重建是将 GS 结果转换为 **mesh/点云** 供 CAD/BIM 使用。

## 核心方法

| 方法 | 特点 |
|------|------|
| **SuGaR** | 表面高斯，与 mesh 联合优化 |
| **GaussianEditor** | 可控编辑 + 表面编辑 |
| **MLS（Moving Least Squares）** | UE5 插件，高斯→碰撞体 |

## 工具链

| 工具 | 用途 |
|------|------|
| SuperSplat | GS 模型编辑 |
| Blender | Mesh 处理 |
| CloudCompare | 点云对比 |
| Unreal Engine 5 | 实时渲染 + MLS 插件 |

## 应用场景
- 竣工验收（GS模型 vs 设计BIM）
- 工程量测算
- 碰撞检测
