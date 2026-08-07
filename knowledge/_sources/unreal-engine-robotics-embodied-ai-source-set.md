---
title: Unreal Engine 机器人与具身智能项目、论文和许可来源集
type: source
date_created: 2026-08-06
last_updated: 2026-08-06
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-428-unrealcv-official-repository-readme.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-431-microsoft-airsim-official-repository-readme.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-440-unreal-robotics-lab-official-repository-readme.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-442-spear-official-repository-readme.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-445-simworld-robotics-synthesizing-photorealistic-and-dynamic-urban-environments.md
tags:
  - source/github
  - source/paper
  - industry/robotics-embodied-ai
  - simulation/unreal-engine
status: active
aliases:
  - UE 机器人仿真来源集
---

# Unreal Engine 机器人与具身智能项目、论文和许可来源集

> [!summary]
> 本来源集汇总 Epic 官方许可/物理文档、20 个公开项目或研究交付物、18 篇代表论文，以及 2026-08-06 GitHub 动态元数据。综合结论见 [[robotics-embodied-ai/research-notes/unreal-engine-in-robotics-and-embodied-ai-2026-08-06|Unreal Engine 在机器人与具身智能中的应用调研]]。

## 提取方式

- GitHub README：从默认分支或明确分支直接下载 Markdown。
- 论文：优先保存 arXiv abstract 页面；HoloOcean 保存 ICRA PDF。
- 官方文档：使用 Defuddle 清洗；Epic licensing 页面自动抓取返回 403，失败记录保留在 manifest，当前许可结论同时经 Epic 官方网页实时核验。
- GitHub 动态状态：2026-08-06 通过官方 REST API 查询；stars、forks、issues 和 `pushed_at` 只作维护上下文。
- 未克隆、编译或运行 20 个项目，因此不声称安装、性能或 sim-to-real 已复现。

## 来源分组

| 分组 | SRC | 主要用途 |
|---|---|---|
| UE 基础边界 | `SRC-robotics-426`–`427` | EULA、商业许可、Chaos 物理定位。 |
| 通用视觉/编程 | `SRC-robotics-428`–`430`、`442`–`443` | UnrealCV、Gym-UnrealCV、SPEAR。 |
| UAV/道路/空地 | `SRC-robotics-431`–`439`、`456` | AirSim、Project AirSim、Cosys-AirSim、CARLA、CARLA-Air、HERCULES。 |
| 混合机器人仿真 | `SRC-robotics-440`–`441`、既有 `SRC-robotics-310`–`315` | Unreal Robotics Lab、MATRiX、UE + MuJoCo。 |
| 城市具身与 Agent 世界 | `SRC-robotics-444`–`445`、`460`–`462` | SimWorld-Robotics、VirtualEnv、SimWorld Studio。 |
| ROS 接口 | `SRC-robotics-446`–`447` | rclUE、ROSIntegration。 |
| 室内视觉/数据 | `SRC-robotics-448`–`450`、`455`、`459` | UnrealROX、RobotriX、NDDS、3DGS 合成数据。 |
| 水下与灾害 | `SRC-robotics-451`–`454`、`457` | UNav-Sim、HoloOcean、HEROES。 |
| 数字孪生 | `SRC-robotics-458` | UE5 + ROS 2 协作机器人 digital twin。 |

## 关键证据边界

- UE 是可访问源代码的 proprietary licensed technology，不是 OSI 意义的开源引擎；项目插件的 MIT/Apache 许可不覆盖 UE 本体或第三方资产。
- CARLA-Air 当前仓库许可限制学术/非商业用途；NVIDIA NDDS 为 CC BY-NC-SA 4.0。两者不能仅因代码公开就视为可自由商用。
- Microsoft AirSim 的正式 release 停在 2022，但 GitHub API 当前显示 `archived=false`；应区分“项目主线停止”和“仓库 archived 标志”。
- VirtualEnv 的论文称 open source，但本轮未定位到可审计官方仓库；SimWorld Studio 公开 README 表明完整源码构建依赖另一个受限仓库；HERCULES 仍待代码和许可证审计。
- 所有论文性能均为作者设置下的实验，不做跨论文横向排名。

## 机器可读资产

- [项目矩阵](../../raw/robotics-embodied-ai/data/unreal-engine-robotics-open-projects-2026-08-06.csv)
- [论文索引](../../raw/robotics-embodied-ai/data/unreal-engine-robotics-papers-2026-08-06.csv)
- [来源捕获 manifest](../../raw/robotics-embodied-ai/documents/source_capture_manifest.csv)

## 关联连接

- [[robotics-embodied-ai/research-notes/unreal-engine-in-robotics-and-embodied-ai-2026-08-06|UE 机器人与具身智能调研]]
- [[robotics-embodied-ai/research-notes/zsibot-matrix-robotics-simulator-deep-dive-2026-07-20|MATRiX 深研]]
- [[robotics-embodied-ai/research-notes/isaac-sim-vs-gazebo-vs-mujoco-2026-07-14|机器人模拟器选型]]
- [[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]]
