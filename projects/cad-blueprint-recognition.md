---
title: 施工图CAD图纸识别
created: 2026-04-19
updated: 2026-04-19
type: project
tags: [CAD, blueprint, OCR, computer-vision, construction, DXF, DWG]
sources: []
---

# 施工图CAD图纸识别

## 简介

利用 AI 对建筑工程 CAD 图纸（DWG/DXF/PDF格式）进行**自动解析、要素提取和结构化理解**，识别图元、尺寸标注、设计意图。

## 核心能力

### 图元识别
- 线条、弧线、多段线、填充区域
- 块（Block）识别和解包
- 图层分类（结构、配筋、设备、标注等）

### 标注提取
- 尺寸标注（线性、角度、半径、直径）
- 标高标注
- 文字说明读取（多行文字 MTEXT）

### 语义理解
- 识别图纸类型（建筑/结构/机电/给排水）
- 图例对照解析
- 图表联动（平立剖对应关系）

## 技术路线

| 层级 | 技术 |
|------|------|
| 文件解析 | LibreDWG（开源DWG）、EzDXF、CAD直读 |
| 图像处理 | 栅格化 + OpenCV 预处理 |
| OCR | Tesseract（已配置）、PaddleOCR（中文更强） |
| 目标检测 | YOLO 系列（检测图元类型） |
| 布局理解 | 坐标+图层+图框联合推理 |

## 工具链

| 工具 | 用途 | 状态 |
|------|------|------|
| LibreDWG | DWG 文件读写（C库） | ✅ 可用 |
| EzDXF | DXF Python 库 | ✅ pip 可装 |
| Tesseract | OCR（Windows版已装） | ✅ 已配置 |
| PaddleOCR | 中文 OCR 更强 | ⏳ 待安装 |
| ODA File Converter | DWG → DXF/IFC 转换 | ⏳ 待配置 |

## 工作流程

```
DWG/DXF 文件
    ↓ LibreDWG / EzDXF 解析
矢量图元数据 + 图层信息
    ↓
文字标注 → OCR（Tesseract / PaddleOCR）
图元几何 → 结构化数据（JSON/GeoJSON）
    ↓
AI 语义理解 → 图纸摘要 + 关键要素提取
```

## 适用场景
- 施工图审查（自动检查缺漏项）
- 工程量统计（混凝土方量、钢筋用量）
- 设计变更追踪（版本对比）
- 竣工图核对

## 局限
- DWG 格式版本兼容问题（需多个解析器兜底）
- 复杂配筋图识别精度有限
- 关联图纸联动需要额外逻辑

## 相关项目
- [[drone-image-recognition|航拍图像识别]] — 实景与图纸对照
- [[三维场景识别]] — 点云与BIM模型对比
