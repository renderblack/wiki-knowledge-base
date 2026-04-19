---
title: Agent Computer Use 研究
created: 2026-04-19
updated: 2026-04-19
type: project
tags: [agent, computer-use, GUI-automation, Agent-S, OSWorld, grounding-model]
sources: []
---

# Agent Computer Use 研究

## 概述

让 AI Agent 直接操控电脑 GUI（图形界面），像人一样移动鼠标、敲键盘、操作应用程序。比浏览器自动化更通用，但门槛更高。

## 代表工作

### Agent S（S3版本）

| 项目 | 说明 |
|------|------|
| GitHub | https://github.com/simular-ai/Agent-S |
| Stars | ~10k |
| 基准 | OSWorld（电脑操作），S3版本 **72.6% 超越人类表现** |
| 支持平台 | Linux, Mac, Windows |

**核心能力：**
- AI 自主规划鼠标/键盘操作序列
- 处理多步骤复杂任务（如"整理桌面文件夹"）
- 屏幕视觉理解 + 操作执行闭环

**组件需求：**

| 组件 | 推荐 | 当前环境 |
|------|------|----------|
| 主模型 | GPT-5-2025-08-07 | 可用 Claude/Gemini 替代 |
| Grounding模型 | UI-TARS-1.5-7B | ⏳ INT4量化版本待获取 |
| Grounding部署 | vLLM/TGI @ localhost:8080 | ⏳ 待部署 |

**显存分析（RTX 4060 8GB）：**

| 模型 | 精度 | 显存需求 | 可行性 |
|------|------|---------|--------|
| UI-TARS-1.5-7B | FP16 | ~14GB | ❌ 不够 |
| UI-TARS-1.5-7B | INT8 | ~7GB | ⚠️ 勉强 |
| UI-TARS-1.5-7B | INT4 | ~4GB | ✅ 可行 |

## 技术原理

### OSWorld 基准测试
- 标准化的电脑操作评测环境
- 涵盖：文件管理、浏览器操作、文档编辑、编程等任务
- 评估 AI 完成真实世界任务的能力

### Grounding 模型的作用
- 将 GUI 界面元素（按钮、菜单、图标）**定位**到屏幕坐标
- 告诉主模型"你要点击的元素在哪里"
- 没有 Grounding 模型，Agent 无法精准操作 GUI

## 当前障碍

1. **Grounding 模型**：需要 INT4 量化版（FP16需14GB，现有8GB不够）
2. **vLLM 服务**：需额外启动量化推理服务，占用资源
3. **主模型成本**：GPT-5 使用成本高，需评估 Claude/Gemini 替代方案

## 其他相关工作

| 工作 | 特点 |
|------|------|
| Claude Code | AI编程助手，OSWorld 高分（需 Claude 3.7+） |
| Agent S | GUI自动化，S3版本超越人类 |
| Chrome DevTools MCP | 浏览器专项自动化（[[浏览器自动化]]） |

## 行动计划

| 步骤 | 行动 | 状态 |
|------|------|------|
| 1 | 获取 UI-TARS INT4 量化模型 | ⏳ |
| 2 | 部署 vLLM 本地推理服务 | ⏳ |
| 3 | 验证 Agent S Linux 版 | ⏳ |
| 4 | 测试典型任务（文件管理/浏览器） | ⏳ |

## 相关方向
- [[浏览器自动化]] — 浏览器专项自动化（门槛更低，已完成）
