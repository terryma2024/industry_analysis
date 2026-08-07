---
title: Unity 机器人与具身智能来源集
type: source
date_created: 2026-08-06
last_updated: 2026-08-06
sources:
  - knowledge/robotics-embodied-ai/sources.csv
  - raw/robotics-embodied-ai/data/unity-robotics-open-projects-2026-08-06.csv
  - raw/robotics-embodied-ai/data/unity-robotics-papers-2026-08-06.csv
tags:
  - source-set
  - industry/robotics-embodied-ai
  - simulation/unity
status: active
---

# Unity 机器人与具身智能来源集

## 来源范围

本来源集支撑 [[robotics-embodied-ai/research-notes/unity-in-robotics-and-embodied-ai-2026-08-06|Unity 在机器人与具身智能中的应用、开源项目和论文调研]]。检索截至 2026-08-06，优先使用 Unity/项目官方仓库、官方文档、Autoware Foundation 和论文原文。

## 核心来源分组

| 分组 | 来源 ID | 用途 |
|---|---|---|
| Unity 许可与商业边界 | `SRC-robotics-463` | 当前工业客户、订阅与 Runtime 条款入口。 |
| Unity Robotics / ROS / URDF | `SRC-robotics-464`–`466`, `470`–`472`, `499` | ROS 1/2、URDF、LiDAR、C#/.NET 和端到端抓取示例。 |
| 学习与合成数据 | `SRC-robotics-467`–`469` | ML-Agents、参考论文和已停更的 Perception。 |
| AI2-THOR 具身环境 | `SRC-robotics-473`–`484` | AI2-THOR、RoboTHOR、ProcTHOR、ManipulaTHOR、Holodeck、ALFRED、TEACh。 |
| 家庭活动/多模态/VR | `SRC-robotics-485`–`490` | VirtualHome、VRKitchen、ThreeDWorld。 |
| UAV/自动驾驶/多机器人 | `SRC-robotics-491`–`498`, `500`–`501` | Flightmare、AWSIM、SVL、AutoDRIVE、CLOiSim 及分布式 AWSIM 论文。 |

## 证据使用规则

- GitHub API 的 stars、push、archived 只表示维护信号，不能替代编译和运行验证。
- arXiv/会议论文中的指标是作者实验，不做跨论文横排。
- 仓库许可证、Unity Editor/runtime、下载资产、数据集和云服务分别审计。
- `open source` 只在来源明确且组件边界清楚时使用；否则写“公开仓库”或“论文交付”。

## 已知限制

- 未逐一构建所有项目，也未做统一硬件/场景 benchmark。
- TEACh、VRKitchen、RGL 等项目的 GitHub API 未可靠返回 SPDX，商业复用前需人工检查仓库文件和资产条款。
- Unity 商业条款会变化，采购和客户部署时需重新核验。
- AI2-THOR/ALFRED 等抽象动作 benchmark 不证明真实机械臂的连续控制与抓取能力。

## 机器可读附件

- [开源项目清单](../../raw/robotics-embodied-ai/data/unity-robotics-open-projects-2026-08-06.csv)
- [论文清单](../../raw/robotics-embodied-ai/data/unity-robotics-papers-2026-08-06.csv)

## 关联连接

- [[robotics-embodied-ai/00-index|机器人与具身智能研究入口]]
- [[robotics-embodied-ai/research-notes/unreal-engine-in-robotics-and-embodied-ai-2026-08-06|Unreal Engine 机器人与具身智能调研]]
- [[unreal-engine-robotics-embodied-ai-source-set|Unreal Engine 机器人与具身智能来源集]]
- [[robotics-embodied-ai/research-notes/isaac-sim-vs-gazebo-vs-mujoco-2026-07-14|Isaac Sim vs Gazebo vs MuJoCo]]
