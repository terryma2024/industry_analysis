---
title: Wiki Log
type: log
date_created: 2026-05-29
last_updated: 2026-09-01
tags:
  - wiki
  - log
  - llm-wiki
---

# Wiki Log

本文件为按日期归并的 append-only 操作日志。每个日期只使用一个 `## [YYYY-MM-DD]`，当天的变更使用 `- **action | summary**` 紧凑追加在该日期下；便于按日期检索，同时避免重复日期标题。

## [2026-09-01]

- **automation | Bilibili 收藏夹候选读取失败，未生成研究包**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-09-01|Bilibili AI Daily Run 2026-09-01]]；更新 [[index|Knowledge Index]]。
  - **结果**: `opencli doctor` 显示 daemon 正常但 Browser Bridge extension 未连接；有界的第一阶段收藏夹读取返回 `BROWSER_CONNECT`（exit code `69`），候选、重复跳过、模型选中与 processed 均为 0。
  - **限制**: 未运行第二阶段、TOS/ASR、source card、`sources.csv` 或单视频深研；TOS 前缀 `asr-audio/2026/09/01` 为空，符合零视频选中的预期。需在 Chrome/Chromium 恢复 OpenCLI Browser Bridge 后从第一阶段重跑。

## [2026-08-31]

- **automation | Bilibili 收藏夹候选读取失败，未生成研究包**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-08-31|Bilibili AI Daily Run 2026-08-31]]；更新 [[index|Knowledge Index]]。
  - **结果**: `opencli doctor` 显示 daemon 正常但 Browser Bridge extension 未连接；规范第一阶段及一次直接 `bilibili favorite` 读取均未产生可解析候选，故候选、重复跳过、模型选中、processed 均为 0。
  - **限制**: 未运行第二阶段、TOS/ASR、source card、`sources.csv` 或单视频深研；在 Chrome/Chromium 恢复 OpenCLI Browser Bridge 连接后从第一阶段重跑。

## [2026-08-30]

- **automation | Bilibili 收藏夹筛选完成并修复瞬时抓取失败**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-08-30|Bilibili AI Daily Run 2026-08-30]]；更新 [[index|Knowledge Index]]、`tools/bilibili_ai_daily_research.py` 与其回归测试。
  - **结果**: 20 个候选中 18 个为已有 source packet/研究资产；`BV1s43t6UEaW` 与 `BV1cvTq68E5g` 经模型复核均非 AI/具身智能相关，模型选中 0，未运行二阶段，也未创建 transcript、ASR、source card、`sources.csv` 或单视频深研。
  - **修复与验证**: Browser Bridge 的首次 `Navigation rejected` 可由同一只读请求重试恢复；收藏夹抓取增加一次有界重试，`uv run python -m unittest tests.test_bilibili_ai_daily_research` 通过（19 tests）。
  - **限制**: TOS 前缀 `asr-audio/2026/08/30` 为空，符合零视频选中的预期；不存在待重试视频。

## [2026-08-29]

- **automation | Bilibili 收藏夹候选筛选完成，无新增研究包**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-08-29|Bilibili AI Daily Run 2026-08-29]] 并更新 [[index|Knowledge Index]]。
  - **结果**: 20 个候选中 18 个为既有记录；`BV1s43t6UEaW` 与 `BV1cvTq68E5g` 经模型复核均非 AI/具身智能相关，未运行二阶段转录、ASR、source card、`sources.csv` 或单视频深研。
  - **限制**: TOS 前缀 `asr-audio/2026/08/29` 可检查但为空；这是零视频被选中的正常结果，而非处理失败。

## [2026-08-28]

- **automation | Bilibili 收藏夹候选拉取失败并修复 command discovery**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-08-28|Bilibili AI Daily Run 2026-08-28]]，更新 [[index|Knowledge Index]]；修复 `tools/bilibili_ai_daily_research.py` 并新增回归测试。
  - **结果**: OpenCLI 的 `bilibili favorite` 因 Browser Bridge 未连接而返回 `BROWSER_CONNECT`（exit code `69`），候选数为 0；因此没有模型选中、下载、ASR、source card、`sources.csv` 写入或单视频深研。
  - **验证**: `uv run python -m unittest tests.test_bilibili_ai_daily_research` 通过（18 tests）；discovery 只会执行命令名为收藏夹/collection 的 Bilibili adapter。
  - **人工处理**: 在 Chrome/Chromium 中打开并启用 OpenCLI Browser Bridge 扩展后，重新运行 `uv run python tools/bilibili_ai_daily_research.py --limit 20 --json`；无需重置任何仓库产物。

## [2026-08-27]

- **automation | Bilibili 收藏夹候选拉取失败，未生成研究包**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-08-27|Bilibili AI Daily Run 2026-08-27]] 并更新 [[index|Knowledge Index]]。
  - **结果**: OpenCLI 的 Bilibili Browser Bridge 未连接，候选数为 0；因此没有模型选中项、重复判断、下载、ASR、source card、`sources.csv` 写入或单视频深研。
  - **人工处理**: 在 Chrome/Chromium 中打开并启用 OpenCLI Browser Bridge 扩展后，重新运行 `uv run python tools/bilibili_ai_daily_research.py --limit 20 --json`；无需重置任何仓库产物。

## [2026-05-29]

- **migration | 初始化 Karpathy LLM Wiki 结构**
  - **变更**: 新增 [[index]]、[[log]]、`_sources/`、`_entities/`、`_concepts/`、`_claims/`、`_syntheses/`，并保留现有行业目录作为 Industries/Syntheses 层；更新 `AGENTS.md` 和 `.agents/skills/industry-analysis/SKILL.md` 以固化新工作流。
  - **登记**: 首批登记行业入口、新闻摘要、机器人训练数据深度调研、UMI 研究、LeRobot/UMI/具身智能相关概念和实体；为 10 个行业 `00-index.md` 增加 wiki frontmatter 和 `## 关联连接`。
  - **冲突**: 无。当前迁移不重命名既有行业笔记，避免破坏已存在 wikilinks。

## [2026-06-02]

- **ingest | Scale AI 与中国 AI 数据基础设施对标**
  - **变更**: 新增 [[ai/research-notes/scale-ai-and-china-data-infrastructure-peers-2026-06-02|Scale AI 发展历程与中国对标公司]]、[[ai/research-notes/README|AI Research Notes]] 和 [[ai/00-source-capture-index|AI Source Capture Index]]；更新 [[ai/00-index|AI 相关 - 研究入口]]、[[ai/04-companies|AI 相关 - 公司与竞争]]、[[index|Knowledge Index]]。
  - **来源**: 在 `knowledge/ai/sources.csv` 登记 Scale AI、Meta 交易、海天瑞声、数据堂、云测数据、标贝科技、曼孚科技、龙猫数据、GOMAX、Xpert、星尘数据、天衍奇点等公开来源，并运行 `tools/extract_sources_with_defuddle.py --industry ai --timeout 60` 抽取到 `raw/ai/documents/`。
  - **待继续**: `SRC-ai-012` Axios 来源因 403 抓取失败；`SRC-ai-001`、`SRC-ai-003`、`SRC-ai-010`、`SRC-ai-016`、`SRC-ai-021`、`SRC-ai-022`、`SRC-ai-024` 为 fallback HTML，正式投资 memo 前应手工核验。

- **ingest | Scale AI 公司发展史入库**
  - **变更**: 新增 [[ai/research-notes/scale-ai-company-history-2026-06-02|Scale AI 公司发展史]] 和 [[_entities/ScaleAI|Scale AI]] 实体卡；更新 [[ai/research-notes/README|AI Research Notes]]、[[ai/00-index|AI 相关 - 研究入口]]、[[index|Knowledge Index]]。
  - **来源**: 复用 `knowledge/ai/sources.csv` 中 `SRC-ai-001` 至 `SRC-ai-012` 和 `raw/ai/documents/` 来源抽取结果。
  - **待继续**: 正式投资 memo 前仍需对 `SRC-ai-012` Axios 403 失败项和部分 fallback HTML 来源做人工核验。

- **synthesis | 具身智能数据采集和服务公司对比**
  - 新增 [[robotics-embodied-ai/11-embodied-ai-data-service-companies-2026-06-02|具身智能数据采集和服务公司对比]]，覆盖智元、补天石、它石、简智、Maxinsights、自变量、帕西尼的发展历史、解决方案、产品服务、技术路线、岗位信号和优劣势。
  - 更新 [[index|Knowledge Index]] 的 Syntheses 区。
  - 待后续：将本轮 web source 抽取为 `raw/robotics-embodied-ai/documents/SRC-*`，并补充 `sources.csv` 与 source_capture_manifest。

- **concept | Vision-Language-Tactile-Action 术语解释**
  - 新增 [[_concepts/vision-language-tactile-action|Vision-Language-Tactile-Action]] 概念页，解释 VLTA/VTLA 与 VLA 的区别、四个模态和对具身数据公司的含义。
  - 更新 [[robotics-embodied-ai/11-embodied-ai-data-service-companies-2026-06-02|具身智能数据采集和服务公司对比]] 的行业位置与关联连接。
  - 更新 [[index|Knowledge Index]] 的 Concepts 区。

- **migration | UMI 技术术语迁移为 entity 层**
  - 将旧 UMI 技术术语教学页改造为实体索引页。
  - 新建/更新 64 个 `knowledge/_entities/` 术语实体页，覆盖 UMI、夹爪、传感器、位姿/坐标、SLAM、数据格式、模仿学习模型、质检和 ToB 交付物。
  - 更新 [[_entities/README|Entities Layer]] 和 [[index|Knowledge Index]]，登记 UMI 术语实体包与关键实体。
  - 冲突/限制：本次主要基于既有 UMI 研究页和 raw UMI 资料迁移补充；未新增外部检索，后续可按 source-backed 深化每个实体的原论文/官方文档引用。

- **maintenance | UMI 技术术语旧页去链**
  - 将 UMI 业务计划、LeRobot 初学者笔记、实体层 README、全局索引和术语实体页中的旧术语页链接改为对应 entity 链接。
  - 将旧术语页标记为 `deprecated`，后续新笔记应直接链接 [[_entities/UniversalManipulationInterface|UMI]]、[[_entities/IMU|IMU]]、[[_entities/SLAM|SLAM]]、[[_entities/Zarr|Zarr]]、[[_entities/HuggingFaceLeRobot|LeRobot]]、[[_entities/DiffusionPolicy|Diffusion Policy]]、[[_entities/ActionChunkingTransformer|ACT]] 等实体页。

- **maintenance | 删除 UMI 技术术语旧页**
  - 已确认 `knowledge/` 内没有指向旧 slug `10-umi-technical-terms-for-beginners` 的链接。
  - 删除旧页 `knowledge/robotics-embodied-ai/10-umi-technical-terms-for-beginners.md`；UMI 初学者术语入口保留在 [[_entities/README|Entities Layer]]，具体术语直接链接对应 entity。

## [2026-06-04]

- **ingest | 逐际动力 LimX Dynamics 公司调研**
  - **变更**: 新增 [[_entities/LimXDynamics|LimX Dynamics]] 实体页；更新 [[robotics-embodied-ai/04-companies|机器人公司和竞争格局]]、[[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]] 和 [[index|Knowledge Index]]。
  - **来源**: 在 `knowledge/robotics-embodied-ai/sources.csv` 登记 `SRC-robotics-103` 至 `SRC-robotics-113`，覆盖官网、TRON 1/Oli/TRON 2、FluxVLA、A/B 轮融资、行业周报和创始人访谈；抽取到 `raw/robotics-embodied-ai/documents/`。
  - **待继续**: `SRC-robotics-105` TRON 1 用户手册因官网 PDF 证书过期自动下载失败；后续需浏览器手工保存或替换新版下载地址。逐际动力成立时间、主体名称改制、实际出货/收入和 COSA/VGM 可复现材料仍需继续验证。

- **synthesis | 机器人工程平台综合调研**
  - **变更**: 新增 [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]；更新 [[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]] 和 [[index|Knowledge Index]]。
  - **来源**: 在 `knowledge/robotics-embodied-ai/sources.csv` 登记 `SRC-robotics-114` 至 `SRC-robotics-124`，覆盖 NVIDIA Isaac Sim/Lab、OpenPI、OpenVLA、robomimic、LIBERO、ManiSkill、ROS、MoveIt 2、Agibot Genie Studio、EmbodiFlow，并运行来源抽取脚本。
  - **待继续**: `SRC-robotics-120`、`SRC-robotics-122`、`SRC-robotics-123` 为 fallback HTML；正式竞品尽调前需手工补采 ManiSkill、MoveIt 2 和智元 Genie Studio 的页面正文或官方 PDF。

## [2026-06-05]

- **news | NVIDIA Cosmos 3 上手调研**
  - **变更**: 新增 [[news/2026-06-05-nvidia-cosmos-3-getting-started-plan|NVIDIA Cosmos 3 上手调研与计划]]；更新 [[news/00-index|新闻速记]] 和 [[index|Knowledge Index]]。
  - **来源**: 核对 NVIDIA Newsroom、NVIDIA Developer Blog、NVIDIA Research Cosmos Lab、NVIDIA/Cosmos GitHub、Hugging Face Cosmos3 collection/model card、arXiv `2606.02800`。
  - **待继续**: 若进入正式机器人实验，需要补充本地/云端 GPU 型号、显存、CUDA driver、NGC/Hugging Face 权限，并把实际跑通记录转入 [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]] 或新建实验笔记。

## [2026-06-08]

- **ingest | RoboAlign-R1 论文入库**
  - **变更**: 新增 [[_sources/roboalign-r1-reward-aligned-robot-video-world-models|RoboAlign-R1 - Reward-Aligned Robot Video World Models]]；更新 [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]、[[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]]、[[_sources/README|Sources Layer]]、[[index|Knowledge Index]]。
  - **来源**: 在 `knowledge/robotics-embodied-ai/sources.csv` 登记 `SRC-robotics-125` arXiv 主论文和 `SRC-robotics-126` ModelScope/具身智能之心中文解读；PDF、arXiv HTML、ModelScope HTML/Markdown 均保存到 `raw/robotics-embodied-ai/documents/`。
  - **限制**: `defuddle parse` 对 ModelScope 页面失败，原因是页面 metadata 中的 protocol-relative `og:url` 触发 invalid URL；已改用 raw HTML 中的 `window.__detail_data__` 生成 Markdown，并在 raw artifact 记录限制。

- **synthesis | 中国可购买 UMI 夹爪设备检索**
  - **变更**: 新增 [[_syntheses/china-umi-gripper-purchase-scan-2026-06-08|中国可购买 UMI 夹爪设备检索]]；更新 [[_syntheses/README|Syntheses Layer]]、[[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]]、[[index|Knowledge Index]]。
  - **来源**: 在 `knowledge/robotics-embodied-ai/sources.csv` 登记 `SRC-robotics-127` 至 `SRC-robotics-134`，覆盖 AIFITLAB 的 LUMOS FastUMI Pro/Ego/Go 商品页、鹿明 AWE2026 发布、觅蜂 MEgo 量产发货、BeingBeyond U1/RealDexUMI 官方与论文来源；已抽取 8 个 raw Markdown artifact 并更新 source_capture_manifest。
  - **待继续**: 京东正式商品链接、AIFITLAB 中国大陆发票/售后、MEgo Gripper 是否单独出售和各设备 SDK/data license 仍需商务确认。

- **synthesis | 机器人公司产品型号全景对比**
  - **变更**: 新增 [[robotics-embodied-ai/13-robot-company-product-comparison-2026-06-08|机器人公司产品型号全景对比]]；更新 [[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/04-companies|机器人公司与竞争]] 和 [[index|Knowledge Index]]。
  - **范围**: 覆盖 `04-companies` 主表中的机器人整机、协作机器人、工业机器人、AMR/移动操作公司，按通用具身/人形、协作臂/工业机器人、AMR/仓储移动操作三类比较型号、参数、技术路线、优缺点和待验证项；新增 `raw/robotics-embodied-ai/data/robot_company_product_models_2026-06-08.csv` 作为可筛选数据表初版。
  - **待继续**: `SRC-robotics-135` 至 `SRC-robotics-155` 为本轮 web 核验新增来源线索，需后续执行正式 raw capture 并补齐 `source_capture_manifest.csv`；协作臂/工业机器人/AMR 的每个 SKU 还需从产品手册拆成 CSV。

## [2026-06-09]

- **synthesis | 具身智能业务落地 know-how 职业方向思考**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]]，将 Thinking Partner 对话沉淀为 Obsidian research note；更新 [[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]] 和 [[index|Knowledge Index]]。
  - **范围**: 记录职业方向锚点、成功标准、家庭/健康约束、行业结构假设、业务落地 know-how、企业决策者成本/收入/风险痛点、早期反馈标准和零售后场/餐饮后厨/酒店后台等待验证场景。
  - **待继续**: 本页主要基于对话综合，行业与场景判断需继续用客户访谈、招聘 JD、订单/复购证据和 raw source 入库验证。

- **synthesis | 零售后场职业切入点验证分支**
  - **变更**: 更新 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]]，新增“零售后场是否适合作为职业切入点”澄清分支和拓扑图节点。
  - **研究问题**: 中国市场中，按门店/仓库规模排名前 10 的大型零售/电商公司里，是否有超过一半已经启动机器人/具身智能项目，并进入真实门店或仓库运行。
  - **治理更新**: 将 Thinking Partner skill 复制到 `.agents/skills/thinking-partner/`，并新增“每完成一个澄清分支就更新 durable document”的文档化规则。

- **synthesis | 线下零售门店验证口径汇总**
  - **变更**: 合并记录 Thinking Partner 对话中关于零售后场 / 线下零售门店职业切入点的系列口径澄清，并更新 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]]。
  - **澄清结果**: 样本优先用公开行业排名；若门店/仓库规模排名不可得，则用中国零售销售额前 10。项目范围从“零售后场”放宽为“线下零售门店前场/后场”，导购、巡店、清洁、安防、门店内自动化仓库计入；中央仓、区域仓、纯仓配体系不计入。必须有外部具身智能、机器人或通用服务机器人公司参与；公司公告或年报确认合作即可作为早期计入证据，媒体和供应商案例仅作线索。
  - **门槛**: 前 10 公司中有 5 家满足条件，即视为“超过一半”通过；该门槛同时用于判断是否值得继续调研，以及是否值得作为职业切入点投入 6 个月验证。

## [2026-06-10]

- **synthesis | 线下零售门店与跨场景短期落地调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/retail-store-robotics-entry-scan-2026-06-10|线下零售门店机器人合作验证初扫]] 和 [[robotics-embodied-ai/research-notes/cross-scenario-near-term-landing-candidate-pool-2026-06-10|具身智能短期落地跨场景候选池]]；更新 [[robotics-embodied-ai/sources|机器人来源表]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]] 和 [[index|Knowledge Index]]。
  - **零售初扫**: 暂定样本中未找到公司公告/年报级线下门店机器人合作证据，按当前严格口径为 0/10，未达到 5/10 门槛；由于 CCFA 或同等公开排名与逐家公司公告/年报全文尚未补齐，该结果只作为第一轮未通过，不能最终否定。
  - **跨场景候选池**: 场景选择标准从“生活近/场景亲近感”修正为“1 年内真实订单或试点转生产”。全部具身智能/机器人应用场景纳入；客户案例和媒体报道可作为入池最低证据，硬来源用于后续加权。初步入池场景包括汽车制造/工业制造人形机器人、仓储物流/履约中心机器人、酒店/咖啡/商业服务人形机器人、电力设施/数据中心/国企采购型场景、医疗手术机器人。

- **synthesis | 候选池反馈与平台工程师角色收敛**
  - **变更**: 更新 [[robotics-embodied-ai/research-notes/cross-scenario-near-term-landing-candidate-pool-2026-06-10|具身智能短期落地跨场景候选池]] 和 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]]，将决策变量从场景差异转向角色类型。
  - **澄清结果**: 医疗手术机器人因过于硬核，从职业切入候选中降级为“排除 / 仅作行业观察”；其他候选场景当前没有明显区别。下一层优先比较系统工程师、平台工程师、数据处理 / 数据闭环相关角色，其中平台工程师是第一优先验证方向。平台工程师的关键吸引力是：既能迁移已有的软件平台经验，也能逐步获得具身智能全局认知。
  - **取舍规则**: 如果岗位只能强满足一个吸引点，优先选择经验迁移更强；当前路径是先有工作进入行业，再通过真实项目逐步拓展全局认知。
  - **JD 信号**: 强迁移岗位内容包括运营系统开发、后端开发、仿真平台开发；相对边界是离本体控制和“大脑”核心技术稍远一点，因为当前没有嵌入式编程和大模型训练经验，本体控制和大脑核心技术不适合作为第一入口。
  - **学习飞轮**: “先进入行业”的关键价值是接触真实场景和相关人才，从而更快积累行业理解和经验。
  - **时间窗口**: 年龄、行业升温和进入者增多会让未来机会变少、竞争加大，因此需要优先选择能较快入场并快速积累经验的岗位路径。
  - **较快入场标准**: 优先选择把通用软件平台能力作为硬要求、把机器人领域知识作为可补齐能力的岗位；反向信号是把控制算法、运动规划、嵌入式实时系统、强化学习或大模型训练作为硬门槛。
  - **下一步**: 围绕“具身智能/机器人平台工程师”做岗位/JD/公司信号外部调研，优先验证岗位是否能复用平台工程、基础设施、工程效率、数据平台、运营平台、仿真/评测平台等既有经验。

- **research | 平台工程师 JD 快速入场扫描**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/platform-engineer-jd-entry-scan-2026-06-10|具身智能平台工程师 JD 快速入场扫描]] 和 `raw/robotics-embodied-ai/data/platform_engineer_jd_samples_2026-06-10.csv`；更新 [[robotics-embodied-ai/sources|机器人来源表]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/06-career-view|机器人求职与学习视角]] 和 [[index|Knowledge Index]]。
  - **初步结果**: 第一轮样本支持“通用软件平台能力是硬要求、机器人领域知识可补齐”的快速入场标准。优先岗位族群为后端 / 云端 / Fleet / RobotOps 平台、数据管线 / 数据闭环 / 评测平台、仿真平台和运营系统。
  - **限制**: 国内公开可抓取 JD 样本暂以宇树为主，智元等公司需下一轮通过飞书招聘页、猎聘、Boss 直聘或内推渠道补齐具体岗位文本；1X 样本仅作为海外岗位形态参照。

## [2026-06-11]

- **research | LIBERO 终身学习仿真平台调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/libero-lifelong-robot-learning-platform-2026-06-11|LIBERO 终身学习仿真平台调研]]；更新 [[robotics-embodied-ai/sources|机器人来源表]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]] 和 [[index|Knowledge Index]]。
  - **来源**: 复用 `SRC-robotics-119` LIBERO 官方文档；新增 `SRC-robotics-169` 至 `SRC-robotics-173`，覆盖 LIBERO 原论文、GitHub 仓库、LIBERO-PRO、LIBERO-Para 和 2026 年 manipulation benchmark 审计论文。
  - **初步结果**: LIBERO 适合作为 VLA/IL 和终身机器人学习的入门评测平台，可用于平台工程作品集中的 benchmark runner、evaluation service、model adapter 和 robustness harness；但固定 LIBERO 分数不能直接代表真实机器人泛化能力，应与扰动评测、多 benchmark 和真机 rollout 组合使用。

- **research | 开源具身智能训练与评估数据集横向调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/open-embodied-ai-datasets-comparison-2026-06-11|开源具身智能训练与评估数据集横向调研]] 和 `raw/robotics-embodied-ai/data/open_embodied_ai_datasets_comparison_2026-06-11.csv`；更新 [[robotics-embodied-ai/sources|机器人来源表]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]] 和 [[index|Knowledge Index]]。
  - **来源**: 复用已有 OXE、DROID、RoboMIND、AgiBot、RoboTwin、MimicGen、ALOHA/Mobile ALOHA、LeRobot、LIBERO 来源；新增 `SRC-robotics-174` 至 `SRC-robotics-182`，覆盖 BridgeData V2、RH20T、CALVIN、RLBench、Meta-World、ManiSkill3、RoboCasa、RoboTwin 2.0 和 Galaxea Open-World Dataset。
  - **初步结果**: 数据集应按用途分层理解：预训练/跨本体混合、真实机器人微调/后训练、特定能力数据集、仿真与评估 benchmark。格式上研究生态仍偏 RLDS/OXE，工程互通正在向 LeRobot v3 收敛；真实部署能力不能只看 benchmark 分数，必须结合任务完整度、失败/接管标注、元数据和真机 rollout。

- **research | JEPA 核心原理快速调研**
  - **变更**: 新增 [[_concepts/joint-embedding-predictive-architecture|Joint-Embedding Predictive Architecture]] 概念页和 [[ai/research-notes/jepa-core-principles-2026-06-11|JEPA 核心原理快速调研]]；更新 [[_concepts/README|Concepts Layer]]、[[ai/research-notes/README|AI Research Notes]]、[[ai/00-index|AI 相关 - 研究入口]] 和 [[index|Knowledge Index]]。
  - **来源**: 在 `knowledge/ai/sources.csv` 登记 `SRC-ai-025` 至 `SRC-ai-032`，覆盖 LeCun 2022 AMI 位置论文、Meta I-JEPA/V-JEPA/V-JEPA 2 官方说明、I-JEPA/V-JEPA/V-JEPA 2 原论文和 2026 年 LeWorldModel 后续研究。
  - **初步结果**: JEPA 应理解为“在 latent space 预测目标/未来表示”的非生成式自监督世界模型路线；其当前价值主要在高效表征学习、视频物理理解和短程机器人规划信号，长程分层规划和真实世界可靠性仍是未解决问题。

- **research | 集成电路 AI 芯片全球上市公司初筛**
  - **变更**: 更新 [[integrated-circuits/00-index|集成电路研究入口]]、[[integrated-circuits/01-industry-map|产业链地图]]、[[integrated-circuits/02-technology-and-products|技术和产品]]、[[integrated-circuits/03-market-and-policy|市场与政策]]、[[integrated-circuits/04-companies|公司与竞争]]、[[integrated-circuits/05-investment-view|投资视角]]、[[integrated-circuits/06-career-view|求职与学习视角]]；新增 [[integrated-circuits/07-ai-chip-global-supply-chain-and-stock-screen-2026-06-11|AI 芯片全球上市公司、供应链关系与股票初筛]] 和 `raw/integrated-circuits/data/ai_chip_listed_company_universe_2026-06-11.csv`。
  - **范围**: 覆盖 AI GPU/ASIC、HBM、晶圆代工、设备、EDA/IP、先进封装测试、PCB/载板和中国国产替代链。供应链关系仅记录公开财报、公告或公开报道中明确出现的关系；未披露客户不做猜测。
  - **来源**: 在 `knowledge/integrated-circuits/sources.csv` 登记 `SRC-ic-001` 至 `SRC-ic-035`，包含 NVIDIA FY2026 财报、StockAnalysis/CompaniesMarketCap market-cap 页面、TSMC/ASML/AMD/Broadcom/SK hynix/Micron 公开报道和中国公司待补来源占位。
  - **待继续**: A/H/日韩台公司仍需补最新市值、估值、财务指标和年报原文；SIA/WSTS、TSMC transcript、ASML/TEL/Advantest、中国上市公司年报需要转为 raw artifact 并提高证据等级。
  - **2026-06-11 追加**: 在 `ai_chip_listed_company_universe_2026-06-11.csv` 中补充 `pe_ttm`、`forward_pe`、`pe_data_date`、`pe_source`、`pe_notes`。当前 38 家公司中 24 家有 TTM PE，19 家有 forward PE；A/H 股和部分台股公司仍需下一轮用本地行情源补齐。

## [2026-06-23]

- **research | AIRSPEED 具身智能数据生产平台调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/airspeed-data-production-platform-2026-06-23|AIRSPEED 具身智能数据生产平台调研]]、[[_sources/airspeed-open-source-data-production-platform|AIRSPEED 来源组]]、[[_entities/AIRSPEED|AIRSPEED]]；更新 [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]、[[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]]、[[_sources/README|Sources Layer]]、[[_entities/README|Entities Layer]] 和 [[index|Knowledge Index]]。
  - **来源**: 在 `knowledge/robotics-embodied-ai/sources.csv` 登记 `SRC-robotics-183` 至 `SRC-robotics-188`，覆盖 AIRSPEED 官网、技术报告、EAI 数据工程综述、英文/中文技术转移报告和 GitHub README；保存 HTML/PDF/README raw artifact，并为 PDF 生成 `pdftotext` sidecar，更新 `source_capture_manifest.csv`。
  - **初步结果**: AIRSPEED 应分版本理解：当前 GitHub v1.3 可复用能力偏 ROS2/YAML/HDF5/LeRobot 转换的数据采集核心；官网/论文/技术转移报告描述的完整平台覆盖数据采集、仿真生成和数据集构建。商业化报告中的客户、融资、标准参与等 claim 暂标记为待独立验证。
  - **待继续**: clone 仓库做代码级验证，核验 license、release、converter、ROS2 mock 采集、LeRobot v3 导出；独立验证技术转移报告中的客户、融资和标准化 claim。

- **research | dora 1.0 vs ROS 2 调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/dora-1-vs-ros2-2026-06-23|dora 1.0 vs ROS 2 调研]]；更新 [[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]、[[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]] 和 [[index|Knowledge Index]]。
  - **来源**: 在 `knowledge/robotics-embodied-ai/sources.csv` 登记 `SRC-robotics-189` 至 `SRC-robotics-199`，覆盖 dora 官网、GitHub README、PyPI、GitHub v0.5.0 release、DORA 论文、dora benchmark、ROS 2 release/nodes/QoS 官方文档和 ROS 2 综述论文；已生成 raw artifacts 并更新 `raw/robotics-embodied-ai/documents/source_capture_manifest.csv`。
  - **初步结果**: dora 更适合作为高带宽 AI dataflow runtime，与 ROS 2 bridge 组合承担 perception/VLA/inference、record/replay 和 observability；ROS 2 仍更适合作为真实机器人硬件、驱动、控制、规划和生态底座。
  - **限制**: dora 官网称 `1.0.0-rc1`，但 PyPI/GitHub 稳定版本为 `0.5.0`，本文将“dora 1.0”按官网/RC 能力主张处理；`SRC-robotics-190` dora guides 自动抽取失败，需后续通过官网 `/book`、GitHub raw docs 或浏览器手工补采。

## [2026-06-29]

- **research | LiDAR 世界模型训练论文与方案调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/lidar-world-model-training-2026-06-29|激光雷达数据融合进入世界模型训练论文与方案调研]]；更新 [[_entities/LiDAR|LiDAR 激光雷达]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]] 和 [[index|Knowledge Index]]。
  - **来源**: 在 `knowledge/robotics-embodied-ai/sources.csv` 登记 `SRC-robotics-200` 至 `SRC-robotics-217`，覆盖 Sense, Imagine, Act、MUVO、Copilot4D、OccWorld、LidarDM、OccSora、BEVWorld、Drive-OccWorld、DFIT-OccWorld、OccLLaMA、AD-L-JEPA、RoboOccWorld、LiSTAR、LiDAR navigation DreamerV3、AD-LiST-JEPA、HERMES++、GEM 和 UniDriveDreamer；已生成 raw artifacts 并更新 `raw/robotics-embodied-ai/documents/source_capture_manifest.csv`。
  - **初步结果**: LiDAR 融入 world model 训练的主流方案分为 LiDAR-native generative model、BEV/occupancy world model、camera-LiDAR unified latent、JEPA latent predictive model 和移动机器人 Dreamer 类导航模型；若目标是规划安全，BEV/occupancy 路线优先；若目标是数据合成，LiDAR-native 路线优先。
  - **限制**: 本轮主要抓取 arXiv 摘要页作为 raw artifact，尚未下载 PDF 或做代码级复现；`SRC-robotics-210` 为 HTML fallback。下一轮应为重点论文建立 `knowledge/_sources/` source card，并补 PDF/key-info 级证据。

- **ingest | 七个行业初步调研补齐**
  - **变更**: 补齐 [[6g/00-index|6G]]、[[aerospace/00-index|航空航天]]、[[biopharma/00-index|生物医药]]、[[brain-computer-interface/00-index|脑机接口]]、[[future-energy/00-index|未来能源]]、[[low-altitude-economy/00-index|低空经济]]、[[quantum-technology/00-index|量子科技]] 的标准初调页、sources.csv、source capture index 和 raw source notes。
  - **来源**: 以 `十四五规划纲要`、`2024年政府工作报告`、`未来产业实施意见` 为共同政策底座，并为 6G、航空航天、生物医药、脑机接口、未来能源、低空经济、量子科技分别登记行业专属来源。
  - **限制**: 本轮 raw artifact 多为 analyst source note，适合做初步 traceability；高价值政策、PDF、年报和标准仍需后续运行完整网页/PDF 抽取并拆成 source card / claim。

- **ingest | AI 总行业分析重做**
  - **变更**: 重写 [[ai/00-index|AI 研究入口]]、[[ai/01-industry-map|产业链地图]]、[[ai/02-technology-and-products|技术与产品]]、[[ai/03-market-and-policy|市场与政策]]、[[ai/04-companies|公司与竞争]]、[[ai/05-investment-view|投资视角]]、[[ai/06-career-view|求职与学习视角]]；更新 [[ai/00-source-capture-index|AI Source Capture Index]] 和 [[ai/research-notes/README|AI Research Notes]]。
  - **来源**: 追加 `SRC-ai-033` 至 `SRC-ai-046`，覆盖十四五规划、新一代人工智能发展规划、2024 年政府工作报告、生成式人工智能服务管理暂行办法、未来产业实施意见、DeepSeek、Qwen、文心一言、Kimi、智谱、腾讯混元、华为昇腾、寒武纪和 ModelScope。
  - **初步结果**: AI 行业不再只按 Scale AI / 数据基础设施理解，而改为“算力与基础设施 - 基础模型 - 数据与评测 - 应用/Agent - 安全合规”的总产业链框架；投资与职业页分别强调国产算力、AI 平台、应用 ROI、数据评测和安全合规。
  - **限制**: 本轮新增来源为 analyst source note，模型备案清单、公司财报、API 收入、国产算力订单、企业续费率和地方 AI 政策仍需下一轮补硬证据。

- **research | 具身智能训练数据价值评估框架**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/robot-training-data-value-evaluation-2026-06-29|具身智能训练数据价值评估框架]]；更新 [[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]] 和 [[index|Knowledge Index]]。
  - **来源**: 复用 LeRobot、DROID、RoboMIND、AgiBot World、Data Scaling Laws、失败/接管数据、AIRSPEED 与 EAI data engineering survey 等已有来源；并以 2026-06-29 在线核验的 arXiv/官方页面作为当前性补充。
  - **初步结果**: 数据价值不应按小时数或 episode 数单独估算，而应按 `Expected Capability Lift x Reuse Multiplier x Trust Multiplier / Fully Loaded Cost and Risk` 判断；采集前做任务缺口和数据组合打分，采集中做同步/标定/分布/QC stop-loss，采后用 holdout rollout 或 ablation 验证边际提升。

## [2026-07-02]

- **ingest | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-02|Bilibili AI Daily Run 2026-07-02]]；处理 1 个 Bilibili 视频 source packet。
  - **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
  - **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

- **synthesis | MATLAB/Simulink Agentic AI 工具链视频调研**
  - **变更**: 新增 [[_syntheses/matlab-simulink-agentic-ai-tools-bilibili-2026-07-02|MATLAB/Simulink Agentic AI 工具链视频调研]]；更新 [[index|Knowledge Index]]。
  - **来源**: 复用 [[_sources/bilibili-bv1bbtv6ueaf-5-skill-codex-matlab|Bilibili source card]] 与 raw transcript，并核验 MathWorks 官方 `matlab` GitHub 组织、`matlab-mcp-server`、`matlab-agentic-toolkit`、`simulink-agentic-toolkit`、`agent-skills-playground`。
  - **初步结果**: 工程软件 Agent 化需要 MCP/API 工具层、领域 skills 和仿真/测试反馈闭环；MATLAB/Simulink 是较早成体系的样板，后续应扫描国产工业软件的 agent-ready 能力。

- **synthesis | Bilibili 具身智能与 AI 工具链线索**
  - **变更**: 新增 [[_syntheses/bilibili-embodied-ai-signals-2026-07-02|Bilibili 具身智能与 AI 工具链线索 2026-07-02]]；更新 [[index|Knowledge Index]]、[[robotics-embodied-ai/sources|机器人来源表]] 和 [[ai/sources|AI 来源表]]。
  - **来源**: 使用每日 Bilibili 自动化中断前成功落盘的 source cards 与 raw transcripts，覆盖 ZR-0/VLA、VLA 数据基建、GENIE SIM、TensorRT、ROS2/LiDAR、LeWorldModel、机械臂安全和 ForceBand。
  - **限制**: Bilibili 视频仅作为 B 级线索；`BV1ogTT6PE2s` transcript 无有效正文，不纳入观点抽取；ZR-0、ForceBand、GENIE SIM 和安全规范相关 claim 需要一级来源验证。

- **automation | Bilibili AI/具身智能每日增量重跑**
  - **变更**: 更新 [[_syntheses/bilibili-ai-daily-run-2026-07-02|Bilibili AI Daily Run 2026-07-02]]、[[_syntheses/bilibili-embodied-ai-signals-2026-07-02|Bilibili 具身智能与 AI 工具链线索 2026-07-02]]、[[index|Knowledge Index]] 和 [[robotics-embodied-ai/sources|机器人来源表]]；新增 3 个 Bilibili source cards 与 raw transcripts。
  - **来源**: 新增 `BV1oPTq6SENP` 家庭人形机器人访谈、`BV1wCTu6nEF2` GENIE SIM 3.0 闭环仿真上篇、`BV1cL7p6VEH9` VLA 入门教程；均为 B 级视频线索，需一级来源交叉验证。
  - **失败**: 选中的 `BV1bGxEz7EWa`、`BV1UR7H6dEy5`、`BV1v17Y6aE2L`、`BV161jy6MEwt` 无可用平台字幕；`BV1UR7H6dEy5` 外部 Volcengine ASR 在 300 秒超时，最终用禁用 ASR 的重跑记录为失败。
  - **限制**: 本轮第一批默认 ASR 超时路径需人工中断；脚本当前未捕获 `subprocess.TimeoutExpired`，后续可修复为 per-video failed result，避免整批退出。

## [2026-07-03]

- **research | 具身大模型物理理解评估框架**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/embodied-model-physical-understanding-evaluation-2026-07-03|具身智能大模型物理理解能力评估框架]]；更新 [[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]] 和 [[index|Knowledge Index]]。
  - **来源**: 复用 [[_sources/roboalign-r1-reward-aligned-robot-video-world-models|RoboAlign-R1]]、[[news/2026-06-05-nvidia-cosmos-3-getting-started-plan|NVIDIA Cosmos 3 上手调研]]、[[ai/research-notes/jepa-core-principles-2026-06-11|JEPA 核心原理快速调研]]；新增 `SRC-robotics-218` 至 `SRC-robotics-223`，覆盖 RT-2、OpenVLA、Meta V-JEPA 2、Gemini Robotics、EWMBench 和 World Action Models。
  - **初步结果**: 判断具身大模型是否理解物理规律，应从 `observation + instruction -> action` 的动作生成评估，升级为 `state + candidate action -> future state / outcome / risk` 的动作条件预测与闭环规划收益评估；核心方法包括反事实预测、minimal physical pairs、forward/inverse dynamics、policy-only vs world-model-assisted A/B 和多模态接触/空间约束。
  - **限制**: 本轮为 query-style 框架调研，新增外部来源已登记但尚未执行 raw artifact 抽取；若进入正式 benchmark 复现或公司尽调，应补采 PDF/HTML、建立 source card，并对 judge/reward model 做人评和真机交叉验证。

- **ingest | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-03|Bilibili AI Daily Run 2026-07-03]]；处理 7 个 Bilibili 视频 source packet。
  - **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
  - **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

- **synthesis | Bilibili AI 与具身智能线索**
  - **变更**: 新增 [[_syntheses/bilibili-ai-embodied-signals-2026-07-03|Bilibili AI 与具身智能线索 2026-07-03]]；更新 [[index|Knowledge Index]] 中 7 个 Bilibili source packet 的 synthesis 指向。
  - **来源**: 只使用 2026-07-03 每日自动化中 `status=processed` 的 7 个 source cards 与 raw transcripts，覆盖 PhysisForcing、家用人形机器人产品定义、GENIE SIM 3.0 上篇、VLA 入门、SLAM/ROS、数值优化和 ESP Cloud/ESP32。
  - **限制**: `BV1bGxEz7EWa` 为 failed，不纳入综合；PhysisForcing 指标、GENIE SIM 能力、ESP Cloud 项目边界、家用机器人关节参数和市场判断均需一级来源验证。

- **synthesis | Bilibili 单视频深度调研产物修正**
  - **变更**: 新增 [[_syntheses/bilibili-physisforcing-world-simulator-deep-dive-2026-07-03|PhysisForcing 物理一致世界模拟器视频深度调研]] 和 [[_syntheses/bilibili-esp-claw-embedded-ai-deep-dive-2026-07-03|ESP-Claw 自然语言驱动嵌入式开发视频深度调研]]；更新 [[_syntheses/bilibili-ai-daily-run-2026-07-03|Bilibili AI Daily Run 2026-07-03]]、[[_syntheses/bilibili-ai-embodied-signals-2026-07-03|Bilibili AI 与具身智能线索 2026-07-03]]、[[index|Knowledge Index]]、[[ai/sources|AI 来源表]] 和 [[robotics-embodied-ai/sources|机器人来源表]]。
  - **来源**: 用 arXiv `2606.28128` 校验 PhysisForcing 视频 claim；用乐鑫 ESP-Claw 官网、文档、GitHub、ESP32-S3 与 ESP-IDF 官方资料校验 `BV1PCjA6bEi4` 中的 ESP Cloud/Club 线索，并统一项目名为 ESP-Claw。
  - **规范修正**: 每日 Bilibili 自动化未来应以“每个 selected + processed 视频一篇独立深研页”为主要产物，横向综述只作为导航/交叉线索，不替代单视频深研。

## [2026-07-04]

- **ingest | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-04|Bilibili AI Daily Run 2026-07-04]]；处理 1 个 Bilibili 视频 source packet。
  - **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
  - **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

- **synthesis | Agent 时代 GUI 与 Headless 软件视频深研**
  - **变更**: 新增 [[_syntheses/bilibili-agent-gui-headless-software-deep-dive-2026-07-04|Agent 时代 GUI 与 Headless 软件视频深度调研]]；更新 [[_sources/bilibili-bv1bktk69edd-agent-500-gui|Bilibili source card]] 和 [[index|Knowledge Index]]。
  - **来源**: 使用 `BV1bKTk69EDD` source card 与 raw transcript，并用 MCP、Claude Code overview、Claude Code skills、Vercel AI SDK 官方文档交叉验证 Agent-ready 软件接口、skills 和工具调用趋势。
  - **初步结果**: GUI 不应被简单否定；AI 应用的关键分层正在变成 human UI、agent interface 和 workflow assets。投资/职业判断应同时评估界面信任层、工具接口、上下文资产、权限审计和 skill/workflow 复用能力。
  - **限制**: 视频中关于飞书、Google Workspace、Supabase、MongoDB、瑞幸、KFC、微信等具体产品开放 CLI/MCP 的说法尚未逐项核验，暂作为访谈观点和后续验证任务。

## [2026-07-05]

- **ingest | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-05|Bilibili AI Daily Run 2026-07-05]]；处理 3 个 Bilibili 视频 source packet。
  - **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
  - **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

- **synthesis | Bilibili 单视频深研三篇**
  - **变更**: 新增 [[_syntheses/bilibili-hapmorph-haptic-feedback-deep-dive-2026-07-05|HapMorph 触觉反馈视频深度调研]]、[[_syntheses/bilibili-physical-ai-time-scale-deep-dive-2026-07-05|Physical AI 时间尺度视频深度调研]] 和 [[_syntheses/bilibili-vla-tutorial-deep-dive-2026-07-05|VLA 入门教程视频深度调研]]；更新 [[_syntheses/bilibili-ai-daily-run-2026-07-05|Bilibili AI Daily Run 2026-07-05]]、[[index|Knowledge Index]]、[[robotics-embodied-ai/sources|机器人来源表]] 和机器人来源抽取 manifest。
  - **来源**: 只综合本次自动化中 `status=processed` 的 `BV12XTM6sEGF`、`BV1y3T46NEUf`、`BV1ifTp62EaV`；用 arXiv `2509.05433` / `SRC-robotics-233` 校验 HapMorph 触觉反馈关键指标，并复用既有 VLA、数据集、评测和工程平台来源。
  - **初步结果**: 触觉反馈的关键问题是多属性反馈、人类可辨识与任务闭环价值；Physical AI 需要按多时间尺度系统理解；VLA 学习应从模型扩展到数据 schema、benchmark、真机部署和失败回流。
  - **限制**: Bilibili 仍为 B 级线索；GelSight、DIGIT 360、RT-1、RT-2、RoboFlamingo、MDT、RDT、LAPA 等模型/硬件名需要后续补独立 source card 后再推广为事实。

## [2026-07-06]

- **research | 家庭养老机器人公司与方案调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/home-elderly-care-robots-2026-07-06|家庭养老机器人公司与方案调研]]；更新 [[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]] 和 [[index|Knowledge Index]]。
  - **来源**: 复用中国人口老龄化、`机器人+`、北京/上海医疗康养和家庭场景政策来源；在线核验 ElliQ、Hyodol、Joy for All、LOVOT、Labrador、傅利叶、1X、Figure 和 Tesla 官方页面，并用 arXiv `2410.12205`、`2302.12686` 补充老年人采用偏好研究。Weave Isaac 与优必选 UWorld U1 仅作为媒体线索列入待验证。
  - **初步结果**: 家庭养老机器人应分为陪伴提醒、远程巡视、移动载物、康复护理和通用家务五层；2026 年更可行的是“AI 照护终端 + 家属 App + IoT + 社区/护理服务”闭环，而不是直接售卖昂贵全能人形机器人。
  - **限制**: 本轮未系统抓取中国地方养老机器人招投标、真实家庭部署数量、价格带和留存数据；国内智能家居/IoT 厂商在养老闭环中的角色需下一轮补公司级来源。

- **research | 中国养老行业头部公司与科技创新创业公司**
  - **变更**: 新建 `eldercare` 行业工作区；新增 [[eldercare/00-index|养老服务与银发科技研究入口]] 和 [[eldercare/04-companies|中国养老行业头部公司与科技创新创业公司]]；更新 [[index|Knowledge Index]]、[[README|Knowledge README]] 和 `tools/industry_registry.json`。
  - **来源**: 复用国家统计局 2025 年公报；核验泰康之家、椿萱茂、安康通、金牌护士、亲和源、万物云官网；补充 arXiv 中国社区养老科技研究和毫米波人体感知综述；复用前序家庭养老机器人调研。
  - **初步结果**: 养老行业头部应按保险系医养社区、连锁养老运营、居家/社区/机构服务、智慧养老平台、互联网护理和智能硬件分层看；科技创新的近期重点在长护险履约、上门护理、智慧养老指挥中心、无感监测、社区空间科技和康复/护理机器人。
  - **限制**: 太保家园、国寿嘉园、大家的家、梧桐人家、九如城、光大养老、福寿康、青松康护、小柏家护等头部候选仍需下一轮补官方项目、床位、城市、收入或招投标证据；本轮不做硬排名。

- **automation | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-07-06|Bilibili AI Daily Run 2026-07-06]]；更新 [[index|Knowledge Index]]。
  - **来源**: 运行 `uv run python tools/bilibili_ai_daily_research.py --limit 20 --json` 获取默认收藏夹最新 20 个候选。
  - **结果**: 20 个候选全部为 `skipped_duplicate`；`needs_model_review=0`、模型选中 0、`processed=0`、`failed=0`，因此未进入第二阶段、未新增 transcript、source card 或单视频深研页。
  - **限制**: 本轮没有新视频内容可综合；后续运行继续只处理 selected + processed 视频。

- **synthesis | VLA&世界模型数据基建平台系统设计**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/vla-world-model-data-infrastructure-platform-design-2026-07-06|VLA&世界模型数据基建平台系统调研与设计]]；更新 [[index|Knowledge Index]]。
  - **来源**: 以 [[_sources/bilibili-bv1zftq6pea3-vla|BV1ZFTq6pEA3 source card]] 和 `raw/_inbox/transcripts/2026-07-02-bilibili-bv1zftq6pea3-vla.json` 的 15 阶段 SOP 为主线，复用 [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]、[[robotics-embodied-ai/research-notes/airspeed-data-production-platform-2026-06-23|AIRSPEED 调研]]、[[robotics-embodied-ai/research-notes/robot-training-data-value-evaluation-2026-06-29|训练数据价值评估框架]]、[[robotics-embodied-ai/research-notes/open-embodied-ai-datasets-comparison-2026-06-11|开源具身数据集对比]] 和 [[robotics-embodied-ai/research-notes/dora-1-vs-ros2-2026-06-23|dora vs ROS 2]]。
  - **初步结果**: 平台应定位为具身智能数据生产操作系统，核心对象是 episode 和数据飞轮；MVP 应优先做任务契约、采集接入、同步缓存、自动质检、episode builder、多格式导出、dataset registry、baseline 评测和失败补采闭环。
  - **限制**: Bilibili 视频仍为 B 级线索；具体性能、成本、QC 阈值、dora/AIRSPEED 复用程度和真实客户 ROI 需要用小规模实采和代码级复现继续验证。

- **governance | 行业完整调研文档存放规则修正**
  - **变更**: 将 [[robotics-embodied-ai/research-notes/vla-world-model-data-infrastructure-platform-design-2026-07-06|VLA&世界模型数据基建平台系统调研与设计]] 放入机器人行业 `research-notes/`；更新 [[index|Knowledge Index]]、[[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]] 和 `AGENTS.md`。
  - **规则**: 后续完整行业调研文档应写入对应 `knowledge/<industry>/research-notes/`，而不是默认放入 `knowledge/_syntheses/`；`_syntheses/` 主要用于跨行业综合、迁移计划或无明确产业归属的高价值输出。

## [2026-07-07]

- **ingest | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-07|Bilibili AI Daily Run 2026-07-07]]；处理 5 个 Bilibili 视频 source packet。
  - **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
  - **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

- **synthesis | Bilibili 单视频深研五篇**
  - **变更**: 新增 [[_syntheses/bilibili-physical-ai-productivity-revolution-deep-dive-2026-07-07|Physical AI 生产力革命播客视频深度调研]]、[[_syntheses/bilibili-isaac-sim-tutorial-deep-dive-2026-07-07|Isaac Sim 教程视频深度调研]]、[[_syntheses/bilibili-multiview-embodied-perception-deep-dive-2026-07-07|多目具身感知视频深度调研]]、[[_syntheses/bilibili-do-as-i-do-dexterous-video-data-deep-dive-2026-07-07|Do As I Do 灵巧操作视频数据深度调研]] 和 [[_syntheses/bilibili-abot-m05-world-action-model-deep-dive-2026-07-07|ABot-M0.5 世界动作模型视频深度调研]]；更新 [[_syntheses/bilibili-ai-daily-run-2026-07-07|Bilibili AI Daily Run 2026-07-07]]、[[index|Knowledge Index]]、AI/机器人 sources.csv、source cards 和 source capture manifest。
  - **来源**: 只综合本次自动化中 `status=processed` 的 `BV17eTk6vETX`、`BV1G8kBBvEzR`、`BV1j9jd6aE7c`、`BV1WfTk6EEZ8`、`BV1F7Ts6WEYj`；用 NVIDIA Isaac Sim/Isaac Lab 官方文档、arXiv `2606.19333` 和 arXiv `2607.00678` 交叉验证关键技术事实。
  - **初步结果**: Physical AI 需要按系统工程和产业链分层理解；Isaac Sim 的价值在多传感器仿真、ROS2、synthetic data 和 RL 工具链；多目感知选型应匹配任务和模型目标；Do As I Do 强调观察性视频到机器人轨迹需要严格筛选和重定向；ABot-M0.5 把移动操作 WAM 的瓶颈明确为时间粒度、动作空间和训练/推理条件三层错配。
  - **限制**: Bilibili 仍为 B 级线索；摩尔线程 Lambda 平台、高德/AMAP 后续产品化、ABot 代码开放状态、多目设备真实 BOM 和工厂采集 ROI 仍需一级来源或实测验证。

## [2026-07-08]

- **automation | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-07-08|Bilibili AI Daily Run 2026-07-08]]；更新 [[index|Knowledge Index]]。
  - **来源**: 运行 `uv run python tools/bilibili_ai_daily_research.py --limit 20 --json` 获取默认收藏夹最新 20 个候选。
  - **结果**: 20 个候选全部为 `skipped_duplicate`；`needs_model_review=0`、模型选中 0、`processed=0`、`failed=0`，因此未进入第二阶段、未新增 transcript、source card 或单视频深研页。
  - **限制**: 本轮没有新视频内容可综合；后续运行继续只处理 selected + processed 视频。

- **automation | Bilibili AI/具身智能每日视频采集补跑**
  - **变更**: 更新 [[_syntheses/bilibili-ai-daily-run-2026-07-08|Bilibili AI Daily Run 2026-07-08]]，新增 [[_sources/bilibili-bv1mgja6cebk-200|千寻智能 Bilibili source card]] 和 [[_syntheses/bilibili-qianxun-intelligence-deep-dive-2026-07-08|千寻智能具身智能公司视频深度调研]]；补充 `knowledge/ai/sources.csv` 与 `knowledge/robotics-embodied-ai/sources.csv`。
  - **来源**: 第一阶段候选池 20 个，模型选中 `BV1mgja6CEbK`、`BV1q3TE6AE4b`、`BV1Z7jA6LE8s`；其中仅 `BV1mgja6CEbK` 生成 `raw/_inbox/transcripts/2026-07-08-bilibili-bv1mgja6cebk-200.json` 和 source card。
  - **限制**: `BV1q3TE6AE4b` 与 `BV1Z7jA6LE8s` 外部 ASR subprocess 长时间不返回，已中断，未写 source card 或单视频深研页；`BV1mgja6CEbK` 的公司估值、营收、客户、数据规模、Spirit VLA 和政策 claim 均为 B 级线索，需一级来源验证。

- **tooling | Bilibili ASR/TOS 上传诊断优化**
  - **变更**: 更新 `tools/bilibili_ai_daily_research.py`、`tools/volcengine_asr.py`、`tools/tos_upload.py` 和 `docs/bilibili_daily_research_automation.md`，为每日 Bilibili 自动化增加 TOS 今日目录检查、上传后 URL 可达性验证、上传失败重试和外部 ASR 进程组超时清理。
  - **原因**: 今日补跑中 `BV1q3TE6AE4b` 与 `BV1Z7jA6LE8s` 卡在 external ASR，人工检查 TOS 今日目录只有一个音频文件，说明失败视频可能未成功上传且主脚本缺少明确上传失败反馈。
  - **验证**: `uv run python -m unittest tests.test_volcengine_asr tests.test_bilibili_ai_daily_research tests.test_tos_upload` 通过。

- **governance | Bilibili 失败 case 自主排查规则**
  - **变更**: 更新 `docs/bilibili_daily_research_automation.md`，新增 `Failed Case Handling And Self-Repair` 规则，要求每日任务对 selected 视频的失败 case 自主定位失败边界、保留证据、bounded retry、能修则修并补测试，只有外部状态不可控时才作为人工 blocker 报告。
  - **约束**: 失败视频仍不得伪造 transcript、source card 或单视频深研页；只有 `status=processed` 才进入 durable synthesis。

- **ingest | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-08|Bilibili AI Daily Run 2026-07-08]]；处理 2 个 Bilibili 视频 source packet。
  - **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
  - **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

- **tooling | Bilibili 失败 case 补跑修复**
  - **变更**: 修复 `tools/bilibili_ai_daily_research.py` 的 dry-run JSON report path 问题、失败日志误触发重复检测问题、TOS 列目录候选检查 runner；修复 `tools/tos_upload.py` 的 SDK list-prefix 路径；同步更新 `docs/bilibili_daily_research_automation.md` 的 TOS 检查命令。
  - **原因**: `BV1q3TE6AE4b` 与 `BV1Z7jA6LE8s` 初始重试被 `knowledge/log.md` 中的失败记录误判为 `skipped_duplicate`；TOS 前缀检查落到 S3-compatible fallback signer 时返回 `Unsupported Authorization Type`。
  - **验证**: 两个 BV 的 dry-run 均恢复为 `selected` 且 TOS 今日前缀检查返回 3 个对象、无错误；`uv run python -m unittest tests.test_volcengine_asr tests.test_bilibili_ai_daily_research tests.test_tos_upload` 通过 33 个测试。

- **synthesis | Bilibili 失败 case 单视频深研补齐**
  - **变更**: 新增 [[_syntheses/bilibili-boden-intelligence-data-infrastructure-deep-dive-2026-07-08|博登智能 Physical AI 数据基建视频深度调研]] 和 [[_syntheses/bilibili-qianxun-intelligence-bv1z7-deep-dive-2026-07-08|千寻智能 BV1Z7jA6LE8s 视频深度调研]]；更新 [[_syntheses/bilibili-ai-daily-run-2026-07-08|Bilibili AI Daily Run 2026-07-08]]、[[index|Knowledge Index]]、AI/机器人 sources.csv。
  - **来源**: 只综合本次补跑中 `status=processed` 的 `BV1q3TE6AE4b` 和 `BV1Z7jA6LE8s`；复用 OpenVLA、Open X-Embodiment、NVIDIA GR00T N1 等一级技术来源验证“真实机器人数据 + VLA/动作模型”的行业逻辑。
  - **初步结果**: 博登智能视频提供“真实场景网络 + 数据引擎 + 验证体系”的具身数据基建线索；千寻智能 `BV1Z7jA6LE8s` 独立页补充融资、团队、墨子一硬件、Spirit VLA 和客户落地线索。
  - **限制**: 两条视频中的公司估值、融资、客户、营收、数据规模、机器人数量、模型指标和订单均未找到足够一级来源支撑，全部保留为 `待验证`。

- **synthesis | 博登智能商业与技术综述**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/boden-intelligence-business-technology-overview-2026-07-08|博登智能商业逻辑、商业计划与技术方案综述]]；更新 [[index|Knowledge Index]]、[[robotics-embodied-ai/00-index|机器人研究入口]] 和 [[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]。
  - **来源**: 基于 [[_syntheses/bilibili-boden-intelligence-data-infrastructure-deep-dive-2026-07-08|博登智能 Physical AI 数据基建视频深度调研]]、[[_sources/bilibili-bv1q3te6ae4b-10-ai|BV1q3TE6AE4b source card]] 和 `raw/_inbox/transcripts/2026-07-08-bilibili-bv1q3te6ae4b-10-ai.json`，并复用 [[robotics-embodied-ai/research-notes/vla-world-model-data-infrastructure-platform-design-2026-07-06|VLA&世界模型数据基建平台系统调研与设计]] 的 episode-first 数据平台框架。
  - **初步结果**: 将博登智能叙事整理为“自动化标注现金流 + 真实场景训练基地 + 跨本体数据采集 + 数据资产治理 + 现实验证闭环”的 Physical AI 数据工厂商业计划，并拆解 BASE、BreakRobot、Blink、BIBOT 四类产品角色。
  - **限制**: 本文仍不新增一级来源验证；公司主体、产品名、融资、客户、基地规模、产能、数据交易和订单 claim 均保持 `待验证`。

## [2026-07-09]

- **automation | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-07-09|Bilibili AI Daily Run 2026-07-09]]；更新 [[index|Knowledge Index]]。
  - **来源**: 运行 `uv run python tools/bilibili_ai_daily_research.py --limit 20 --json` 获取默认收藏夹最新 20 个候选。
  - **结果**: 20 个候选全部为 `skipped_duplicate`；`needs_model_review=0`、模型选中 0、`processed=0`、`failed=0`，因此未进入第二阶段、未新增 transcript、source card 或单视频深研页。
  - **限制**: 本轮没有新视频内容可综合；后续运行继续只处理 selected + processed 视频。

- **synthesis | 遥操训练数据成本与占比调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/teleoperation-training-data-cost-and-share-2026-07-09|遥操训练数据每小时成本与训练数据占比快速调研]]；更新 [[index|Knowledge Index]]、[[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]] 和 `knowledge/robotics-embodied-ai/sources.csv`。
  - **来源**: 复用 DROID、RoboMIND、AgiBot World、Open X-Embodiment、pi0、Mobile ALOHA 等既有 raw source，并补充 Washington Post、The Verge、Business Insider、RoboTurk、COBALT 等公开资料。
  - **初步结果**: 成本应按“有效可训练小时”而非操作者工时核算；人类视频直接成本低，机器人原生遥操数据因占用设备、场地、工程和 QC，通常是人工单价的数倍到十几倍；在机器人 action 轨迹数据中遥操占比常为 `80-100%`，但在包含 VLM 预训练、视频、仿真和合成数据的 foundation model 总混合中占比低且未公开。
  - **限制**: 中国国内供应商报价、遥操员薪资和头部公司真实训练混合比例仍缺少一手证据，需后续用 JD、报价单和访谈补证。

- **synthesis | 具身智能训练数据小时数需求调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/embodied-ai-training-data-hour-requirements-2026-07-09|具身智能训练数据需求量与小时数分层估算]]；更新 [[index|Knowledge Index]]、[[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]] 和 `knowledge/robotics-embodied-ai/sources.csv`。
  - **来源**: 复用 DROID、Octo、AgiBot World、pi0、Data Scaling Laws 等既有来源，并补充 RT-1、LingBot-VLA 2.0、Green-VLA、HumanEgo、ACE-Ego-0 和 Business Insider 等公开资料。
  - **初步结果**: demo 级可从 `0.5-5h` 起步，单任务有限泛化通常 `5-50h`，客户场景产品化通常 `50-500h`，跨任务/跨本体策略模型进入 `500-5,000h+`，前沿 VLA/foundation model 已公开到 `10,000-60,000h+` 混合数据量级。
  - **限制**: 小时数必须区分有效可训练小时、robot action hours、人类视频小时和 raw footage；国内头部公司真实训练 mix、QC 通过率和有效小时仍需供应商报价、JD 和访谈补证。

- **update | 遥操成本笔记补充数据需求与运维长尾价值**
  - **变更**: 将具身智能训练数据需求小时数分层估算合并进 [[robotics-embodied-ai/research-notes/teleoperation-training-data-cost-and-share-2026-07-09|遥操训练数据每小时成本与训练数据占比快速调研]]，并新增“运维场景采集 80% 长尾遥操数据”的市场价值测算；补充 `knowledge/robotics-embodied-ai/sources.csv`。
  - **来源**: 复用上一轮训练数据小时数来源，并补充 Business Insider / Instawork robotics training data 报道作为运维人员与现场数据网络线索。
  - **初步结果**: 若运维平台能在真实部署中捕获 `80%` 的异常、接管、失败恢复和现场扰动数据，试点阶段可能对应 `千万元级` 数据资产价值，万台级部署后可能形成 `亿元级` 年收入机会，十万台级且授权清晰时才有 `十亿元级` 数据飞轮想象空间。
  - **限制**: 该测算是替代采集成本和可收入化比例模型，不是已验证市场规模；前提是存在真实活跃部署、清晰数据授权和可量化的模型成功率/人工值守成本改善。

- **update | 1 亿小时具身基座模型数据 TAM 测算**
  - **变更**: 在 [[robotics-embodied-ai/research-notes/teleoperation-training-data-cost-and-share-2026-07-09|遥操训练数据每小时成本与训练数据占比快速调研]] 中新增“1 亿小时 AGI 级具身基座模型数据 TAM”章节。
  - **初步结果**: 若 `1 亿小时` 主要是低成本视频，数据层 TAM 约 `50亿-200亿 RMB`；若按具身基座模型混合数据结构，数据资产 TAM 约 `205亿-925亿 RMB`、平台可收入 TAM 约 `20亿-278亿 RMB`；若 `1 亿小时` 本身就是长尾遥操/action 数据需求，数据资产 TAM 可到 `800亿-4,000亿 RMB`，平台可收入 TAM 约 `40亿-800亿 RMB`。
  - **限制**: 该测算完全依赖用户指定的 `1 亿小时` 假设和本文既有单位小时价值区间；不是已验证市场规模，需用真实机器人活跃部署量、接管分钟数、数据授权和模型收益补证。

- **update | TAM 测算逻辑说明补充**
  - **变更**: 在 [[robotics-embodied-ai/research-notes/teleoperation-training-data-cost-and-share-2026-07-09|遥操训练数据每小时成本与训练数据占比快速调研]] 的 `1 亿小时 AGI 级具身基座模型数据 TAM` 章节开头补充“简化计算逻辑”。
  - **初步结果**: 将 TAM 测算压缩为四步：定总量、拆数据结构、给有效小时单价、乘可收入化比例；并用基准混合情景和 `80%` 运维长尾捕获情景各给一条公式。

## [2026-07-10]

- **automation | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-07-10|Bilibili AI Daily Run 2026-07-10]]；更新 [[index|Knowledge Index]]。
  - **来源**: 运行 `uv run python tools/bilibili_ai_daily_research.py --limit 20 --json` 获取默认收藏夹最新 20 个候选。
  - **结果**: 20 个候选全部为 `skipped_duplicate`；`needs_model_review=0`、模型选中 0、`processed=0`、`failed=0`，因此未进入第二阶段、未新增 transcript、source card 或单视频深研页。
  - **限制**: 本轮没有新视频内容可综合；后续运行继续只处理 selected + processed 视频。

- **tooling | Xiaohongshu AI/具身智能收藏夹流程**
  - **变更**: 新增 `tools/xiaohongshu_ai_daily_research.py`、`tests/test_xiaohongshu_ai_daily_research.py` 和 `docs/xiaohongshu_daily_research_automation.md`；更新 [[index|Knowledge Index]]。
  - **参照**: 复用 Bilibili 收藏夹自动化的两阶段流程：先抓候选并去重，Codex/模型筛选 `needs_model_review`，再对 selected 笔记写入 raw source packet、C 级 source card 和 daily run report。
  - **限制**: 小红书默认是 C 级发现线索；脚本依赖 OpenCLI/JSON 导出提供正文和媒体元数据，不伪造笔记正文、作者、日期、截图或互动数据。
  - **验证**: `uv run python -m unittest tests.test_xiaohongshu_ai_daily_research tests.test_bilibili_ai_daily_research` 通过 24 个测试。

- **tooling | Xiaohongshu 图片 OCR 与视频 ASR 适配**
  - **变更**: 扩展 `tools/xiaohongshu_ai_daily_research.py`，selected 笔记现在会合并基础正文、图片 OCR/视觉命令输出和视频字幕/ASR 输出；更新 `docs/xiaohongshu_daily_research_automation.md` 与 [[index|Knowledge Index]]。
  - **配置**: 图片使用 `XIAOHONGSHU_IMAGE_OCR_COMMAND`；视频先走 `XIAOHONGSHU_VIDEO_SUBTITLE_COMMAND`，失败后走 `XIAOHONGSHU_ASR_COMMAND` 或复用 `VOLCENGINE_ASR_COMMAND`。
  - **限制**: 媒体提取失败不会伪造内容；若仍有正文或 OCR/ASR 任一文本，会写入 source packet 并记录 media errors；若完全无文本则失败，除非显式使用 `--allow-empty-content`。
  - **验证**: `uv run python -m unittest tests.test_xiaohongshu_ai_daily_research tests.test_bilibili_ai_daily_research` 通过 31 个测试。

- **synthesis | Xiaohongshu WAM 与具身智能基础设施线索**
  - **变更**: 新增 [[_syntheses/xiaohongshu-wam-robotics-infrastructure-deep-dive-2026-07-10|小红书 WAM 与具身智能基础设施线索深度调研]]；刷新两条小红书 source packet 详情正文；更新 [[index|Knowledge Index]]。
  - **来源**: `6a44a669000000001101bdc2` 与 `6a2667410000000006031e64` 两条小红书收藏；交叉核验 PAIWorld、World Value Models、WAM-TTT arXiv 页面，以及三个 GitHub Awesome 项目元数据。
  - **结果**: 小红书流程可生成线索型深度调研；核心判断是具身智能竞争重心从“单个更大模型”转向记忆、数据引擎、世界模型评估、仿真/部署和操作任务验证的系统基础设施。
  - **限制**: 小红书仍为 C 级线索；`ImageWAM` 未找到足够一级来源，互动数据仅作弱信号。

- **ingest | Xiaohongshu AI/具身智能每日笔记采集**
  - **变更**: 新增或更新 [[_syntheses/xiaohongshu-ai-daily-run-2026-07-10|Xiaohongshu AI Daily Run 2026-07-10]]；处理 2 个 Xiaohongshu note source packet。
  - **来源**: `raw/_inbox/articles/` 与 `knowledge/_sources/` 中的小红书笔记采集产物。
  - **限制**: 小红书默认是 C 级发现线索；脚本只完成候选筛选、去重和 source card 交接，关键事实仍需一级来源交叉验证。

## [2026-07-11]

- **ingest | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-11|Bilibili AI Daily Run 2026-07-11]]；处理 4 个 Bilibili 视频 source packet。
  - **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
  - **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

- **synthesis | Bilibili AI/具身智能四条单视频深研**
  - **变更**: 新增 4 篇 Bilibili 单视频深研页；补充自变量官网和 LingBot-Vision 论文交叉验证。
  - **结论**: 具身赛道中，数据采集的同步/标定可复用性、空间感知的置信度管理、仿真教程的工程正确性，以及公司模型方向与商业化事实必须分开验收。
  - **限制**: Bilibili 均为 B 级线索；除上述两项一级来源外，视频中的融资、客户、性能和教程准确性仍需独立验证。

## [2026-07-12]

- **ingest | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-12|Bilibili AI Daily Run 2026-07-12]]；处理 4 个 Bilibili 视频 source packet。
  - **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
  - **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

- **synthesis | Bilibili AI/具身智能四条单视频深研**
  - **变更**: 新增 Kimodo、RKDA、Graph-as-Policy 和子虔科技云原生 CAD 四篇独立视频深研；更新 [[index|Knowledge Index]]、AI 与机器人具身智能来源台账。
  - **来源**: 四份 Bilibili ASR source packet；补充 NVIDIA Kimodo 文档/技术报告、GaP arXiv/项目页、CaP-X 开源仓库、子虔官网及浩辰软件公开公告。
  - **结论**: 动作生成、智能体编排和云 CAD 的共同产业价值在于将模型/工具输出置入可验证的约束、版本、仿真与执行闭环；RKDA 的具体论文和性能结论仍待定位一手来源。
  - **限制**: Bilibili 视频及演讲内未被一手材料覆盖的性能、客户、产品限制和商业化陈述均保留为待验证线索。

## [2026-07-13]

- **automation | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-07-13|Bilibili AI Daily Run 2026-07-13]]；更新 [[index|Knowledge Index]]。
  - **来源**: 运行 `uv run python tools/bilibili_ai_daily_research.py --limit 20 --json` 获取默认收藏夹最新 20 个候选并完成模型复核。
  - **结果**: 19 个候选为 `skipped_duplicate`；唯一 `needs_model_review` 视频 `BV1SAMv6iELC` 是 BilibiliWorld 会场出行内容，判定与本自动化范围无关，模型选中 0、`processed=0`、`failed=0`，未进入第二阶段。
  - **限制**: 本轮没有新的 AI/具身智能视频内容可综合；未新增 transcript、source card、行业 `sources.csv` 或单视频深研页。

- **synthesis | SRT 软体机器人公司深度调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/srt-soft-robot-tech-company-deep-dive-2026-07-13|SRT 软体机器人公司深度调研]] 和 [[_entities/SRTSoftRobotTech|SRT 软体机器人实体页]]；更新 [[index|Knowledge Index]]、[[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[_entities/README|Entities Layer]]、[[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]] 与 `knowledge/robotics-embodied-ai/sources.csv`。
  - **来源**: 新增并捕获 `SRC-robotics-254` 至 `SRC-robotics-270`，覆盖 SRT 官网/产品/融资、北京市政府报告、上交所招股书、工商聚合、创始人离职媒体线索和 OnRobot/柔触竞争对比；上交所 PDF 另生成 Markdown/JSON/key-info。
  - **初步结果**: SRT 的成熟定位是“气动柔性末端执行器 + 行业自动化方案”，而非通用人形整机或具身大模型；公开可识别融资约 3.1 亿元以上，但营收、毛利、复购、现金流、最新估值与完整 cap table 不公开。
  - **核心风险**: 媒体称创始人兼原 CEO 高少龙及两名前高管于 2026 年转向具身数据创业；融资、专利和客户数量存在统计口径差异；当前应优先核验团队迁移、标准品收入占比、应收回款和客户复购。
  - **限制**: `SRC-robotics-266` 与 `SRC-robotics-267` 的自动正文抽取质量不足，未作为关键结论的唯一依据；医疗注册证当前有效状态、法院案件详情和上市辅导状态仍待官方数据库复核。

## [2026-07-14]

- **ingest | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-14|Bilibili AI Daily Run 2026-07-14]]；处理 1 个 Bilibili 视频 source packet。
  - **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
  - **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

- **synthesis | Bilibili UMI、SLAM 与 Diffusion Policy 单视频深研**
  - **变更**: 新增 [[_syntheses/bilibili-umi-diffusion-policy-robotics-tutorial-deep-dive-2026-07-14|UMI、SLAM 与 Diffusion Policy 具身智能教程视频深度调研]]；更新每日报告、[[index|Knowledge Index]]、AI 与机器人具身智能来源台账。
  - **来源**: Bilibili `BV1qDjh64EEo` 的 ASR source packet；复用 UMI 官方项目/论文/代码仓库（`SRC-robotics-065`–`067`）与 Diffusion Policy 论文（`SRC-robotics-079`）。
  - **结论**: 具身智能的可交付最小闭环是任务、示教数据、观测/动作对齐、策略、部署与真机验收；双臂协作臂是验证受限操作任务的可行起点，但不能把视频中的公司、规格与实时性表述视为已证实事实。
  - **限制**: 视频是 B 级课程线索且使用 ASR；具体公司状态、自由度/精度、通信频率、纯视觉能力和通用化时间表仍须逐项一手核验。

- **synthesis | Google MediaPipe 功能、原理与使用指南**
  - **变更**: 新增 [[ai/research-notes/google-mediapipe-comprehensive-guide-2026-07-14|Google MediaPipe 全面调研：功能、原理与使用方法]]；更新 [[ai/00-index|AI 研究入口]]、[[ai/research-notes/README|AI Research Notes]]、[[ai/00-source-capture-index|AI Source Capture Index]]、[[index|Knowledge Index]] 和 `knowledge/ai/sources.csv`。
  - **来源**: 新增并成功捕获 `SRC-ai-061` 至 `SRC-ai-079`，覆盖 MediaPipe 官方仓库、Solutions/Tasks、Framework 原理、同步/GPU、Hand Landmarker、平台安装、Model Maker、LLM/RAG/Function Calling、LiteRT、最新版本说明与原始论文。
  - **结果**: 将 MediaPipe 定位为“现成任务 API + 预训练模型 + 端侧实时计算图框架”，说明检测—跟踪、时间戳同步、CPU/GPU 数据流和 IMAGE/VIDEO/LIVE_STREAM 用法；结论是经典视觉/音频 Tasks 与 Framework 仍有价值，Legacy Solutions 和已 deprecated/maintenance-only 的生成式 AI SDK 不宜作为新长期架构。
  - **限制**: 文档中的 Preview、iOS 支持和 Holistic 状态存在不一致；官方 benchmark 未在本地目标设备复现，具体项目仍需按语言包、模型版本和设备矩阵重新验证。

- **synthesis | Ego 视频到灵巧手训练数据系统方案**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/ego-video-to-dexterous-hand-training-data-system-design-2026-07-14|Ego 视频到灵巧手训练数据：技术路线、系统设计与落地方案]]；更新 [[index|Knowledge Index]]、[[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/09-training-data-deep-dive|训练数据深度调研]]、[[robotics-embodied-ai/research-notes/README|研究中间笔记]]、[[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]] 和 `knowledge/robotics-embodied-ai/sources.csv`。
  - **来源**: 复用 `SRC-robotics-134` RealDexUMI 与 `SRC-robotics-241` Do As I Do；新增并成功捕获 `SRC-robotics-275` 至 `SRC-robotics-283`，覆盖 HaWoR、DexUMI、DexCap、UniDex、EgoScale、SPIDER 与 GeoRT 的论文或官方实现。
  - **结论**: 手骨架识别不能直接替代灵巧手动作数据；建议以受控 RGB-D/手姿采集跑通首个 PoC，以 HaWoR/Do As I Do 盘活存量单目视频，以 GeoRT 做实时运动学映射，以 SPIDER 做离线动力学修正，并用仿真和真机 rollout 双门验收。
  - **限制**: 论文中的成功率、数据规模和速度均为作者报告，未在目标国产灵巧手与实际任务上复现；200–500 个候选 episode 和 6–8 周为项目规划估计，需用首周通过率与硬件适配结果修正。

- **synthesis | Isaac Sim vs Gazebo vs MuJoCo 机器人仿真平台选型**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/isaac-sim-vs-gazebo-vs-mujoco-2026-07-14|Isaac Sim vs Gazebo vs MuJoCo 机器人仿真平台选型]]；更新 [[index|Knowledge Index]]、[[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/research-notes/README|研究中间笔记]]、[[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]、[[robotics-embodied-ai/00-source-capture-index|来源抽取索引]] 与 `knowledge/robotics-embodied-ai/sources.csv`。
  - **来源**: 新增并成功捕获 `SRC-robotics-284` 至 `SRC-robotics-295`，覆盖 Isaac Sim 6.0.1 下载/系统要求/许可、Gazebo Jetty/Harmonic 生命周期与 ROS 配套、MuJoCo 3.9.0/MJX-Warp/许可证官方资料。
  - **结论**: Isaac Sim 的优势是高保真传感器、合成数据、OpenUSD 和数字孪生；Gazebo 的优势是 ROS 2 系统联调；MuJoCo 的优势是控制、接触动力学、系统辨识和批量策略训练。应按任务采用一主一辅，并用统一 schema、回归测试和真机 rollout 验收。
  - **风险**: 尚无统一硬件/模型/精度条件下的三方 benchmark；Isaac Sim 对 RTX/许可交付依赖高，Gazebo 需严格锁定 ROS/版本，MuJoCo 的 ROS 与高保真传感器工作流需项目自建。

- **research | Harness Engineering for Self-Improvement 深度研读**
  - **变更**: 新增 [[news/2026-07-14-harness-engineering-self-improvement-deep-dive|Harness Engineering for Self-Improvement 深度研读与公式通俗解释]]；保存 Lilian Weng 原文 Defuddle 快照；更新 [[news/00-index|新闻速记]]、[[ai/00-index|AI 研究入口]]、[[ai/research-notes/README|AI Research Notes]] 与 [[index|Knowledge Index]]。
  - **来源**: Lil’Log 原文；交叉核验 MCE、STOP、Meta-Harness、ADAS、AFlow、Self-Harness、DGM 与 SIA 的论文页面。
  - **结论**: 近中期可执行的自我改进主要发生在模型外部 harness；MCE 用双层优化同时搜索上下文与上下文工程技能，STOP 用跨任务元效用让改进器把自身代码当作待优化对象。博客的 STOP 元效用公式疑似把“样本平均求和”与“期望”重复归一化，已按原论文更正并保留冲突说明。
  - **限制**: 多篇 2026 工作仍为预印本，模型、任务、预算和评估器不统一；benchmark 增益不等价于开放世界长期 RSI。

- **entity | Monte Carlo Tree Search**
  - **变更**: 新增 [[_entities/MonteCarloTreeSearch|Monte Carlo Tree Search（MCTS）]] 实体页；更新 [[_entities/README|Entities Layer]]、[[index|Knowledge Index]]、[[ai/00-index|AI 研究入口]] 和 [[news/2026-07-14-harness-engineering-self-improvement-deep-dive|Harness Engineering 深度研读]]回链。
  - **来源**: Kocsis 与 Szepesvári 的 UCT 原始论文、Browne 等人的 MCTS 综述、AFlow 论文及既有 Harness 研究笔记。
  - **内容**: 解释选择—扩展—模拟—回传循环、UCT 公式、探索系数、数值例子、相邻搜索方法、Agent 工作流映射、工程设计与易错边界。
  - **边界**: 遵照用户要求归入 `_entities/`，实体类型标记为 `entity/algorithm`；从知识本体角度它也可视为算法概念，但本轮不重复建立 `_concepts/` 页面。

- **update | 仿真平台国产 GPU/AI 加速器支持矩阵**
  - **变更**: 更新 [[robotics-embodied-ai/research-notes/isaac-sim-vs-gazebo-vs-mujoco-2026-07-14|Isaac Sim vs Gazebo vs MuJoCo 机器人仿真平台选型]]、[[index|Knowledge Index]]、[[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/research-notes/README|研究中间笔记]]、[[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]、[[robotics-embodied-ai/00-source-capture-index|来源抽取索引]] 与 `knowledge/robotics-embodied-ai/sources.csv`。
  - **来源**: 新增并成功捕获 `SRC-robotics-296` 至 `SRC-robotics-306`，覆盖 JAX 官方 accelerator matrix、Gazebo OGRE2/Vulkan/OpenGL/EGL 文档，以及摩尔线程、海光、昇腾、沐曦、壁仞、天数智芯、寒武纪官方材料；两份 PDF 已生成 `pdftotext` Markdown sidecar。
  - **结论**: Isaac Sim 无脱离 NVIDIA RTX 的官方路径；Gazebo 依靠标准图形 API，最有国产全功能 GPU 适配空间；MuJoCo 核心可走 CPU，但 MJX-JAX 未列国产 backend，MuJoCo Warp 仍绑定 NVIDIA CUDA。国产 AI 加速器现阶段更适合作为 ROS 2/RPC 推理旁路。
  - **边界**: 厂商的 CUDA/ROCm 或主流框架兼容声明不等于平台认证；所有性能、渲染正确性、EGL headless、JAX/PJRT 与长期稳定性结论仍需目标硬件 PoC。

## [2026-07-15]

- **ingest | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-15|Bilibili AI Daily Run 2026-07-15]]；处理 1 个 Bilibili 视频 source packet。
  - **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
  - **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

- **synthesis | Bilibili ENPIRE 真实世界机器人自我改进单视频深研**
  - **变更**: 新增 [[_syntheses/bilibili-enpire-physical-autoresearch-deep-dive-2026-07-15|ENPIRE 真实世界机器人自我改进视频深度调研]]；更新 source card、[[ai/00-source-capture-index|AI Source Capture Index]]、[[index|Knowledge Index]] 和 AI 来源台账；归档 [`SRC-ai-080`](../raw/ai/documents/SRC-ai-080-enpire-agentic-robot-policy-self-improvement-in-the-real-world.md)。
  - **来源**: Bilibili `BV1WLja6gEwq` 的 ASR source packet；ENPIRE 官方 NVIDIA 项目页与 arXiv `2606.19980`。
  - **结论**: ENPIRE 的核心是把已定义的真实世界机器人任务组织为可复位、可验证、可审计的 EN–PI–R–E 优化闭环；其 `99% pass@8` 是带上下文重试/恢复的任务指标，不能外推为无重试、跨场景的通用机器人成功率或通用科研自动化。
  - **限制**: 视频为 B 级线索且存在框架名 ASR 误识别；具体 coding-agent 对比、硬件配置、人工参与边界、O.O.D. 泛化与生产部署可靠性仍需回到论文完整实验和现场验证。

- **governance | 固化深度调研分类与商业分析要求**
  - **变更**: 新增 `.agents/skills/industry-analysis/references/research-report-taxonomy.md`，固定 R01–R10 十类调研报告、R00 无匹配兜底链路及内容源触发的先分类后调研流程；同步更新 `AGENTS.md`、industry-analysis skill、研究框架和 Bilibili 每日调研文档。
  - **统一要求**: 所有深度调研必须记录主分类、可选次分类、分类理由与研究边界，并强制包含“商业应用可能性”和“中小型创业者的机会”；证据不足时写明 `待验证`、置信度和下一步。
  - **自动化**: 已更新 Codex automation `bilibili` 的实际调度 prompt；后续每个 processed 视频按选定分类完成单视频深研，无合适分类时使用“行业全景 → 关键产业环节 → 技术与公司 → 产品与场景 → 商业真实性 → 成本与市场空间 → 投资、创业或职业决策”完整链路。

- **maintenance | Wiki Log 按日期压缩**
  - **变更**: 将历史日志从“每项变更重复一个日期标题”重排为“每个日期一个二级标题、当天事件使用紧凑列表”，并按日期恢复时间顺序。
  - **保留范围**: 原有 action、summary、变更、来源、结论、限制和待继续内容均保留，只压缩结构与空白，不改写历史事实。
  - **新规则**: 后续同一天的日志继续追加到当天 `## [YYYY-MM-DD]` 下，不再创建重复日期标题。

## [2026-07-16]

- **ingest | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-16|Bilibili AI Daily Run 2026-07-16]]；处理 1 个 Bilibili 视频 source packet。
  - **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
  - **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

- **synthesis | Bilibili AI 人才市场与职业路径单视频深研**
  - **变更**: 新增 [[_syntheses/bilibili-ai-talent-market-and-career-path-deep-dive-2026-07-16|AI 人才市场与职业路径视频深度调研]]；更新 [[ai/06-career-view|AI 求职与学习视角]]、[[ai/00-source-capture-index|AI 来源抽取索引]]、[[index|Knowledge Index]]、AI 来源台账与日运行报告；修复每日脚本写入日志时的日期标题格式。
  - **来源**: Bilibili `BV152Ne6qEuF` ASR source packet（B）与国务院《人工智能+》行动意见 `SRC-ai-081`（S）。
  - **结论**: 国家政策支持长期 AI 人才培养、青年人才发展、产教融合及规范期权激励；视频中的薪酬、岗位数、人员流动与资本市场数字未取得原始表或披露，均保留为待核验线索。
  - **限制**: 本轮不对个体薪酬、公司招聘强度或 AI 周期作价格预测；后续应取得招聘平台方法页、官方 JD/公告和公司财务资料。

## [2026-07-17]

- **automation | Bilibili 收藏夹每日候选去重**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-07-17|Bilibili AI Daily Run 2026-07-17]] 并更新 [[index|Knowledge Index]]。
  - **结果**: 20 个候选全部命中既有 BV 标识；0 个进入模型复核，0 个转录或深研。TOS 当日前缀为空符合未处理音频的预期。

## [2026-07-18]

- **ingest | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-18|Bilibili AI Daily Run 2026-07-18]]；处理 2 个 Bilibili 视频 source packet。
  - **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
  - **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

- **synthesis | Bilibili RoboTTT 与 Codex/Blender MCP 单视频深研**
  - **变更**: 新增 [[_syntheses/bilibili-robottt-long-context-robot-policy-deep-dive-2026-07-18|RoboTTT 长上下文机器人策略视频深度调研]]（R04，R07）与 [[_syntheses/bilibili-codex-blender-mcp-toolchain-deep-dive-2026-07-18|Codex 与 Blender MCP 工具链视频深度调研]]（R05，R07）；更新两张 source card、每日报告、全局索引、AI/机器人来源台账及来源抽取 MOC。
  - **来源**: 新增并成功捕获 `SRC-robotics-307` RoboTTT arXiv 预印本与 `SRC-ai-082` BlenderMCP 项目 README；视频转录均保留 B 级边界。
  - **结论**: RoboTTT 的可信增量是长程视觉—动作上下文的 fast-weight TTT 机制及论文内结果，现场商业可靠性待验证；BlenderMCP 证明 Agent 可操控 Blender 的工具层，而 ASR 所称模型品牌、质量、耗时和成本不构成已核验事实。
  - **限制**: TOS 当日前缀记录 4 个音频对象而仅有 2 条 processed source packet；一次受控补跑在 Volcengine 查询阶段 TLS/remote-disconnect 失败，未写入第三份 source packet。精确对象—尝试映射待在存储生命周期审查后确认，不应据此推断第三条视频。

## [2026-07-19]

- **ingest | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-19|Bilibili AI Daily Run 2026-07-19]]；处理 2 个 Bilibili 视频 source packet。
  - **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
  - **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

- **synthesis | Bilibili 具身机器人项目与 PI VLA 经验闭环深研**
  - **变更**: 新增 [[_syntheses/bilibili-low-cost-embodied-robot-project-deep-dive-2026-07-19|低成本具身智能机器人项目视频深度调研]]（R05，R07）与 [[_syntheses/bilibili-physical-intelligence-vla-experience-loop-deep-dive-2026-07-19|Physical Intelligence VLA 与经验闭环视频深度调研]]（R04，R07）；修复当日汇总被重试覆盖的 processed 计数，更新两张 source card、全局索引及机器人来源台账。
  - **来源**: B 级 ASR transcript；S 级 `SRC-robotics-061`、`SRC-robotics-308`、`SRC-robotics-309`。
  - **限制**: HiReReLift 的获奖、成本、规格和开源交付物尚无一手可复核材料；PI 视频中的 π0.7、PI Layer、OpenPI、创始/融资与全部数字未逐一被一手来源支持。

## [2026-07-20]

- **synthesis | zsibot/matrix（MATRiX）机器人仿真平台深度调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/zsibot-matrix-robotics-simulator-deep-dive-2026-07-20|MATRiX 深度调研]]、[[_sources/zsibot-matrix-robotics-simulator-source-set|来源集]]与[[_entities/MATRiXSimulator|实体页]]；更新全局索引、机器人 MOC、研究笔记索引和来源捕获索引。
  - **来源**: 固定提交源码/文档审计、v0.1.2 Release 与资产 manifest、GitHub API/issue/PR/tag、GENISOM.AI 官方目录、致谢上游、相关预印本、2026 真实场景训练行动和国家标准计划；归档 `SRC-robotics-310`–`317`。
  - **结论**: MATRiX 的现实价值是把 MuJoCo 控制/动力学与 Unreal 高保真场景包装为面向四足机器人的本土化联调和演示入口；当前更适合限定 PoC，不宜未经实测替代 Gazebo、MuJoCo 或 Isaac Sim 等通用底座。
  - **限制**: 未在 Ubuntu、NVIDIA GPU 和目标真机上运行多 GB 发行包；性能、确定性、传感器标定、批量并行、许可证链与若干文档漂移问题仍需供应商答复和现场验收。

- **ingest | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-20|Bilibili AI Daily Run 2026-07-20]]；处理 1 个 Bilibili 视频 source packet。
  - **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
  - **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

- **synthesis | Bilibili 途见科技柔性电子皮肤单视频深研**
  - **变更**: 新增 [[_syntheses/bilibili-tachin-flexible-electronic-skin-deep-dive-2026-07-20|途见科技柔性电子皮肤视频深度调研]]（R03，R07）；更新 source card、每日运行报告、[[index|Knowledge Index]]、机器人来源台账和来源抽取 MOC。
  - **来源**: B 级 `BV17WNv6GEro` ASR transcript；A 级 `SRC-robotics-318` 途见官网与 `SRC-robotics-319` 深圳发改委托管报道；S 级 `SRC-robotics-320` 兆威机电 2025 年报。
  - **结论**: 可确认公司面向灵巧手、机器人全身和数据采集的触觉产品方向，以及 2025 CES 与兆威共同展示；现有材料不确认融资额、客户订单、量产、性能、投资或供应关系。最小商业验证应比较有/无触觉时的任务成功率、人工干预、寿命与单位合格任务成本。
  - **限制**: `SRC-robotics-319` 因源站 TLS `BAD_ECPOINT` 未能自动抽取，`SRC-robotics-320` PDF 文本转换失败但 PDF 已留存；两者均记录在 manifest/MOC，后续需补稳定镜像或转换后端。

## [2026-07-22]

- **ingest | Bilibili AI/具身智能每日视频采集失败记录**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-07-22|Bilibili AI Daily Run 2026-07-22]]；20 个候选中 15 个重复，模型选中 4 个，未创建 transcript/source card/单视频深研页。
  - **来源**: TOS `asr-audio/2026/07/22` 前缀的两个 102,786,476-byte 音频对象及本地 ASR 进程诊断。
  - **限制**: `BV1cRK86zEpQ` 在上传后约七分钟没有 ASR 输出；另三条选中视频没有启动。需先核验 Volcengine 任务/配额与上传对象映射，再做一次有界重试。

## [2026-07-23]

- **ingest | Bilibili AI/具身智能每日视频采集与 LingBot-VLA 深研**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-07-23|Bilibili AI Daily Run 2026-07-23]] 与 [[_syntheses/bilibili-lingbot-vla-hands-on-deep-dive-2026-07-23|LingBot-VLA 上手教程视频深度调研]]；更新视频 source card、全局索引、机器人来源台账与来源 MOC。
  - **来源**: B 级 `BV1X45w6YENG` ASR transcript；S 级 `SRC-robotics-321` 官方代码/文档与 `SRC-robotics-322` 技术报告。
  - **结论**: 公开后训练与部署闭环可确认；论文/README 分数不等同于目标工位的商业可靠性。
  - **限制**: 5 条已选视频未启动；Volcengine `45000292` 表示 `audio_duration_lifetime` 配额耗尽，需恢复配额后有界重试。

- **synthesis | 蚂蚁灵波具身原生模型战略访谈深研补录**
  - **变更**: 后台完成 `BV1cRK86zEpQ` 转写后，新增 [[_syntheses/bilibili-robbyant-native-embodied-model-strategy-deep-dive-2026-07-23|蚂蚁灵波具身原生模型战略访谈深度调研]] 并更新 source card、来源台账与全局索引。
  - **结论**: 确认公开 LingBot-VLA 技术资产和后训练入口；访谈中的组织、数据联盟、竞争与商业化主张保持 B 级待验证。

## [2026-07-24]

- **ingest | Bilibili 人形机器人运控与 MemoryVLA 视频深研**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-07-24|Bilibili AI Daily Run 2026-07-24]]、两篇视频 source card、[[_syntheses/bilibili-humanoid-motion-control-algorithms-deep-dive-2026-07-24|运控算法深研]]与[[_syntheses/bilibili-memoryvla-temporal-memory-deep-dive-2026-07-24|MemoryVLA 深研]]；更新 AI/机器人来源台账和全局索引。
  - **来源**: B 级 `BV17ooSB2E93`、`BV17doLBJEBt` ASR transcripts；S 级 DeepMimic、AMP、MemoryVLA/ReMem-VLA 论文和 `SRC-robotics-001` / `SRC-robotics-316`。
  - **结论**: 运控和 VLA 记忆都应按实际任务的鲁棒性、接管、延迟与安全分层验收；仿真/论文结果不能外推为商业可靠性。
  - **限制**: 两条 source packet 已成功生成；TOS 当日 6 个对象包含重试上传，数量不等于成功转录数。

## [2026-07-25]

- **automation | Bilibili 收藏夹每日候选去重与模型相关性判断**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-07-25|Bilibili AI Daily Run 2026-07-25]] 并更新 [[index|Knowledge Index]]。
  - **结果**: 20 个候选中 19 个命中既有 BV 标识；唯一 `needs_model_review` 项 `BV1cvTq68E5g` 是个人经历/人生感悟内容，与 AI/具身智能调研范围无关。模型选中 0 个，未启动转录、ASR、source card 或单视频深研。
  - **限制**: TOS 前缀 `asr-audio/2026/07/25` 为空，符合本日没有选中音频处理任务的预期。

## [2026-07-26]

- **automation | Bilibili 收藏夹每日候选与失败记录**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-07-26|Bilibili AI Daily Run 2026-07-26]] 并更新 [[index|Knowledge Index]]。
  - **结果**: 20 个候选中 18 个重复；模型选中 `BV1DKMt6HEvk`（DYNA 机器人联创访谈），`BV1cvTq68E5g`（个人感悟）不相关而未选。字幕路径未返回文本，Volcengine `volc.seedasr.auc` 与 `volc.bigasr.auc` 的 5 秒有界诊断均超时；0 个 processed、0 个 source card、0 篇单视频深研。
  - **限制**: TOS `asr-audio/2026/07/26` 可列出 4 个本次尝试音频对象，说明上传可达但不表示转录成功。下次应在可执行长轮询的环境按默认时限有界重试，并保留 submit/query 状态、`X-Tt-Logid` 与配额错误。

## [2026-07-28]

- **ingest | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-28|Bilibili AI Daily Run 2026-07-28]]；处理 2 个 Bilibili 视频 source packet。
  - **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
  - **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

- **synthesis | RLinf 与开源机械臂两条单视频深研**
  - **变更**: 新增 [[_syntheses/bilibili-rlinf-embodied-reinforcement-learning-infrastructure-deep-dive-2026-07-28|RLinf 具身强化学习基础设施视频深研]]（R04，R07）和 [[_syntheses/bilibili-open-robot-arm-platform-selection-deep-dive-2026-07-28|开源机器人与机械臂选型视频深研]]（R05，R07）；补充 `SRC-robotics-323`–`326` raw captures、来源 MOC、source card 回链与全局索引。
  - **结论**: RL 基础设施应以目标任务的安全、成本与可复现 A/B 证明价值；开源机器人选择的最小闭环是 BOM/CAD、控制、标定/遥操、可训练数据、部署、许可证和安全，而非视频价格或“开源”标签。
  - **限制**: Bilibili ASR 中的性能、价格、平台/数据集名称、采用方和商业化信息未逐一得到一手来源支持，均未升级为行业事实。

- **synthesis | RoboVerse 能力边界与具身数采数据增益深研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/roboverse-platform-and-real-data-deep-dive-2026-07-28|RoboVerse 深度调研]]、[[_sources/roboverse-platform-dataset-benchmark-source-set|来源集]]与[[_entities/RoboVerse|实体页]]；归档 `SRC-robotics-327`–`336` 并更新全局/行业/研究笔记/来源索引。
  - **来源**: RSS 2025 论文、固定提交 `e9b5c6e` 的 RoboVerse 仓库与文档、2026-07-28 GitHub 元数据、Isaac Lab/LeRobot/ManiSkill 官方文档。
  - **结论**: RoboVerse 是 MetaSim 之上的任务、数据、benchmark 和学习层，不是基础模型；L2 以上的真实 episode、Real2Sim 扫描、物理参数、失败/接管和真机 holdout 能提升其数据、仿真、评测或其中训练的模型，但必须用 real-only/sim-only/naive-mix/calibrated-mix 四组 A/B 证明。
  - **限制**: 未运行 Linux/GPU 环境或独立复现实验；论文 mixed world-model 增益主要为定性，sim-to-real 样本有限，第三方资产许可仍需逐项审计。

## [2026-08-05]

- **ingest | 微信《一文速览具身智能机器人相关核心技术体系》入库**
  - **变更**: 新增 [[_sources/wechat-embodied-intelligence-robotics-core-technology-overview|来源卡]]和 `SRC-robotics-337` Defuddle 全文；更新机器人来源台账、来源 MOC、行业索引与全局索引。
  - **结论**: 该文可作感知—决策—执行—反馈—学习的入门地图，不能单独支撑商业成熟度、政策、市场或产业链判断。
  - **限制**: 原文发布日期未从页面元数据可靠提取；公司案例、进口依赖、政策预测和 2030 年市场表述均保留为 C 级待验证线索。

- **synthesis | ORB-SLAM3 技术、工程与商业深度调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/orb-slam3-technology-engineering-commercial-deep-dive-2026-08-05|ORB-SLAM3 深度调研]]、[[_sources/orb-slam3-paper-code-benchmark-source-set|来源集]]，扩充 [[_entities/ORBSLAM3|ORB-SLAM3 实体页]]；归档 `SRC-robotics-338`–`349` 并更新来源 MOC、行业/全局索引。
  - **来源**: ORB-SLAM3 T-RO/arXiv 论文、固定提交官方 README/Calibration/Dependencies、2026-08-05 GitHub API 快照、EuRoC/TUM-VI 官方 benchmark，以及 VINS-Fusion/OpenVINS/RTAB-Map/cuVSLAM 官方资料。
  - **结论**: ORB-SLAM3 仍是理解和验证稀疏特征、紧耦合视觉惯性、回环与 Atlas 多地图的强基线；它不是稠密语义导航产品。2026 年新商业项目必须先验证目标场景失效率、现代 ROS 2/依赖维护、GPL/商业许可和下游任务 ROI。
  - **限制**: 未在目标相机、ROS 2、国产算力或客户现场编译复现；论文 ATE/timing 是作者实验，商业订单、许可费用、SLA 与现场长期可靠性均待询价和 PoC。

- **synthesis | RTAB-Map、cuVSLAM、OpenVINS 技术与工程选型深度调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/rtabmap-cuvslam-openvins-comparative-deep-dive-2026-08-05|三方案深度调研]]、[[_sources/rtabmap-cuvslam-openvins-source-set|来源集]]和 [[_entities/RTABMap|RTAB-Map]]、[[_entities/cuVSLAM|cuVSLAM]]、[[_entities/OpenVINS|OpenVINS]] 实体页；归档 `SRC-robotics-350`–`361` 并更新来源 MOC、行业/全局索引。
  - **来源**: RTAB-Map 2019 JFR/2024 arXiv 全文、cuVSLAM 2025 technical report、OpenVINS ICRA 2020 论文，三方固定提交 README/许可证/官方文档及 2026-08-05 GitHub API 快照。
  - **结论**: RTAB-Map 是长期 ROS 2 graph-SLAM/数据库/occupancy 层，cuVSLAM 是 NVIDIA 多相机低延迟 VO/VSLAM SDK，OpenVINS 是 MSCKF VIO/标定研究平台；默认选型分别对应 AMR/Nav2、Jetson 多相机和 estimator 研发。
  - **限制**: 未做统一 rig/硬件复现；作者 benchmark 不可跨论文横排。cuVSLAM NVIDIA-only 授权、OpenVINS GPL 与最终依赖/分发架构仍需法律审核和任务级 PoC。

- **synthesis | Jetson Thor 与替代边缘 AI 平台规格、价格及选型调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/jetson-thor-and-alternatives-spec-price-comparison-2026-08-05|Jetson Thor 选型调研]]、[[_sources/jetson-thor-edge-ai-compute-platform-source-set|来源集]]和机器可读规格/价格 CSV；登记 `SRC-robotics-363`–`375`，完成 Thor 与 Orin、IQ-9075、DGX Spark、Ryzen AI Max+ 395、Hailo/Atlas/征程 6 的分层比较。
  - **来源**: NVIDIA 当前 Thor/Jetson FAQ/Marketplace/JetPack/benchmark，Qualcomm IQ-9075，AMD 与 MINISFORUM，DGX Spark、Hailo、华为昇腾和地平线官方页面，以及 iCEasy 中国渠道动态报价线索（B 级）。
  - **结论**: 2026-08-05 当前 Thor 开发套件官方价为 US$5,499，而非仍被旧材料引用的 US$3,499；Thor 的一比一价值来自 128GB、CUDA/Isaac、机器人 I/O 和量产模组路径，不能用异精度 TOPS 或美元/TOPS 替代目标模型 PoC。
  - **限制**: 未取得 IQ-9075/国产方案书面报价，也未用同一真实 VLA/VLM、传感器与功耗条件做跨平台 A/B；动态价格、库存和交期必须在采购日复核。

## [2026-08-06]

- **synthesis | 3D 仿真资产生产技术管线综合调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/3d-simulation-asset-production-pipelines-comparison-2026-08-06|3D 仿真资产管线调研]]、[[_sources/3d-simulation-asset-production-pipeline-source-set|来源集]]和九路线机器可读 CSV；登记并捕获 `SRC-robotics-407`–`422`，更新行业/研究笔记/来源/全局索引。
  - **来源**: OpenUSD、UsdPhysics、SimReady Foundation、Isaac Sim、Datasmith、COLMAP、ReCap、Nerfstudio、Infinigen-Sim、Hunyuan3D、TRELLIS、MuJoCo、ROS 2 URDF 和 Houdini Solaris 官方文档/代码/论文。
  - **结论**: CAD 保工程结构，扫描保尺度/外观，3DGS/NeRF 保视觉，程序化保规模，生成式 3D 保候选速度；生产默认应采用 OpenUSD canonical package，并独立编译 collision、physics、articulation、semantics、sensor material 和 runtime adapter，再以任务证据验收。
  - **限制**: 未做统一资产和人员条件下的跨工具成本 benchmark，也未验证多仿真器物理等价；生成式 3D 的 metric、physics、许可与真机增益仍需目标 PoC。
  - **补充验收**: 新增 SimReady L1 规范/L2 运行时/L3 任务三级验收、Profile 选择矩阵、`PASS/CONDITIONAL PASS/FAIL/NOT APPLICABLE` 判定、机器可读清单；登记并捕获 `SRC-robotics-423`–`425`。正式 L1 门采用选定 Profile requirement 零失败，MUST 不允许豁免，SHOULD 偏离需批准；官方通过不替代 runtime 与 real holdout。

- **synthesis | 光轮智能同类创业公司与商业模式扫描**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/lightwheel-peer-companies-business-model-comparison-2026-08-06|同类公司对比调研]]、[[_sources/lightwheel-peer-physical-ai-data-simulation-companies-source-set|来源集]]和机器可读候选矩阵；登记/捕获 `SRC-robotics-394`–`406`，更新行业公司表、来源 MOC、研究笔记 MOC 和全局索引。
  - **结论**: Applied Intuition 是最接近的平台商业对标，Parallel Domain 最接近 Real2Sim 资产飞轮，Duality AI 最接近 SimReady/合成数据/验证组合；求之科技是中国产品覆盖最接近候选，极佳视界则是纵向一体化替代。
  - **限制**: 多数未上市公司不公开收入、毛利、回款和复购；Rendered.ai 抓取 403、具身智境 TLS 失败，极佳官网为 HTML fallback；官网客户数、订单和性能均未升级为审计事实。

- **synthesis | 光轮智能公司与商业模式深度调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/lightwheel-company-and-commercial-model-deep-dive-2026-08-06|光轮智能深度调研]]、[[_sources/lightwheel-company-technology-commercial-source-set|来源集]]和 [[_entities/LightwheelAI|实体页]]；登记并捕获 `SRC-robotics-377`–`393`，更新全局/行业/研究笔记/公司/实体/来源索引。
  - **来源**: 光轮官网与产品页、NVIDIA/吉利部署案例、政府平台订单与交付报道、GitHub/Hugging Face 公开资产、融资媒体及奇绩创坛团队资料。
  - **结论**: 公司已越过概念和单一 Demo，形成真实数据、SimReady、训练、评测和部署反馈闭环；但 5.5 亿元新增订单不等于收入或回款，150 万小时与复售率等口径仍需合同、财务和客户复购穿透。
  - **限制**: 未获得审计财务、合同、回款、客户集中度、平台定价或 cap table；`SRC-robotics-390` 旧经纬页面自动抽取返回 404，失败记录已保留。

- **synthesis | Unreal Engine 在机器人与具身智能中的应用、开源项目和论文调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/unreal-engine-in-robotics-and-embodied-ai-2026-08-06|UE 机器人与具身智能调研]]、[[_sources/unreal-engine-robotics-embodied-ai-source-set|来源集]]及项目/论文两个机器可读 CSV；登记 `SRC-robotics-426`–`462`，更新行业、研究笔记、来源和全局索引。
  - **来源**: Epic 官方许可/Chaos 文档，UnrealCV、AirSim 系列、CARLA、URLab、SPEAR、SimWorld、ROS 接口、UnrealROX、UNav-Sim、HoloOcean 等官方仓库/文档及代表论文；GitHub 动态元数据查询于 2026-08-06。
  - **结论**: UE 最适合作为高真实感场景、传感器、人机交互和数字孪生层；精确操作与控制优先采用 UE + MuJoCo/专用物理 + ROS 2。第一梯队 PoC 为 UnrealCV、SPEAR、URLab、Project/Cosys-AirSim、CARLA、rclUE 和 MATRiX。
  - **限制**: 未逐一编译运行项目；Epic licensing 自动抽取 403；VirtualEnv 未定位官方仓库，SimWorld Studio 公开构建依赖受限源码，HERCULES 未完成仓库审计；论文指标不跨项目横排。

- **synthesis | Unity 在机器人与具身智能中的应用、开源项目和论文调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/unity-in-robotics-and-embodied-ai-2026-08-06|Unity 机器人与具身智能调研]]、[[_sources/unity-robotics-embodied-ai-source-set|来源集]]及项目/论文机器可读 CSV；登记并捕获 `SRC-robotics-463`–`501`，更新行业、研究笔记、来源和全局索引，并从 UE 报告回链。
  - **来源**: Unity 当前产品/条款、Unity Robotics/ML-Agents/Perception、RobotecAI/ROS#、AI2-THOR/ProcTHOR/ALFRED/TEACh、VirtualHome/TDW、Flightmare/AWSIM/SVL/AutoDRIVE/CLOiSim 官方仓库和代表论文；GitHub 动态元数据查询于 2026-08-06。
  - **结论**: Unity 最适合构建可编程交互世界、室内具身任务、合成观测、VR 示教和 ROS/学习闭环；ML-Agents 与 AI2-THOR 生态是突出优势。代码开源、Unity 引擎、资产、数据和云服务必须分层审计。
  - **限制**: 未逐一编译 23 个项目；Perception 已停更，SVL 已 sunset，TDW 处于 LTS；AWSIM 代码 Apache-2.0 而资产 CC BY-NC；`SRC-robotics-474`、`484` 为 fallback HTML，论文指标未独立复现。

## [2026-08-09]

- **synthesis | EtherCAT 技术、生态与机器人工程选型深度调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/ethercat-technology-ecosystem-engineering-deep-dive-2026-08-09|EtherCAT 深度调研]]和[[_sources/ethercat-technology-implementation-policy-source-set|来源集]]；登记 `SRC-robotics-505`–`515`，成功捕获其中 10 项网页来源，更新行业、研究笔记、来源与全局索引。
  - **来源**: ETG 官方技术/标准化/许可/Implementation Guide/EtherCAT G/TSN、SOEM、IgH、ODVA CIP Motion 和工信部政策文件。
  - **结论**: EtherCAT 的价值来自帧内处理、逻辑过程映像、分布式时钟与成熟 profile，适合机器人控制器到驱动/I/O 的确定性内环；协议实时不能替代 OS、控制算法、驱动器与安全的端到端验收。
  - **限制**: `SRC-robotics-508` 官方 PDF 自动抽取未产出 raw，待补采；未运行真实 6/12 轴台架，也未取得中国市场份额、供应商报价、功能安全证书或客户复购数据；ETG 性能数字为官方口径，政策未点名 EtherCAT。

- **synthesis | DexCap 灵巧操作动捕数据采集系统深度调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/dexcap-dexterous-mocap-data-collection-deep-dive-2026-08-09|DexCap 深度调研]]、[[_sources/dexcap-paper-project-code-source-set|来源集]]和 [[_entities/DexCap|实体页]]；复用既有论文 `SRC-robotics-277`，新增并捕获官网/固定提交代码 `SRC-robotics-502`、`504`，更新行业、研究笔记、来源和全局索引。
  - **结论**: DexCap 证明人类穿戴动捕可提升灵巧示教吞吐，并通过点云重定向训练 robot policy；但无力觉、跨本体接触差异、视野盲区、40 分钟续航和老化 BOM 使其更适合研究/数据服务 PoC，而不是直接量产复制。
  - **限制**: 未复现双 Franka/LEAP 实验，未核验当前完整 BOM、数据商业许可或客户收入；作者任务成功率不构成产品 SLA。

## [2026-08-10]

- **synthesis | onshape-to-robot 用法、工程边界与选型调研**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/onshape-to-robot-usage-selection-deep-dive-2026-08-10|onshape-to-robot 用法与选型调研]]和[[_sources/onshape-to-robot-official-source-set|官方来源集]]；登记 `SRC-robotics-516`–`528`，更新行业、研究笔记、来源与全局索引。
  - **来源**: 固定主仓库 commit `7d0803d`、示例 commit `7e40fd6`、官方 Read the Docs/PyPI、固定源码 diff，以及 API rate limit、嵌套 DoF 和 retrieve/convert 配置行为三个具体 GitHub issue。
  - **结论**: 该工具适合 Onshape-first 团队把版本化装配编译为 URDF/SDF/MuJoCo，并减少结构、几何和惯量的重复录入；不能替代 ROS 2/MoveIt/控制器、碰撞优化、动力学辨识和任务级模型验收。PyPI v1.8.2 与 latest master 存在未发布差异，SDF 用户必须 pin 并回归。
  - **限制**: 本轮未使用 Onshape API 密钥或真实用户装配，只有源码 `compileall` 和静态/文档审计；`SRC-robotics-525` PyPI 正文 Defuddle 超时但 HTML 已保存，版本和依赖由 PyPI JSON 与 `pyproject.toml` 交叉核验。

## [2026-08-11]

- **synthesis | Bilibili AI/具身智能视频入库**
  - **变更**: 新增每日运行页及 FlexiTac、SAM2Act、TurboVLA、光模块工位、Isaac Lab 五篇单视频深研，并归档原文/source card。
  - **限制**: 视频性能、价格、公司和订单主张均保持 B 级，关键技术只按论文/官方资料交叉验证。

- **ingest | 微信具身数据处理 RoadMap 入库并编译工程知识**
  - **变更**: 登记并捕获 `SRC-robotics-529`，新增 [[_sources/wechat-embodied-data-processing-roadmap|文章来源卡]]、[[robotics-embodied-ai/research-notes/embodied-ai-model-data-processing-pipeline-2026-08-11|具身智能模型数据处理闭环]]，扩充 [[_concepts/robot-training-data|Robot Training Data]]，并更新训练数据父页、深研汇总、行业/来源/研究笔记/全局索引。
  - **结论**: 数据处理从采集前的数据契约开始，必须分层保留 raw、canonical dataset 与 model view；同步、标定、自动质量门、episode/事件、action/schema、无泄漏切分、baseline、真实 holdout 和部署失败回流共同构成可训练闭环。
  - **来源**: 微信文章作为 C 级问题地图；LeRobot v3、Open X-Embodiment、DROID 与 LeRobot HIL 作为 S 级工程边界。
  - **限制**: 原文发布日期未可靠返回；毛利、标注价格、`50 ms` 同步阈值和优化周期均无可核查口径，未升级为行业事实。真实机器人 raw→训练→部署回流 PoC 尚未执行。

## [2026-08-12]

- **synthesis | CodeX—ROS 2 视频深研入库**
  - **变更**: 新增每日运行页、source card、原文与 [[_syntheses/bilibili-codex-ros2-mcp-robot-control-deep-dive-2026-08-12|R05/R07 深研]]。
  - **结论**: MCP 工具编排不能替代车端安全状态机、限幅和急停。

- **synthesis | EtherCAT 与 TCP/IP 机器人实时控制时延专题**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/ethercat-vs-tcp-ip-robot-control-latency-2026-08-12|EtherCAT vs TCP/IP 时延专题]]；登记并捕获 IETF `SRC-robotics-530`–`531`，更新 EtherCAT 来源集、来源 MOC、行业/研究笔记/全局索引，并从原 EtherCAT 深调回链。
  - **结论**: EtherCAT 在多轴控制中的优势来自单帧服务多节点、ESC on-the-fly 硬件处理、固定主站/拓扑、Distributed Clocks 和 Working Counter，不是峰值带宽；TCP 的可靠有序重传适合通用数据，但会在丢包后放大控制尾时延。
  - **边界**: TCP 连接并非每周期握手，UDP 也不自动具备实时同步；1/10 Gbit/s IP 网络在吞吐和理想串行化时间上可快于 100 Mbit/s EtherCAT。未做统一 6/12 轴台架，因此不提供“快几倍”的产品结论。

## [2026-08-13]

- **synthesis | Bilibili 已处理视频深研补齐**
  - **变更**: 归档 ROS 2、具身数据集、空间智能、Harness VLA、EtherCAT 与人形机器人研究方法的 source packet；六条均有独立深研。
  - **限制**: ASR/视频是 B 级线索；数据集、Harness、EtherCAT 机制以一手论文/官方资料为界，商业数字仍待核验。

## [2026-08-14]

- **automation | Bilibili 收藏夹候选采集未启动**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-08-14|Bilibili AI Daily Run 2026-08-14]]；未创建本日 transcript 或 source card。
  - **失败边界**: OpenCLI `bilibili favorite` 返回 `BROWSER_CONNECT`，Browser Bridge extension 未连接；启用并连接 Chrome/Chromium 扩展后再执行候选命令。

## [2026-08-15]

- **automation | Bilibili 收藏夹候选筛选完成，无新增研究包**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-08-15|Bilibili AI Daily Run 2026-08-15]] 并更新 [[index|Knowledge Index]]。
  - **结果**: 20 个候选中 18 个为既有记录；剩余 `BV1s43t6UEaW` 与 `BV1cvTq68E5g` 经模型审阅均非 AI/具身智能相关，未运行二阶段转录、ASR、source card 或单视频深研。
  - **限制**: TOS 前缀 `asr-audio/2026/08/15` 可检查但为空；这是零视频被选中的正常结果，而非处理失败。

## [2026-08-16]

- **automation | Bilibili 收藏夹候选筛选完成，无新增研究包**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-08-16|Bilibili AI Daily Run 2026-08-16]] 并更新 [[index|Knowledge Index]]。
  - **结果**: 20 个候选中 18 个为既有记录；剩余 `BV1s43t6UEaW` 与 `BV1cvTq68E5g` 经模型审阅均非 AI/具身智能相关，未运行二阶段转录、ASR、source card 或单视频深研。
  - **限制**: TOS 前缀 `asr-audio/2026/08/16` 可检查但为空；这是零视频被选中的正常结果，而非处理失败。

## [2026-08-17]

- **automation | Bilibili 收藏夹候选筛选完成，无新增研究包**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-08-17|Bilibili AI Daily Run 2026-08-17]] 并更新 [[index|Knowledge Index]]。
  - **结果**: 20 个候选中 18 个为既有记录；剩余 `BV1s43t6UEaW` 与 `BV1cvTq68E5g` 经模型审阅均非 AI/具身智能相关，未运行二阶段转录、ASR、source card 或单视频深研。
  - **限制**: TOS 前缀 `asr-audio/2026/08/17` 可检查但为空；这是零视频被选中的正常结果，而非处理失败。

## [2026-08-18]

- **automation | Bilibili 收藏夹候选筛选完成，无新增研究包**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-08-18|Bilibili AI Daily Run 2026-08-18]] 并更新 [[index|Knowledge Index]]。
  - **结果**: 20 个候选中 18 个为既有记录；剩余 `BV1s43t6UEaW` 与 `BV1cvTq68E5g` 经模型审阅均非 AI/具身智能相关，未运行二阶段转录、ASR、source card 或单视频深研。
  - **限制**: TOS 前缀 `asr-audio/2026/08/18` 可检查但为空；这是零视频被选中的正常结果，而非处理失败。

## [2026-08-19]

- **automation | Bilibili 收藏夹候选筛选完成，无新增研究包**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-08-19|Bilibili AI Daily Run 2026-08-19]] 并更新 [[index|Knowledge Index]]。
  - **结果**: 20 个候选中 18 个为既有记录；剩余 `BV1s43t6UEaW` 与 `BV1cvTq68E5g` 经模型审阅均非 AI/具身智能相关，未运行二阶段转录、ASR、source card 或单视频深研。
  - **限制**: TOS 前缀 `asr-audio/2026/08/19` 可检查但为空；这是零视频被选中的正常结果，而非处理失败。

## [2026-08-20]

- **automation | Bilibili 收藏夹候选筛选完成，无新增研究包**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-08-20|Bilibili AI Daily Run 2026-08-20]] 并更新 [[index|Knowledge Index]]。
  - **结果**: 20 个候选中 18 个为既有记录；剩余 `BV1s43t6UEaW` 与 `BV1cvTq68E5g` 经模型审阅均非 AI/具身智能相关，未运行二阶段转录、ASR、source card 或单视频深研。
  - **限制**: TOS 前缀 `asr-audio/2026/08/20` 可检查但为空；这是零视频被选中的正常结果，而非处理失败。

## [2026-08-21]

- **automation | Bilibili 收藏夹候选筛选完成，无新增研究包**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-08-21|Bilibili AI Daily Run 2026-08-21]] 并更新 [[index|Knowledge Index]]。
  - **结果**: 20 个候选中 18 个为既有记录；剩余 `BV1s43t6UEaW` 与 `BV1cvTq68E5g` 经模型审阅均非 AI/具身智能相关，未运行二阶段转录、ASR、source card 或单视频深研。
  - **限制**: TOS 前缀 `asr-audio/2026/08/21` 可检查但为空；这是零视频被选中的正常结果，而非处理失败。

## [2026-08-22]

- **automation | Bilibili 收藏夹候选筛选完成，无新增研究包**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-08-22|Bilibili AI Daily Run 2026-08-22]] 并更新 [[index|Knowledge Index]]。
  - **结果**: 20 个候选中 18 个为既有记录；剩余 `BV1s43t6UEaW` 与 `BV1cvTq68E5g` 经模型审阅均非 AI/具身智能相关，未运行二阶段转录、ASR、source card 或单视频深研。
  - **限制**: TOS 前缀 `asr-audio/2026/08/22` 可检查但为空；这是零视频被选中的正常结果，而非处理失败。

## [2026-08-23]

- **automation | Bilibili 收藏夹候选筛选完成，无新增研究包**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-08-23|Bilibili AI Daily Run 2026-08-23]] 并更新 [[index|Knowledge Index]]。
  - **结果**: 20 个候选中 18 个为既有记录；剩余 `BV1s43t6UEaW` 与 `BV1cvTq68E5g` 经模型审阅均非 AI/具身智能相关，未运行二阶段转录、ASR、source card 或单视频深研。
  - **限制**: TOS 前缀 `asr-audio/2026/08/23` 可检查但为空；这是零视频被选中的正常结果，而非处理失败。

## [2026-08-24]

- **automation | Bilibili 收藏夹候选筛选完成，无新增研究包**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-08-24|Bilibili AI Daily Run 2026-08-24]] 并更新 [[index|Knowledge Index]]。
  - **结果**: 20 个候选中 18 个为既有记录；`BV1s43t6UEaW` 与 `BV1cvTq68E5g` 经模型审阅均非 AI/具身智能相关，未运行二阶段转录、ASR、source card 或单视频深研。
  - **限制**: TOS 前缀 `asr-audio/2026/08/24` 可检查但为空；这是零视频被选中的正常结果，而非处理失败。

## [2026-08-26]

- **automation | Bilibili 收藏夹候选筛选完成，无新增研究包**
  - **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-08-26|Bilibili AI Daily Run 2026-08-26]] 并更新 [[index|Knowledge Index]]。
  - **结果**: 20 个候选中 18 个为既有记录；`BV1s43t6UEaW` 与 `BV1cvTq68E5g` 经模型审阅均非 AI/具身智能相关，未运行二阶段转录、ASR、source card 或单视频深研。
  - **限制**: TOS 前缀 `asr-audio/2026/08/26` 可检查但为空；这是零视频被选中的正常结果，而非处理失败。

- **ingest | WRC 具身大脑可靠性、模型规模与按结果付费文章入库**
  - **变更**: 登记并捕获 `SRC-robotics-534`–`536`，新增 [[_sources/wechat-wrc-embodied-ai-reliability-scaling-token-business|文章来源卡]]和[[robotics-embodied-ai/research-notes/embodied-ai-reliability-scaling-and-outcome-pricing-2026-08-26|商业化门槛调研]]，更新来源 MOC、行业/来源/研究笔记/全局索引。
  - **来源**: 微信文章作为 C 级问题地图；雷峰网 WRC 演讲整理和量子位/AITNT 访谈作为 B 级归因证据；π0、OpenVLA 与政策原文用于限制模型规模、真实场景验收和按效用付费边界。
  - **结论**: 原子技能可靠性、长程任务、陌生分布和生产运营必须分层验收；`7B`/万卡不是已验证的能力门槛；“物理 Token”近期应还原为按任务、合格件或可用小时计费，并同时验证 SLA、责任、复购和单位经济性。
  - **限制**: 原文发布日期未可靠返回；公司成功率、训练规模、毛利和客户部署缺少原始演讲、trial protocol、审计财务和客户侧验收，均未升级为事实。

## [2026-09-02]

- **ingest | Bilibili AI/具身智能每日视频采集**
  - **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-09-02|Bilibili AI Daily Run 2026-09-02]]；处理 3 个 Bilibili 视频 source packet。
  - **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
  - **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。
- **research | 完成 3 篇 Bilibili 单视频深度调研**
  - **变更**: 新增 [[_syntheses/bilibili-microduck-hardware-architecture-deep-dive-2026-09-02|Microduck 架构]]、[[_syntheses/bilibili-unitree-commercialization-and-valuation-deep-dive-2026-09-02|宇树商业化]]、[[_syntheses/bilibili-sudo-technology-full-stack-embodied-ai-deep-dive-2026-09-02|苏度全栈路线]]，并更新 [[index|Knowledge Index]]。
  - **结论**: Microduck 的公开证据支持轻量控制架构而非量产/成本主张；宇树的上市事实与人形商业化期权应分开看；苏度的仿真+真机全栈路线需以多客户回款和可靠性验证。
  - **限制**: Bilibili 仅为 B 级线索；价格、订单、估值、融资与成功率均未提升为事实。
- **research | 宇树科技上市供应链 A 股公司核验**
  - **变更**: 新增 [[robotics-embodied-ai/research-notes/unitree-listed-supply-chain-public-companies-2026-09-02|宇树科技上市供应链 A 股公司调研]]、[[_sources/unitree-listed-supply-chain-source-set|来源集]]和统一行情 CSV；登记 `SRC-robotics-541`–`550`，更新行业、来源、研究笔记与全局索引。
  - **结论**: 直接证据支持蔚蓝锂芯、新洁能、创世纪、丰立智能、长盛轴承 5 家核心名单；宇树招股书前五大供应商多数匿名或非上市，上市供应链股不等于最大供应商。5 家在宇树上市日全部下跌，近一个月表现分化。
  - **来源**: 上交所/巨潮披露与互动易为 S 级关系证据；2026-08-31 行情快照为 B 级聚合数据。
  - **限制**: 五家公司均未披露宇树收入、毛利、份额或订单占比；动态行情页部分 raw 抽取失败，真实交易前需券商终端复核。
