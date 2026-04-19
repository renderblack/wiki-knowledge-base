---
title: Memory 与 Wiki 沉淀策略
created: 2026-04-19
updated: 2026-04-19
type: guide
tags: [memory, wiki, knowledge-management]
sources: []
---

# Memory 与 Wiki 沉淀策略

## 背景

Hermes Memory 有容量限制：
- MEMORY.md：2,200 字符
- USER.md：1,375 字符

这是**刻意设计**，目的是保持记忆精简、减少 token 消耗。但长期积累会导致信息被压缩丢失。

## 解法：Wiki 做结构化沉淀

将重要知识沉淀到 `~/wiki/`，不受 memory 容量限制，不因压缩丢失。

### Wiki 结构

```
~/wiki/
├── config/            # 环境配置手册
│   ├── tts.md        # TTS 配置
│   └── environment.md # 环境和工具链
├── projects/         # 项目知识
│   └── 3dgs-learning.md
├── research/         # 研究主题
│   └── china-debt-resolution/  # 化债研究
├── raw/              # 原始素材
└── index.md         # 总索引
```

### 沉淀规则

**→ Wiki（不压缩）**
- 环境配置详情（TTS、代理、工具链）
- 项目知识（路径、工具、推荐算法）
- 研究主题（化债等专题）
- 操作手册（详细步骤和命令）

**→ Memory（容量有限）**
- "配置在 `~/wiki/config/tts.md`"（指向 wiki）
- "化债知识在 `~/wiki/research/china-debt-resolution/`"
- 当前 session 正在做的任务状态
- 临时的、一次性的信息

## 好处

1. **不丢失**：Wiki 是文件系统，永久存在
2. **可检索**：`session_search` 可以搜 wiki 内容
3. **可共享**：Obsidian 可以直接打开 wiki 目录
4. **Memory 轻量化**：只需记住"去哪里找"，不用记细节

## 维护

- 新知识直接写 wiki，不走 memory
- Memory 满了就迁到 wiki，不强行压缩
- 定期更新 wiki index.md 保持导航清晰
