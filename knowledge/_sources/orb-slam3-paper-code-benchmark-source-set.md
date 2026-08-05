---
title: ORB-SLAM3 论文、代码与 benchmark 来源集
type: source
date_created: 2026-08-05
last_updated: 2026-08-05
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-338-orb-slam3-full-paper.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-339-orb-slam3-official-repository-readme-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-340-orb-slam3-github-repository-and-maintenance-audit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-341-orb-slam3-v1-0-calibration-tutorial.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-342-orb-slam3-dependency-and-license-inventory-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-343-vins-fusion-official-repository-readme-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-344-openvins-official-repository-readme-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-345-rtab-map-ros2-official-repository-readme-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-346-nvidia-cuvslam-official-repository-readme-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-347-tum-vi-benchmark-official-dataset-page.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-348-euroc-mav-dataset-official-page.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-349-rtab-map-ros2-bsd-3-clause-license-at-audited-commit.md
tags:
  - source/paper
  - source/github
  - source/benchmark
  - industry/robotics-embodied-ai
  - slam
status: active
aliases:
  - ORB-SLAM3 来源摘要
---

# ORB-SLAM3 论文、代码与 benchmark 来源集

> [!summary]
> 本来源集以 ORB-SLAM3 T-RO/arXiv 论文、固定提交的官方仓库/校准/依赖、2026-08-05 GitHub 动态审计、EuRoC/TUM-VI 官方 benchmark 和四套一手替代方案资料为证据底座。稳定结论是：ORB-SLAM3 是多传感器模式统一、支持 Atlas 多地图的稀疏特征 V/VI-SLAM 库；它不是稠密语义导航栈，官方上游也不是现代 ROS 2 成品包。综合判断见 [[robotics-embodied-ai/research-notes/orb-slam3-technology-engineering-commercial-deep-dive-2026-08-05|ORB-SLAM3 深度调研]]。

## 审阅方法

- 论文：保存 arXiv v2 PDF，用 `pdftotext` 生成可检索 Markdown；按表格脚注区分成功序列平均、Sim(3)/SE(3)、作者自跑与他人报告值。
- 代码：固定官方 `master` head `4452a3c4ab75b1cde34e5505a36ec3f9edcdc4c4`，审阅 README、Calibration Tutorial、Dependencies 和根目录结构；未编译运行。
- 维护：2026-08-05 查询 GitHub repository/commits/releases API 与公开 UI；动态计数只用于时间点判断。
- 对照：使用 VINS-Fusion、OpenVINS、RTAB-Map ROS2、cuVSLAM 官方固定提交；只比较产品边界和生态，不做跨硬件速度排名。

## 核心来源

| SRC | 内容 | 等级 | 关键用途 |
|---|---|---:|---|
| [`SRC-robotics-338`](../../raw/robotics-embodied-ai/documents/SRC-robotics-338-orb-slam3-full-paper.md) | ORB-SLAM3 完整论文 | S | 架构、MAP 视觉惯性初始化、Atlas、EuRoC/TUM-VI、timing、低纹理失败 |
| [`SRC-robotics-339`](../../raw/robotics-embodied-ai/documents/SRC-robotics-339-orb-slam3-official-repository-readme-at-audited-commit.md) | 固定提交 README | S | 支持模式、依赖、相机运行流程、ROS1-era、GPL/商业许可路径 |
| [`SRC-robotics-340`](../../raw/robotics-embodied-ai/documents/SRC-robotics-340-orb-slam3-github-repository-and-maintenance-audit.md) | GitHub 维护快照 | S | 当前 head、release、stars/forks/issues/PR；动态计数不可外推 |
| [`SRC-robotics-341`](../../raw/robotics-embodied-ai/documents/SRC-robotics-341-orb-slam3-v1-0-calibration-tutorial.md) | 官方校准教程 | S | 坐标系、双目/IMU 外参、内参、噪声、频率与配置格式 |
| [`SRC-robotics-342`](../../raw/robotics-embodied-ai/documents/SRC-robotics-342-orb-slam3-dependency-and-license-inventory-at-audited-commit.md) | 官方依赖清单 | S | DBoW2/g2o/Sophus/OpenCV/Pangolin/Eigen/ROS 许可链 |
| [`SRC-robotics-343`](../../raw/robotics-embodied-ai/documents/SRC-robotics-343-vins-fusion-official-repository-readme-at-audited-commit.md) | VINS-Fusion 官方 README | S | 优化型多传感器 VIO、在线时空标定、loop/GPS 对照 |
| [`SRC-robotics-344`](../../raw/robotics-embodied-ai/documents/SRC-robotics-344-openvins-official-repository-readme-at-audited-commit.md) | OpenVINS 官方 README | S | MSCKF、仿真/标定、ROS 2 和 GPLv3 对照 |
| [`SRC-robotics-345`](../../raw/robotics-embodied-ai/documents/SRC-robotics-345-rtab-map-ros2-official-repository-readme-at-audited-commit.md) | RTAB-Map ROS2 官方 README | S | ROS 2、RGB-D/stereo/LiDAR、Nav2/机器人集成对照 |
| [`SRC-robotics-346`](../../raw/robotics-embodied-ai/documents/SRC-robotics-346-nvidia-cuvslam-official-repository-readme-at-audited-commit.md) | cuVSLAM 官方 README | S | CUDA、多相机/IMU、ROS 2/Jetson 和 vendor stack 对照 |
| [`SRC-robotics-347`](../../raw/robotics-embodied-ai/documents/SRC-robotics-347-tum-vi-benchmark-official-dataset-page.md) | TUM-VI 官方 benchmark | S | 20 Hz 鱼眼双目、200 Hz IMU、硬件同步、GT 覆盖边界 |
| [`SRC-robotics-348`](../../raw/robotics-embodied-ai/documents/SRC-robotics-348-euroc-mav-dataset-official-page.md) | EuRoC MAV 官方页 | S | MAV 视觉惯性 benchmark 的传感器/场景边界 |
| [`SRC-robotics-349`](../../raw/robotics-embodied-ai/documents/SRC-robotics-349-rtab-map-ros2-bsd-3-clause-license-at-audited-commit.md) | RTAB-Map ROS2 license | S | BSD-3-Clause 许可证对照；不覆盖依赖/数据许可 |

## 可直接引用的事实边界

- 论文作者报告 EuRoC 双目惯性平均 RMS ATE 约 3.5 cm、TUM-VI room 双目惯性 9 mm；这是作者实验，不是产品 SLA。
- 论文单目使用 Sim(3) 对齐；部分系统/序列只报告成功运行平均，表格脚注明确存在 raw/processed GT、keyframe/full trajectory 与作者自跑差异。
- 官方支持 mono、stereo、RGB-D、mono-inertial、stereo-inertial，pinhole 和 fisheye；核心输出仍是稀疏地图和轨迹。
- 官方 README 测试环境是 Ubuntu 16.04/18.04 和 ROS Melodic；默认分支未提供官方 ROS 2 包。
- 2026-08-05 审计时默认分支最后提交为 2022-02-10，最新 release 为 2021-12-22；社区 fork 活跃度未在本来源集一概等同于上游维护。
- ORB-SLAM3 为 GPLv3；闭源商业使用应走官方联系路径并做独立法律审查。

## 证据限制

- 本次没有编译 ORB-SLAM3，也没有在目标相机、ROS 2、国产 SoC/GPU 或客户现场复现。
- GitHub stars/forks/issues/PR 是动态社区信号，不是生产采用、缺陷严重度或付费需求。
- 替代方案资料来自各自官方文档，性能和“最优”营销主张未纳入统一排名。
- 商业成熟度、订单、许可费用、SLA 和现场维护成本没有公开一手数据，均需询价/PoC。

## 关联连接

- [[ORBSLAM3|ORB-SLAM3 实体页]]
- [[robotics-embodied-ai/research-notes/orb-slam3-technology-engineering-commercial-deep-dive-2026-08-05|ORB-SLAM3 深度调研]]
- [[SLAM|SLAM 同时定位与建图]]
- [[VisualInertialSLAM|视觉惯性 SLAM]]
- [[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]]

