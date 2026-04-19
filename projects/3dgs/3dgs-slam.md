---
title: 3DGS SLAM 导航
created: 2026-04-19
updated: 2026-04-19
type: project
tags: [3dgs, SLAM, robotics, navigation, computer-vision]
sources: []
---

# 3DGS SLAM 导航

## 概述

SLAM（同步定位与建图）是机器人/无人机自主导航的核心。3DGS-SLAM 用高斯替代传统点云/TSDF作为建图表示。

## 核心方法

| 方法 | 特点 |
|------|------|
| **GS-SLAM** | 稠密视觉SLAM |
| **RadarSplat-RIO** | 雷达+惯性+高斯束调整（最新） |

## 应用场景
- 无人机自主巡检
- 室内机器人导航
- 施工进度自动化监测

## 相关方向
- [[3dgs-large-scale|大规模场景]] — SLAM建图结果的处理
- [[3d-scene-recognition|三维场景识别]] — 建图后的语义理解
