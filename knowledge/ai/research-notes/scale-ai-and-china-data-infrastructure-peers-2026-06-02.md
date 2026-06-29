---
title: Scale AI 发展历程与中国对标公司
type: synthesis
date_created: 2026-06-02
last_updated: 2026-06-02
status: active
tags:
  - industry/ai
  - research-note
  - ai-data-infrastructure
  - company-comparison
sources:
  - ai/sources.csv
aliases:
  - Scale AI 中国对标
  - AI 数据基础设施公司对标
---

# Scale AI 发展历程与中国对标公司

> [!summary]
> Scale AI 的核心不是做基础模型，而是把 AI 产业链中最难规模化管理的数据采集、标注、反馈、评测和后训练数据工程做成基础设施。它从 2016 年的通用人力任务 API 起步，先抓住自动驾驶标注需求，再切入大模型 SFT/RLHF/评测和政府 AI，2025 年获得 Meta 约 143 亿美元战略投资。中国目前没有一个完全等价的 Scale AI，但海天瑞声、数据堂、云测数据、标贝科技、曼孚科技、龙猫数据，以及 GOMAX/Xpert/星尘数据/天衍奇点等新型专家数据公司，分别覆盖了 Scale 的不同侧面。

## 结论

- **不能简单说 Scale AI 被 Meta 收购。** 更准确的表述是：Meta 在 2025 年向 Scale AI 投入约 143 亿美元，取得约 49% 少数股权；Scale 官方称公司仍独立运营，同时创始人 Alexandr Wang 加入 Meta 负责 AI 相关工作。证据见 [`SRC-ai-008`](../../../raw/ai/documents/SRC-ai-008-scale-ai-announces-next-phase-of-company-evolution.md)、[`SRC-ai-009`](../../../raw/ai/documents/SRC-ai-009-customer-trust-and-scale-meta-deal.md)、[`SRC-ai-010`](../../../raw/ai/documents/SRC-ai-010-scale-ai-not-winding-down-following-meta-deal-interim-ceo-says.md)。
- **Scale AI 的真正产品是高质量数据生产体系。** 早期卖自动驾驶图像、视频、点云标注，后期卖大模型 SFT、RLHF、DPO、红队、评测、专家数据和政府/企业 AI 数据工程。
- **中国对标公司不能只看“数据标注公司”。** 更合适的分类是：传统训练数据供应商、自动驾驶数据平台、大模型后训练/专家数据公司、模型评测和企业 AI 交付商。
- **中国目前缺少一个同时具备全球大模型客户、政府订单、中立第三方地位、自动驾驶数据闭环和大模型后训练平台的综合型公司。** 但多个公司合起来已经覆盖 Scale AI 的主要业务版图。

## Scale AI 时间线

| 阶段 | 时间 | 关键事件 | 战略含义 | 证据 |
|---|---:|---|---|---|
| 0 到 1：人力任务 API | 2016 | Alexandr Wang 与 Lucy Guo 参加 Y Combinator，早期定位是通过 API 调用人工任务。 | 把人工劳动 API 化，而不是一开始就做模型。 | [`SRC-ai-001`](../../../raw/ai/documents/SRC-ai-001-scale-yc-company-post.md) |
| 杀手场景：自动驾驶 | 2016-2018 | 自动驾驶公司需要大量图像、视频、3D 点云标注，Scale 转向训练数据平台。 | 抓住第一轮 AI 工业化中“数据标注是瓶颈”的需求。 | [`SRC-ai-001`](../../../raw/ai/documents/SRC-ai-001-scale-yc-company-post.md), [`SRC-ai-002`](../../../raw/ai/documents/SRC-ai-002-scale-announces-series-b-funding.md) |
| Series B | 2018 | 融资 1800 万美元，强调 human intelligence + machine learning 的训练数据服务。 | 从众包任务平台升级为 AI 数据基础设施。 | [`SRC-ai-002`](../../../raw/ai/documents/SRC-ai-002-scale-announces-series-b-funding.md) |
| 独角兽 | 2019 | Series C 融资 1 亿美元，估值超 10 亿美元。 | 将“AI 的关键瓶颈是标注数据”讲成资本市场可理解的基础设施故事。 | [`SRC-ai-003`](../../../raw/ai/documents/SRC-ai-003-scale-ai-series-c.md) |
| 自动驾驶与传统 AI 扩张 | 2020-2021 | 2020 年 Series D 后估值约 35 亿美元；2021 年 Series E 后估值约 73 亿美元。 | 在自动驾驶、视觉、企业 AI 数据服务中扩大交付能力。 | [`SRC-ai-004`](../../../raw/ai/documents/SRC-ai-004-scale-ai-breaking-even-after-it-scaled-back-hiring.md), [`SRC-ai-005`](../../../raw/ai/documents/SRC-ai-005-scale-ai-scores-325-million-to-grow-ai-solution.md) |
| 政府/国防线 | 2022 | 获美国国防部近 2.5 亿美元 BPA 合同。 | 从商业数据服务商扩展为政府 AI 基础设施供应商。 | [`SRC-ai-006`](../../../raw/ai/documents/SRC-ai-006-scale-ai-awarded-250m-ai-contract-by-department-of-defense.md) |
| 大模型红利 | 2022-2024 | 生成式 AI 爆发后，Scale 转向 SFT、RLHF、DPO、红队和模型评测等后训练数据服务。 | “标注”升级为“人类反馈、专家数据、模型可靠性评测”。 | [`SRC-ai-007`](../../../raw/ai/documents/SRC-ai-007-scale-ai-series-f.md) |
| Series F | 2024 | 融资 10 亿美元，估值约 138 亿美元，投资方包括 Amazon、Meta、Intel、AMD、Qualcomm 等。 | 被视为 AI 数据供应链中的中立基础设施。 | [`SRC-ai-007`](../../../raw/ai/documents/SRC-ai-007-scale-ai-series-f.md) |
| Meta 战略投资 | 2025 | Meta 向 Scale 投资约 143 亿美元，取得约 49% 少数股权；Alexandr Wang 加入 Meta。 | Meta 获得数据能力、组织经验和关键人才，但 Scale 官方称仍独立运营。 | [`SRC-ai-008`](../../../raw/ai/documents/SRC-ai-008-scale-ai-announces-next-phase-of-company-evolution.md), [`SRC-ai-009`](../../../raw/ai/documents/SRC-ai-009-customer-trust-and-scale-meta-deal.md), [`SRC-ai-010`](../../../raw/ai/documents/SRC-ai-010-scale-ai-not-winding-down-following-meta-deal-interim-ceo-says.md) |
| 后交易阶段 | 2025-2026 | Scale 强调客户数据隔离与独立运营，并继续推进企业、政府、评测与数据业务。 | 最大风险变成“中立性是否被大模型客户信任”。 | [`SRC-ai-009`](../../../raw/ai/documents/SRC-ai-009-customer-trust-and-scale-meta-deal.md), [`SRC-ai-011`](../../../raw/ai/documents/SRC-ai-011-meta-restructures-its-ai-unit-under-superintelligence-labs.md), [[00-source-capture-index|SRC-ai-012]] |

## Scale AI 的能力拆解

| 能力层 | 早期形态 | 大模型时代形态 | 中国对标观察 |
|---|---|---|---|
| 数据采集 | 人力任务、图片/文本采集 | 多模态、领域专家、复杂推理轨迹 | 海天瑞声、数据堂、云测数据、标贝科技均覆盖部分环节。 |
| 数据标注 | 自动驾驶图像、视频、点云标注 | SFT、RLHF、DPO、CoT、工具调用轨迹 | 曼孚科技、龙猫数据偏自动驾驶；GOMAX、Xpert 偏专家数据和 Agent 数据。 |
| 质量控制 | 标注流程、质检、交付 SLA | 多轮专家质检、模型评测、红队 | 公开信息中，国内公司普遍披露不足，需要继续验证交付体系。 |
| 客户结构 | 自动驾驶/企业 AI 客户 | 大模型公司、政府、军方、企业 AI | 中国公司多数偏国内政企、大模型厂商和自动驾驶客户，全球头部实验室客户较少。 |
| 战略地位 | AI 数据外包商 | 数据基础设施和后训练供应链 | 中国的对应主题是“AI 数据要素 + 大模型后训练 + 智能驾驶数据闭环”。 |

## 中国公司分层

| 公司 | 更像 Scale 的哪一面 | 当前判断 | 主要证据 |
|---|---|---|---|
| 海天瑞声 | AI 训练数据、大模型后训练、评测 | 最适合作为公开市场中的 Scale AI 对标样本。官网已覆盖语音、图像、自然语言、多模态，以及 SFT、RLHF、DPO、评测等大模型数据服务。 | [`SRC-ai-013`](../../../raw/ai/documents/SRC-ai-013-source.md) |
| 数据堂 | 数据资产、数据采集/标注、行业数据集 | 更像长期积累训练数据集和交付能力的数据供应商，覆盖大模型、智能驾驶、医疗等场景。 | [`SRC-ai-014`](../../../raw/ai/documents/SRC-ai-014-source.md), [`SRC-ai-015`](../../../raw/ai/documents/SRC-ai-015-source.md) |
| Testin 云测 / 云测数据 | AI 数据平台、标注工具、测试与企业服务 | 从应用测试扩展到 AI 训练数据与大模型微调，多模态标注和测试能力使其更偏“数据 + 测试平台”。 | [`SRC-ai-016`](../../../raw/ai/documents/SRC-ai-016-testin.md) |
| 标贝科技 / DataBaker | 语音数据、多模态采集标注、大模型数据 | 语音数据和语音交互能力更强，是“语音数据能力突出的 Scale 子集”。 | [`SRC-ai-017`](../../../raw/ai/documents/SRC-ai-017-source.md) |
| 曼孚科技 MindFlow | 自动驾驶/CV 数据标注平台 | 对标 Scale 早期自动驾驶数据标注路线，强调自动驾驶数据标注、人机融合和平台化。 | [`SRC-ai-018`](../../../raw/ai/documents/SRC-ai-018-source.md) |
| 龙猫数据 | 自动驾驶、CV、语音、NLU 数据标注 | 偏智能驾驶和通用标注服务，公开信息提到自动驾驶自动标注能力。 | [`SRC-ai-019`](../../../raw/ai/documents/SRC-ai-019-source.md), [`SRC-ai-020`](../../../raw/ai/documents/SRC-ai-020-autopilotgpt.md) |
| GOMAX LAB / 骨码智元 | 大模型专家数据、训练/对齐/评测 | 更贴近 Scale 后期的专家数据和大模型评测路线，值得继续跟踪。 | [`SRC-ai-021`](../../../raw/ai/documents/SRC-ai-021-gomax-lab.md) |
| Xpert Studio | Agent/复杂任务专家数据 | 覆盖 CoT、Tool/Browser/Computer Use、RLVR 等复杂任务标注，方向很新，但商业规模待验证。 | [`SRC-ai-022`](../../../raw/ai/documents/SRC-ai-022-xpert-studio.md) |
| 星尘数据 Stardust AI | SFT/RLHF 数据标注、语料定制 | 公开材料显示覆盖 SFT 数据集、RLHF、语料和模型训练服务，仍需验证客户和交付规模。 | [`SRC-ai-023`](../../../raw/ai/documents/SRC-ai-023-stardust-ai-smart-education-scenario.md) |
| 天衍奇点 | 大模型数据工程、标注服务 | 新公司，定位很贴近大模型时代数据工程，但公开验证材料较少。 | [`SRC-ai-024`](../../../raw/ai/documents/SRC-ai-024-source.md) |

## 对标判断

### 最接近 Scale AI 的中国公司

- **资本市场/上市公司口径：海天瑞声。** 适合用来跟踪 AI 训练数据、大模型后训练数据、评测服务在中国资本市场中的定价。
- **数据资产和传统训练数据口径：数据堂。** 适合观察数据集资产、采集标注交付和行业数据集商业化。
- **自动驾驶早期 Scale 路线：曼孚科技、龙猫数据、云测数据。** 适合对标 Scale 早期靠自动驾驶 2D/3D/点云标注起飞的阶段。
- **大模型后训练/专家数据口径：GOMAX、Xpert Studio、星尘数据、天衍奇点。** 这些公司更像 Scale 后期的 Outlier/专家数据/评测路线，但目前多数公开规模、客户结构和交付指标仍需验证。

### 中国市场的结构性差异

- **客户集中于国内模型厂商、自动驾驶企业和政企项目。** 与 Scale 服务 OpenAI、Meta、Microsoft 等全球头部实验室的客户结构不同。
- **中立第三方地位更难建立。** 国内大模型厂商通常有自建数据团队和外包体系，第三方数据平台很难完全进入核心后训练链路。
- **数据合规和跨境限制更强。** 中国数据出境、安全审查、个人信息保护和行业数据合规，会限制“全球化数据供应链”模式。
- **政策机会更偏数据要素和行业智能化。** 中国机会可能不只是“标注外包”，而是政企行业数据治理、数据要素入表、行业大模型评测、智能驾驶数据闭环。

## 投资与研究启发

- **观察指标 1：收入是否从低毛利标注转向高毛利专家数据/评测。** 传统标注容易价格竞争，专家数据、模型评测、红队和行业知识工程才更接近 Scale 后期叙事。
- **观察指标 2：客户是否进入核心模型训练链路。** 如果只是外围语料清洗或标注外包，壁垒弱；如果进入 SFT/RLHF/DPO/评测闭环，战略价值更高。
- **观察指标 3：是否有平台化工具和质量体系。** Scale 的价值不只是人多，而是任务拆解、质检、路由、验收、交付和客户集成。
- **观察指标 4：是否具备行业专家网络。** 大模型后训练越来越需要医学、法律、金融、工程、代码、数学等高质量专家数据。
- **观察指标 5：是否被核心大模型厂商信任。** Meta 投资 Scale 后，其他模型公司可能担心中立性；中国市场也会面临类似竞合关系。

## 待验证

- 国内各公司大模型数据业务的真实收入占比、毛利率、客户集中度。
- 海天瑞声、数据堂、云测数据等是否进入国内头部大模型公司的核心后训练链路。
- GOMAX、Xpert、星尘数据、天衍奇点的客户、融资、交付规模和专家网络质量。
- 中国政企 AI 数据工程项目是否会形成类似美国国防部 BPA 那样的大额、长期、可复用框架合同。
- 这批公司是否会从“标注服务商”升级为“模型评测/数据飞轮/行业 AI 基础设施商”。

## 关联连接

- [[../00-index|AI 相关 - 研究入口]]
- [[../04-companies|AI 相关 - 公司与竞争]]
- [[README|AI Research Notes]]
- [[../../index|Knowledge Index]]

## 来源

来源索引见 [[../sources.csv|AI sources.csv]]，离线抓取状态见 [[../00-source-capture-index|AI Source Capture Index]]。本笔记当前以公开网页来源、`raw/ai/documents/` 抽取结果和前序调研整理为基础；其中 [[00-source-capture-index|SRC-ai-012]] 抓取失败，[`SRC-ai-001`](../../../raw/ai/documents/SRC-ai-001-scale-yc-company-post.md)、[`SRC-ai-003`](../../../raw/ai/documents/SRC-ai-003-scale-ai-series-c.md)、[`SRC-ai-010`](../../../raw/ai/documents/SRC-ai-010-scale-ai-not-winding-down-following-meta-deal-interim-ceo-says.md)、[`SRC-ai-016`](../../../raw/ai/documents/SRC-ai-016-testin.md)、[`SRC-ai-021`](../../../raw/ai/documents/SRC-ai-021-gomax-lab.md)、[`SRC-ai-022`](../../../raw/ai/documents/SRC-ai-022-xpert-studio.md)、[`SRC-ai-024`](../../../raw/ai/documents/SRC-ai-024-source.md) 为 fallback HTML，需要正式投资 memo 前继续核验。
