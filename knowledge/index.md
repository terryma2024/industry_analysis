---
title: Knowledge Index
type: index
date_created: 2026-05-29
last_updated: 2026-06-10
tags:
  - wiki
  - index
  - llm-wiki
---

# Knowledge Index

本页是 LLM 维护本仓库知识库时优先读取的全局目录。`knowledge/README.md` 面向人类导航；本页面向 ingest/query/lint 工作流，所有重要页面都应在这里登记，并附一句话说明。

## Sources

- [[_sources/karpathy-llm-wiki-pattern|Karpathy LLM Wiki Pattern]] — LLM Wiki 的原始理念和 Jason 文章中的实践化解读。
- [[ai/00-source-capture-index|AI Source Capture Index]] — AI 行业来源抽取状态，包含 Scale AI 与中国 AI 数据基础设施对标调研的 raw artifact 入口。
- [[news/2026-05-29-us-productivity-miracle|美国正在爆发一场生产力奇迹]] — 关于美国生产率加速、AI 时滞、能源优势和经济灵活性的新闻摘要。
- [[_sources/roboalign-r1-reward-aligned-robot-video-world-models|RoboAlign-R1 - Reward-Aligned Robot Video World Models]] — arXiv `2605.03821` 论文卡片，聚焦机器人视频世界模型的多模态奖励对齐、RobotWorldBench、RoboAlign-Judge 和 SWR。

## Entities

- [[_entities/AndrejKarpathy|Andrej Karpathy]] — LLM Wiki 理念提出者，强调把知识管理从 RAG 转向持续编译。
- [[_entities/ScaleAI|Scale AI]] — 美国 AI 数据基础设施公司，从自动驾驶标注扩展到大模型后训练、评测和政府 AI，并于 2025 年获得 Meta 战略投资。
- [[_entities/HuggingFaceLeRobot|Hugging Face LeRobot]] — 机器人学习数据、加载、训练与评测工具链，也是 UMI 数据包可复现交付的重要格式入口。
- [[_entities/README|Entities Layer]] — 人物、公司、工具、产品和 UMI 技术术语实体索引。
- [[_entities/UniversalManipulationInterface|Universal Manipulation Interface]] — 低成本手持夹爪示教路线，把人类操作转成机器人可训练轨迹数据。
- [[_entities/SLAM|SLAM]] — UMI-like 数据采集中的位姿恢复与轨迹质量核心模块。
- [[_entities/DiffusionPolicy|Diffusion Policy]] — UMI 常用的机器人模仿学习策略模型基线。
- [[_entities/ActionChunkingTransformer|ACT]] — 用 Transformer 一次预测动作 chunk 的模仿学习基线。
- [[_entities/DataPackage|Data Package]] — ToB 机器人数据服务的交付资产包概念。
- [[_entities/QualityControl|Quality Control]] — 机器人训练数据从原始采集走向可训练交付的质检流程。
- [[_entities/UnitreeRobotics|Unitree Robotics]] — 中国具身智能/机器人公司，现有研究中用于跟踪整机与数据平台线索。
- [[_entities/LimXDynamics|LimX Dynamics]] — 逐际动力，中国人形机器人与具身智能公司，当前研究重点是“机器人本体 + 运动控制小脑 + 具身大脑/工具链”的开发者平台路线。
- [[_entities/Agibot|Agibot]] — 中国具身智能公司，现有研究中用于跟踪开放数据集和整机生态。
- [[_entities/IOAI|IO-AI]] — 中国具身数据基础设施公司，现有研究中用于跟踪遥操作、数据标注管理与格式导出。

## Concepts

- [[_concepts/llm-wiki|LLM Wiki]] — 以 Markdown wiki 作为 LLM 可维护的持久知识编译层。
- [[_concepts/knowledge-compilation|Knowledge Compilation]] — 把原始来源在摄入阶段编译为可复用、可链接、可审计的知识资产。
- [[_concepts/source-traceability|Source Traceability]] — 本仓库的核心质量约束：重要判断必须能回到原始来源。
- [[_concepts/embodied-ai|Embodied AI]] — AI 进入物理世界的机器人产业化方向。
- [[_concepts/robot-training-data|Robot Training Data]] — 具身智能训练数据、episode、schema、质检与交付体系。
- [[_concepts/vision-language-tactile-action|Vision-Language-Tactile-Action]] — 视觉、语言、触觉/力觉和动作轨迹融合的具身模型/数据范式。
- [[_concepts/universal-manipulation-interface|Universal Manipulation Interface]] — UMI-like 采集设备和机器人示教数据包路线。
- [[_concepts/lerobot-dataset-schema|LeRobot Dataset Schema]] — LeRobot v3 及相关机器人数据格式概念。

## Claims

- [[_claims/README|Claims Index]] — 原子化、可溯源判断的登记区；当前先建规则，后续在研究深化时逐条抽取。

## Syntheses

- [[_syntheses/karpathy-wiki-migration-plan|Karpathy Wiki Migration Plan]] — 本仓库从行业分析工作区升级为 LLM Wiki 的迁移设计。
- [[ai/research-notes/scale-ai-company-history-2026-06-02|Scale AI 公司发展史]] — Scale AI 从 2016 年人力任务 API、自动驾驶数据标注、大模型后训练到 2025 年 Meta 战略投资的完整复盘。
- [[ai/research-notes/scale-ai-and-china-data-infrastructure-peers-2026-06-02|Scale AI 发展历程与中国对标公司]] — Scale AI 从人力任务 API 到 Meta 战略投资的路径，以及中国 AI 数据基础设施公司对标。
- [[robotics-embodied-ai/09-training-data-deep-dive|机器人训练数据深度调研]] — 具身智能训练数据、地方政策、schema、失败轨迹和 UMI-like 业务路线综合。
- [[robotics-embodied-ai/08-umi-gripper-research-and-business-plan|UMI Gripper 研究与业务计划]] — UMI-like 数据采集硬件、学习路径与 ToB 落地方案。
- [[robotics-embodied-ai/11-embodied-ai-data-service-companies-2026-06-02|具身智能数据采集和服务公司对比]] — 对智元、补天石、它石、简智、Maxinsights、自变量、帕西尼的数据采集/服务路线、岗位和优劣势做横向分析。
- [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]] — 对机器人数据、训练、评测、部署、真机推理平台做分层拆解，并比较 LeRobot、FluxVLA、Isaac、OpenPI、Unitree G1-D、EmbodiFlow 等选项。
- [[robotics-embodied-ai/13-robot-company-product-comparison-2026-06-08|机器人公司产品型号全景对比]] — 汇总 `04-companies` 主表机器人公司的产品型号、参数、技术路线、优缺点和待验证事项。
- [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]] — 基于 Thinking Partner 对话沉淀的职业方向锚点，聚焦用具身智能业务落地 know-how 解决企业成本、收入或风险痛点。
- [[robotics-embodied-ai/research-notes/retail-store-robotics-entry-scan-2026-06-10|线下零售门店机器人合作验证初扫]] — 验证大型零售公司线下门店机器人合作是否超过 5/10；第一轮公开检索未通过，需继续补实权威排名与公告/年报全文。
- [[_syntheses/china-umi-gripper-purchase-scan-2026-06-08|中国可购买 UMI 夹爪设备检索]] — 追踪 LUMOS FastUMI、觅蜂 MEgo Gripper、BeingBeyond U1 等 UMI-like 数采设备在中国的购买状态、价格线索和待验证事项。

## Industries

- [[6g/00-index|6G]] — 6G 行业研究入口。
- [[aerospace/00-index|航空航天]] — 航空航天行业研究入口。
- [[ai/00-index|AI]] — AI 相关行业研究入口。
- [[biopharma/00-index|生物医药]] — 生物医药行业研究入口。
- [[brain-computer-interface/00-index|脑机接口]] — 脑机接口行业研究入口。
- [[future-energy/00-index|未来能源]] — 未来能源行业研究入口。
- [[integrated-circuits/00-index|集成电路]] — 集成电路行业研究入口。
- [[low-altitude-economy/00-index|低空经济]] — 低空经济行业研究入口。
- [[quantum-technology/00-index|量子科技]] — 量子科技行业研究入口。
- [[robotics-embodied-ai/00-index|机器人与具身智能]] — 机器人与具身智能行业研究入口。

## News

- [[news/00-index|新闻速记]] — ad hoc 新闻/文章/视频摘要入口；每条摘要独立成文。
- [[news/2026-06-05-nvidia-cosmos-3-getting-started-plan|NVIDIA Cosmos 3 上手调研与计划]] — NVIDIA 2026 年发布的 Cosmos 3 omnimodal world model 调研、关键事实与两周上手计划。

## Operations

- [[log|Wiki Log]] — append-only 操作日志，记录 ingest/query/lint/migration。
- [[README|Knowledge README]] — 面向人类的 Obsidian vault 首页。
