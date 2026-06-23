---
title: Observation Gap 观测差异
type: entity
date_created: 2026-06-02
last_updated: 2026-06-02
aliases:
  - Observation Gap
  - 观测差异
sources:
  - knowledge/robotics-embodied-ai/08-umi-gripper-research-and-business-plan.md
tags:
  - entity/risk
  - industry/robotics-embodied-ai
  - umi
status: active
---

# Observation Gap 观测差异

## 初学者解释

Observation gap 指训练时模型看到的画面/状态和部署时看到的不一致。

例如人手持相机采集的数据和机器人腕部相机画面差别太大，模型就可能无法泛化。

UMI 通过相似夹爪和相似腕部相机来减少这个差异。

## 补充说明

补充：观测差异是 UMI-like 路线能否泛化的核心风险之一；设备设计、相机安装位置、视角畸变、光照和机器人端传感器都需要尽量匹配。

## 在 UMI 数据闭环中的位置

- **采集侧：** 判断它是否影响传感器选择、操作者 SOP、标定、时间同步或原始数据质量。
- **处理侧：** 判断它是否影响轨迹恢复、字段设计、数据格式、episode 切分和质量等级。
- **训练/部署侧：** 判断它是否影响 policy 输入输出、机器人可执行性、rollout 成功率和跨本体迁移。

## 易错边界

- 不要只按字面翻译理解；在机器人数据里，它通常和坐标系、时间轴、动作表示、数据 schema 共同起作用。
- 不要把“能记录”误认为“可训练”；只有经过标定、同步、质检并能被训练代码读取的数据，才有稳定商业价值。
- 如果用于 ToB 交付，应明确记录字段定义、单位、采样率、质量等级和失败口径。

## 关联连接

- [[Observation]]
- [[WristView]]
- [[RobotMounted]]
- [[robotics-embodied-ai/08-umi-gripper-research-and-business-plan|UMI Gripper 研究与业务计划]]
- [[_entities/README|UMI 技术术语实体索引]]
