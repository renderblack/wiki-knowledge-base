---
title: 浏览器自动化
created: 2026-04-19
updated: 2026-04-19
type: project
tags: [browser, automation, chrome, CDP, headless, computer-use]
sources: []
---

# 浏览器自动化

## 概述

让 AI 直接控制 Chrome 浏览器，通过 CDP（Chrome DevTools Protocol）协议实现自动化操作。

## 当前状态

**✅ 已完成配置，可正常使用。**

## 两套方案

### 方案一：Chrome DevTools MCP（WSL2 内置Chrome）

| 项目 | 配置 |
|------|------|
| 驱动 | `chrome-devtools-mcp@latest` |
| Chrome路径 | `/usr/bin/google-chrome` |
| 调试端口 | 9222 |
| tmux会话 | `chrome-headless` |

**启动命令（headless模式）：**
```bash
tmux new-session -d -s chrome-headless "xvfb-run --auto-servernum --server-num=99 google-chrome --headless --no-sandbox --disable-gpu --remote-debugging-port=9222"
```

**启动命令（露头可视化模式）：**
```bash
tmux new-session -d -s chrome-visible 'DISPLAY=:0 google-chrome --no-sandbox --disable-gpu --remote-debugging-port=9222 --user-data-dir=/home/xiong/.chrome-visible'
```

**验证：**
```bash
curl -s http://127.0.0.1:9222/json/version
```

**OpenClaw配置：**
```json
"browser": {
  "profiles": {
    "openclaw": {
      "driver": "launch",
      "executablePath": "/usr/bin/google-chrome",
      "headless": true,
      "noSandbox": true,
      "cdpPort": 9222
    }
  },
  "defaultProfile": "openclaw"
}
```

### 方案二：agent-browser（独立工具）

| 项目 | 说明 |
|------|------|
| 安装位置 | `~/.openclaw/skills/agent-browser/` |
| 来源 | 用户提供的源码 |

**常用命令：**
```bash
agent-browser open --proxy http://172.18.176.1:7890 <url>
agent-browser screenshot
agent-browser snapshot -i
agent-browser find text "登录" click
agent-browser close --all
```

**截图目录：** `~/.agent-browser/tmp/screenshots/`

**适用场景：** B站扫码登录、订阅列表抓取、视频信息获取。

## 技术原理

| 层级 | 技术 |
|------|------|
| 控制协议 | Chrome DevTools Protocol（CDP） |
| 调用方式 | Puppeteer / MCP server / agent-browser |
| 无头引擎 | Xvfb（虚拟显示，WSL2无GUI环境必需） |
| X11转发 | DISPLAY=:0（露头模式，Windows桌面显示） |

## 应用场景

| 场景 | 方案 |
|------|------|
| B站扫码登录 | agent-browser 露头模式 |
| 视频下载 | Chrome headless + yt-dlp |
| 网页内容抓取 | Chrome DevTools MCP |
| 自动化表单填写 | agent-browser |

## 已知限制

- WSL2 内置 Chrome 与 Windows Chrome **无法同时**连接同一调试端口
- 重启 Gateway 会 kill Chrome 窗口（露头模式）
- Windows Chrome 直连方案待研究（防火墙/WSL2网络配置）

## 相关方向
- [[agent-computer-use|Agent Computer Use]] — AI像人一样操控电脑（更高级的GUI自动化）
