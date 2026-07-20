---
title: "MATRiX Simulator"
type: entity
date_created: 2026-07-20
last_updated: 2026-07-20
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-310-matrix-repository-readme-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-312-matrix-github-maintenance-and-issue-audit.md
tags:
  - entity/project
  - industry/robotics-embodied-ai
  - simulation
status: active
aliases:
  - MATRiX
  - zsibot/matrix
  - GENISOM MATRiX
---

# MATRiX Simulator

> [!summary]
> MATRiX 是 GENISOM AI / ZsiBot 维护的四足机器人软件在环仿真发行环境，组合 MuJoCo 动力学、Unreal Engine 5 场景/传感器、ROS 2 与 GENISOM 控制/导航生态。最适合四足导航、巡检场景和教学 PoC；核心运行时主要以预编译 Release 资产交付。

## 实体属性

| 字段 | 内容 |
|---|---|
| 类型 | 开源外层 + 预编译运行时的机器人仿真平台 |
| 维护者 | GENISOM AI / ZsiBot |
| 仓库 | [zsibot/matrix](https://github.com/zsibot/matrix) |
| 审阅稳定版 | v0.1.2（2026-04-28） |
| 根许可证 | BSD-3-Clause；第三方/二进制/资产需单独审计 |
| 主要本体 | 四足/轮足机器人 |
| 关键依赖 | Ubuntu 22.04、ROS 2 Humble、NVIDIA RTX、MuJoCo、UE5 |
| 生态连接 | RoamerX/Nav2、genisom_vln、机器人 SDK、URDF 模型 |

## 稳定判断

- 产品价值在于把四足本体、控制、导航、传感器和场景包装为可安装环境。
- 不是等价于 MuJoCo/Isaac Lab 的大规模 RL 框架，也不是完整源码可重建的 UE 仿真器。
- 采用前应完成许可证、安装复现、topic/TF、长稳、自定义本体和真机相关性 PoC。

## 关联连接

- [[robotics-embodied-ai/research-notes/zsibot-matrix-robotics-simulator-deep-dive-2026-07-20|MATRiX 深度调研]]
- [[_sources/zsibot-matrix-robotics-simulator-source-set|MATRiX 来源集]]
- [[robotics-embodied-ai/research-notes/isaac-sim-vs-gazebo-vs-mujoco-2026-07-14|机器人仿真平台选型]]
- [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]
