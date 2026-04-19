---
title: 3DGS 模型压缩
created: 2026-04-19
updated: 2026-04-19
type: project
tags: [3dgs, compression, quantization, pruning, computer-vision]
sources: [https://w-m.github.io/3dgs-compression-survey/, https://onlinelibrary.wiley.com/doi/10.1111/cgf.70078]
---

# 3DGS 模型压缩

## 概述

3DGS 原始模型通常包含 **10万~700万** 个高斯基元，存储体积从数百MB到数GB不等。压缩技术是**工程落地的关键门槛**。

## 三大技术路线

| 路线 | 核心手段 | 代表工作 |
|------|---------|----------|
| **剪枝 Pruning** | 删除不重要高斯，保留关键基元 | PUP 3D-GS（剪枝90%基元，3.56×加速） |
| **量化 Quantization** | 减少属性值精度（FP32→INT8等） | HAC++、EAGLES、HEMGS |
| **熵编码 Entropy Coding** | 利用属性相关性压缩编码 | ContextGS、CodecGS |

## 主流方法（按benchmark排名）

### 🏆 第一梯队（HAC系列）

| 方法 | 核心创新 | 最佳体积 | PSNR |
|------|---------|---------|------|
| **HAC++** | Hash-grid上下文 + 自适应量化 + 偏移掩码 | 0.8~8.7 MB | 33.76（Synthetic） |
| **HAC** | Hash-grid辅助上下文模型 | 5.4~16 MB | 33.24 |
| **HEMGS** | 混合熵模型 | 1.3~12.5 MB | 33.71 |

### 🥈 第二梯队

| 方法 | 核心创新 | 最佳体积 | PSNR |
|------|---------|---------|------|
| **ContextGS** | Anchor级自回归模型，分层预测 | 3.7~13.3 MB | — |
| **CodecGS** | Tri-plane + 视频编解码器（DCT熵建模） | 7.8~10.3 MB | 29.81 |
| **Compact3D** | K-means矢量量化，16K Gaussians | 12~18 MB | — |
| **EAGLES** | 颜色/旋转属性压缩（占80%+内存） | — | — |

### 前馈压缩（无需优化）

| 方法 | 特点 |
|------|------|
| **FCGS** | 免优化快速压缩，适合边缘部署 |
| **PCGS** | 渐进式量化，逐步细化精度 |

## 4DGS 动态压缩

动态场景（4DGS）的压缩额外面临**时间维度冗余**：

| 方法 | 压缩比 | 场景 |
|------|--------|------|
| Rate-Distortion Optimized 4DGS | **91×** vs Ex4DGS | 边缘设备→高性能平台 |

## 核心原理速览

### 高斯基元属性
每个高斯 = 7个基本属性 + SH系数（颜色）：

```
位置(3) + 协方差矩阵(3) + 不透明度(1) + SH系数(球谐, 颜色)
```

其中**颜色（SH）+ 旋转**占 80%+ 存储，是量化重点。

### 剪枝策略（PUP 3D-GS）
- 基于**不确定性敏感度分数**评估基元重要性
- **多轮剪枝-精调** pipeline（可适用于任意预训练模型）
- 剪枝 90% 基元仍保持高图像质量

### Hash-grid 上下文（HAC系列）
- 用 Hash-grid 特征辅助预测高斯属性
- 利用高斯属性与 Hash-grid 特征之间的**互信息**
- 自适应量化模块（AQM）动态调整量化步长

## 评测基准

| 数据集 | 特点 |
|--------|------|
| Mip-NeRF 360 | 360°室内外场景，最常用 |
| Tanks & Temples | 户外大规模场景 |
| Deep Blending | 室内挑战场景 |
| Synthetic NeRF | 控制合成场景 |

**关键指标**：PSNR（质量）、SSIM（结构相似度）、LPIPS（感知质量）、Size（MB）、b/G（每基元比特数）

## 工程落地要点

1. **体积目标**：移动端 < 10 MB，嵌入式 < 1 MB
2. **推理速度**：目标 > 30 FPS（实时渲染）
3. **精度损失**：可接受范围 LPIPS < 0.25，PSNR > 25 dB
4. **工具**：gsplat（HAC++官方实现）、SuperSplat（模型编辑）

## 相关方向
- [[3dgs-large-scale|大规模场景]] — 城市级GS压缩
- [[3dgs-training|训练加速]] — FastGS（100秒训练）
