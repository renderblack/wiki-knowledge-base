---
title: 3DGS 编辑与生成
created: 2026-04-19
updated: 2026-04-19
type: project
tags: [3dgs, editing, text-to-3d, generation, computer-vision]
sources: []
---

# 3DGS 编辑与生成

## 概述

在 3DGS 表示上进行**可控编辑**和**文本生成**，实现"改个颜色/换个角度"类的交互操作。

## 核心方法

| 方法 | 特点 |
|------|------|
| **GaussianEditor** | Swift可控3D编辑 |
| **Text-to-3D (LucidDreamer)** | 文本→3DGS场景 |
| **DOC-GS** | 稀疏视角条件下的编辑 |

## 应用场景
- 施工现场对比（修复前后）
- 设计方案可视化
- 施工模拟动画

## 相关方向
- [[cad-blueprint-recognition|CAD图纸识别]] — 2D图纸→3DGS联动
- [[3dgs-surface|表面重建]] — 编辑后的mesh导出
