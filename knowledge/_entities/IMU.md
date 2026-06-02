---
title: IMU 惯性测量单元
type: entity
date_created: 2026-06-02
last_updated: 2026-06-02
aliases:
  - IMU
  - Inertial Measurement Unit
  - 惯性测量单元
sources:
  - knowledge/robotics-embodied-ai/08-umi-gripper-research-and-business-plan.md
tags:
  - entity/sensor
  - industry/robotics-embodied-ai
  - umi
status: active
---

# IMU 惯性测量单元

## 初学者解释

IMU 是 Inertial Measurement Unit，惯性测量单元。你写的 “ime” 大概率指的是 IMU。

IMU 通常测量两类信息：加速度和角速度。它不能直接告诉你绝对位置，但能帮助估计设备运动。

在 UMI 中，GoPro 视频里的 IMU 数据和图像一起用于视觉惯性 SLAM，提高轨迹恢复能力。

容易误解：IMU 不是 GPS。IMU 会漂移，单独用很难长期准确定位，需要和视觉、LiDAR 或其他传感器融合。

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

- [[VisualInertialSLAM]]
- [[GoPro]]
- [[TimeSynchronization]]
- [[robotics-embodied-ai/08-umi-gripper-research-and-business-plan|UMI Gripper 研究与业务计划]]
- [[_entities/README|UMI 技术术语实体索引]]
