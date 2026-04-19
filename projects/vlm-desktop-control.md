---
title: VLM 桌面控制
created: 2026-04-19
updated: 2026-04-19
type: project
tags: [VLM, desktop-automation, GUI, computer-use, vision-language-model]
sources: [openclaw]
---

# VLM 桌面控制

## 概述

使用视觉语言模型（Vision Language Model）直接理解和控制 Windows/macOS 桌面 GUI。VLM 通过截屏感知界面状态，通过自然语言规划操作，通过系统 API 执行鼠标/键盘动作。

## 与 Agent Computer Use 的关系

| 维度 | Agent Computer Use | VLM 桌面控制 |
|------|-------------------|-------------|
| 核心能力 | GUI 操作规划 + 执行 | 纯视觉理解 + 操作 |
| Grounding | 需要专用模型定位元素 | 同左 |
| 泛化性 | 强（跨应用） | 强（像素级感知） |
| 速度 | 较慢（多模型协作） | 较快（单 VLM） |
| 落地难度 | 高（需 Grounding 模型） | 中（现成 VLM 可用） |

## 技术路径

### 路径 A：现成 VLM + 系统 API（快速验证）
1. 截图（每500ms）
2. VLM 分析截图 → 生成操作指令
3. 调用 OS API 执行鼠标/键盘动作
4. 循环直到任务完成

**优势**：无需 Grounding 模型，用 Qwen-VL / GPT-4V / Claude Vision 即可
**劣势**：无法精准点击小按钮，长任务链效果差

### 路径 B：专用 GUI Agent 模型（高精度）
- UI-TARS（字节）/ SeeClick（智谷）/ CogAgent
- 内置 GUI 元素检测 + 定位能力
- 参考 [[Agent Computer Use]] 的 Agent S 路线

## 当前环境评估

| 组件 | 状态 |
|------|------|
| VLM 推理 | ✅ Claude Vision / GPT-4V 可用（API） |
| 截图采集 | ✅ Python + PIL 可行 |
| 系统 API（Windows） | ✅ pywinauto / pyautogui 可行 |
| Grounding 模型 | ⏳ 待获取（[[Agent Computer Use]] 同款） |

## 相关方向

- [[Agent Computer Use]] — 更通用的 GUI 自动化框架
- [[浏览器自动化]] — 浏览器专项，更容易落地
- [[CLI-Anything]] — 工具封装方法论
