---
title: LimX Dynamics
type: entity
date_created: 2026-06-04
last_updated: 2026-06-04
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-103-limx-dynamics-about-page.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-104-limx-tron-1-product-page.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-106-limx-oli-product-page.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-107-limx-tron-2-product-page.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-108-fluxvla-engine-documentation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-110-2-b.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-111-5-a.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-112-source.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-113-source.md
tags:
  - entity/company
  - robotics
  - embodied-ai
  - humanoid-robot
status: active
aliases:
  - 逐际动力
  - LimX Dynamics
---

# LimX Dynamics

逐际动力 LimX Dynamics 是深圳的人形机器人与具身智能公司。本仓库对它的核心判断是：逐际不是单纯“卖人形机器人整机”的公司，而是在押注“机器人本体 + 小脑运动控制 + 具身大脑/工具链”的开发者平台路线，目标客户更像科研团队、开发者、系统集成商和具身应用创新者，而不是直接为单一工厂场景做交付解决方案。

> [!summary]
> 逐际动力的战略关键词是“工具链”和“大小脑融合”。短期商业化看 TRON/Oli 等硬件是否能稳定卖给科研、教育、展示、巡检、集成商；中期价值看 LimX COSA、FluxVLA、VGM 等软件/数据/训练部署工具能否形成跨本体复用能力。

## 关键事实

| 维度 | 结论 | 证据 |
|---|---|---|
| 公司定位 | AI 驱动的人形机器人公司，聚焦全尺寸通用人形机器人，并衍生 TRON 等多形态机器人 | [`SRC-robotics-103`](../../raw/robotics-embodied-ai/documents/SRC-robotics-103-limx-dynamics-about-page.md) |
| 技术主线 | 本体硬件设计制造、大小脑融合、具身 Agentic OS；研发人员占比超过 80% | [`SRC-robotics-103`](../../raw/robotics-embodied-ai/documents/SRC-robotics-103-limx-dynamics-about-page.md) |
| 创始人/路线 | 创始人张巍在访谈中把公司定位为“具身工具公司”，提供机器人本体和 AI 软件工具，服务创新者/集成商 | [`SRC-robotics-113`](../../raw/robotics-embodied-ai/documents/SRC-robotics-113-source.md) |
| 融资 | 2025 年 3 月披露 A+ 轮，半年累计完成 5 亿元 A 轮系列融资；2026 年 2 月披露完成 2 亿美元 B 轮 | [`SRC-robotics-111`](../../raw/robotics-embodied-ai/documents/SRC-robotics-111-5-a.md) [`SRC-robotics-110`](../../raw/robotics-embodied-ai/documents/SRC-robotics-110-2-b.md) |
| 同业位置 | 国金证券周报将其列为 2022 年成立、6 次融资、B 轮、累计融资超 2 亿美元、估值 12 亿美元的本体公司 | [`SRC-robotics-112`](../../raw/robotics-embodied-ai/documents/SRC-robotics-112-source.md) |
| 产品矩阵 | TRON 1、Oli、TRON 2、FluxVLA 已有可验证页面；官网历史还列出 CL-1、W1、Luna、COSA、VGM | [`SRC-robotics-103`](../../raw/robotics-embodied-ai/documents/SRC-robotics-103-limx-dynamics-about-page.md) [`SRC-robotics-104`](../../raw/robotics-embodied-ai/documents/SRC-robotics-104-limx-tron-1-product-page.md) [`SRC-robotics-106`](../../raw/robotics-embodied-ai/documents/SRC-robotics-106-limx-oli-product-page.md) [`SRC-robotics-107`](../../raw/robotics-embodied-ai/documents/SRC-robotics-107-limx-tron-2-product-page.md) |

## 产品与技术

| 产品/技术 | 定位 | 观察 |
|---|---|---|
| TRON 1 | 多形态双足机器人，面向人形 RL/运动控制入门和科研开发 | 三合一足端：点足、脚掌、轮足；支持 Python、SDK、URDF、NVIDIA Isaac/MuJoCo/Gazebo，并提供机械臂、语音、感知扩展套件。 |
| Oli | 全尺寸通用人形机器人 | 官网披露 165cm、31 DoF、双语语音交互、SDK/API/URDF/仿真支持；应用场景偏科研、表演、展会导览、巡检、工业作业、物业。 |
| TRON 2 | 多形态具身机器人/模块化基座 | 形态包括双臂、轮足、脚掌；强调 10kg 双臂负载、全视野感知、VLA 数据采集管理、训练推理任务流程，更像“移动操作 + VLA 开发平台”。 |
| FluxVLA Engine | 开源 VLA 工程平台 | 覆盖数据、训练、评测、部署和真机推理；支持 OpenVLA、LlavaVLA、GR00T、Pi0、Pi0.5，数据支持 Parquet/RLDS。 |
| COSA / VGM | 具身 Agentic OS / 具身操作算法 | 官网和融资稿提到，但当前 raw 证据主要来自官网摘要和新闻稿；需要继续补官方产品页、视频演示和可复现实验结果。 |

## 投资视角

**正面因素：** 逐际的差异化不在“有没有人形样机”，而在把运动控制、开发者硬件、VLA 工具链和 Agentic OS 串成平台叙事；京东、阿里、上汽/尚颀、蔚来资本等产业资本参与，说明它在零售、物流、汽车、制造供应链资源上有潜在场景入口。

**主要不确定性：** 公开资料多为官网/融资/媒体稿，缺少收入、毛利、客户续约、出货量、留存、实际任务成功率等硬指标。TRON 1 “全球多个国家和地区交付、初步商业闭环”的说法来自媒体稿，仍需客户案例或合同证据交叉验证。

**关键监控指标：**

- TRON 1/2、Oli 的真实交付数量、复购率、海外销售和售后能力。
- FluxVLA 的 GitHub 活跃度、外部开发者采用、第三方复现实验、数据集质量。
- COSA/VGM 是否从 demo 走向可购买、可部署、可维护的软件产品。
- 与京东、上汽、蔚来、阿里等产业方是否出现明确场景项目，而不只是资本背书。
- 现金消耗和硬件量产良率，因为公司同时做 AI、软件工具链、硬件和供应链，组织复杂度高。

## 职业视角

逐际更适合关注以下岗位族：机器人软件平台、VLA/多模态模型、强化学习与运动控制、仿真/Sim2Real、数据闭环、SDK/开发者生态、产品经理、解决方案与客户工程。对软件背景转机器人方向的人来说，它比纯机械本体厂更有“软件平台 + 工程化 + 开发者工具”的切入口。

## 知识冲突

- **成立时间口径：** 官网时间线写“2022 年 7 月正式孵化，完成天使轮融资”；国金证券表格写“成立时间 2022 年 1 月”；晚点访谈写 Optimus 亮相前 5 个月成立于深圳。后续若需要公司沿革，应以工商登记、官网公司历史和创始人访谈三方校准。
- **商业化口径：** 盖世汽车称 TRON 1 已完成全球多个国家和地区交付、初步实现设计-研发-量产-销售闭环；但缺少公开销量、客户名单和收入数据。暂按“商业闭环线索”处理，不升级为确定的规模化商业化结论。

## 待验证

- 工商主体变化：`深圳逐际动力科技有限公司` 与公开报道中的 `深圳逐际动力科技股份有限公司` 是否为改制/同一主体。
- 张力等管理层变动、组织架构和海外团队情况。
- COSA、VGM、Luna 的完整官方产品页和可复现实验材料。
- TRON 1 用户手册 `SRC-robotics-105` 自动下载失败，原因是证书过期；需后续通过浏览器手工保存或寻找新版下载地址。

## 关联连接

- [[_concepts/embodied-ai|Embodied AI]]
- [[_concepts/robot-training-data|Robot Training Data]]
- [[_concepts/lerobot-dataset-schema|LeRobot Dataset Schema]]
- [[robotics-embodied-ai/04-companies|机器人公司和竞争格局]]
- [[robotics-embodied-ai/09-training-data-deep-dive|机器人训练数据深度调研]]
