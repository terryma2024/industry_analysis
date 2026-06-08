---
title: Wiki Log
type: log
date_created: 2026-05-29
last_updated: 2026-06-02
tags:
  - wiki
  - log
  - llm-wiki
---

# Wiki Log

本文件为 append-only 操作日志。每条记录使用 `## [YYYY-MM-DD] action | summary`，便于 `rg "^## \\[" knowledge/log.md` 快速检索。

## [2026-05-29] migration | 初始化 Karpathy LLM Wiki 结构

- **变更**: 新增 [[index]]、[[log]]、`_sources/`、`_entities/`、`_concepts/`、`_claims/`、`_syntheses/`，并保留现有行业目录作为 Industries/Syntheses 层；更新 `AGENTS.md` 和 `.agents/skills/industry-analysis/SKILL.md` 以固化新工作流。
- **登记**: 首批登记行业入口、新闻摘要、机器人训练数据深度调研、UMI 研究、LeRobot/UMI/具身智能相关概念和实体；为 10 个行业 `00-index.md` 增加 wiki frontmatter 和 `## 关联连接`。
- **冲突**: 无。当前迁移不重命名既有行业笔记，避免破坏已存在 wikilinks。

## [2026-06-02] ingest | Scale AI 与中国 AI 数据基础设施对标

- **变更**: 新增 [[ai/research-notes/scale-ai-and-china-data-infrastructure-peers-2026-06-02|Scale AI 发展历程与中国对标公司]]、[[ai/research-notes/README|AI Research Notes]] 和 [[ai/00-source-capture-index|AI Source Capture Index]]；更新 [[ai/00-index|AI 相关 - 研究入口]]、[[ai/04-companies|AI 相关 - 公司与竞争]]、[[index|Knowledge Index]]。
- **来源**: 在 `knowledge/ai/sources.csv` 登记 Scale AI、Meta 交易、海天瑞声、数据堂、云测数据、标贝科技、曼孚科技、龙猫数据、GOMAX、Xpert、星尘数据、天衍奇点等公开来源，并运行 `tools/extract_sources_with_defuddle.py --industry ai --timeout 60` 抽取到 `raw/ai/documents/`。
- **待继续**: `SRC-ai-012` Axios 来源因 403 抓取失败；`SRC-ai-001`、`SRC-ai-003`、`SRC-ai-010`、`SRC-ai-016`、`SRC-ai-021`、`SRC-ai-022`、`SRC-ai-024` 为 fallback HTML，正式投资 memo 前应手工核验。

## [2026-06-02] ingest | Scale AI 公司发展史入库

- **变更**: 新增 [[ai/research-notes/scale-ai-company-history-2026-06-02|Scale AI 公司发展史]] 和 [[_entities/ScaleAI|Scale AI]] 实体卡；更新 [[ai/research-notes/README|AI Research Notes]]、[[ai/00-index|AI 相关 - 研究入口]]、[[index|Knowledge Index]]。
- **来源**: 复用 `knowledge/ai/sources.csv` 中 `SRC-ai-001` 至 `SRC-ai-012` 和 `raw/ai/documents/` 来源抽取结果。
- **待继续**: 正式投资 memo 前仍需对 `SRC-ai-012` Axios 403 失败项和部分 fallback HTML 来源做人工核验。

## [2026-06-02] synthesis | 具身智能数据采集和服务公司对比

- 新增 [[robotics-embodied-ai/11-embodied-ai-data-service-companies-2026-06-02|具身智能数据采集和服务公司对比]]，覆盖智元、补天石、它石、简智、Maxinsights、自变量、帕西尼的发展历史、解决方案、产品服务、技术路线、岗位信号和优劣势。
- 更新 [[index|Knowledge Index]] 的 Syntheses 区。
- 待后续：将本轮 web source 抽取为 `raw/robotics-embodied-ai/documents/SRC-*`，并补充 `sources.csv` 与 source_capture_manifest。

## [2026-06-02] concept | Vision-Language-Tactile-Action 术语解释

- 新增 [[_concepts/vision-language-tactile-action|Vision-Language-Tactile-Action]] 概念页，解释 VLTA/VTLA 与 VLA 的区别、四个模态和对具身数据公司的含义。
- 更新 [[robotics-embodied-ai/11-embodied-ai-data-service-companies-2026-06-02|具身智能数据采集和服务公司对比]] 的行业位置与关联连接。
- 更新 [[index|Knowledge Index]] 的 Concepts 区。

## [2026-06-02] migration | UMI 技术术语迁移为 entity 层

- 将旧 UMI 技术术语教学页改造为实体索引页。
- 新建/更新 64 个 `knowledge/_entities/` 术语实体页，覆盖 UMI、夹爪、传感器、位姿/坐标、SLAM、数据格式、模仿学习模型、质检和 ToB 交付物。
- 更新 [[_entities/README|Entities Layer]] 和 [[index|Knowledge Index]]，登记 UMI 术语实体包与关键实体。
- 冲突/限制：本次主要基于既有 UMI 研究页和 raw UMI 资料迁移补充；未新增外部检索，后续可按 source-backed 深化每个实体的原论文/官方文档引用。

## [2026-06-02] maintenance | UMI 技术术语旧页去链

- 将 UMI 业务计划、LeRobot 初学者笔记、实体层 README、全局索引和术语实体页中的旧术语页链接改为对应 entity 链接。
- 将旧术语页标记为 `deprecated`，后续新笔记应直接链接 [[_entities/UniversalManipulationInterface|UMI]]、[[_entities/IMU|IMU]]、[[_entities/SLAM|SLAM]]、[[_entities/Zarr|Zarr]]、[[_entities/HuggingFaceLeRobot|LeRobot]]、[[_entities/DiffusionPolicy|Diffusion Policy]]、[[_entities/ActionChunkingTransformer|ACT]] 等实体页。

## [2026-06-02] maintenance | 删除 UMI 技术术语旧页

- 已确认 `knowledge/` 内没有指向旧 slug `10-umi-technical-terms-for-beginners` 的链接。
- 删除旧页 `knowledge/robotics-embodied-ai/10-umi-technical-terms-for-beginners.md`；UMI 初学者术语入口保留在 [[_entities/README|Entities Layer]]，具体术语直接链接对应 entity。

## [2026-06-04] ingest | 逐际动力 LimX Dynamics 公司调研

- **变更**: 新增 [[_entities/LimXDynamics|LimX Dynamics]] 实体页；更新 [[robotics-embodied-ai/04-companies|机器人公司和竞争格局]]、[[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]] 和 [[index|Knowledge Index]]。
- **来源**: 在 `knowledge/robotics-embodied-ai/sources.csv` 登记 `SRC-robotics-103` 至 `SRC-robotics-113`，覆盖官网、TRON 1/Oli/TRON 2、FluxVLA、A/B 轮融资、行业周报和创始人访谈；抽取到 `raw/robotics-embodied-ai/documents/`。
- **待继续**: `SRC-robotics-105` TRON 1 用户手册因官网 PDF 证书过期自动下载失败；后续需浏览器手工保存或替换新版下载地址。逐际动力成立时间、主体名称改制、实际出货/收入和 COSA/VGM 可复现材料仍需继续验证。

## [2026-06-04] synthesis | 机器人工程平台综合调研

- **变更**: 新增 [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]；更新 [[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]] 和 [[index|Knowledge Index]]。
- **来源**: 在 `knowledge/robotics-embodied-ai/sources.csv` 登记 `SRC-robotics-114` 至 `SRC-robotics-124`，覆盖 NVIDIA Isaac Sim/Lab、OpenPI、OpenVLA、robomimic、LIBERO、ManiSkill、ROS、MoveIt 2、Agibot Genie Studio、EmbodiFlow，并运行来源抽取脚本。
- **待继续**: `SRC-robotics-120`、`SRC-robotics-122`、`SRC-robotics-123` 为 fallback HTML；正式竞品尽调前需手工补采 ManiSkill、MoveIt 2 和智元 Genie Studio 的页面正文或官方 PDF。

## [2026-06-05] news | NVIDIA Cosmos 3 上手调研

- **变更**: 新增 [[news/2026-06-05-nvidia-cosmos-3-getting-started-plan|NVIDIA Cosmos 3 上手调研与计划]]；更新 [[news/00-index|新闻速记]] 和 [[index|Knowledge Index]]。
- **来源**: 核对 NVIDIA Newsroom、NVIDIA Developer Blog、NVIDIA Research Cosmos Lab、NVIDIA/Cosmos GitHub、Hugging Face Cosmos3 collection/model card、arXiv `2606.02800`。
- **待继续**: 若进入正式机器人实验，需要补充本地/云端 GPU 型号、显存、CUDA driver、NGC/Hugging Face 权限，并把实际跑通记录转入 [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]] 或新建实验笔记。

## [2026-06-08] ingest | RoboAlign-R1 论文入库

- **变更**: 新增 [[_sources/roboalign-r1-reward-aligned-robot-video-world-models|RoboAlign-R1 - Reward-Aligned Robot Video World Models]]；更新 [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]、[[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]]、[[_sources/README|Sources Layer]]、[[index|Knowledge Index]]。
- **来源**: 在 `knowledge/robotics-embodied-ai/sources.csv` 登记 `SRC-robotics-125` arXiv 主论文和 `SRC-robotics-126` ModelScope/具身智能之心中文解读；PDF、arXiv HTML、ModelScope HTML/Markdown 均保存到 `raw/robotics-embodied-ai/documents/`。
- **限制**: `defuddle parse` 对 ModelScope 页面失败，原因是页面 metadata 中的 protocol-relative `og:url` 触发 invalid URL；已改用 raw HTML 中的 `window.__detail_data__` 生成 Markdown，并在 raw artifact 记录限制。

## [2026-06-08] synthesis | 中国可购买 UMI 夹爪设备检索

- **变更**: 新增 [[_syntheses/china-umi-gripper-purchase-scan-2026-06-08|中国可购买 UMI 夹爪设备检索]]；更新 [[_syntheses/README|Syntheses Layer]]、[[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]]、[[index|Knowledge Index]]。
- **来源**: 在 `knowledge/robotics-embodied-ai/sources.csv` 登记 `SRC-robotics-127` 至 `SRC-robotics-134`，覆盖 AIFITLAB 的 LUMOS FastUMI Pro/Ego/Go 商品页、鹿明 AWE2026 发布、觅蜂 MEgo 量产发货、BeingBeyond U1/RealDexUMI 官方与论文来源；已抽取 8 个 raw Markdown artifact 并更新 source_capture_manifest。
- **待继续**: 京东正式商品链接、AIFITLAB 中国大陆发票/售后、MEgo Gripper 是否单独出售和各设备 SDK/data license 仍需商务确认。
