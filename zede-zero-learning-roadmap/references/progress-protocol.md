# Progress Protocol v2（进度协议）

保存、更新或恢复路线时完整读取本文件。每次创建或更新文件前都必须重新获得用户明确同意。

## 目录

- 文件位置
- YAML frontmatter
- 正文结构
- 创建与更新
- 恢复与迁移

## 文件位置

默认不创建文件。用户同意后，在当前合适工作区使用：

`learning-roadmaps/<goal-english-slug>.md`

使用小写英文和连字符生成文件名。若没有合适工作区，先询问保存位置。

## YAML frontmatter

```yaml
---
schema_version: 2
goal_id: python-automation
goal_type: technical-project
status: active
target_date: 2026-10-31
plan_revision: 1
output_mode: layered
current_stage: foundations
weekly_hours: 8
last_updated: 2026-07-27
sources_checked_on: 2026-07-27
verified_capabilities: []
unresolved_gaps: []
next_checkpoint: 2026-08-03
---
```

字段约束：

- `schema_version`：当前固定为整数 `2`
- `goal_id`：与文件名一致的小写英文短名，路线建立后保持不变
- `goal_type`：只能是 `exam-certification`、`technical-project`、`career-transition`、`language-expression`、`theory-academic`、`business-entrepreneurship` 或 `exploration`
- `status`：只能是 `planning`、`active`、`paused` 或 `completed`
- `target_date`：`YYYY-MM-DD`；没有固定期限时为 `null`
- `plan_revision`：正整数；首次正式路线为 `1`
- `output_mode`：只能是 `layered` 或 `full`
- `current_stage`：当前阶段的稳定英文短名
- `weekly_hours`：当前每周可用小时数，必须大于 `0`
- `last_updated`：最近一次写入日期，格式为 `YYYY-MM-DD`
- `sources_checked_on`：关键来源最近核验日期；尚未核验时为 `null`
- `verified_capabilities`：仅列出有任务、作品或验收证据的能力
- `unresolved_gaps`：列出尚未验证或仍阻塞路线的能力
- `next_checkpoint`：下次检查日期；完成且无需检查时为 `null`

不要把用户自述写入 `verified_capabilities`。

## 正文结构

frontmatter 之后固定包含：

- 目标卡
- 第一性原理摘要
- 诊断证据与置信度
- 依据表与来源核验状态
- 三层成果
- 具体学习内容与项目模块映射
- 任务、暴露缺口、即时学习与产出证据
- 当前阶段
- 完整路线与资源
- 当前周期计划
- 完成记录与验收结果
- 迁移证据与反馈来源
- 7/30/90 天复测记录
- 卡点与风险
- 检查点效果记录
- 调整记录
- 最近更新时间

每次检查点效果记录至少包含：计划时间、实际时间、任务完成率、阶段验收通过率、主要卡点类型、主资源帮助程度和是否需要重新估算。缺少可靠数据时标注未知，不编造精确百分比。

每条迁移证据至少记录：能力、目标迁移层级、完成任务、反馈层级与来源、日期、结果、证据和下一步。反馈层级或来源未知时如实标注，不把自检、AI 建议或用户自述升级为专家、真实用户或正式考试证据。

每条延迟复测至少记录：能力、计划节点、实际日期、复测任务、迁移层级、结果、证据和失败后的聚焦补救。路线在目标完成后仍可保留尚未到期的维护任务，但不得因此把 `status: completed` 改回 `active`，也不得把截止日后的维护时间静默计入原计划预算。

## 创建与更新

每次创建或更新前说明将写入哪些内容，并等待明确同意。

按以下规则维护 `plan_revision`：

- 首次正式路线：设为 `1`
- 目标、期限、验收标准、阶段结构或可用时间发生结构性变化：递增 `1`
- 普通完成记录、卡点、资源反馈或当前周期任务量调整：不递增

每次结构性重排记录日期、触发原因、保留、删除、修改和新的下一步。目标本质、关键结果变量、不可绕过的能力、具体内容或项目模块、最小验证闭环改变时，更新对应摘要与映射。记录代表任务暴露的缺口、为解决它即时学习的内容及产出证据，不能用资源完成记录代替任务证据。保留历史完成记录、迁移证据、反馈来源、延迟复测、检查点效果证据和验收结果，不用新路线覆盖过去证据。

## 恢复与迁移

恢复时完整读取文件，校验协议并简要复述目标、已通过内容、当前卡点、来源时效和下一步，然后只问一个最关键的进度问题。恢复路线不重复首次规则。

兼容规则：

- 没有 frontmatter：视为 legacy v0，从正文恢复；下一次用户同意保存时迁移到 v2
- `schema_version: 1`：按已知 v1 字段恢复；缺少的 v2 字段从正文安全确认，无法确认且会影响路线时逐题询问；下一次获准保存时迁移到 v2
- `schema_version: 2`：校验字段、枚举和日期；低风险缺项可以从正文补全并标注，高影响缺项必须询问
- `schema_version` 大于 `2`：不得覆盖、降级或静默迁移；只读取明确兼容的正文并说明当前 Skill 不支持该版本

任何迁移都必须保留目标卡、可恢复的第一性原理摘要、可识别的具体内容与项目模块、完成记录、验收结果、迁移与反馈证据、延迟复测、检查点效果证据、卡点和调整历史。旧路线没有第一性原理摘要、具体内容映射、迁移层级或反馈层级时从正文安全提取；无法确认时标注未知，不伪造历史内容或层级。只有在用户同意实际写入时才完成迁移。

若 `sources_checked_on` 缺失，或易变化来源超过 30 天未核验、链接失效、版本不明，先标记为待复核；结构性重排前完成复核。
