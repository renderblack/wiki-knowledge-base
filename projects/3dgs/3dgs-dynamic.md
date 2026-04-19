---
title: 3DGS 动态场景
created: 2026-04-19
updated: 2026-04-19
type: project
tags: [3dgs, 4dgs, dynamic-scene, animation, computer-vision]
sources: []
---

# 3DGS 动态场景

## 概述

静态 3DGS 只能表示单一时点，**4DGS（动态3DGS）** 增加时间维度，捕捉人体、物体、场景的**运动过程**。

## 核心方法

| 方法 | 场景 | 特点 |
|------|------|------|
| **4D Gaussian Splatting** | 人体/物体运动 | 实时动态渲染 |
| **AvatarPointillist** | 单图→动态4D化身 | CVPR 2026 |
| **ClipGStream** | 长多视角动态场景 | VR/AR 友好 |

## 动态压缩

动态场景压缩更难（时间维度冗余）：
- **91× 压缩比**（Rate-Distortion Optimized 4DGS vs Ex4DGS）
- 关键：利用时序平滑性

## 应用场景
- 人员施工动画模拟
- 机械设备运动轨迹
- 施工过程回放

## 相关方向
- [[3dgs-compression|模型压缩]] — 动态压缩单独有挑战
- [[3dgs-semantic|语义理解]] — 动态语义分割
