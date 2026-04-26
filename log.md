# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete

## [2026-04-19] create | Wiki initialized
- Domain: 中国经济转型与化债
- Structure created with SCHEMA.md, index.md, log.md

## [2026-04-19] ingest | 3 articles + 1 RHG report
Sources:
- raw/articles/caixin-2026-debt-map.md（财新周刊2026化债图谱）
- raw/articles/sina-swap-bond-2026.md（新浪财经2万亿置换债报道）
- raw/articles/rhg-china-economy-2026.md（Rhodium Group中国经济报告）

## [2026-04-19] create | 10 wiki pages
Entities: hidden-debt, swap-bond, local-government-financing-vehicles, ministry-of-finance
Concepts: debt-resolution, fiscal-deficit, deflation, investment-collapse, property-crisis
Comparisons: debt-scale-gap

## [2026-04-19] ingest | 4 new articles
Sources:
- raw/articles/21jingji-2025-debt-2026-outlook.md（21世纪经济报道：2025年化债债券3.59万亿，2026年2.8万亿框架）
- raw/articles/wallstreetcn-debt-resolution-impact.md（华尔街见闻/中金固收：10万亿化债影响，城投债供给预测）
- raw/articles/thinkchina-10trillion-gap.md（Think China/Lianhe Zaobao：10万亿化债不够，IMF口径60万亿）
- raw/articles/cls-debt-resolution-midterm.md（财联社：化债半程成绩单，1年隐债减少近4万亿，平台退出超6成）

## [2026-04-19] update | 5 wiki pages
- hidden-debt.md：新增债务规模争议（官方 vs IMF）、利息节约数据（>4500亿）
- local-government-financing-vehicles.md：退出时间表细化（2025→6成/2026→9成/2027→全部）
- central-economic-work-conference.md：新建实体页，中央经济工作会议化债部署
- debt-resolution.md：进展数据更新（截至2025年9月），"加减乘除"四要点
- debt-gap.md：新建概念页，官方 vs IMF vs 真实债务规模对比


## [2026-04-19] create | 1 concept page
- lgfv-bond-maturity.md：城投债到期压力，9万亿到期时间轴、2027年6月金边属性弱化、经营性债务风险


## [2026-04-19] create | 1 comparison page
- china-vs-japan-vs-euro-crisis.md：中国化债 vs 日本失去十年 vs 欧债危机，从触发因素/处置路径/经济结果/制度根源四个维度对比


## [2026-04-19] create | Cron job for weekly wiki updates
- Job ID: e45967377326
- Name: 中国化债知识库周更
- Schedule: 每周一 09:00 (cron: 0 9 * * 1)
- Deliver: telegram
- Skills: llm-wiki, karpathy-mental-models
- Task: 搜索本周化债相关文章，抓取并保存到 ~/wiki/raw/articles/，如有新内容则更新 wiki-ingest-hint

## [2026-04-21] update | 3DGS 压缩方案 + 批量压缩 + 坐标修复
- 压缩方案文档：`projects/3dgs/3dgs-compression-plan.md`
- 工作日志：`projects/3dgs/2025-04-21-work-log.md`
- Data-Compression/：137个L20压缩至905MB（4.18×）
- 合并文件：`point_cloud_L20_merged_correct.ply`（3.04GB，无缝）
- 坐标公式修复：`world = SRS + raw_ply_xyz`（Box.Center勿加）
- Skills：`3dgs-tile-model-workflow` + `splat-transform-compressed-ply`

## [2026-04-21] create | 日结定时任务 + 项目进度页
- 新增 cron job：每日 19:00 结构化日结（job_id: fb2e80cad6fa）
- 新增：`projects/3dgs/PROGRESS.md`（按季度记录里程碑）

## [2026-04-21] create | 课题进度页体系 + index.md 重建
- 13个课题新建 PROGRESS.md：化债/每日观察/航拍/ACU/AI生态/CLI/VLM/EchoMan/钢铁/CAD识别/CAD生成/三维/REAL
- 2个课题新建 INDEX.md：化债/航拍
- 重建 wiki/index.md：清理重复章节，建立课题进度链接体系

## [2026-04-25] restructure | Wiki schema 全面整理
- 更新 SCHEMA.md：扩展 domain 至「虚拟技术部 + 中国经济 + AI前沿」
- 重建 index.md：按 Entity/Concept/Comparison/Projects 四层结构
- 新建 entities/company/：virtual-tech-dept-2026, construction-progress-viz, unityplate
- 新建 concepts/tech/：3dgs, ai-agent, vlm, cad-intelligence
- concepts/debt/：将散在根目录的7个化债概念页迁入子目录
- 删除 wiki/knowledge/ 孤儿目录
- 迁移私人内容至 ~/.hermes/private/：self-understanding/, worldview/, career-development.md, micro-environment.md
- 新建 raw/INDEX.md：12篇原始资料索引

## [2026-04-25] update | 实体页信息补全
- entities/company/unityplate.md：补充核心定位、功能模块（4个）、技术栈、验收状态、对照集成平台方案
- entities/company/construction-progress-viz.md：补充核心定位、8大功能模块、技术栈、关键概念、验收状态
- entities/company/virtual-tech-dept-2026.md：补充两大产品定位对比、技术栈差异、战略方向、当前挑战
