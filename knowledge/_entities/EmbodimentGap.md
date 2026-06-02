---
title: Embodiment Gap 本体差异
type: entity
date_created: 2026-06-02
last_updated: 2026-06-02
aliases:
  - Embodiment Gap
  - 本体差异
sources:
  - knowledge/robotics-embodied-ai/08-umi-gripper-research-and-business-plan.md
tags:
  - entity/risk
  - industry/robotics-embodied-ai
  - umi
status: active
---

# Embodiment Gap 本体差异

## 初学者解释

Embodiment gap 指不同身体结构或机器人结构之间的差异。

人手、UMI 手持夹爪、UR 机械臂、Franka 机械臂、人形机器人都有不同 embodiment。

业务意义：跨本体数据价值大，但动作映射和可执行性更难。

## 补充说明

补充：本体差异决定了数据能否跨机器人复用。人手、手持夹爪、平行夹爪、灵巧手和双臂机器人之间的 retargeting 是高价值但高难度能力。

## 在 UMI 数据闭环中的位置

- **采集侧：** 判断它是否影响传感器选择、操作者 SOP、标定、时间同步或原始数据质量。
- **处理侧：** 判断它是否影响轨迹恢复、字段设计、数据格式、episode 切分和质量等级。
- **训练/部署侧：** 判断它是否影响 policy 输入输出、机器人可执行性、rollout 成功率和跨本体迁移。

## 易错边界

- 不要只按字面翻译理解；在机器人数据里，它通常和坐标系、时间轴、动作表示、数据 schema 共同起作用。
- 不要把“能记录”误认为“可训练”；只有经过标定、同步、质检并能被训练代码读取的数据，才有稳定商业价值。
- 如果用于 ToB 交付，应明确记录字段定义、单位、采样率、质量等级和失败口径。

## 关联连接

- [[RelativePose]]
- [[KinematicFeasibility]]
- [[UniversalManipulationInterface]]
- [[robotics-embodied-ai/08-umi-gripper-research-and-business-plan|UMI Gripper 研究与业务计划]]
- [[_entities/README|UMI 技术术语实体索引]]
