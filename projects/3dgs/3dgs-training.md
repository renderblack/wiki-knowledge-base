---
title: 3DGS 训练加速
created: 2026-04-19
updated: 2026-04-19
type: project
tags: [3dgs, training, speed-up, computer-vision]
sources: []
---

# 3DGS 训练加速

## 概述

3DGS 原始训练依赖 SfM 预处理（C蛮）、迭代优化，场景大时耗时数小时。训练加速是工程落地的核心瓶颈。

## 主流方法

| 方法 | 训练时间 | 核心创新 | 来源 |
|------|---------|----------|------|
| **FastGS** | **100秒** | 全新训练范式，大幅减少迭代 | CVPR 2026 |
| **LongSplat** | 分钟级 | 长序列处理，适合大场景 | — |
| **Gaustudio** | 可配置 | 模块化框架，支持多种加速策略 | 开源工具 |

## FastGS（CVPR 2026）

**核心突破**：从数小时压缩到 100 秒量级，训练速度提升 50~100×。

关键思路（待深入研究）：
- 重新设计初始化策略
- 减少迭代次数
- 并行化计算

## Gaustudio 模块化框架

模块化设计，支持独立升级各组件：
- `GaussianRasterizer` — 渲染
- `MipEncoder` — 多尺度编码
- `Densifier` — 致密化控制
- `AnchorManager` — 基元管理

## 工程参考

| 工具 | 用途 |
|------|------|
| COLMAP | SfM 预处理（金字塔） |
| 优云智算 | 云端 5090 GPU |
| gaustudio | 模块化训练 |

## 相关方向
- [[3dgs-compression|模型压缩]] — 训练后压缩
- [[3dgs-large-scale|大规模场景]] — 大场景训练
