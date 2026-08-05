---
title: cuVSLAM
type: entity
date_created: 2026-08-05
last_updated: 2026-08-05
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-346-nvidia-cuvslam-official-repository-readme-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-354-cuvslam-cuda-accelerated-visual-odometry-and-mapping-paper-full-pdf.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-355-cuvslam-nvidia-community-license-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-356-cuvslam-github-repository-release-and-maintenance-audit.md
tags:
  - entity/tool
  - slam
  - cuda
  - nvidia
status: active
aliases:
  - NVIDIA cuVSLAM
---

# cuVSLAM

cuVSLAM 是 NVIDIA 的 CUDA 加速视觉 odometry 与 mapping 库，采用低延迟局部前端和异步回环/pose-graph 后端，支持 Mono、RGB-D、multi-camera、stereo-inertial 和实验性 Multisensor 模式，并通过 Isaac ROS 接入 ROS 2。

## 选型速记

- **适合**：Jetson/RTX、多方向硬件同步相机、实时定位和 NVIDIA 机器人栈。
- **不等于**：跨平台开源 SLAM、Nav2 occupancy map 或无需标定的视觉定位黑盒。
- **当前快照**：最新 release `v17.0.0` 发布于 2026-07-23；审计 head 为 2026-07-28。
- **许可边界**：NVIDIA Community License 允许商业使用/衍生分发，但只授权 NVIDIA Platforms；非 NVIDIA 迁移是许可和技术双重门槛。

## 关联连接

- [[robotics-embodied-ai/research-notes/rtabmap-cuvslam-openvins-comparative-deep-dive-2026-08-05|三方案深度调研]]
- [[_sources/rtabmap-cuvslam-openvins-source-set|来源集]]
- [[SLAM]]
- [[RTABMap|RTAB-Map]]
- [[OpenVINS]]
- [[robotics-embodied-ai/research-notes/isaac-sim-vs-gazebo-vs-mujoco-2026-07-14|NVIDIA Isaac Sim]]
