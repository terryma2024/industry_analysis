---
title: AI相关 - 公司与竞争
type: industry
date_created: 2026-05-29
last_updated: 2026-06-29
status: draft
tags:
  - industry/ai
  - companies
sources:
  - ai/sources.csv
---

# AI相关 - 公司与竞争

## 公司分层

| 公司/机构 | 环节 | 商业模式 | 客户/入口 | 优势 | 风险 | 证据 |
| --- | --- | --- | --- | --- | --- | --- |
| 华为昇腾 | AI 算力/软件栈 | 芯片、服务器、开发套件、生态 | 政企、云、模型厂商 | 国产算力核心生态 | 产能、生态兼容、性能/成本待验证 | [`SRC-ai-044`](../../raw/ai/documents/SRC-ai-044-source.md) |
| 寒武纪 | AI 芯片 | 芯片/加速卡/系统 | 云、政企、数据中心 | A 股 AI 芯片代表 | 订单、盈利、估值和供应链待验证 | [`SRC-ai-045`](../../raw/ai/documents/SRC-ai-045-source.md) |
| 阿里 Qwen/ModelScope | 基础模型/云/开源生态 | 模型 API、云服务、开源生态 | 开发者、企业、阿里生态 | 开源社区和云平台协同 | 云收入拆分和海外合规待验证 | [`SRC-ai-039`](../../raw/ai/documents/SRC-ai-039-source.md) [`SRC-ai-046`](../../raw/ai/documents/SRC-ai-046-source.md) |
| 百度文心 | 基础模型/搜索/智能云 | C 端助手、API、行业解决方案 | 搜索、内容、企业云 | 搜索和知识入口、智能云 | 模型产品商业化弹性待验证 | [`SRC-ai-040`](../../raw/ai/documents/SRC-ai-040-source.md) |
| DeepSeek | 基础模型/推理模型 | API、开源/开放模型、开发者生态 | 开发者、企业、模型社区 | 成本效率和技术影响力强 | 商业化、算力和持续领先待验证 | [`SRC-ai-038`](../../raw/ai/documents/SRC-ai-038-source.md) |
| 月之暗面 Kimi | C 端助手/模型应用 | 订阅、流量、API/企业服务待验证 | C 端用户、长文本场景 | 产品心智强 | 获客成本和收入结构待验证 | [`SRC-ai-041`](../../raw/ai/documents/SRC-ai-041-source.md) |
| 智谱 AI | 基础模型/政企服务/Agent | API、私有化、企业服务 | 政企、开发者 | 清华系和企业服务基础 | 收入规模和客户复购待验证 | [`SRC-ai-042`](../../raw/ai/documents/SRC-ai-042-source.md) |
| 腾讯混元 | 基础模型/云/生态应用 | 云 API、内部生态赋能 | 微信、QQ、腾讯云、游戏/内容 | 流量和应用生态强 | 对外商业化收入待验证 | [`SRC-ai-043`](../../raw/ai/documents/SRC-ai-043-source.md) |
| Scale AI | 数据/后训练/评测 | 数据生产、后训练、评测、政府/企业交付 | 海外模型公司、企业、政府 | 数据基础设施标杆 | 中立性、客户集中、劳动争议 | [`SRC-ai-001`](../../raw/ai/documents/SRC-ai-001-scale-yc-company-post.md) 至 [[00-source-capture-index|SRC-ai-012]] |
| 海天瑞声/数据堂/云测/标贝等 | 中国数据基础设施 | 采集、标注、SFT/RLHF、评测 | 国内模型和行业客户 | 数据服务基础和垂直资源 | 毛利率、客户结构、核心链路待验证 | [`SRC-ai-013`](../../raw/ai/documents/SRC-ai-013-source.md) 至 [`SRC-ai-024`](../../raw/ai/documents/SRC-ai-024-source.md) |

> [!note]
> AI 数据基础设施的公司对标详见 [[research-notes/scale-ai-and-china-data-infrastructure-peers-2026-06-02|Scale AI 发展历程与中国对标公司]]。本页把它放回 AI 总产业链，而不是只围绕数据服务展开。

## 竞争格局

- 基础模型：头部互联网平台、创业公司和开源模型并存；模型能力差距会被开源和推理成本下降快速压缩，商业化关键转向入口、生态和场景。
- 算力层：先进 GPU 受外部限制，国产算力是政策和产业链主线，但生态迁移、性能/成本和供给节奏需长期验证。
- 应用层：C 端助手流量大但付费不确定；B 端应用更看行业 know-how、数据接入、权限、安全和工作流改造。
- 数据/评测：低端标注价格竞争强，高价值专家数据、评测、红队、安全和 Agent 任务数据更可能形成溢价。

## 需要跟踪的公司

- 上市/大平台：阿里、百度、腾讯、华为、寒武纪、科大讯飞、金山办公、用友、金蝶、海天瑞声。
- 创业模型公司：DeepSeek、月之暗面、智谱 AI、MiniMax、阶跃星辰、百川智能、零一万物等。
- 大厂应用入口观察：字节/豆包、火山引擎、抖音、剪映等需要另起官方来源专项，重点看 C 端活跃、API 商业化和内容工具闭环。
- 数据与评测：Scale AI、海天瑞声、数据堂、Testin 云测、标贝科技、GOMAX、Xpert Studio、星尘数据、天衍奇点。
- 应用与 Agent：办公、编程、营销、客服、教育、医疗、金融和制造软件公司，需要按真实付费场景拆分。

## 关联连接

- [[00-index|AI 相关 - 研究入口]]
- [[research-notes/README|AI Research Notes]]
- [[research-notes/scale-ai-and-china-data-infrastructure-peers-2026-06-02|Scale AI 发展历程与中国对标公司]]
