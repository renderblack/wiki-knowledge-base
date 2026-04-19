---
title: 三维场景识别
created: 2026-04-19
updated: 2026-04-19
type: project
tags: [3d, scene-recognition, computer-vision, point-cloud, SLAM]
sources: []
---

# 三维场景识别

## 简介

利用 AI 对三维空间数据（点云、深度图、mesh）进行**语义理解和场景解析**。与 [[3dgs-learning|3DGS]] 的区别：3DGS 侧重视觉重建，本课题侧重**场景理解和语义分割**。

## 核心技术

| 技术 | 说明 |
|------|------|
| Point Cloud Segmentation | 点云语义分割（PointNet++、PointTransformer） |
| 3D Object Detection | 三维目标检测（PointPillars、VoteNet） |
| SLAM + 语义地图 | 同时定位与建图 + 语义层 |
| Scene Graph | 场景图谱（物体关系推理） |

## 典型任务
- **室内场景理解**：房间布局、家具检测、语义分割
- **室外场景理解**：道路、建筑、植被点云分类
- **施工场景理解**：工地结构物识别、工程进度分析
- **BIM + 点云融合**：CAD模型与实景点云对齐

## 工具链
- [[3dgs-learning|3DGS]] — 三维视觉重建输入
- **LingBot-Map** — 航拍视频 → 实时点云（XYZ+颜色，~20 FPS，导出.ply/.pcd）
- COLMAP — SfM 稀疏重建
- Open3D — 点云处理库

## 12周学习计划（参考）

| 阶段 | 周数 | 内容 |
|------|------|------|
| 理论基础 | 1-3周 | PointNet → PointNet++ → PointTransformer 原理 |
| 工具掌握 | 4-6周 | Open3D、点云处理、入门数据集（ScanNet） |
| 进阶应用 | 7-9周 | 语义分割实战、场景图谱构建 |
| 前沿探索 | 10-12周 | 最新论文 + 项目实战 |

## 论文追踪

- TokenGS — 基于可学习 Token 的 3D 高斯预测解耦（2026-04）
- NG-GS — NeRF 引导的 3D 高斯分割（2026-04）
- RadarSplat-RIO — 雷达-惯性里程计与高斯光束调整（2026-04）
- HY-World 2.0 — 多模态世界模型重建与生成（2026-04）

## 相关项目
- [[drone-image-recognition|航拍图像识别]] — 航拍图量化分析
- [[3dgs-learning|3DGS Learning]] — 路桥航拍三维重建
