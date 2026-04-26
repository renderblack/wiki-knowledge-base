# 3DGS 项目进度

> 本页按季度记录 3DGS 相关工作的里程碑进展，供年底汇总使用。

---

## 2026 年度

### Q1（1-3月）

*暂无记录*

---

### Q2（4-6月）

#### 4月21日 — Tile 模型压缩与合并（里程碑 ✅）

**背景**：524国道新塍至王江泾段 3DGS 模型，137 个 Tile，L20 精度，原始 3.69 GB。

**主要工作**：
- 分析 GridMaster PLY 格式（17 property，68B/vertex）
- 验证 splat-transform 压缩格式（14 property，56B/vertex）
- 批量压缩 137 Tile → 905 MB（4.18×）
- 发现并修复坐标变换公式错误：`world = SRS + raw_ply_xyz`
- 生成无缝合并文件：3.04 GB，58,289,866 顶点

**关键文件**：
- `~/wiki/projects/3dgs/3dgs-compression-plan.md` — 压缩方案
- `~/wiki/projects/3dgs/2025-04-21-work-log.md` — 详细工作日志
- `~/wiki/projects/3dgs/3dgs-compression-plan.pdf` — 方案 PDF

**Skills**：
- `splat-transform-compressed-ply` — 格式解析 + CLI 语法 + 解码算法
- `3dgs-tile-model-workflow` — 完整工作流

**关键参数**：
- SRS Origin = (562378.833, 3407695.236, -4.975)
- 坐标公式：**world = SRS + raw_ply_xyz**（Box.Center 勿加）

**待办**：
- [ ] DasViewer 验证合并文件无缝拼接
- [ ] 清理废弃文件（错公式版）
- [ ] GridMaster 质量验收

---

#### 早期探索（4月）

| 时间 | 内容 |
|------|------|
| 4月10日 | 3DGS 本地环境搭建 |
| 4月11日 | OpenClaw 文档重建（3DGS 部分关联） |
| 4月23日 | session_search 根因调查：定位 FTS5 无法按日期过滤 + USER 消息截断导致 summary 误判两层 bug；GitHub tracker 脚本修复（Token + 去重正则）；UnityPlate 集成平台首次被发现 |
| 4月24日 | OpenClaw + Windows Chrome CDP 自动化踩坑（文档归档 `openclaw-windows-chrome-cdp.md`）；Chrome remote-debugging-port 跨主机限制确认不通；Claude Code Windows 安装咨询 |

---

## 历史记录索引

| 年份 | 内容 |
|------|------|
| 2025 | 参考 `~/wiki/projects/3dgs/3dgs-*.md` 各专题文件 |
