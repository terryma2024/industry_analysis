---
title: OpenVINS
type: entity
date_created: 2026-08-05
last_updated: 2026-08-05
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-344-openvins-official-repository-readme-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-357-openvins-research-platform-for-visual-inertial-estimation-paper-full-pdf.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-358-openvins-official-project-features-and-architecture-documentation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-359-openvins-official-sensor-calibration-guide.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-360-openvins-github-repository-release-and-maintenance-audit.md
tags:
  - entity/tool
  - vio
  - msckf
  - calibration
status: active
aliases:
  - Open VINS
---

# OpenVINS

OpenVINS 是 RPNG 开发的 visual-inertial estimation 研究平台。核心是带 IMU pose clones 的滑窗 EKF/MSCKF，提供 FEJ、可扩展状态/协方差类型、在线相机—IMU 时空标定、静态/动态初始化、仿真与评测工具。

## 选型速记

- **适合**：VIO 研究、滤波一致性、标定、传感器评测、教学和定制 estimator。
- **不等于**：默认全局回环、多会话数据库、占据栅格或完整导航栈；官方 `ov_secondary` 回环是松耦合外部示例。
- **当前快照**：latest tag `v2.7` 为 2023-06-20，默认分支 head 到 2025-11-30；有 ROS 2、ROS-free 和 Docker。
- **许可边界**：GPL-3.0；闭源产品分发需先做架构与法律审查。

## 关联连接

- [[robotics-embodied-ai/research-notes/rtabmap-cuvslam-openvins-comparative-deep-dive-2026-08-05|三方案深度调研]]
- [[_sources/rtabmap-cuvslam-openvins-source-set|来源集]]
- [[SLAM]]
- [[IMU]]
- [[RTABMap|RTAB-Map]]
- [[cuVSLAM]]

