---
title: 3DGS Learning 项目
created: 2026-04-18
updated: 2026-04-19
type: project
tags: [3dgs, computer-vision, photogrammetry, drone]
sources: []
---

# 3DGS Learning 项目

## 路径

`/home/xiong/workspace/3DGS-Learning/`

## 用户需求

- **场景**：线性路桥施工场景，航拍/无人机影像
- **目标**：真实感三维重建（非精确测量）
- **输入**：无人机拍摄的照片

## 推荐算法（按门槛从低到高）

1. **LongSplat** — 门槛最低，优先测试
2. **DroneSplat** — 专为无人机场景优化
3. **Horizon-GS** — 适合大场景
4. **CityGaussianV2** — 城市级重建

## 微信公众号（已验证可检索）

- AI paper实验室
- 3D视觉工坊
- SLAM与AI智能体
- 学姐带你玩AI

## 相关工具

- 无人机影像采集
- COLMAP（SfM，用于稀疏重建）
- Fast-BEV（BEV 感知，可辅助重建）
