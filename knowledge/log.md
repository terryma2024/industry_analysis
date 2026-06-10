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

## [2026-06-08] synthesis | 机器人公司产品型号全景对比

- **变更**: 新增 [[robotics-embodied-ai/13-robot-company-product-comparison-2026-06-08|机器人公司产品型号全景对比]]；更新 [[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/04-companies|机器人公司与竞争]] 和 [[index|Knowledge Index]]。
- **范围**: 覆盖 `04-companies` 主表中的机器人整机、协作机器人、工业机器人、AMR/移动操作公司，按通用具身/人形、协作臂/工业机器人、AMR/仓储移动操作三类比较型号、参数、技术路线、优缺点和待验证项；新增 `raw/robotics-embodied-ai/data/robot_company_product_models_2026-06-08.csv` 作为可筛选数据表初版。
- **待继续**: `SRC-robotics-135` 至 `SRC-robotics-155` 为本轮 web 核验新增来源线索，需后续执行正式 raw capture 并补齐 `source_capture_manifest.csv`；协作臂/工业机器人/AMR 的每个 SKU 还需从产品手册拆成 CSV。

## [2026-06-09] synthesis | 具身智能业务落地 know-how 职业方向思考

- **变更**: 新增 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]]，将 Thinking Partner 对话沉淀为 Obsidian research note；更新 [[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]] 和 [[index|Knowledge Index]]。
- **范围**: 记录职业方向锚点、成功标准、家庭/健康约束、行业结构假设、业务落地 know-how、企业决策者成本/收入/风险痛点、早期反馈标准和零售后场/餐饮后厨/酒店后台等待验证场景。
- **待继续**: 本页主要基于对话综合，行业与场景判断需继续用客户访谈、招聘 JD、订单/复购证据和 raw source 入库验证。

## [2026-06-09] synthesis | 零售后场职业切入点验证分支

- **变更**: 更新 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]]，新增“零售后场是否适合作为职业切入点”澄清分支和拓扑图节点。
- **研究问题**: 中国市场中，按门店/仓库规模排名前 10 的大型零售/电商公司里，是否有超过一半已经启动机器人/具身智能项目，并进入真实门店或仓库运行。
- **治理更新**: 将 Thinking Partner skill 复制到 `.agents/skills/thinking-partner/`，并新增“每完成一个澄清分支就更新 durable document”的文档化规则。

## [2026-06-09] synthesis | 零售后场样本排名口径澄清

- **变更**: 更新 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]] 的零售后场验证分支，补充样本排名口径。
- **澄清结果**: 优先用公开行业排名；若门店/仓库规模排名不可得，则使用中国零售销售额前 10，避免使用 GMV/平台交易额或公司总营收作为首选口径。
- **下一步**: 查找中国零售销售额前 10 的大型零售/电商公司名单，并验证其中是否超过一半已有机器人/具身智能项目进入真实门店或仓库运行。

## [2026-06-09] synthesis | 零售后场项目证据来源口径澄清

- **变更**: 更新 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]] 的零售后场验证分支，补充项目落地证据来源口径。
- **澄清结果**: 判断机器人/具身智能项目是否进入真实门店或仓库运行时，最低接受公司公告或年报；媒体报道、案例文章、展会材料、供应商宣传和采访仅作为线索。
- **下一步**: 查找中国零售销售额前 10 企业的公司公告/年报，验证是否存在机器人/具身智能项目进入真实门店或仓库运行。

## [2026-06-09] synthesis | 零售后场项目范围口径澄清

- **变更**: 更新 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]] 的零售后场验证分支，补充项目范围计入口径。
- **澄清结果**: “自动化仓库”计入机器人/具身智能相关落地项目；“智能物流”等其它泛化说法不计入，除非明确包含机器人/具身智能系统或自动化仓库。
- **下一步**: 在公告/年报检索时区分自动化仓库、机器人/具身智能项目和其它泛化数字化/智能物流表述。

## [2026-06-09] synthesis | 零售后场场景边界澄清

- **变更**: 更新 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]] 的零售后场验证分支，明确门店后场与仓配体系边界。
- **澄清结果**: 中央仓、区域仓和纯仓配体系不计入“零售后场实践机会”；机器人/具身智能项目或自动化仓库必须发生在线下零售门店后场。
- **下一步**: 调研时优先查找商超、生鲜、便利店、仓储会员店等线下门店后场的项目证据。

## [2026-06-09] synthesis | 零售后场合作范围口径澄清

- **变更**: 更新 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]] 的零售后场验证分支，明确外部合作要求。
- **澄清结果**: 必须有外部具身智能/机器人公司参与；大型零售公司内部自研或内部试验不计入“实践机会”证据。
- **下一步**: 调研时同时识别零售公司、外部具身智能/机器人公司、项目发生位置和公告/年报证据。

## [2026-06-09] synthesis | 零售后场最低项目证据放宽

- **变更**: 更新 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]] 的零售后场验证分支，放宽最低项目证据标准。
- **澄清结果**: 公司公告或年报确认大型零售公司与外部具身智能/机器人公司合作即可计入；不要求公告或年报明确写明项目已经进入真实门店后场运行。
- **下一步**: 调研时将“合作存在”作为早期计入标准，将“进入真实门店后场运行、复购、扩店、ROI”作为更强证据单独标注。

## [2026-06-09] synthesis | 线下零售门店场景范围放宽

- **变更**: 更新 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]]，将职业切入点验证范围从“零售后场”放宽为“线下零售门店场景”。
- **澄清结果**: 门店前场的导购、巡店、清洁、安防等机器人项目也计入；中央仓、区域仓和纯仓配体系仍不计入。
- **下一步**: 调研中国零售销售额前 10 大型零售公司时，同时检索门店前场和门店后场的外部具身智能/机器人合作项目。

## [2026-06-09] synthesis | 通用服务机器人合作对象计入口径澄清

- **变更**: 更新 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]]，放宽外部合作对象范围。
- **澄清结果**: 清洁机器人、安防巡检机器人等通用服务机器人公司计入；不要求合作对象必须明确自称具身智能公司。
- **下一步**: 调研时将外部合作对象分为具身智能公司、机器人公司、通用服务机器人公司三类标注。

## [2026-06-09] synthesis | 线下零售门店继续调研门槛澄清

- **变更**: 更新 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]]，明确“超过一半前 10 公司有合作”的门槛用途。
- **澄清结果**: 该门槛只用于判断线下零售门店场景是否值得继续调研，不是判断是否值得作为职业切入点投入 6 个月验证的最终门槛。
- **下一步**: 继续澄清 6 个月职业验证所需的更强证据或成功标准。

## [2026-06-10] synthesis | 线下零售门店 6 个月验证门槛确认

- **变更**: 更新 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]]，确认“超过一半前 10 公司有合作”的门槛用途。
- **澄清结果**: 该门槛同时用于判断线下零售门店场景是否值得继续调研，以及是否值得作为职业切入点投入 6 个月验证。
- **下一步**: 进入外部调研：查找中国零售销售额前 10 大型零售公司名单，并验证是否超过一半有公告/年报确认的外部机器人/具身智能/通用服务机器人合作。

## [2026-06-10] synthesis | 线下零售门店验证通过阈值确认

- **变更**: 更新 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]] 的验证阈值。
- **澄清结果**: 前 10 公司中有 5 家满足条件，即视为“超过一半”门槛通过。
- **下一步**: 开始外部调研验证该门槛。

## [2026-06-10] synthesis | 线下零售门店机器人合作外部调研初扫

- **变更**: 新增 [[robotics-embodied-ai/research-notes/retail-store-robotics-entry-scan-2026-06-10|线下零售门店机器人合作验证初扫]]，并更新 [[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]] 和 [[index|Knowledge Index]]。
- **初步结果**: 暂定样本中未找到公司公告/年报级线下门店机器人合作证据，按当前严格口径为 0/10，未达到 5/10 通过门槛。
- **限制**: 尚未稳定获取 CCFA 或同等公开来源的最新中国零售销售额前 10 榜单，也未完成逐家公司公告/年报全文检索，因此该结果只能作为第一轮未通过，不能作为最终否定。

## [2026-06-10] synthesis | 场景选择标准修正为短期落地机会

- **变更**: 更新 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]]，记录线下零售门店初扫后的目标修正。
- **澄清结果**: 场景差异本身不是当前职业决策的关键；短期应用前景更重要，因为真实落地才能形成 feedback loop。当前优先证据是“真实订单”或“试点转生产”。
- **下一步**: 继续澄清“短期”的时间范围，再启动跨场景调研，比较哪些具身智能/机器人应用场景更可能出现真实订单或试点转生产。

## [2026-06-10] synthesis | 短期落地时间窗确认

- **变更**: 更新 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]]，明确短期落地机会的时间窗。
- **澄清结果**: “短期”定义为 1 年内；跨场景调研应比较 1 年内更可能出现真实订单或试点转生产的具身智能/机器人应用场景。
- **下一步**: 澄清调研时优先比较的候选场景范围。

## [2026-06-10] synthesis | 跨场景调研范围确认

- **变更**: 更新 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]]，明确 1 年内短期落地机会的候选场景范围。
- **澄清结果**: 全部具身智能/机器人应用场景都纳入比较，不只看零售、餐饮、酒店等生活近场景；工业、仓储、巡检、能源、制造等场景也纳入。
- **下一步**: 澄清跨场景调研的最小通过门槛，即什么样的订单/试点转生产证据足以把某个场景列为优先切入点。
