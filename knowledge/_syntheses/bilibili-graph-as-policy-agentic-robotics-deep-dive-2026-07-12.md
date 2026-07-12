---
title: Graph-as-Policy 智能体机器人视频深度调研
type: synthesis
date_created: 2026-07-12
last_updated: 2026-07-12
sources:
  - knowledge/_sources/bilibili-bv1c5nj6ve6y-icra-2026-ken-goldberg-agentic-coding-va-agentic-robot.md
  - raw/_inbox/transcripts/2026-07-12-bilibili-bv1c5nj6ve6y-icra-2026-ken-goldberg-agentic-coding-va-agentic-robot.json
  - https://arxiv.org/abs/2607.05369
  - https://graph-robots.github.io/gap/
  - https://github.com/capgym/cap-x
tags: [bilibili, robotics, embodied-ai, agentic-coding, automation]
status: active
---

# Graph-as-Policy 智能体机器人视频深度调研

> [!summary]
> Ken Goldberg 的 ICRA 2026 演讲不是简单押注 VLA 或传统自动化，而是提出第三种工程组织方式：由多智能体生成、验证和迭代**有向计算图**，将感知、规划、抓取与控制模块装配为可解释的策略。GaP 论文和项目页可核验该方向；视频里的多数精确成功率仍是作者报告，应按任务、基线和真实/仿真边界使用。

## 来源与主线

| 项目 | 内容 |
|---|---|
| 视频 | [ICRA 2026 Ken Goldberg：Agentic Coding 能弥合机器人鸿沟吗？](https://www.bilibili.com/video/BV1C5Nj6vE6y) |
| 作者 / 文本 | 具身智能机器人入门；Volcengine ASR 原文见 `raw/_inbox/transcripts/2026-07-12-bilibili-bv1c5nj6ve6y-icra-2026-ken-goldberg-agentic-coding-va-agentic-robot.json` |
| B 级演讲线索 | 机器人数据缺口、VLA 与模块工程的互补、Dex-Net/Ambi 的产业经验、Code-as-Policy、Graph-as-Policy（GaP） |
| 一级交叉来源 | [GaP arXiv:2607.05369](https://arxiv.org/abs/2607.05369)、[GaP 项目页](https://graph-robots.github.io/gap/)、[CaP-X GitHub](https://github.com/capgym/cap-x) |

## 可核验技术内核

GaP 论文将目标限定为“变异性自动化”（Variational Automation）：对象几何和位姿变化比固定自动化更大、却要求长时间可靠运行的任务。其多智能体 harness 从任务文本、场景/对象几何、机器人与传感器配置生成带有感知、规划和控制节点的有向计算图，再在内部仿真中并行试验并迭代图结构和参数。论文报告了 8 个开放 VA benchmark（4 个仿真、4 个真实世界），并称其相对所列基线有显著成功率提升；这支持“结构化智能体编排值得验证”，但不自动证明跨行业通用性。

CaP-X 则为 Code-as-Policy agent 提供可交互环境和 benchmark，覆盖 Robosuite、LIBERO-PRO 和 BEHAVIOR 等任务。二者共同说明：将 LLM 的生成能力放入显式 API、技能库、仿真和回归评测，才有机会把它转成可维护的机器人系统。

## 事实、估计、判断与假设

| 类型 | 内容 | 证据边界 |
|---|---|---|
| 事实（一级来源） | GaP 生成可组合计算图而非单段机器人代码，并在内部仿真中迭代图与参数。 | arXiv / 项目页 |
| 事实（一级来源） | CaP-X 是机器人操控 coding agent 的开源评测框架，含交互式环境和基准。 | GitHub |
| 视频线索 | 传统模块工程在高可靠变异任务中仍有作用；VLA 可在其降低视角/几何不确定性后受益。 | B 级观点，值得实验 |
| 作者报告 | 演讲内的 98%、95%、100%、97% 等任务成功率，以及相对 Pi 0.5 的差距。 | 应回到 GaP 论文 tables、试验协议和置信区间；不可当成跨任务 KPI |
| 判断 | 近期可落地的价值是“LLM 生成的候选结构 + 确定性模块/类型接口 + 仿真/真机回归门槛”，不是让 agent 直接无监督控制设备。 | 工程判断 |
| 假设 | 自动生成图能长期降低集成成本且不牺牲安全。 | 需用变更率、人工审核时间、回归失败率、事故/近失事件验证 |

## 中国具身产业启发

- 适合中国制造、仓储和柔性工位的切入点，是对象/位姿变化有限但又超过固定治具能力的“变异性自动化”，而非直接承诺家庭通用机器人。
- 工具链应把 ROS2 节点、坐标系、传感器标定、技能 API、仿真场景和回归案例做成版本化接口；这样智能体的输出能被静态检查、仿真检查和人工审核。
- 投资尽调应要求公司分别披露：生成层（模型/agent）、执行层（图/模块）、验证层（仿真、HIL、真机）与运行层（监控、回滚）的指标，防止以单次 demo 混淆系统可靠性。

## 职业视角、风险与下一步

- 作品集：用 ROS2/MuJoCo 或 Isaac Lab 编写 4–6 节点抓取图，让 LLM 仅生成节点连接和参数候选；对每次变更运行类型/接口检查、随机化仿真、失败回放和回滚。
- 核验 GaP 论文中每项 baseline 的任务协议和真实硬件设置；不要将视频中“人类 99%”“VLA 20%”等数字跨 benchmark 比较。
- agent 生成的代码/图仍有资产误识别、坐标系错误、接口幻觉、仿真遗漏及安全风险；真机执行须保留速度/力限制、急停、物理隔离和人工批准。

## 关联连接

- [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]
- [[robotics-embodied-ai/02-technology-and-products|机器人技术与产品]]
- [[ai/02-technology-and-products|AI 技术与产品]]
- [[_concepts/embodied-ai|Embodied AI]]
