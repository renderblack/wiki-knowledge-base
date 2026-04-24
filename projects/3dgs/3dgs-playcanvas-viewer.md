---
title: 3DGS 模型浏览器端查看方案
created: 2026-04-21
updated: 2026-04-21
type: project
tags: [3dgs, browser, playcanvas, supersplat, webgl]
---

# 3DGS 模型浏览器端查看方案

## 背景

目标：为「新塍至王江泾 524 国道」施工场景 3DGS 模型（L20，共 137 tiles，3.78 GB）提供浏览器端实时查看能力，替代沉重的 GridMaster 客户端。

核心约束：
- 模型必须能通过浏览器直接打开，无需安装任何插件
- 支持 .compressed.ply 压缩格式（PlayCanvas 官方格式，4.3× 压缩）
- GridMaster 不支持 .compressed.ply，需要独立查看器

---

## 一、核心技术方案

### 方案选择：SuperSplat（PlayCanvas 官方）

经过调研，确定使用 [PlayCanvas SuperSplat](https://playcanvas.com/super-splat) 作为渲染引擎：
- 开源（npm 包 `@playcanvas/supersplat-viewer` v1.19.1）
- 原生支持 .compressed.ply 格式（4.3× 压缩，比自定义 .3dgs 格式更好）
- WebGL/WebGPU 渲染，性能优秀
- 支持 orbit/fly/walk 多种相机模式

### 压缩效果对比

| 方案 | 单 Tile 原始 | 单 Tile 压缩后 | 压缩比 | GridMaster 支持 |
|------|------------|--------------|--------|----------------|
| 原始 .ply (float32) | 27.6 MB | 27.6 MB | 1× | ✅ |
| 自定义 .3dgs (float16) | 27.6 MB | 11 MB | 2.4× | ❌ |
| **PlayCanvas .compressed.ply** | 27.6 MB | **6.4 MB** | **4.3×** | ❌ |

**结论**：放弃自定义 .3dgs 方案，改用官方 .compressed.ply 格式 + SuperSplat 查看器。

---

## 二、技术架构

### 2.1 文件结构

```
E:\3DGS模型 新塍至王江泾524国道\Data\Data-Compression\
├── Tile_+001_+002_L20.compressed.ply   # 单块测试模型，4.2 MB
├── scene.compressed.ply                 # SuperSplat 默认加载文件名，4.1 MB
├── settings.json                        # 空 JSON，满足 SuperSplat 的 404 要求
├── index.html                           # SuperSplat 主页面
├── index.css                            # 样式
├── index.js                             # 渲染引擎（79 KB，自包含）
└── splat_viewer.html                    # 嵌入了 base64 数据的独立版本
```

### 2.2 SuperSplat 加载流程

```
browser
├── index.html (前端配置)
│   ├── <head>: window.sse.config = { contentUrl, contents: fetch(contentUrl) }
│   └── <body>: import { main } from './index.js'
│
├── index.js (79 KB，单文件，无外部依赖)
│   ├── createApp(canvas, config) → PlayCanvas App + WebGL device
│   ├── loadGsplat(app, config) → Asset('gsplat', { contents }) → app.assets.load()
│   │   └── Asset 内部：new AssetFile(url, filename, hash, size, opt, contents)
│   │       └── gsplat handler 解析 contents → 创建 SplatMesh entity
│   ├── loadSkybox / loadCollision
│   └── Viewer(global, gsplatLoad, ...) → 相机控制 + UI 事件绑定
│
└── scene.compressed.ply (二进制模型数据)
    └── .compressed.ply 格式（PlayCanvas 私有压缩格式）
```

### 2.3 关键参数

```
窗口.sse.config = {
    contentUrl: './scene.compressed.ply',
    contents: fetch('./scene.compressed.ply'),     // Promise<Response>
    // 其他可选：
    poster: Image,          // 加载时的预览图
    skyboxUrl: string,      // 天空盒
    collisionUrl: string,   // 碰撞数据
    noui: boolean,          // 隐藏 UI
    noanim: boolean,        // 禁用动画
    webgpu: boolean,        // 强制 WebGPU
    aa: boolean,            // 抗锯齿
    heatmap: boolean,        // 热力图模式
    fullload: boolean,      // 完整加载（非渐进式）
}
```

### 2.4 URL 参数

```
# 加载自定义模型文件
?content=URL                    # 指定 .compressed.ply 地址
?settings=URL                   # 指定 settings.json 地址

# 渲染选项
?webgpu                         # 强制 WebGPU 渲染
?aa                             # 启用抗锯齿
?heatmap                        # 热力图模式
?fullload                       # 不使用渐进式加载
?unified                        # 统一模式
?noui                           # 隐藏所有 UI
```

---

## 三、已知问题与解决方案

### 3.1 scene.compressed.ply HTTP 200 Size 0（缓存问题）

**现象**：通过 Python HTTP 服务器访问时，浏览器 Network 面板显示 `scene.compressed.ply` 返回 HTTP 200 但 size 0。PowerShell 服务器日志显示从未收到对该文件的请求。

**原因**：浏览器缓存了之前的失败响应（0 字节），`python -m http.server` 不设置 `Cache-Control` 头，导致缓存的 0 字节响应永久生效。

**解法**（任选其一）：
1. **嵌 base64 数据**：将模型数据内嵌到 HTML 里，完全消除网络请求
2. **Python 服务器 + 强制刷新**：`Ctrl+Shift+R` 强制刷新
3. **PowerShell 服务器**：`Start-Process` 启动，添加 `Cache-Control: no-store` 响应头

### 3.2 splat_viewer.html 空白（嵌 base64 版）

**现象**：`splat_viewer.html` 包含完整的 base64 模型数据（4.1 MB），但双击打开后画面空白。

**原因**：`index.js` 里 `loadGsplat` 调用 `app.assets.load(asset)` 时，PlayCanvas Asset Loader 内部通过 `fetch(contents)` 加载数据。在 `file://` 协议下，**`fetch('data:...')` URL 可能不被 PlayCanvas 的 Asset loader 正确处理**，导致数据永远处于 pending 或 error 状态。

**待解决**：→ 见下方「四、待验证方案」

### 3.3 色彩偏暗

**现象**：`splat_viewer.html` 打开后模型渲染出来但颜色暗淡，不够鲜艳。

**分析**：PlayCanvas SuperSplat 使用 2.2 gamma 校正，嵌 base64 版可能存在 gamma/曝光参数差异。

**待解决**：→ 见下方「四、待验证方案」

---

## 四、待验证方案

### 方案 A：blob URL 替代 data URL（推荐）

**思路**：在 `splat_viewer.html` 里，不修改 `index.js`，而是：
1. 在 HTML `<head>` 段提前把 `data:` URL 转为 **blob URL**（`URL.createObjectURL(blob)`）
2. 将 blob URL 注入 `window.sse.config.contents`
3. 绕过 `index.js` 里 `fetch('data:...')` 的处理路径

**关键改动**：在 `index.html` 的 `<script type="module">` 之前注入 JS，将 `window.sse.config.contents` 从 `fetch('data:...')` 替换为预先生成的 blob URL。

```javascript
// 在 <script type="module"> 之前注入
<script>
(async () => {
    const b64 = '...'; // 4.1 MB base64 数据
    const binary = atob(b64);
    const arr = new Uint8Array(binary.length);
    for (let i = 0; i < binary.length; i++) arr[i] = binary.charCodeAt(i);
    const blob = new Blob([arr], { type: 'application/octet-stream' });
    const blobUrl = URL.createObjectURL(blob);
    
    // 等待 index.js 执行到 window.sse.config 设置点
    const config = {
        contentUrl: blobUrl,
        contents: fetch(blobUrl),
        // ... 其他默认参数
    };
    window.sse = { config, settings: fetch('./settings.json').then(r => r.json()) };
})();
</script>
```

**验证步骤**：
1. 生成 `splat_viewer_blob.html`
2. Bolt老大双击打开
3. 确认 3D 模型正常渲染，色彩正常

### 方案 B：Python HTTP 服务器（临时验证用）

**命令**：
```powershell
cd E:\3DGS模型 新塍至王江泾524国道\Data\Data-Compression
python -m http.server 8765
```

**访问**：`http://localhost:8765/?content=./scene.compressed.ply`

**注意**：需要先清理浏览器缓存（Ctrl+Shift+R），避免 0 字节缓存问题。

### 方案 C：完全自建 gsplat 渲染器

**思路**：不依赖 PlayCanvas，自己写 WebGL 渲染管线：
- 解析 .compressed.ply 二进制格式
- 将高斯点渲染为半透明圆点（splat）
- 实现 GPU 深度排序 + alpha blending

**工作量**：大（~500 行 GLSL + 渲染逻辑）

**优点**：完全可控，无任何第三方依赖

---

## 五、SuperSplat npm 包关键源码

### 5.1 loadGsplat 函数（核心加载逻辑）

位置：`index.js` 第 78816 行

```javascript
const loadGsplat = async (app, config, progressCallback) => {
    const { contents, contentUrl, unified, aa } = config;
    const c = contents;
    // contentUrl = 'scene.compressed.ply'（不含路径）
    const filename = new URL(contentUrl, location.href).pathname.split('/').pop();
    // 创建 Asset，contents 就是 fetch(url) 返回的 Promise<Response>
    const asset = new Asset(filename, 'gsplat', { url: contentUrl, filename, contents: c }, data);
    return new Promise((resolve, reject) => {
        asset.on('load', () => { /* 创建 gsplat entity */ });
        asset.on('progress', (received, length) => { /* 进度回调 */ });
        asset.on('error', (err) => { console.log(err); reject(err); });
        app.assets.add(asset);
        app.assets.load(asset);
    });
};
```

### 5.2 Asset 内部数据流

```
Asset 构造函数接收 { url, filename, contents }
  → AssetFile(value.url, value.filename, value.hash, value.size, value.opt, value.contents)
    → contents = Promise<Response>
    → handler.open(url, data, asset) 
      → gsplat handler 解析二进制数据
```

**关键洞察**：`contents` 就是 `fetch()` 返回的 `Promise<Response>`，PlayCanvas Asset loader 内部会调用 `await contents` 获取 Response，然后读取 `response.arrayBuffer()` 得到二进制数据。

---

## 六、后续计划

### 优先级 1：修复空白问题
- [ ] 方案 A：生成 blob URL 版 `splat_viewer_blob.html`
- [ ] 方案 A：Bolt老大测试，确认渲染正常 + 色彩正常
- [ ] 方案 A：验证 3D 交互（orbit/zoom/pan）正常

### 优先级 2：批量转换
- [ ] 编写脚本批量转换 137 个 L20 tiles 为 .compressed.ply
- [ ] 支持断点续传（checkpoint）
- [ ] 预计时间：~30 分钟

### 优先级 3：生产部署
- [ ] 评估：嵌 base64 单文件方案 vs HTTP 服务器方案
- [ ] 如嵌 base64：生成完整的模型集合页面
- [ ] 如 HTTP：部署稳定的文件服务器 + CDN

---

## 七、关键文件路径

| 文件 | 路径 |
|------|------|
| 原始模型目录 | `E:\3DGS模型 新塍至王江泾524国道\Data\` |
| 压缩工作目录 | `E:\3DGS模型 新塍至王江泾524国道\Data\Data-Compression\` |
| 单块测试模型 | `Tile_+001_+002_L20.compressed.ply` (4.2 MB) |
| SuperSplat 源码 | `index.html/css/js`（npm 包提取） |
| 嵌 base64 查看器 | `splat_viewer.html` (5.6 MB) |
| Tile 元数据 | Box Center (246.001, 398.297, 16.916), SRS: EPSG:4549 |

---

## 八、经验教训

1. **Python http.server 不设置 Cache-Control**：缓存的 0 字节响应导致误判问题根源
2. **file:// + fetch('data:') 可能不兼容**：PlayCanvas Asset loader 的 HTTP 层无法正确处理 data: URL
3. **SuperSplat npm 包是组件库而非完整 app**：index.html 分为两段 JS（config 设置 + main 调用），需要正确配合才能工作
4. **splat-transform CLI 是最可靠的压缩工具**：官方支持，格式最稳定，4.3× 压缩率
5. **GridMaster 和 .compressed.ply 不兼容**：必须自建查看器，不能依赖 GridMaster
