---
title: Coordinate Frame 坐标系
type: entity
date_created: 2026-06-02
last_updated: 2026-06-02
aliases:
  - Coordinate Frame
  - 坐标系
sources:
  - knowledge/robotics-embodied-ai/08-umi-gripper-research-and-business-plan.md
tags:
  - entity/robotics-frame
  - industry/robotics-embodied-ai
  - umi
status: active
---

# Coordinate Frame 坐标系

## 初学者解释

坐标系是用来描述位置和方向的参考框架。

机器人里常见坐标系包括世界坐标系、机器人基座坐标系、相机坐标系、夹爪坐标系、TCP 坐标系。

UMI 的难点之一就是把相机看到的运动、手持夹爪运动和机器人末端运动放到可对齐的坐标系里。

## 补充说明

补充：在 UMI-like 数据采集业务中，这个术语既要按技术定义理解，也要按“是否影响可训练数据交付、质检和客户复现”来理解。初学者应优先掌握它和 observation、action、episode、schema、quality control 之间的关系。

## 在 UMI 数据闭环中的位置

- **采集侧：** 判断它是否影响传感器选择、操作者 SOP、标定、时间同步或原始数据质量。
- **处理侧：** 判断它是否影响轨迹恢复、字段设计、数据格式、episode 切分和质量等级。
- **训练/部署侧：** 判断它是否影响 policy 输入输出、机器人可执行性、rollout 成功率和跨本体迁移。

## 易错边界

- 不要只按字面翻译理解；在机器人数据里，它通常和坐标系、时间轴、动作表示、数据 schema 共同起作用。
- 不要把“能记录”误认为“可训练”；只有经过标定、同步、质检并能被训练代码读取的数据，才有稳定商业价值。
- 如果用于 ToB 交付，应明确记录字段定义、单位、采样率、质量等级和失败口径。

## 关联连接

- [[Calibration]]
- [[Pose]]
- [[ToolCenterPoint]]
- [[robotics-embodied-ai/08-umi-gripper-research-and-business-plan|UMI Gripper 研究与业务计划]]
- [[_entities/README|UMI 技术术语实体索引]]
