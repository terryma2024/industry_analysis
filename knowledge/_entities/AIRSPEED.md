---
title: AIRSPEED
type: entity
date_created: 2026-06-23
last_updated: 2026-06-23
aliases:
  - AIRSPEED
  - AIRSPEED Data Production Platform
  - Airspeed
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-183-airspeed-project-page.html
  - raw/robotics-embodied-ai/documents/SRC-robotics-184-airspeed-technical-report.pdf
  - raw/robotics-embodied-ai/documents/SRC-robotics-188-airspeed-github-readme.md
tags:
  - entity/project
  - entity/tool
  - industry/robotics-embodied-ai
  - embodied-ai
  - data-platform
status: active
---

# AIRSPEED

## 初学者解释

AIRSPEED 是深圳市人工智能与机器人研究院（AIRS）推出的具身智能数据生产平台项目。它想解决的问题不是“训练一个机器人模型”，而是让不同遥操作设备、机器人本体、传感器和仿真环境产生的数据能够被统一采集、清洗、对齐、转换并进入训练数据集。

更直白地说，AIRSPEED 试图把机器人数据从“每个实验室/公司一套脚本”变成“可配置、可复用、可转换、可交付”的数据基础设施。

## 当前状态

| 维度 | 判断 |
|---|---|
| 项目归属 | AIRS / 深圳市人工智能与机器人研究院来源组 |
| 技术定位 | 具身智能数据生产平台 / data infrastructure |
| 官网定位 | 真实数据采集、仿真数据生成、数据集自动构建三服务平台 |
| 当前开源 README | v1.3 包含 Teleoperation Interface、Robot Interface、Sensor Interface、Data Collection Service |
| 数据格式 | AIRS HDF5 episodes，可转换为 Parquet、Zarr、LeRobot v3、JSON Lines |
| 核心中间件 | ROS2 topic contract；论文中也比较 DORA 与 ROS2 |
| 主要边界 | GitHub 当前开源能力与论文/技术转移报告中的完整平台能力存在版本差异 |

## 在具身数据闭环中的位置

- **采集侧**：通过遥操作接口、机器人接口、传感器接口，把不同硬件发布为标准 ROS2 topics。
- **处理侧**：用 YAML 描述 session、topic、字段提取、QoS、存储和验证规则，减少为每个设备重写采集脚本。
- **格式侧**：先保存 AIRS HDF5 episode，再按训练/分析需要转换为 LeRobot v3、Zarr、Parquet 或 JSON Lines。
- **仿真侧**：论文和报告强调真实数据与仿真数据对齐、合成数据扩增和数据飞轮；当前开源 README 把仿真数据生成列为 future releases。
- **交付侧**：技术转移报告把可复用资产描述为 robot adapter、teleoperation interface、dataset template、deployment script、quality report 和私有化部署能力。

## 易错边界

- 不要把 AIRSPEED 当前 GitHub v1.3 等同于已经完整开源的“三服务”平台；当前公开代码更像数据采集核心与接口规范。
- 不要把技术转移报告中的客户、融资和商业化 claim 当作独立验证事实；这些属于项目方报告，需要继续补工商、公告、客户或投资方证据。
- 不要把“能采集”误认为“可训练”。可训练数据还需要时间同步、坐标/单位对齐、episode 切分、质检、格式转换和训练代码验证。

## 关联连接

- [[_sources/airspeed-open-source-data-production-platform|AIRSPEED 来源组]]
- [[robotics-embodied-ai/research-notes/airspeed-data-production-platform-2026-06-23|AIRSPEED 具身智能数据生产平台调研]]
- [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]
- [[robotics-embodied-ai/09-training-data-deep-dive|机器人训练数据深度调研]]
- [[_concepts/robot-training-data|Robot Training Data]]
- [[_entities/HuggingFaceLeRobot|Hugging Face LeRobot]]
- [[HDF5]]
- [[Zarr]]
- [[TimeSynchronization]]
- [[QualityControl]]
