# 化债研究 — 项目进度

> 按季度记录里程碑。月底汇总写入此页。

---

## 2026 年度

### Q1（1-3月）
*暂无系统记录*

### Q2（4-6月）

#### 4月19-21日 — 知识库初始化
- 从 6 篇原始文章建立概念和实体页面
- 关键实体：hidden-debt, swap-bond, lgfv-bond-maturity, local-government-financing-vehicles
- 关键概念：debt-resolution, fiscal-deficit, debt-gap, investment-collapse, deflation

#### 每周一 — cron 自动更新
- 任务 ID: `e45967377326`，每周一 5:00 推送
- 扫描本周新发表的化债相关文章
- 自动 ingest 到 `raw/articles/` 并更新相关概念/实体页面
