---
title: 机器人（具身智能） - 研究中间笔记
date: 2026-05-27
tags:
  - industry/robotics-embodied-ai
  - research-notes
  - obsidian/moc
aliases:
  - 具身智能研究中间笔记
last_updated: 2026-07-06
---

# 机器人（具身智能） - 研究中间笔记

> [!info]
> 本目录保存专题深度调研的中间笔记。结论成熟后再汇总进入上层知识笔记，如 [[07-training-data|训练数据生产与处理]] 和 [[09-training-data-deep-dive|训练数据深度调研]]。

## 2026-05-27 并行调研

- [[training-data-company-verification-2026-05-27]]: 公司/方案交叉验证。
- [[local-policy-data-platforms-2026-05-27]]: 地方政策、公共训练场、数据工厂和测评中心。
- [[dataset-schema-comparison-2026-05-27]]: OXE、DROID、RoboMIND、AgiBot World、LeRobot schema 横向。
- [[failure-intervention-data-2026-05-27]]: 失败轨迹和人工接管数据。
- [[umi-hardware-localization-2026-05-27]]: UMI 硬件 BOM、许可证、可采购性和国产替代。

## 2026-05-28 UMI v0 模板补全

- [[umi-v0-sop-schema-data-package-2026-05-28]]: UMI-like v0 采集 SOP、UMI/Zarr 与 LeRobot schema 对照、客户数据包样例目录。
- [[lerobot-beginner-guide-2026-05-28]]: LeRobot 初学者教学，解释 LeRobotDataset、数据目录、UMI/Zarr 转换和 ToB 数据服务意义。

## 2026-06-09 职业方向与业务落地入口

- [[career-direction-business-landing-knowhow-2026-06-09]]: 基于 Thinking Partner 对话沉淀的职业方向锚点，聚焦通过具身智能业务落地 know-how 解决企业决策者的成本、收入或风险痛点。

## 2026-06-10 线下零售门店场景验证

- [[retail-store-robotics-entry-scan-2026-06-10]]: 对“中国零售销售额前 10 大型零售公司是否超过一半已有线下门店机器人合作”的第一轮外部调研初扫。
- [[cross-scenario-near-term-landing-candidate-pool-2026-06-10]]: 跨全部具身智能/机器人应用场景，按 1 年内真实订单或试点转生产证据建立短期落地候选池。

## 2026-06-10 平台工程师 JD 入场验证

- [[platform-engineer-jd-entry-scan-2026-06-10]]: 用“通用软件平台能力是硬要求、机器人领域知识可补齐”作为第一筛选门槛，初扫具身智能/机器人平台工程、后端、数据管线、仿真平台和运营系统岗位。

## 2026-06-11 仿真评测平台

- [[libero-lifelong-robot-learning-platform-2026-06-11]]: LIBERO 终身学习仿真/评测平台调研，拆解任务套件、数据、baseline、平台工程价值、局限和 2025-2026 年鲁棒性批评。
- [[open-embodied-ai-datasets-comparison-2026-06-11]]: 开源具身智能训练与评估数据集横向调研，按预训练、真实微调、特定能力和仿真 benchmark 比较格式、任务完整度与模型适配。

## 2026-06-23 数据生产平台

- [[airspeed-data-production-platform-2026-06-23]]: AIRSPEED 具身智能数据生产平台调研，区分当前 GitHub v1.3 开源采集核心、论文/官网三服务架构和技术转移报告中的商业化叙事。

## 2026-06-23 机器人中间件与 dataflow runtime

- [[dora-1-vs-ros2-2026-06-23]]: 对比 dora 1.0 能力主张与 ROS 2 生态底座，重点拆解版本状态、性能、QoS、ROS 2 bridge、平台工程选型和职业学习路径。

## 2026-06-29 LiDAR 世界模型训练

- [[lidar-world-model-training-2026-06-29]]: 调研激光雷达数据如何通过点云/range/ray token、BEV/occupancy、camera-LiDAR unified latent 和 JEPA 进入世界模型训练，并给出自动驾驶、传感器仿真、多模态生成和移动机器人导航的工程方案。

## 2026-06-29 训练数据价值评估

- [[robot-training-data-value-evaluation-2026-06-29]]: 面向采集前立项、采集中质检和采后验证的具身智能训练数据价值评估框架，核心是边际能力提升、复用性、可信度与全成本风险比。

## 2026-07-03 世界模型与物理理解评估

- [[embodied-model-physical-understanding-evaluation-2026-07-03]]: 区分具身大模型的动作生成、语义泛化、动作条件预测和规划可用世界模型，提出反事实预测、minimal physical pairs、forward/inverse dynamics、闭环 A/B 和多模态约束的评估框架。

## 2026-07-06 家庭养老机器人

- [[home-elderly-care-robots-2026-07-06]]: 家庭养老机器人公司与方案调研，按陪伴提醒、远程巡视、移动载物、康复护理和通用家务机器人分层，比较国内外代表公司、落地阶段和中国方案机会。

## 2026-07-06 VLA 与世界模型数据基建

- [[vla-world-model-data-infrastructure-platform-design-2026-07-06]]: 基于 `BV1ZFTq6pEA3` 的 15 阶段数据生产 SOP，设计 VLA&世界模型数据基建平台，覆盖 episode-first 架构、自动质检、多格式导出、dataset registry、baseline 评测和失败补采闭环。
