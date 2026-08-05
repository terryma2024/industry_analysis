---
title: RTAB-Map
type: entity
date_created: 2026-08-05
last_updated: 2026-08-05
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-350-rtab-map-large-scale-and-long-term-lidar-and-visual-slam-paper-full-pdf.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-351-rtab-map-core-repository-readme-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-353-rtab-map-github-repository-release-and-maintenance-audit.md
tags:
  - entity/tool
  - slam
  - ros2
  - mapping
status: active
aliases:
  - RTABMap
  - Real-Time Appearance-Based Mapping
---

# RTAB-Map

RTAB-Map 是 IntRoLab 维护的长期在线视觉/LiDAR graph-SLAM 库和独立应用。它允许自带或外部 odometry，使用视觉回环、几何 proximity、图优化和 Working Memory/Long-Term Memory 管理大图，并输出图、数据库、点云、2D occupancy 和 OctoMap。

## 选型速记

- **适合**：ROS 2 移动机器人、Nav2、RGB-D/stereo/LiDAR 比较、多会话数据库和导航地图。
- **不等于**：单一最强 VIO 前端、语义/动态地图或功能安全导航产品。
- **当前快照**：core `0.23.8` 发布于 2026-07-05；审计 head 为 2026-08-03；core 与 ROS package 为 BSD-3-Clause 文本。
- **核心风险**：参数复杂、弱纹理/几何退化、误回环、动态障碍和大图资源/地图完整性权衡。

## 关联连接

- [[robotics-embodied-ai/research-notes/rtabmap-cuvslam-openvins-comparative-deep-dive-2026-08-05|三方案深度调研]]
- [[_sources/rtabmap-cuvslam-openvins-source-set|来源集]]
- [[SLAM]]
- [[robotics-embodied-ai/research-notes/dora-1-vs-ros2-2026-06-23|ROS 2 与 dora]]
- [[cuVSLAM]]
- [[OpenVINS]]
