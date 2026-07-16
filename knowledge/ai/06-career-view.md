---
title: AI相关 - 求职与学习视角
type: industry
date_created: 2026-05-29
last_updated: 2026-07-16
status: draft
tags:
  - industry/ai
sources:
  - ai/sources.csv
---

# AI相关 - 求职与学习视角

## 岗位地图

| 岗位族群 | 典型职位 | 核心能力 | 代表公司/场景 | 证据 |
| --- | --- | --- | --- | --- |
| 大模型工程 | LLM 训练/后训练/评测/推理优化 | PyTorch、分布式训练、RLHF/RLVR、评测、推理服务 | 模型公司、云厂商 | [`SRC-ai-038`](../../raw/ai/documents/SRC-ai-038-source.md) 至 [`SRC-ai-043`](../../raw/ai/documents/SRC-ai-043-source.md) |
| AI 平台/基础设施 | 训练平台、推理平台、MLOps、GPU 调度 | 后端、K8s、分布式系统、可观测性、成本优化 | 云厂商、算力平台、企业 AI 平台 | [`SRC-ai-044`](../../raw/ai/documents/SRC-ai-044-source.md) [`SRC-ai-046`](../../raw/ai/documents/SRC-ai-046-source.md) |
| 数据/评测/安全 | 数据工程、标注平台、模型评测、红队、安全合规 | 数据治理、质检、评测设计、内容安全、合规文档 | Scale AI、中国数据服务公司、安全评测公司 | [`SRC-ai-001`](../../raw/ai/documents/SRC-ai-001-scale-yc-company-post.md) 至 [`SRC-ai-024`](../../raw/ai/documents/SRC-ai-024-source.md) |
| AI 产品/Agent | AI PM、Agent 产品、行业解决方案 | 工作流分析、prompt/工具编排、ROI、权限安全 | 办公、客服、教育、医疗、制造 | [`SRC-ai-035`](../../raw/ai/documents/SRC-ai-035-source.md) |
| 行业 AI 交付 | 售前、解决方案、项目经理、架构师 | 行业 know-how、系统集成、数据接入、验收指标 | 政企、金融、制造、医疗 | [`SRC-ai-034`](../../raw/ai/documents/SRC-ai-034-source.md) |
| AI 投资/研究 | 产业研究、二级/一级投资、战略 | 政策、财务、技术路线、公司验证 | 券商、基金、产业资本 | 本仓库研究框架 |

## 学习路径

- 基础概念：Transformer、token、上下文窗口、RAG、fine-tuning、RLHF/RLAIF、Agent、embedding、推理成本、模型备案。
- 技术/业务能力：Python/后端、API 集成、数据治理、评测设计、云平台、权限/安全、行业流程建模。
- 推荐资料：官方模型文档、开源模型仓库、云厂商 Model Studio、网信办监管文件、头部公司财报、AI 工程实践博客。
- 可做项目：
  - 企业知识库/RAG demo：包含权限、评测集、失败案例和成本统计。
  - Agent 工作流 demo：明确工具调用、回滚、安全边界和人工接管。
  - 模型评测平台 demo：对比多个模型在真实任务上的成功率、成本和延迟。
  - 行业公司池：按算力、模型、数据、应用、安全分层，记录收入证据和招聘信号。

## 进入策略

- 适合背景：软件平台/后端/数据工程/产品/解决方案/行业运营背景都可切入；不一定要从底层模型训练开始。
- 入门岗位：AI 平台工程师、AI 应用后端、数据/评测工程师、Agent 产品经理、行业 AI 解决方案、模型应用工程师。
- 作品集建议：不要只做聊天壳；要展示数据接入、评测、权限、安全、成本和真实场景流程。
- 面试准备：解释一个 AI 产品如何从 demo 到生产，包括数据、模型、评测、上线、监控、合规和 ROI。
- 招聘信号：JD 中出现推理服务、RAG、Agent、模型评测、GPU 调度、MLOps、AI 平台、数据治理、企业知识库，通常比“会 prompt”更有含金量。

## 人才市场观察（2026-07-16）

- 国家层面已把高层次、青年与复合型 AI 人才培养、符合岗位特点的评价、产教融合以及股权/期权等中长期激励纳入“人工智能+”行动；这表明人才供给与留用是长期能力建设议题，而非单次校招热度。证据：[`SRC-ai-081`](../../raw/ai/documents/SRC-ai-081-source.md)。
- 但“顶尖人才高价竞争”不等于一般 AI 岗位普涨。求职与转岗应以可复用的工程交付证据（数据、评测、成本、安全、行业流程）判断，不以短视频中的年薪、岗位数或个别跳槽传闻推断个人市场价。详见 [[_syntheses/bilibili-ai-talent-market-and-career-path-deep-dive-2026-07-16|AI 人才市场与职业路径视频深度调研]]。

## 关联连接

- [[00-index|AI 相关 - 研究入口]]
- [[03-market-and-policy|AI 相关 - 市场与政策]]
- [[_syntheses/bilibili-ai-talent-market-and-career-path-deep-dive-2026-07-16|AI 人才市场与职业路径视频深度调研]]
- [[research-notes/README|AI Research Notes]]
