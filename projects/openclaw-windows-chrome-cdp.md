# OpenClaw Windows Chrome CDP 自动化 — 踩坑记录

> **结论：此路线不通**  
> 时间：2026-04-24

---

## 目标

WSL2 里的 OpenClaw Gateway 通过 Windows Chrome 的调试端口（CDP）控制有窗口的 Windows Chrome。

---

## 已验证不可行的方案

### 1. WSL2 直接连接 Windows Chrome 调试端口（CDP over TCP）

```
WSL (172.28.15.79) → Windows 宿主机 (172.28.0.1) → Chrome localhost:9222
```

**症状：** TCP 握手成功，但 Chrome 主动关闭连接（exit:52 Empty reply from server）

**尝试过的修复：**
- `netsh portproxy listenaddress=127.0.0.1:9222` → Chrome 拒绝非 localhost
- `netsh portproxy listenaddress=0.0.0.0:9222` → 同样被拒
- Chrome 参数 `--remote-debugging-address=0.0.0.0` → 无效，行为仍像绑定 127.0.0.1
- Windows 防火墙规则添加 9222 → 同样被拒

**结论：** Chrome 的 `--remote-debugging-port` 不支持跨主机访问，需要专门的代理方案。

### 2. OpenClaw Node browser.proxy

**症状：** Node 的 `browser.proxy` 启动的 Chrome 是 `--headless` 模式，完全无窗口。

**根因：** OpenClaw 硬编码 headless 模式（issue #14803），`headless: false` 配置不生效。

**验证：**
- `browser_navigate()` 返回 DOM 快照 ✅（技术通了）
- 用户在 Windows 桌面看不到任何 Chrome 窗口 ❌

**结论：** 唯一有窗口的 Chrome 是手动启动的，但 CDP 无法跨 WSL 访问。

---

## 唯一成功的事

| 目标 | 方法 | 结果 |
|------|------|------|
| WSL2 Gateway 控制 Windows Chrome | OpenClaw Node 架构 | **技术通但无窗口** |
| Windows Chrome 有窗口可见 | 手动启动 + 调试参数 | ✅ 成功 |
| CDP 连接（WSL → Windows Chrome） | — | ❌ 未打通 |

---

## 当前可用状态

```
WSL2 Gateway (172.28.15.79:18789)
    └── OpenClaw Node (已连接，browser.proxy 已启用)
            └── Chrome (Windows, localhost:9222, 有窗口)
                    └── CDP 无法从 WSL 访问 ❌
```

**browser_navigate() 等 browser tool 可用**，但控制的是 Node 启动的 headless Chrome。

---

## 下次尝试的正确方向

1. **Chrome 替代方案**：Windows 上用 Firefox/Edge 的远程调试，或用 Playwright/Selenium 启动有窗口 Chrome
2. **反向通道**：Windows Node 执行 `screenshot` 命令返回图片流给 WSL（纯命令结果，不依赖 CDP）
3. **专用代理**：Puppeteer CDP-over-WS 等中间件
4. **放弃 CDP**：直接用 Node 的 `system.run` 执行 PowerShell 脚本控制 Chrome（DOM 操作、截图等）

---

## 关键文件位置

- OpenClaw 配置：`~/.openclaw/openclaw.json`
- Node 配对信息：`~/.openclaw/node.json`
- Windows Chrome 调试启动：`--remote-debugging-port=9222 --remote-debugging-address=0.0.0.0 --user-data-dir=C:\temp\chrome-debug`
- Gateway token：`11c15b...fd39`
- Node ID：`3ff6bfb8369f6f4f...`

---

## 核心教训

- Chrome 的 `--remote-debugging-port` 对跨主机访问有严格限制，不是简单端口转发能解决的
- OpenClaw Node 的 `browser.proxy` 强制 headless，无法启动可视化 Chrome
- WSL2 NAT 模式下 `172.28.0.1` 只是 WSL 虚拟适配器地址，不等于 Windows localhost
