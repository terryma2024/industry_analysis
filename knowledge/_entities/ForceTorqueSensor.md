---
title: Force/Torque Sensor 力/力矩传感器
type: entity
date_created: 2026-06-02
last_updated: 2026-06-02
aliases:
  - Force/Torque Sensor
  - F/T Sensor
  - 力/力矩传感器
sources:
  - knowledge/robotics-embodied-ai/08-umi-gripper-research-and-business-plan.md
tags:
  - entity/sensor
  - industry/robotics-embodied-ai
  - umi
status: active
---

# Force/Torque Sensor 力/力矩传感器

## 初学者解释

力/力矩传感器可以测量力和扭矩。

在机器人操作中，它用于感知接触，例如插入、擦拭、压紧、拧动。

UMI-FT 和 TacUMI 强调力/触觉，是因为很多接触丰富任务只靠视觉不够。

## 补充说明

补充：力/力矩传感器比纯视觉更接近“接触是否正确”的真值，可用于构建 VLTA/VTLA 数据，但会提高硬件成本和系统集成难度。

## 在 UMI 数据闭环中的位置

- **采集侧：** 判断它是否影响传感器选择、操作者 SOP、标定、时间同步或原始数据质量。
- **处理侧：** 判断它是否影响轨迹恢复、字段设计、数据格式、episode 切分和质量等级。
- **训练/部署侧：** 判断它是否影响 policy 输入输出、机器人可执行性、rollout 成功率和跨本体迁移。

## 易错边界

- 不要只按字面翻译理解；在机器人数据里，它通常和坐标系、时间轴、动作表示、数据 schema 共同起作用。
- 不要把“能记录”误认为“可训练”；只有经过标定、同步、质检并能被训练代码读取的数据，才有稳定商业价值。
- 如果用于 ToB 交付，应明确记录字段定义、单位、采样率、质量等级和失败口径。

## 关联连接

- [[TactileSensor]]
- [[Action]]
- [[QualityControl]]
- [[robotics-embodied-ai/08-umi-gripper-research-and-business-plan|UMI Gripper 研究与业务计划]]
- [[_entities/README|UMI 技术术语实体索引]]
