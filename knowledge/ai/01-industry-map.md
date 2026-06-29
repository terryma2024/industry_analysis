---
title: AI相关 - 产业链地图
type: industry
date_created: 2026-05-29
last_updated: 2026-06-29
status: draft
tags:
  - industry/ai
sources:
  - ai/sources.csv
---

# AI相关 - 产业链地图

## 产业链总览

| 环节 | 核心价值 | 代表公司/机构 | 关键壁垒 | 证据 |
| --- | --- | --- | --- | --- |
| 算力/芯片/集群 | 决定训练和推理成本、模型规模和可用性 | NVIDIA, 华为昇腾, 寒武纪, 云厂商, 数据中心 | GPU/AI 芯片、互联、供电散热、调度、编译器生态 | [`SRC-ai-044`](../../raw/ai/documents/SRC-ai-044-source.md) [`SRC-ai-045`](../../raw/ai/documents/SRC-ai-045-source.md) |
| 云与模型平台 | 把算力、模型、API、工具链提供给开发者和企业 | 阿里云/ModelScope、百度智能云、腾讯云、火山引擎、华为云 | 开发者生态、API 稳定性、价格、客户迁移成本 | [`SRC-ai-039`](../../raw/ai/documents/SRC-ai-039-source.md) [`SRC-ai-043`](../../raw/ai/documents/SRC-ai-043-source.md) [`SRC-ai-046`](../../raw/ai/documents/SRC-ai-046-source.md) |
| 基础模型 | 生产通用语言/多模态/推理能力 | DeepSeek、Qwen、文心、Kimi、GLM、混元、豆包 | 数据、算法、算力、训练工程、产品分发 | [`SRC-ai-038`](../../raw/ai/documents/SRC-ai-038-source.md) 至 [`SRC-ai-043`](../../raw/ai/documents/SRC-ai-043-source.md) |
| 数据与后训练 | 决定模型对齐、专业能力、评测和安全 | Scale AI、海天瑞声、数据堂、云测、GOMAX、Xpert Studio | 专家网络、质量控制、评测体系、客户信任 | [`SRC-ai-001`](../../raw/ai/documents/SRC-ai-001-scale-yc-company-post.md) 至 [`SRC-ai-024`](../../raw/ai/documents/SRC-ai-024-source.md) |
| 应用/Agent | 把模型转成用户和企业可付费流程 | 办公、编程、客服、营销、教育、医疗、金融、制造软件 | 场景 know-how、工作流集成、可靠性、ROI | [`SRC-ai-035`](../../raw/ai/documents/SRC-ai-035-source.md) |
| 安全与合规 | 保证模型可上线、可审计、可控 | 网信办/模型备案、安全评测、内容安全、数据合规服务商 | 政策理解、红队评测、数据治理、责任边界 | [`SRC-ai-036`](../../raw/ai/documents/SRC-ai-036-source.md) |

## 价值流

- 谁付钱：短期主要是云厂商、互联网平台、政企客户、开发者和消费者订阅；长期要看行业客户是否愿意为效率提升、收入增长或风险降低持续付费。
- 谁获益：算力和云平台先获益；模型公司获益取决于 API/订阅/企业项目能否覆盖训练和推理成本；应用公司获益取决于是否拥有真实工作流入口。
- 成本主要在哪里：训练算力、推理算力、数据/后训练、工程团队、合规安全、销售交付和客户私有化部署。
- 利润池集中在哪里：短期偏算力、云、头部应用入口和高价值数据/评测；长期可能向垂直工作流、平台生态和合规安全工具迁移。

## 关键瓶颈

- 供给瓶颈：先进 AI 芯片、HBM/互联、数据中心电力、国产软件栈、优质中文/专业数据。
- 技术瓶颈：推理能力、长上下文可靠性、多模态一致性、Agent 工具调用、评测真实性、幻觉控制。
- 监管瓶颈：生成式 AI 服务备案、安全评估、数据跨境、版权、个人信息保护和行业准入。
- 渠道瓶颈：C 端流量入口被大平台掌握；B 端要进入企业核心流程，销售周期长。
- 人才瓶颈：大模型训练工程、推理系统、数据治理、AI 产品、行业解决方案和安全评测人才。

## 关联连接

- [[00-index|AI 相关 - 研究入口]]
- [[integrated-circuits/07-ai-chip-global-supply-chain-and-stock-screen-2026-06-11|AI 芯片全球上市公司、供应链关系与股票初筛]]
