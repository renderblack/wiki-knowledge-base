# OpenClaw + Chrome DevTools MCP 现状诊断

**诊断时间：** 2026-04-23 15:10  
**环境：** WSL2 (Ubuntu 24.04) + OpenClaw 2026.4.14

---

## 核心结论

OpenClaw + Chrome DevTools MCP 自动化是**可用的**，但当前是 **headless 无头模式**，用户看不见 Chrome 窗口。

网上那些"露头模式"教程的 Chrome 都是**普通可视化窗口**，WSL2 环境缺少 X Server 所以无法实现。

---

## 当前环境状态

| 组件 | 状态 | 说明 |
|------|------|------|
| Chrome CDP 调试端口 | ✅ | `127.0.0.1:9222` 正常 |
| Chrome DevTools MCP | ✅ | 已配置 `--browser-url http://127.0.0.1:9222` |
| OpenClaw browser | ✅ | profile `openclaw`，driver `openclaw`（Playwright） |
| CDP 页面 | ✅ | 1个空白页 `chrome://newtab/` |
| X Server | ❌ | 无 `$DISPLAY`，只有 Xvfb 虚拟帧缓冲 |
| Windows Chrome 调试 | ❓ | `192.168.22.78:9222` 无法连接 |

### Chrome 启动参数
```
google-chrome --headless --ozone-platform=headless --remote-debugging-port=9222
--remote-allow-origins=* --incognito --user-data-dir=/tmp/chrome-test
```

---

## OpenClaw Browser Driver 类型

| Driver | 说明 | 当前 |
|--------|------|------|
| `openclaw` | Playwright 控制独立 Chrome 实例 | ✅ 在用（headless） |
| `existing-session` | 直连现有 Chrome（保留登录态） | ❌ 连的是 headless Chrome |
| `chrome` + Extension Relay | Chrome 插件方式，手动 attach Tab | ❌ 未安装 |

---

## 露头模式实现路径

### 路径 A：Windows Chrome 远程调试（最快）

**Windows 侧：**
```powershell
# 快捷方式目标加参数：
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
```
或命令行启动：
```powershell
start chrome --remote-debugging-port=9222
```

**验证 Windows 端口：**
```powershell
netstat -ano | findstr 9222
# 应该有 0.0.0.0:9222 或 127.0.0.1:9222 LISTENING
```

**OpenClaw MCP 配置改连 Windows：**
```bash
openclaw mcp set chrome-devtools '{"command":"npx","args":["-y","chrome-devtools-mcp@latest","--browser-url","http://192.168.22.78:9222"]}'
```

### 路径 B：WSL2 + X Server

Windows 装 [VcXsrv](https://sourceforge.net/projects/vcxsrv/)，然后：
```bash
export DISPLAY=host.docker.internal:0.0   # 或 Windows IP
google-chrome --remote-debugging-port=9222
```

### 路径 C：WebTop Docker（生产级最稳定）

详见 WebTop 方案 — Docker 跑完整 Linux 桌面，容器内 Chromium 可视化。

---

## 待验证事项

- [ ] Windows Chrome 是否已开启 `--remote-debugging-port=9222`
- [ ] Windows 防火墙是否放行了 9222 端口
- [ ] `chrome://inspect/#devices` 是否有 "Discover network targets" 勾选

---

## 相关文件

- OpenClaw 配置：`~/.openclaw/openclaw.json`
- OpenClaw MCP：`~/.openclaw/openclaw.json` → `mcpServers.chrome-devtools`
- Chrome 进程：`ps aux | grep chrome`

---

## Path C 进展（2026-04-23）

### 第一步：Hyper-V 开启
- ✅ Windows 11 专业版，版本 23H2 (OS 内部版本 22631.6199)
- ✅ Hyper-V 已从 Disabled → Enabled

### 第二步：Docker Desktop 安装
- 🔄 待安装（用户已下班）

### 待办清单
- [ ] 安装 Docker Desktop for Windows
- [ ] Docker Desktop 启动验证（绿色鲸鱼图标）
- [ ] WSL2 里验证 docker CLI 连通性
- [ ] 拉取 linuxserver/webtop:ubuntu-xfce
- [ ] 配置容器 CDP 端口映射
- [ ] OpenClaw existing-session driver 配置

### 已知问题
- Hyper-V 和 WSL2 共存：Windows 11 专业版没问题
- Docker Desktop WSL2 backend 需要 WSL2 集成开启
- WebTop 容器约 1.5GB，下载需要时间

### 参考：WebTop Docker 方案架构
```
Windows Docker Desktop
  └── linuxserver/webtop:ubuntu-xfce
        ├── Ubuntu XFCE 桌面
        ├── Chromium (可视化)
        ├── socat (CDP 端口转发: 9222)
        └── 端口映射 localhost:9222

WSL2 OpenClaw
  └── Chrome DevTools MCP --browser-url http://localhost:9222
