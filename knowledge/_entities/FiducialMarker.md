---
title: Fiducial Marker 基准标记
type: entity
date_created: 2026-06-02
last_updated: 2026-06-02
aliases:
  - Fiducial Marker
  - 基准标记
  - AprilTag
  - ArUco
sources:
  - knowledge/robotics-embodied-ai/08-umi-gripper-research-and-business-plan.md
tags:
  - entity/vision-tool
  - industry/robotics-embodied-ai
  - umi
status: active
---

# Fiducial Marker 基准标记

## 初学者解释

Fiducial marker 是一种带编码的视觉标记，系统可以识别它的身份和姿态。

在 UMI 中，它可以用于夹爪宽度估计、相机标定或坐标对齐。

业务意义：它适合 v0 原型，但商业产品可能要换成编码器、霍尔传感器或电机反馈来提升稳定性。

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

- [[Marker]]
- [[Calibration]]
- [[GripperWidth]]
- [[robotics-embodied-ai/08-umi-gripper-research-and-business-plan|UMI Gripper 研究与业务计划]]
- [[_entities/README|UMI 技术术语实体索引]]
