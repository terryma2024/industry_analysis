# knowledge

这里是本项目的 Obsidian vault，也是 Karpathy LLM Wiki 式的知识编译层。`raw/` 保存不可变来源，`knowledge/` 保存由来源编译出的结构化、可链接、可审计知识资产。每个行业的知识文件应能回答三个问题：

- 我如何理解这个行业？
- 我如何判断它的投资价值和风险？
- 我如何进入这个行业或围绕它学习？

## Obsidian 维护准则

- 使用 Obsidian Flavored Markdown，保持普通 Markdown 可读。
- 使用 Obsidian wikilinks 连接行业、公司、技术、政策、岗位和资料来源。
- LLM 查询和维护时优先读取 [[index|Knowledge Index]]，并在重要写入后追加 [[log|Wiki Log]]。
- 每个行业保留 `00-index.md` 作为入口笔记。
- 临时新闻、文章、视频和音频摘要统一放在 [[news/00-index|新闻速记]]；每条摘要独立成文，并在该索引页登记。
- 复杂主题可以增加 MOC note、Canvas、Mermaid 或 Excalidraw 图。
- 不把原始大文件塞进知识笔记；原始材料仍放在 `raw/`，知识笔记只保留摘要、判断和来源引用。

## LLM Wiki 编译层

- [[index|Knowledge Index]]：LLM 优先读取的全局内容索引。
- [[log|Wiki Log]]：append-only 操作日志。
- [[_sources/README|Sources]]：从原始来源编译出的一对一来源摘要。
- [[_entities/README|Entities]]：人物、公司、机构、工具、产品和项目。
- [[_concepts/README|Concepts]]：跨行业复用的概念、框架、方法论和技术定义。
- [[_claims/README|Claims]]：原子化、可溯源判断。
- [[_syntheses/README|Syntheses]]：跨来源、跨行业或跨概念的综合分析。

## 分类入口

- [[news/00-index|新闻速记]]：临时新闻、文章、视频和音频摘要。
- [[ai/00-index|AI]]
- [[future-energy/00-index|未来能源]]
- [[integrated-circuits/00-index|集成电路]]
- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[low-altitude-economy/00-index|低空经济]]
- [[aerospace/00-index|航空航天]]
- [[biopharma/00-index|生物医药]]
- [[eldercare/00-index|养老服务与银发科技]]
- [[quantum-technology/00-index|量子科技]]
- [[6g/00-index|6G]]
- [[brain-computer-interface/00-index|脑机接口]]

## 工作流 SOP

- [Obsidian Knowledge Production SOP](../docs/obsidian_knowledge_sop.md): 本仓库知识生产、链接、来源追踪、任务复核和 Obsidian 友好写作的统一 SOP。
- [[_syntheses/karpathy-wiki-migration-plan|Karpathy Wiki Migration Plan]]：本仓库升级为 LLM Wiki 的迁移设计与状态。
