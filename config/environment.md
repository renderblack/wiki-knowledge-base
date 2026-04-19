---
title: 环境与工具链配置
created: 2026-04-19
updated: 2026-04-19
type: config
tags: [environment, wsl2, windows, tools]
sources: []
---

# 环境与工具链配置

## 双环境架构

- **WSL2**：主要工作环境，Linux shell
- **Windows**：桌面、Obsidian、Clash 代理
- WSL2 文件系统在 `/mnt/c/` 访问 Windows 盘符

## Windows 路径对应

| Windows 路径 | WSL2 路径 |
|---|---|
| `C:\Users\xiong\Desktop` | `/mnt/c/Users/xiong/Desktop/` |
| `D:\Documents\` | `/mnt/d/Documents/` |
| 用户主目录 | `/home/xiong/` |

## 代理配置

Clash 运行在 Windows 上，WSL2 通过以下地址访问：

- **HTTP/SOCKS5 混合代理**：`http://172.28.0.1:7890`
- **用途**：访问国际网络（如 `api.minimax.io`）
- **注意**：`api.minimaxi.com` 直连即可，无需代理

## 定时任务

Cron job 默认时间：**早上 7:00**（统一）

查看定时任务：
```
cronjob(action="list")
```

Cron job 输出文件位置：`~/.hermes/cron/output/`

## Obsidian 同步

- Windows 中文版 Obsidian
- 同步文件夹：`D:\Documents\Memory AI\`
- 包含 3 个 vault 链接：我的记忆、知识库、OpenClaw记忆
- 通过符号链接让 Windows Obsidian 访问 WSL2 中的 AI 记忆文件

## OpenClaw

- 装在这台机器上
- Workspace：`~/.openclaw/workspace/`
- OpenClaw 的文件 ≠ Hermes 的文件，文件名相同不代表归属相同
- 不说"我们的OpenClaw"，说"OpenClaw"

## Hermes 项目上下文加载优先级

1. `HERMES.md`（`~/.hermes/HERMES.md`，优先级最高，不受 CWD 影响）
2. `AGENTS.md` / `CLAUDE.md`（从 CWD 加载）
3. `SOUL.md`（从 `HERMES_HOME` 加载，永远有效）

**根本解法**：建 `~/.hermes/HERMES.md`，内容优先级最高。

## 常用命令

```bash
# 查看 cron 任务
cronjob(action="list")

# 搜索历史 session
session_search(query="关键词")

# 查看 skills
skills_list()

# 查看 memory
# memory 内容在 ~/.hermes/memories/MEMORY.md
```
