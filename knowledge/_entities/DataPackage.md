---
title: Data Package 数据包
type: entity
date_created: 2026-06-02
last_updated: 2026-06-02
aliases:
  - Data Package
  - 数据包
sources:
  - knowledge/robotics-embodied-ai/08-umi-gripper-research-and-business-plan.md
tags:
  - entity/business-artifact
  - industry/robotics-embodied-ai
  - umi
status: active
---

# Data Package 数据包

## 初学者解释

数据包是交付给客户的一整套数据资产。

好的机器人数据包不只是视频，还应包含 raw 数据、processed 数据、schema、标定、任务说明、质量报告、训练配置和样例回放。

UMI 报告的商业化建议，本质上是把采集设备变成可交付的数据包服务。

## 补充说明

补充：商业数据包的交付物应包含 raw、processed、metadata、schema、calibration、quality report、training recipe 和 replay/rollout demo；否则客户很难验收。

## 在 UMI 数据闭环中的位置

- **采集侧：** 判断它是否影响传感器选择、操作者 SOP、标定、时间同步或原始数据质量。
- **处理侧：** 判断它是否影响轨迹恢复、字段设计、数据格式、episode 切分和质量等级。
- **训练/部署侧：** 判断它是否影响 policy 输入输出、机器人可执行性、rollout 成功率和跨本体迁移。

## 易错边界

- 不要只按字面翻译理解；在机器人数据里，它通常和坐标系、时间轴、动作表示、数据 schema 共同起作用。
- 不要把“能记录”误认为“可训练”；只有经过标定、同步、质检并能被训练代码读取的数据，才有稳定商业价值。
- 如果用于 ToB 交付，应明确记录字段定义、单位、采样率、质量等级和失败口径。

## 关联连接

- [[DatasetSchema]]
- [[QualityControl]]
- [[BaselineTrainingRecipe]]
- [[robotics-embodied-ai/08-umi-gripper-research-and-business-plan|UMI Gripper 研究与业务计划]]
- [[_entities/README|UMI 技术术语实体索引]]
