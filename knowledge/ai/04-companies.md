---
title: AI相关 - 公司与竞争
type: industry
date_created: 2026-05-29
last_updated: 2026-06-02
status: draft
tags:
  - industry/ai
  - companies
sources:
  - ai/sources.csv
---

# AI相关 - 公司与竞争

## 公司分层

| 公司 | 环节 | 商业模式 | 客户 | 优势 | 风险 | 证据 |
| --- | --- | --- | --- | --- | --- | --- |
| Scale AI | AI 数据基础设施、自动驾驶数据、大模型后训练、评测 | 数据采集/标注/反馈/评测平台与企业/政府交付 | 海外大模型公司、企业、政府 | 把数据生产、质检、后训练和评测做成基础设施；Meta 战略投资后战略地位上升 | 中立性风险、对大客户依赖、标注劳动争议 | [`SRC-ai-001`](../../raw/ai/documents/SRC-ai-001-scale-yc-company-post.md) 至 [SRC-ai-012](00-source-capture-index.md) |
| 海天瑞声 | 训练数据、大模型数据、评测 | 数据采集、标注、SFT/RLHF/DPO、评测 | 国内 AI 公司和政企客户，待进一步验证 | A 股上市公司，公开材料最接近 Scale AI 的训练数据/大模型数据口径 | 大模型数据真实收入占比与毛利率待验证 | [`SRC-ai-013`](../../raw/ai/documents/SRC-ai-013-source.md) |
| 数据堂 | 数据集资产、行业数据、采集标注 | 数据集销售、定制采集标注、平台服务 | 大模型、智能驾驶、医疗等行业客户，待进一步验证 | 长期积累数据资源和行业数据集 | 是否进入核心后训练链路待验证 | [`SRC-ai-014`](../../raw/ai/documents/SRC-ai-014-source.md), [`SRC-ai-015`](../../raw/ai/documents/SRC-ai-015-source.md) |
| Testin 云测 / 云测数据 | AI 数据平台、标注、测试 | 数据服务、测试服务、平台工具 | 企业 AI、智能驾驶、大模型客户，待进一步验证 | 测试业务和数据标注平台结合 | 与纯数据公司相比定位更复合 | [`SRC-ai-016`](../../raw/ai/documents/SRC-ai-016-testin.md) |
| 标贝科技 / DataBaker | 语音数据、多模态采集标注、大模型数据 | 数据采集标注、语音技术服务 | 语音交互、智能硬件、大模型客户，待进一步验证 | 语音数据和语音技术积累较强 | 与 Scale 的自动驾驶/政府/评测综合能力仍不同 | [`SRC-ai-017`](../../raw/ai/documents/SRC-ai-017-source.md) |
| 曼孚科技 | 自动驾驶/CV 数据标注平台 | 标注平台、数据服务 | 自动驾驶和视觉 AI 客户，待进一步验证 | 对标 Scale 早期自动驾驶数据路线 | 大模型后训练能力公开证据较弱 | [`SRC-ai-018`](../../raw/ai/documents/SRC-ai-018-source.md) |
| 龙猫数据 | 自动驾驶、CV、语音、NLU 数据标注 | 标注服务、自动标注工具 | 自动驾驶和通用 AI 客户，待进一步验证 | 覆盖自动驾驶自动标注等方向 | 商业规模和客户结构待验证 | [`SRC-ai-019`](../../raw/ai/documents/SRC-ai-019-source.md), [`SRC-ai-020`](../../raw/ai/documents/SRC-ai-020-autopilotgpt.md) |
| GOMAX LAB / 骨码智元 | 专家数据、大模型训练/对齐/评测 | 专家数据生产和评测服务 | 大模型公司，待进一步验证 | 更接近 Scale 后期专家数据与评测路线 | 新型公司，公开规模待验证 | [`SRC-ai-021`](../../raw/ai/documents/SRC-ai-021-gomax-lab.md) |
| Xpert Studio | Agent/复杂任务专家数据 | CoT、工具调用、RLVR 等复杂任务标注 | 大模型和 Agent 团队，待进一步验证 | 方向贴近 Agent 数据和复杂后训练 | 客户与收入待验证 | [`SRC-ai-022`](../../raw/ai/documents/SRC-ai-022-xpert-studio.md) |
| 星尘数据 Stardust AI | SFT/RLHF、语料定制、模型训练 | 数据集、标注、模型训练服务 | 教育等垂直场景和大模型客户，待进一步验证 | 覆盖大模型后训练数据服务 | 公开验证材料有限 | [`SRC-ai-023`](../../raw/ai/documents/SRC-ai-023-stardust-ai-smart-education-scenario.md) |
| 天衍奇点 | 大模型数据工程、数据标注 | 数据工程和标注服务 | 大模型客户，待进一步验证 | 定位贴近大模型时代数据工程 | 新公司，公开材料和交付规模待验证 | [`SRC-ai-024`](../../raw/ai/documents/SRC-ai-024-source.md) |

> [!note]
> 详见 [[research-notes/scale-ai-and-china-data-infrastructure-peers-2026-06-02|Scale AI 发展历程与中国对标公司]]。本页只保留公司分层和竞争入口，事实与判断以该研究笔记为主。

## 竞争格局

- 集中度：传统标注服务分散，大模型专家数据和评测环节仍在形成头部公司。
- 进入壁垒：低端标注壁垒弱；高壁垒来自专家网络、质量控制、平台化工具、客户信任和进入核心模型训练链路。
- 价格/成本趋势：基础标注容易价格竞争；SFT/RLHF/DPO、红队和专业评测具备更高溢价，但真实毛利率待验证。
- 新进入者：GOMAX、Xpert Studio、星尘数据、天衍奇点等更偏大模型专家数据和 Agent 数据。
- 替代者：大模型厂商自建数据团队、众包平台、自动标注/合成数据工具。

## 需要跟踪的公司

- 上市公司：海天瑞声。
- 未上市公司：数据堂、Testin 云测、标贝科技、曼孚科技、龙猫数据、GOMAX LAB、Xpert Studio、星尘数据、天衍奇点。
- 海外公司：Scale AI。
- 产业链关键供应商：待补充数据采集工具、众包平台、模型评测平台、数据合规服务商。

## 关联连接

- [[00-index|AI 相关 - 研究入口]]
- [[research-notes/README|AI Research Notes]]
- [[research-notes/scale-ai-and-china-data-infrastructure-peers-2026-06-02|Scale AI 发展历程与中国对标公司]]
