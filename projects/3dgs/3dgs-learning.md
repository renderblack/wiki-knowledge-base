---
title: 3DGS Learning — 研究总览
created: 2026-04-18
updated: 2026-04-19
type: project
tags: [3dgs, computer-vision, photogrammetry, drone]
sources: []
---

# 3DGS — 研究总览

## 大类概述

3D Gaussian Splatting（3DGS）是用**高斯椭球**表示三维场景的渲染技术路线，核心优势是**实时渲染 + 高保真Novel View Synthesis**。

本大类下分 8 个研究方向，覆盖从训练到部署的完整链路：

| # | 研究方向 | 说明 | 状态 |
|---|---------|------|------|
| 1 | [[3dgs-training|训练加速]] | 缩短3DGS训练时间 | 🔄 持续 |
| 2 | [[3dgs-compression|模型压缩]] | 减少Gaussians数量+存储体积 | 🆕 新建 |
| 3 | [[3dgs-large-scale|大规模场景]] | 城市场景/航拍场景重建 | 🔄 持续 |
| 4 | [[3dgs-surface|表面重建]] | 提取mesh几何曲面 | ⏳ 待探索 |
| 5 | [[3dgs-slam|SLAM导航]] | 实时定位与建图 | ⏳ 待探索 |
| 6 | [[3dgs-dynamic|动态场景]] | 4DGS人体/物体运动 | ⏳ 待探索 |
| 7 | [[3dgs-semantic|语义理解]] | LanguageGS + 场景分割 | ⏳ 待探索 |
| 8 | [[3dgs-editing|编辑与生成]] | 可控3D编辑 + Text-to-3D | ⏳ 待探索 |

## 工具链

| 工具 | 用途 |
|------|------|
| COLMAP | SfM 稀疏重建 |
| gaustudio | 模块化训练框架 |
| SuperSplat | GS 模型编辑 |
| gsplat | 高性能渲染库 |
| Unreal Engine 5 | 渲染展示 |

## 论文追踪
- **LingBot-Map** — 航拍视频 → 实时点云（独立项目，非3DGS）
- 3DGS 文章追踪：`~/.openclaw/workspace/learn/3d-reconstruction/articles-tracker.md`

## 学习资源
- B站保姆教程：XR_1605 Gaussian Splatting 系列（14期，字幕已转写）
- awesome-3D-gaussian-splatting: 8000+ stars 最全论文列表

## 相关项目
- [[drone-image-recognition|航拍图像识别]] — 航拍图量化分析
- [[3d-scene-recognition|三维场景识别]] — 点云语义理解
