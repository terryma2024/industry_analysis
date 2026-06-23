---
title: Intel RealSense T265
type: entity
date_created: 2026-06-02
last_updated: 2026-06-02
aliases:
  - T265
  - Intel RealSense T265
sources:
  - knowledge/robotics-embodied-ai/08-umi-gripper-research-and-business-plan.md
tags:
  - entity/product
  - industry/robotics-embodied-ai
  - umi
status: active
---

# Intel RealSense T265

## 初学者解释

T265 通常指 Intel RealSense Tracking Camera T265，一种面向设备定位和运动追踪的追踪相机。

初学可以把它理解成：普通相机主要给你图像，T265 这类追踪相机则试图直接给你“设备现在在哪里、朝向哪里”的 6DoF pose。它内部依赖视觉惯性里程计/SLAM 类能力，把相机和 IMU 信息融合成运动轨迹。

在 FastUMI 路线里，T265 被用来替代原始 UMI 中更复杂的 GoPro + ORB-SLAM3 轨迹恢复流程。这样做的好处是工程上更直接，少一部分 SLAM 调试工作；坏处是会依赖一个具体商用传感器。

业务意义：T265 已经停产，且 FastUMI 相关资料提示它不被后续 librealsense 版本支持。因此商业产品不应押注长期采购 T265，而应把 `pose_source` 抽象出来，支持 RoboBaton Mini、ARKit、Vive Tracker、LiDAR-SLAM、外部 MoCap 或其他国产 VIO 模块。证据：[`SRC-robotics-069`](../../raw/robotics-embodied-ai/documents/SRC-robotics-069-fast-umi-a-scalable-and-hardware-independent-universal-manipulation-interface.md)、[[robotics-embodied-ai/research-notes/umi-hardware-localization-2026-05-27]]。

容易误解：T265 不是普通深度相机，也不是训练算法。它只是位姿追踪来源之一；即使用 T265，也仍然需要标定、时间同步、数据质检和机器人端适配。

## 补充说明

补充：T265 的经验说明，商业化 UMI-like 产品不能把核心能力绑定在一个停产传感器上，应把位姿来源抽象成可替换模块。

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
- [[SLAM]]
- [[UniversalManipulationInterface]]
- [[robotics-embodied-ai/08-umi-gripper-research-and-business-plan|UMI Gripper 研究与业务计划]]
- [[_entities/README|UMI 技术术语实体索引]]
