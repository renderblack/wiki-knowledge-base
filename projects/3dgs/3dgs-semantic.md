---
title: 3DGS 语义理解
created: 2026-04-19
updated: 2026-04-19
type: project
tags: [3dgs, semantic-segmentation, language-gs, computer-vision]
sources: []
---

# 3DGS 语义理解

## 概述

在 3DGS 几何表示上**叠加语义层**，实现"这个桥墩完成度多少"的量化理解，而不仅是视觉效果。

## 核心方法

| 方法 | 特点 |
|------|------|
| **Language 3DGS** | 嵌入VLM语义特征，支持开放词汇查询 |
| **NG-GS** | NeRF引导的3DGS语义分割 |
| **CoLaSplat** | 语言3DGS压缩版（ICLR 2026） |
| **TokenGS** | 可学习Token解耦高斯预测 |

## 语义分割任务

| 任务 | 说明 |
|------|------|
| 3D 语义分割 | 点/基元→类别标签 |
| 开放词汇查询 | "找出所有未完成的桥墩" |
| 实例分割 | 单个物体区分 |

## 与航拍图像识别的关系

- **[[drone-image-recognition|航拍图像识别]]** — 2D 图像层面的量化
- **语义 3DGS** — 3D 空间层面的量化（更精确的位置/体积）

两者结合：2D 快速初筛 → 3D 精准量化

## 相关方向
- [[3d-scene-recognition|三维场景识别]] — 通用3D语义理解
- [[3dgs-editing|编辑与生成]] — 语义驱动的编辑
