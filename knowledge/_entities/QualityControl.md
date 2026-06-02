---
title: Quality Control 数据质检
type: entity
date_created: 2026-06-02
last_updated: 2026-06-02
aliases:
  - Quality Control
  - QC
  - 质检
sources:
  - knowledge/robotics-embodied-ai/08-umi-gripper-research-and-business-plan.md
tags:
  - entity/process
  - industry/robotics-embodied-ai
  - umi
status: active
---

# Quality Control 数据质检

## 初学者解释

质检是检查数据是否可用的过程。

UMI 数据质检可以包括：视频清晰度、SLAM 是否成功、轨迹是否跳变、夹爪宽度是否丢失、episode 边界是否正确、时间同步是否正常。

业务意义：ToB 数据服务的核心竞争力之一就是稳定质检，而不是只采集原始视频。

## 补充说明

补充：机器人数据质检应从原始素材检查升级到训练可用性检查，包括轨迹质量、动作可执行性、时间同步、标定版本、任务成功标签和 baseline rollout。

## 在 UMI 数据闭环中的位置

- **采集侧：** 判断它是否影响传感器选择、操作者 SOP、标定、时间同步或原始数据质量。
- **处理侧：** 判断它是否影响轨迹恢复、字段设计、数据格式、episode 切分和质量等级。
- **训练/部署侧：** 判断它是否影响 policy 输入输出、机器人可执行性、rollout 成功率和跨本体迁移。

## 易错边界

- 不要只按字面翻译理解；在机器人数据里，它通常和坐标系、时间轴、动作表示、数据 schema 共同起作用。
- 不要把“能记录”误认为“可训练”；只有经过标定、同步、质检并能被训练代码读取的数据，才有稳定商业价值。
- 如果用于 ToB 交付，应明确记录字段定义、单位、采样率、质量等级和失败口径。

## 关联连接

- [[SLAM]]
- [[KinematicFeasibility]]
- [[DataPackage]]
- [[robotics-embodied-ai/08-umi-gripper-research-and-business-plan|UMI Gripper 研究与业务计划]]
- [[_entities/README|UMI 技术术语实体索引]]
