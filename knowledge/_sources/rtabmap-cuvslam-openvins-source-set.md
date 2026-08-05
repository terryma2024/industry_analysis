---
title: RTAB-Map、cuVSLAM、OpenVINS 论文、文档与代码来源集
type: source
date_created: 2026-08-05
last_updated: 2026-08-05
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-344-openvins-official-repository-readme-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-345-rtab-map-ros2-official-repository-readme-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-346-nvidia-cuvslam-official-repository-readme-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-350-rtab-map-large-scale-and-long-term-lidar-and-visual-slam-paper-full-pdf.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-354-cuvslam-cuda-accelerated-visual-odometry-and-mapping-paper-full-pdf.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-357-openvins-research-platform-for-visual-inertial-estimation-paper-full-pdf.md
tags:
  - source-set
  - industry/robotics-embodied-ai
  - slam
  - vio
status: active
aliases:
  - 三套 SLAM VIO 方案来源集
---

# RTAB-Map、cuVSLAM、OpenVINS 论文、文档与代码来源集

> [!summary]
> 本页汇总 [[robotics-embodied-ai/research-notes/rtabmap-cuvslam-openvins-comparative-deep-dive-2026-08-05|三方案深度调研]]的一手证据。论文用于技术机制与作者实验，固定提交文件用于能力/许可，GitHub API 用于 2026-08-05 动态维护快照；不同论文的性能数字不可直接横排。

## 来源矩阵

| 系统 | 技术论文 | 产品/代码 | 动态审计 | 许可证 | 主要用途 |
|---|---|---|---|---|---|
| RTAB-Map | [`SRC-robotics-350`](../../raw/robotics-embodied-ai/documents/SRC-robotics-350-rtab-map-large-scale-and-long-term-lidar-and-visual-slam-paper-full-pdf.md) | [`351`](../../raw/robotics-embodied-ai/documents/SRC-robotics-351-rtab-map-core-repository-readme-at-audited-commit.md)、[`345`](../../raw/robotics-embodied-ai/documents/SRC-robotics-345-rtab-map-ros2-official-repository-readme-at-audited-commit.md) | [`353`](../../raw/robotics-embodied-ai/documents/SRC-robotics-353-rtab-map-github-repository-release-and-maintenance-audit.md) | [`352`](../../raw/robotics-embodied-ai/documents/SRC-robotics-352-rtab-map-core-bsd-3-clause-license-at-audited-commit.md)、[`349`](../../raw/robotics-embodied-ai/documents/SRC-robotics-349-rtab-map-ros2-bsd-3-clause-license-at-audited-commit.md) | WM/LTM、graph、occupancy、ROS 2、版本与 BSD 边界 |
| cuVSLAM | [`SRC-robotics-354`](../../raw/robotics-embodied-ai/documents/SRC-robotics-354-cuvslam-cuda-accelerated-visual-odometry-and-mapping-paper-full-pdf.md) | [`346`](../../raw/robotics-embodied-ai/documents/SRC-robotics-346-nvidia-cuvslam-official-repository-readme-at-audited-commit.md) | [`356`](../../raw/robotics-embodied-ai/documents/SRC-robotics-356-cuvslam-github-repository-release-and-maintenance-audit.md) | [`355`](../../raw/robotics-embodied-ai/documents/SRC-robotics-355-cuvslam-nvidia-community-license-at-audited-commit.md) | CUDA frontend/backend、多相机/VI/RGB-D、v17、NVIDIA-only 授权 |
| OpenVINS | [`SRC-robotics-357`](../../raw/robotics-embodied-ai/documents/SRC-robotics-357-openvins-research-platform-for-visual-inertial-estimation-paper-full-pdf.md) | [`344`](../../raw/robotics-embodied-ai/documents/SRC-robotics-344-openvins-official-repository-readme-at-audited-commit.md)、[`358`](../../raw/robotics-embodied-ai/documents/SRC-robotics-358-openvins-official-project-features-and-architecture-documentation.md)、[`359`](../../raw/robotics-embodied-ai/documents/SRC-robotics-359-openvins-official-sensor-calibration-guide.md) | [`360`](../../raw/robotics-embodied-ai/documents/SRC-robotics-360-openvins-github-repository-release-and-maintenance-audit.md) | [`361`](../../raw/robotics-embodied-ai/documents/SRC-robotics-361-openvins-gpl-3-0-license-at-audited-commit.md) | MSCKF、标定/仿真、回环边界、head/tag 与 GPL |

## 证据质量与限制

- `S` 级均为作者论文、项目官方文档、固定提交或官方 API；不代表论文 benchmark 独立复现。
- RTAB-Map 论文的 journal reference 为 2019，arXiv deposit 为 2024；技术机制优先于旧硬件速度。
- cuVSLAM 论文与 release KPI 均为 NVIDIA 作者报告，包含对失败序列的预处理/排除说明；不得外推为客户 SLA。
- OpenVINS 2020 论文验证研究平台设计；当前能力以 2026-08-05 文档与 2025 head 补充。
- 许可证页只做事实摘录，不构成法律意见，依赖和最终分发架构需另审。

## 关联连接

- [[robotics-embodied-ai/research-notes/rtabmap-cuvslam-openvins-comparative-deep-dive-2026-08-05|RTAB-Map、cuVSLAM、OpenVINS 技术与工程选型深度调研]]
- [[RTABMap|RTAB-Map]]
- [[cuVSLAM]]
- [[OpenVINS]]
- [[_sources/orb-slam3-paper-code-benchmark-source-set|ORB-SLAM3 来源集]]

