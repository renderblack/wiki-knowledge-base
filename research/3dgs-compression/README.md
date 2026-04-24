# 3DGS 模型压缩研究

> 研究时间：2026-04
> 状态：✅ 已结题（待后续需求重启）

---

## 结论速览

| 项目 | 结论 |
|------|------|
| 工具链 | `splat-transform`（@playcanvas/npm）唯一可用 |
| 压缩格式 | `.compressed.ply`（PlayCanvas SuperSplat 专用） |
| 压缩率 | ~4.3×（18MB → 4.2MB） |
| 解码精度 | 最大误差 < 1.5e-5（纯 IEEE 754 浮点损失） |
| GridMaster 兼容性 | ❌ 不兼容，压缩后需解压回标准 PLY 再导入 |
| 批量压缩 | ✅ 可行（886 个文件，估算 10~20 分钟） |

---

## 压缩格式原理

### .compressed.ply 结构

```
PLY HEADER
  property uint packed_position   // 32bit uint = 11(x) + 10(y) + 11(z) 位
  property uchar/dc_0 ... dc_26  // SH 系数（逐字节，无压缩）
  property uchar/opacity
  property uchar/scale_0 scale_1 scale_2
  property uchar/rot_0 ... rot_3
  ...

CHUNKS（每个 chunk 包含）
  - chunk_min（float3）：chunk 包围盒最小点
  - chunk_range（float3）：chunk 尺寸
  - N 个 gaussian：
      packed_position → uint → v/((2^bits)-1) → min + v*range
      其余属性：逐字节存储
```

### 坐标编码

- X：11 bit，范围 [-2048, 2048]
- Y：10 bit，范围 [-512, 511]（Z 方向高程范围小）
- Z：11 bit，范围 [-2048, 2048]

解码：`real_pos = chunk_min + (packed_value / max_val) * chunk_range`

### 精度损失

- 绝对误差 < 1.5e-5（受 chunk 尺寸影响，chunk 越小精度越高）
- 来源：整数量化 + IEEE 754 双步转换，不可避免

---

## 工具链

### splat-transform

```bash
# 安装
npm install -g splat-transform

# 压缩（标准 PLY → .compressed.ply）
splat-transform -i input.ply -o output.compressed.ply

# 解压（.compressed.ply → 标准 PLY）
splat-transform -i output.compressed.ply -o decoded.ply
```

**源码**：`https://github.com/playcanvas/splat-transform`
**原理**：解析 PLY 头 → 按 chunk 分组高斯 → 坐标量化编码 → 写回 PLY

### PlayCanvas SuperSplat

- Web 版本：`https://playcanvas.github.io/supersplat/`
- 支持加载 .compressed.ply 并可视化
- 不支持标准 PLY 的 `float x y z` 明文坐标格式

### GridMaster

- ❌ 不支持 .compressed.ply
- 原因：GridMaster 读取 `float x y z`，而压缩版是 `uint packed_position`
- 解决方案：压缩后需解压回标准 PLY 再导入 GridMaster

### 其他工具

| 工具 | 支持 compressed.ply | 备注 |
|------|------|------|
| GaussianEditor | ❌ | 专注编辑，不支持压缩格式 |
| 3DGS-Toolbox | ❌ | 不支持 compressed.ply |
| NVIDIA 3DGS SDK | ❌ | 无相关功能 |

---

## 批量压缩方案

### 数据规模

- 数据集：`E:\3DGS模型 新塍至王江泾524国道\Data\`
- 标准 PLY 文件：886 个（140 个 Tile，L15~L21）
- 单文件平均：5.6 MB
- 估算总大小：标准版 4.9 GB → 压缩后 1.1 GB

### 批量脚本

```bash
# 并行压缩（8 核）
find /mnt/e/3DGS模型\ 新塍至王江泾524国道/Data \
  -name "point_cloud_L*.ply" \
  -not -name "*.compressed.ply" \
  | xargs -P 8 -I {} sh -c 'splat-transform -i "{}" -o "{}.compressed.ply"'
```

预计耗时：10~20 分钟（886 个文件）

---

## 决策建议

- ✅ 压缩：模型多（>10 个）、存储紧张、需要网络传输
- ❌ 不压缩：模型少（<10 个）、需要 GridMaster 编辑、精度要求极高
- **推荐策略**：保留标准 PLY 用 GridMaster 编辑；另存压缩版用于存档/传输

---

## 后续待研究

- 若 GridMaster 升级支持 .compressed.ply，压缩方案价值大幅提升
- 若未来需要实时流式加载，可研究分块渐进式解压
- 量化精度可调（当前固定 11/10/11 bit），如需更高精度可探索
