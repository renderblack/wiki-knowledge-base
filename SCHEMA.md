# Wiki Schema — 虚拟技术部知识库

## Domain

本 wiki 覆盖三大领域：

1. **虚拟技术部** — 兴土智瞰（G202501）、UnityPlate（交通工程三维可视化平台）、集成平台战略执行平台
2. **中国经济** — 地方政府债务化解、房地产危机、财政货币政策、中国买单者
3. **AI 前沿** — 3DGS（Gaussian Splatting）、AI Agent、VLM、多模态、CAD智能化

## Conventions

- 文件名：小写、英文优先、中文可用（如 `hidden-debt.md`、`virtual-tech-dept-2026.md`）
- 每个 wiki 页面以 YAML frontmatter 开头（title, created, updated, type, tags, sources）
- 使用 `[[wikilinks]]` 关联其他页面（每页至少 2 条出链）
- 更新页面时同步更新 `updated` 日期
- 新页面必须加入 `index.md` 相应章节
- 所有操作追加到 `log.md`
- `projects/` 目录保留但进 index，每项目至少一个 `PROGRESS.md` 记录里程碑

## Tag Taxonomy

### 主体（Entities）
- `company`: 公司（兴土桥梁、虚拟技术部）
- `product`: 产品（兴土智瞰、UnityPlate）
- `person`: 人物（老板朱兴土等）
- `institution`: 机构（中央/地方政府、城投、银行）

### 话题（Concepts）
- `debt-resolution`: 化债
- `property-crisis`: 房地产危机
- `fiscal-policy`: 财政政策
- `monetary-policy`: 货币政策
- `macro-economy`: 宏观经济
- `3dgs`: Gaussian Splatting
- `ai-agent`: AI Agent
- `vlm`: 视觉语言模型
- `cad-intelligence`: CAD智能化
- `construction-viz`: 施工可视化
- `drone-imagery`: 航拍图像

### 分析维度（Meta）
- `comparison`: 对比分析
- `timeline`: 时间线
- `progress`: 进度追踪
- `prediction`: 预测判断
- `case-study`: 案例研究

## Page Thresholds

- **建页面**：实体/概念在 2+ 来源中出现，或在 1 个核心来源中被深入讨论
- **追加现有页**：来源提到已覆盖的实体/概念
- **不建页面**：仅一次性提及、非本领域内容

## Entity Pages

包含：概述、关键事实与日期、关联实体（wikilinks）、来源引用。

## Concept Pages

包含：定义、当前认知状态、争议与开放问题、关联概念（wikilinks）。

## Comparison Pages

包含：对比对象与原因、维度对比（表格格式优先）、判断或综合结论、来源。

## Update Policy

新信息与现有内容冲突时：
1. 以较新来源为准
2. 真正矛盾时，两个立场并存并标注日期和来源
3. frontmatter 标记：`contradictions: [page-name]`
4. 在 lint 报告中标记给用户仲裁

## 目录结构

```
wiki/
├── index.md              ← 统一入口，总览所有课题
├── SCHEMA.md              ← 本文件
├── log.md                 ← 操作日志
├── raw/                   ← Layer 1：原始资料（只读）
│   ├── articles/          ← 网页剪藏
│   └── papers/            ← 论文/PDF
├── entities/              ← Layer 2：实体页
│   └── company/           ← 公司/产品/人物
├── concepts/              ← Layer 2：概念页
│   ├── debt/              ← 化债相关概念
│   └── tech/              ← AI/3DGS技术概念
├── comparisons/           ← Layer 2：对比分析
└── projects/              ← 项目进度（进 index）
    ├── construction-progress-viz-system/
    ├── 3d-visualization-platform/
    └── ...
```
