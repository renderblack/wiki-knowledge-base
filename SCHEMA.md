# Wiki Schema — 中国经济转型与化债

## Domain

中国地方政府债务风险化解（化债）政策体系、经济转型路径、财政货币政策协调。覆盖 2024—2026 年本轮化债周期全貌。

## Conventions

- 文件名：小写、英文优先、中文可用（如 `hidden-debt.md`）
- 每个 wiki 页面以 YAML frontmatter 开头
- 使用 `[[wikilinks]]` 关联其他页面（每页至少 2 条出链）
- 更新页面时同步更新 `updated` 日期
- 新页面必须加入 `index.md`
- 所有操作追加到 `log.md`

## Tag Taxonomy

### 债务类型
- `hidden-debt`: 隐性债务
- `explicit-debt`: 显性债务
- `lgfv-debt`: 城投债务
- `refinancing`: 债务置换/再融资

### 主体
- `central-gov`: 中央政府（财政部、发改委、央行）
- `local-gov`: 地方政府
- `lgfv`: 城投平台公司
- `bank-sector`: 银行体系

### 政策工具
- `bond-swap`: 置换债
- `special-bond`: 专项债
- `fiscal-policy`: 财政政策
- `monetary-policy`: 货币政策
- `debt-restructuring`: 债务重组

### 概念
- `debt-resolution`: 化债（化解债务风险）
- `fiscal-pressure`: 财政压力
- `fiscal-deficit`: 财政赤字
- `leverage`: 杠杆率
- `property-crisis`: 房地产危机
- `deflation`: 通缩
- `investment`: 固定资产投资

### 分析维度
- `macro`: 宏观经济
- `micro`: 微观主体（企业/居民）
- `regional`: 区域差异
- `timeline`: 时间线
- `comparison`: 对比分析
- `prediction`: 预测判断

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

## 数据精确性规则

- 政府数字精确到小数点后一位（如"4%左右"）
- 机构名称用全称（如"财政部"非"财政部门"）
- 百分比变化标注方向（"降至"vs"升至"）
