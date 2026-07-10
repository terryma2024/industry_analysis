---
title: Wiki Log
type: log
date_created: 2026-05-29
last_updated: 2026-07-03
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

## [2026-06-09] synthesis | 线下零售门店验证口径汇总

- **变更**: 合并记录 Thinking Partner 对话中关于零售后场 / 线下零售门店职业切入点的系列口径澄清，并更新 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]]。
- **澄清结果**: 样本优先用公开行业排名；若门店/仓库规模排名不可得，则用中国零售销售额前 10。项目范围从“零售后场”放宽为“线下零售门店前场/后场”，导购、巡店、清洁、安防、门店内自动化仓库计入；中央仓、区域仓、纯仓配体系不计入。必须有外部具身智能、机器人或通用服务机器人公司参与；公司公告或年报确认合作即可作为早期计入证据，媒体和供应商案例仅作线索。
- **门槛**: 前 10 公司中有 5 家满足条件，即视为“超过一半”通过；该门槛同时用于判断是否值得继续调研，以及是否值得作为职业切入点投入 6 个月验证。

## [2026-06-10] synthesis | 线下零售门店与跨场景短期落地调研

- **变更**: 新增 [[robotics-embodied-ai/research-notes/retail-store-robotics-entry-scan-2026-06-10|线下零售门店机器人合作验证初扫]] 和 [[robotics-embodied-ai/research-notes/cross-scenario-near-term-landing-candidate-pool-2026-06-10|具身智能短期落地跨场景候选池]]；更新 [[robotics-embodied-ai/sources|机器人来源表]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]] 和 [[index|Knowledge Index]]。
- **零售初扫**: 暂定样本中未找到公司公告/年报级线下门店机器人合作证据，按当前严格口径为 0/10，未达到 5/10 门槛；由于 CCFA 或同等公开排名与逐家公司公告/年报全文尚未补齐，该结果只作为第一轮未通过，不能最终否定。
- **跨场景候选池**: 场景选择标准从“生活近/场景亲近感”修正为“1 年内真实订单或试点转生产”。全部具身智能/机器人应用场景纳入；客户案例和媒体报道可作为入池最低证据，硬来源用于后续加权。初步入池场景包括汽车制造/工业制造人形机器人、仓储物流/履约中心机器人、酒店/咖啡/商业服务人形机器人、电力设施/数据中心/国企采购型场景、医疗手术机器人。

## [2026-06-10] synthesis | 候选池反馈与平台工程师角色收敛

- **变更**: 更新 [[robotics-embodied-ai/research-notes/cross-scenario-near-term-landing-candidate-pool-2026-06-10|具身智能短期落地跨场景候选池]] 和 [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]]，将决策变量从场景差异转向角色类型。
- **澄清结果**: 医疗手术机器人因过于硬核，从职业切入候选中降级为“排除 / 仅作行业观察”；其他候选场景当前没有明显区别。下一层优先比较系统工程师、平台工程师、数据处理 / 数据闭环相关角色，其中平台工程师是第一优先验证方向。平台工程师的关键吸引力是：既能迁移已有的软件平台经验，也能逐步获得具身智能全局认知。
- **取舍规则**: 如果岗位只能强满足一个吸引点，优先选择经验迁移更强；当前路径是先有工作进入行业，再通过真实项目逐步拓展全局认知。
- **JD 信号**: 强迁移岗位内容包括运营系统开发、后端开发、仿真平台开发；相对边界是离本体控制和“大脑”核心技术稍远一点，因为当前没有嵌入式编程和大模型训练经验，本体控制和大脑核心技术不适合作为第一入口。
- **学习飞轮**: “先进入行业”的关键价值是接触真实场景和相关人才，从而更快积累行业理解和经验。
- **时间窗口**: 年龄、行业升温和进入者增多会让未来机会变少、竞争加大，因此需要优先选择能较快入场并快速积累经验的岗位路径。
- **较快入场标准**: 优先选择把通用软件平台能力作为硬要求、把机器人领域知识作为可补齐能力的岗位；反向信号是把控制算法、运动规划、嵌入式实时系统、强化学习或大模型训练作为硬门槛。
- **下一步**: 围绕“具身智能/机器人平台工程师”做岗位/JD/公司信号外部调研，优先验证岗位是否能复用平台工程、基础设施、工程效率、数据平台、运营平台、仿真/评测平台等既有经验。

## [2026-06-10] research | 平台工程师 JD 快速入场扫描

- **变更**: 新增 [[robotics-embodied-ai/research-notes/platform-engineer-jd-entry-scan-2026-06-10|具身智能平台工程师 JD 快速入场扫描]] 和 `raw/robotics-embodied-ai/data/platform_engineer_jd_samples_2026-06-10.csv`；更新 [[robotics-embodied-ai/sources|机器人来源表]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/06-career-view|机器人求职与学习视角]] 和 [[index|Knowledge Index]]。
- **初步结果**: 第一轮样本支持“通用软件平台能力是硬要求、机器人领域知识可补齐”的快速入场标准。优先岗位族群为后端 / 云端 / Fleet / RobotOps 平台、数据管线 / 数据闭环 / 评测平台、仿真平台和运营系统。
- **限制**: 国内公开可抓取 JD 样本暂以宇树为主，智元等公司需下一轮通过飞书招聘页、猎聘、Boss 直聘或内推渠道补齐具体岗位文本；1X 样本仅作为海外岗位形态参照。

## [2026-06-11] research | LIBERO 终身学习仿真平台调研

- **变更**: 新增 [[robotics-embodied-ai/research-notes/libero-lifelong-robot-learning-platform-2026-06-11|LIBERO 终身学习仿真平台调研]]；更新 [[robotics-embodied-ai/sources|机器人来源表]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]] 和 [[index|Knowledge Index]]。
- **来源**: 复用 `SRC-robotics-119` LIBERO 官方文档；新增 `SRC-robotics-169` 至 `SRC-robotics-173`，覆盖 LIBERO 原论文、GitHub 仓库、LIBERO-PRO、LIBERO-Para 和 2026 年 manipulation benchmark 审计论文。
- **初步结果**: LIBERO 适合作为 VLA/IL 和终身机器人学习的入门评测平台，可用于平台工程作品集中的 benchmark runner、evaluation service、model adapter 和 robustness harness；但固定 LIBERO 分数不能直接代表真实机器人泛化能力，应与扰动评测、多 benchmark 和真机 rollout 组合使用。

## [2026-06-11] research | 开源具身智能训练与评估数据集横向调研

- **变更**: 新增 [[robotics-embodied-ai/research-notes/open-embodied-ai-datasets-comparison-2026-06-11|开源具身智能训练与评估数据集横向调研]] 和 `raw/robotics-embodied-ai/data/open_embodied_ai_datasets_comparison_2026-06-11.csv`；更新 [[robotics-embodied-ai/sources|机器人来源表]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]] 和 [[index|Knowledge Index]]。
- **来源**: 复用已有 OXE、DROID、RoboMIND、AgiBot、RoboTwin、MimicGen、ALOHA/Mobile ALOHA、LeRobot、LIBERO 来源；新增 `SRC-robotics-174` 至 `SRC-robotics-182`，覆盖 BridgeData V2、RH20T、CALVIN、RLBench、Meta-World、ManiSkill3、RoboCasa、RoboTwin 2.0 和 Galaxea Open-World Dataset。
- **初步结果**: 数据集应按用途分层理解：预训练/跨本体混合、真实机器人微调/后训练、特定能力数据集、仿真与评估 benchmark。格式上研究生态仍偏 RLDS/OXE，工程互通正在向 LeRobot v3 收敛；真实部署能力不能只看 benchmark 分数，必须结合任务完整度、失败/接管标注、元数据和真机 rollout。

## [2026-06-11] research | JEPA 核心原理快速调研

- **变更**: 新增 [[_concepts/joint-embedding-predictive-architecture|Joint-Embedding Predictive Architecture]] 概念页和 [[ai/research-notes/jepa-core-principles-2026-06-11|JEPA 核心原理快速调研]]；更新 [[_concepts/README|Concepts Layer]]、[[ai/research-notes/README|AI Research Notes]]、[[ai/00-index|AI 相关 - 研究入口]] 和 [[index|Knowledge Index]]。
- **来源**: 在 `knowledge/ai/sources.csv` 登记 `SRC-ai-025` 至 `SRC-ai-032`，覆盖 LeCun 2022 AMI 位置论文、Meta I-JEPA/V-JEPA/V-JEPA 2 官方说明、I-JEPA/V-JEPA/V-JEPA 2 原论文和 2026 年 LeWorldModel 后续研究。
- **初步结果**: JEPA 应理解为“在 latent space 预测目标/未来表示”的非生成式自监督世界模型路线；其当前价值主要在高效表征学习、视频物理理解和短程机器人规划信号，长程分层规划和真实世界可靠性仍是未解决问题。

## [2026-06-11] research | 集成电路 AI 芯片全球上市公司初筛

- **变更**: 更新 [[integrated-circuits/00-index|集成电路研究入口]]、[[integrated-circuits/01-industry-map|产业链地图]]、[[integrated-circuits/02-technology-and-products|技术和产品]]、[[integrated-circuits/03-market-and-policy|市场与政策]]、[[integrated-circuits/04-companies|公司与竞争]]、[[integrated-circuits/05-investment-view|投资视角]]、[[integrated-circuits/06-career-view|求职与学习视角]]；新增 [[integrated-circuits/07-ai-chip-global-supply-chain-and-stock-screen-2026-06-11|AI 芯片全球上市公司、供应链关系与股票初筛]] 和 `raw/integrated-circuits/data/ai_chip_listed_company_universe_2026-06-11.csv`。
- **范围**: 覆盖 AI GPU/ASIC、HBM、晶圆代工、设备、EDA/IP、先进封装测试、PCB/载板和中国国产替代链。供应链关系仅记录公开财报、公告或公开报道中明确出现的关系；未披露客户不做猜测。
- **来源**: 在 `knowledge/integrated-circuits/sources.csv` 登记 `SRC-ic-001` 至 `SRC-ic-035`，包含 NVIDIA FY2026 财报、StockAnalysis/CompaniesMarketCap market-cap 页面、TSMC/ASML/AMD/Broadcom/SK hynix/Micron 公开报道和中国公司待补来源占位。
- **待继续**: A/H/日韩台公司仍需补最新市值、估值、财务指标和年报原文；SIA/WSTS、TSMC transcript、ASML/TEL/Advantest、中国上市公司年报需要转为 raw artifact 并提高证据等级。
- **2026-06-11 追加**: 在 `ai_chip_listed_company_universe_2026-06-11.csv` 中补充 `pe_ttm`、`forward_pe`、`pe_data_date`、`pe_source`、`pe_notes`。当前 38 家公司中 24 家有 TTM PE，19 家有 forward PE；A/H 股和部分台股公司仍需下一轮用本地行情源补齐。

## [2026-06-23] research | AIRSPEED 具身智能数据生产平台调研

- **变更**: 新增 [[robotics-embodied-ai/research-notes/airspeed-data-production-platform-2026-06-23|AIRSPEED 具身智能数据生产平台调研]]、[[_sources/airspeed-open-source-data-production-platform|AIRSPEED 来源组]]、[[_entities/AIRSPEED|AIRSPEED]]；更新 [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]、[[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]]、[[_sources/README|Sources Layer]]、[[_entities/README|Entities Layer]] 和 [[index|Knowledge Index]]。
- **来源**: 在 `knowledge/robotics-embodied-ai/sources.csv` 登记 `SRC-robotics-183` 至 `SRC-robotics-188`，覆盖 AIRSPEED 官网、技术报告、EAI 数据工程综述、英文/中文技术转移报告和 GitHub README；保存 HTML/PDF/README raw artifact，并为 PDF 生成 `pdftotext` sidecar，更新 `source_capture_manifest.csv`。
- **初步结果**: AIRSPEED 应分版本理解：当前 GitHub v1.3 可复用能力偏 ROS2/YAML/HDF5/LeRobot 转换的数据采集核心；官网/论文/技术转移报告描述的完整平台覆盖数据采集、仿真生成和数据集构建。商业化报告中的客户、融资、标准参与等 claim 暂标记为待独立验证。
- **待继续**: clone 仓库做代码级验证，核验 license、release、converter、ROS2 mock 采集、LeRobot v3 导出；独立验证技术转移报告中的客户、融资和标准化 claim。

## [2026-06-23] research | dora 1.0 vs ROS 2 调研

- **变更**: 新增 [[robotics-embodied-ai/research-notes/dora-1-vs-ros2-2026-06-23|dora 1.0 vs ROS 2 调研]]；更新 [[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]、[[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]] 和 [[index|Knowledge Index]]。
- **来源**: 在 `knowledge/robotics-embodied-ai/sources.csv` 登记 `SRC-robotics-189` 至 `SRC-robotics-199`，覆盖 dora 官网、GitHub README、PyPI、GitHub v0.5.0 release、DORA 论文、dora benchmark、ROS 2 release/nodes/QoS 官方文档和 ROS 2 综述论文；已生成 raw artifacts 并更新 `raw/robotics-embodied-ai/documents/source_capture_manifest.csv`。
- **初步结果**: dora 更适合作为高带宽 AI dataflow runtime，与 ROS 2 bridge 组合承担 perception/VLA/inference、record/replay 和 observability；ROS 2 仍更适合作为真实机器人硬件、驱动、控制、规划和生态底座。
- **限制**: dora 官网称 `1.0.0-rc1`，但 PyPI/GitHub 稳定版本为 `0.5.0`，本文将“dora 1.0”按官网/RC 能力主张处理；`SRC-robotics-190` dora guides 自动抽取失败，需后续通过官网 `/book`、GitHub raw docs 或浏览器手工补采。

## [2026-06-29] research | LiDAR 世界模型训练论文与方案调研

- **变更**: 新增 [[robotics-embodied-ai/research-notes/lidar-world-model-training-2026-06-29|激光雷达数据融合进入世界模型训练论文与方案调研]]；更新 [[_entities/LiDAR|LiDAR 激光雷达]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]] 和 [[index|Knowledge Index]]。
- **来源**: 在 `knowledge/robotics-embodied-ai/sources.csv` 登记 `SRC-robotics-200` 至 `SRC-robotics-217`，覆盖 Sense, Imagine, Act、MUVO、Copilot4D、OccWorld、LidarDM、OccSora、BEVWorld、Drive-OccWorld、DFIT-OccWorld、OccLLaMA、AD-L-JEPA、RoboOccWorld、LiSTAR、LiDAR navigation DreamerV3、AD-LiST-JEPA、HERMES++、GEM 和 UniDriveDreamer；已生成 raw artifacts 并更新 `raw/robotics-embodied-ai/documents/source_capture_manifest.csv`。
- **初步结果**: LiDAR 融入 world model 训练的主流方案分为 LiDAR-native generative model、BEV/occupancy world model、camera-LiDAR unified latent、JEPA latent predictive model 和移动机器人 Dreamer 类导航模型；若目标是规划安全，BEV/occupancy 路线优先；若目标是数据合成，LiDAR-native 路线优先。
- **限制**: 本轮主要抓取 arXiv 摘要页作为 raw artifact，尚未下载 PDF 或做代码级复现；`SRC-robotics-210` 为 HTML fallback。下一轮应为重点论文建立 `knowledge/_sources/` source card，并补 PDF/key-info 级证据。

## [2026-06-29] ingest | 七个行业初步调研补齐

- **变更**: 补齐 [[6g/00-index|6G]]、[[aerospace/00-index|航空航天]]、[[biopharma/00-index|生物医药]]、[[brain-computer-interface/00-index|脑机接口]]、[[future-energy/00-index|未来能源]]、[[low-altitude-economy/00-index|低空经济]]、[[quantum-technology/00-index|量子科技]] 的标准初调页、sources.csv、source capture index 和 raw source notes。
- **来源**: 以 `十四五规划纲要`、`2024年政府工作报告`、`未来产业实施意见` 为共同政策底座，并为 6G、航空航天、生物医药、脑机接口、未来能源、低空经济、量子科技分别登记行业专属来源。
- **限制**: 本轮 raw artifact 多为 analyst source note，适合做初步 traceability；高价值政策、PDF、年报和标准仍需后续运行完整网页/PDF 抽取并拆成 source card / claim。

## [2026-06-29] ingest | AI 总行业分析重做

- **变更**: 重写 [[ai/00-index|AI 研究入口]]、[[ai/01-industry-map|产业链地图]]、[[ai/02-technology-and-products|技术与产品]]、[[ai/03-market-and-policy|市场与政策]]、[[ai/04-companies|公司与竞争]]、[[ai/05-investment-view|投资视角]]、[[ai/06-career-view|求职与学习视角]]；更新 [[ai/00-source-capture-index|AI Source Capture Index]] 和 [[ai/research-notes/README|AI Research Notes]]。
- **来源**: 追加 `SRC-ai-033` 至 `SRC-ai-046`，覆盖十四五规划、新一代人工智能发展规划、2024 年政府工作报告、生成式人工智能服务管理暂行办法、未来产业实施意见、DeepSeek、Qwen、文心一言、Kimi、智谱、腾讯混元、华为昇腾、寒武纪和 ModelScope。
- **初步结果**: AI 行业不再只按 Scale AI / 数据基础设施理解，而改为“算力与基础设施 - 基础模型 - 数据与评测 - 应用/Agent - 安全合规”的总产业链框架；投资与职业页分别强调国产算力、AI 平台、应用 ROI、数据评测和安全合规。
- **限制**: 本轮新增来源为 analyst source note，模型备案清单、公司财报、API 收入、国产算力订单、企业续费率和地方 AI 政策仍需下一轮补硬证据。

## [2026-06-29] research | 具身智能训练数据价值评估框架

- **变更**: 新增 [[robotics-embodied-ai/research-notes/robot-training-data-value-evaluation-2026-06-29|具身智能训练数据价值评估框架]]；更新 [[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]] 和 [[index|Knowledge Index]]。
- **来源**: 复用 LeRobot、DROID、RoboMIND、AgiBot World、Data Scaling Laws、失败/接管数据、AIRSPEED 与 EAI data engineering survey 等已有来源；并以 2026-06-29 在线核验的 arXiv/官方页面作为当前性补充。
- **初步结果**: 数据价值不应按小时数或 episode 数单独估算，而应按 `Expected Capability Lift x Reuse Multiplier x Trust Multiplier / Fully Loaded Cost and Risk` 判断；采集前做任务缺口和数据组合打分，采集中做同步/标定/分布/QC stop-loss，采后用 holdout rollout 或 ablation 验证边际提升。

## [2026-07-02] ingest | Bilibili AI/具身智能每日视频采集

- **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-02|Bilibili AI Daily Run 2026-07-02]]；处理 1 个 Bilibili 视频 source packet。
- **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
- **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

## [2026-07-02] synthesis | MATLAB/Simulink Agentic AI 工具链视频调研

- **变更**: 新增 [[_syntheses/matlab-simulink-agentic-ai-tools-bilibili-2026-07-02|MATLAB/Simulink Agentic AI 工具链视频调研]]；更新 [[index|Knowledge Index]]。
- **来源**: 复用 [[_sources/bilibili-bv1bbtv6ueaf-5-skill-codex-matlab|Bilibili source card]] 与 raw transcript，并核验 MathWorks 官方 `matlab` GitHub 组织、`matlab-mcp-server`、`matlab-agentic-toolkit`、`simulink-agentic-toolkit`、`agent-skills-playground`。
- **初步结果**: 工程软件 Agent 化需要 MCP/API 工具层、领域 skills 和仿真/测试反馈闭环；MATLAB/Simulink 是较早成体系的样板，后续应扫描国产工业软件的 agent-ready 能力。

## [2026-07-02] synthesis | Bilibili 具身智能与 AI 工具链线索

- **变更**: 新增 [[_syntheses/bilibili-embodied-ai-signals-2026-07-02|Bilibili 具身智能与 AI 工具链线索 2026-07-02]]；更新 [[index|Knowledge Index]]、[[robotics-embodied-ai/sources|机器人来源表]] 和 [[ai/sources|AI 来源表]]。
- **来源**: 使用每日 Bilibili 自动化中断前成功落盘的 source cards 与 raw transcripts，覆盖 ZR-0/VLA、VLA 数据基建、GENIE SIM、TensorRT、ROS2/LiDAR、LeWorldModel、机械臂安全和 ForceBand。
- **限制**: Bilibili 视频仅作为 B 级线索；`BV1ogTT6PE2s` transcript 无有效正文，不纳入观点抽取；ZR-0、ForceBand、GENIE SIM 和安全规范相关 claim 需要一级来源验证。

## [2026-07-03] research | 具身大模型物理理解评估框架

- **变更**: 新增 [[robotics-embodied-ai/research-notes/embodied-model-physical-understanding-evaluation-2026-07-03|具身智能大模型物理理解能力评估框架]]；更新 [[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]、[[robotics-embodied-ai/00-index|机器人研究入口]] 和 [[index|Knowledge Index]]。
- **来源**: 复用 [[_sources/roboalign-r1-reward-aligned-robot-video-world-models|RoboAlign-R1]]、[[news/2026-06-05-nvidia-cosmos-3-getting-started-plan|NVIDIA Cosmos 3 上手调研]]、[[ai/research-notes/jepa-core-principles-2026-06-11|JEPA 核心原理快速调研]]；新增 `SRC-robotics-218` 至 `SRC-robotics-223`，覆盖 RT-2、OpenVLA、Meta V-JEPA 2、Gemini Robotics、EWMBench 和 World Action Models。
- **初步结果**: 判断具身大模型是否理解物理规律，应从 `observation + instruction -> action` 的动作生成评估，升级为 `state + candidate action -> future state / outcome / risk` 的动作条件预测与闭环规划收益评估；核心方法包括反事实预测、minimal physical pairs、forward/inverse dynamics、policy-only vs world-model-assisted A/B 和多模态接触/空间约束。
- **限制**: 本轮为 query-style 框架调研，新增外部来源已登记但尚未执行 raw artifact 抽取；若进入正式 benchmark 复现或公司尽调，应补采 PDF/HTML、建立 source card，并对 judge/reward model 做人评和真机交叉验证。

## [2026-07-02] automation | Bilibili AI/具身智能每日增量重跑

- **变更**: 更新 [[_syntheses/bilibili-ai-daily-run-2026-07-02|Bilibili AI Daily Run 2026-07-02]]、[[_syntheses/bilibili-embodied-ai-signals-2026-07-02|Bilibili 具身智能与 AI 工具链线索 2026-07-02]]、[[index|Knowledge Index]] 和 [[robotics-embodied-ai/sources|机器人来源表]]；新增 3 个 Bilibili source cards 与 raw transcripts。
- **来源**: 新增 `BV1oPTq6SENP` 家庭人形机器人访谈、`BV1wCTu6nEF2` GENIE SIM 3.0 闭环仿真上篇、`BV1cL7p6VEH9` VLA 入门教程；均为 B 级视频线索，需一级来源交叉验证。
- **失败**: 选中的 `BV1bGxEz7EWa`、`BV1UR7H6dEy5`、`BV1v17Y6aE2L`、`BV161jy6MEwt` 无可用平台字幕；`BV1UR7H6dEy5` 外部 Volcengine ASR 在 300 秒超时，最终用禁用 ASR 的重跑记录为失败。
- **限制**: 本轮第一批默认 ASR 超时路径需人工中断；脚本当前未捕获 `subprocess.TimeoutExpired`，后续可修复为 per-video failed result，避免整批退出。

## [2026-07-03] ingest | Bilibili AI/具身智能每日视频采集

- **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-03|Bilibili AI Daily Run 2026-07-03]]；处理 7 个 Bilibili 视频 source packet。
- **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
- **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

## [2026-07-03] synthesis | Bilibili AI 与具身智能线索

- **变更**: 新增 [[_syntheses/bilibili-ai-embodied-signals-2026-07-03|Bilibili AI 与具身智能线索 2026-07-03]]；更新 [[index|Knowledge Index]] 中 7 个 Bilibili source packet 的 synthesis 指向。
- **来源**: 只使用 2026-07-03 每日自动化中 `status=processed` 的 7 个 source cards 与 raw transcripts，覆盖 PhysisForcing、家用人形机器人产品定义、GENIE SIM 3.0 上篇、VLA 入门、SLAM/ROS、数值优化和 ESP Cloud/ESP32。
- **限制**: `BV1bGxEz7EWa` 为 failed，不纳入综合；PhysisForcing 指标、GENIE SIM 能力、ESP Cloud 项目边界、家用机器人关节参数和市场判断均需一级来源验证。

## [2026-07-03] synthesis | Bilibili 单视频深度调研产物修正

- **变更**: 新增 [[_syntheses/bilibili-physisforcing-world-simulator-deep-dive-2026-07-03|PhysisForcing 物理一致世界模拟器视频深度调研]] 和 [[_syntheses/bilibili-esp-claw-embedded-ai-deep-dive-2026-07-03|ESP-Claw 自然语言驱动嵌入式开发视频深度调研]]；更新 [[_syntheses/bilibili-ai-daily-run-2026-07-03|Bilibili AI Daily Run 2026-07-03]]、[[_syntheses/bilibili-ai-embodied-signals-2026-07-03|Bilibili AI 与具身智能线索 2026-07-03]]、[[index|Knowledge Index]]、[[ai/sources|AI 来源表]] 和 [[robotics-embodied-ai/sources|机器人来源表]]。
- **来源**: 用 arXiv `2606.28128` 校验 PhysisForcing 视频 claim；用乐鑫 ESP-Claw 官网、文档、GitHub、ESP32-S3 与 ESP-IDF 官方资料校验 `BV1PCjA6bEi4` 中的 ESP Cloud/Club 线索，并统一项目名为 ESP-Claw。
- **规范修正**: 每日 Bilibili 自动化未来应以“每个 selected + processed 视频一篇独立深研页”为主要产物，横向综述只作为导航/交叉线索，不替代单视频深研。

## [2026-07-04] ingest | Bilibili AI/具身智能每日视频采集

- **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-04|Bilibili AI Daily Run 2026-07-04]]；处理 1 个 Bilibili 视频 source packet。
- **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
- **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

## [2026-07-04] synthesis | Agent 时代 GUI 与 Headless 软件视频深研

- **变更**: 新增 [[_syntheses/bilibili-agent-gui-headless-software-deep-dive-2026-07-04|Agent 时代 GUI 与 Headless 软件视频深度调研]]；更新 [[_sources/bilibili-bv1bktk69edd-agent-500-gui|Bilibili source card]] 和 [[index|Knowledge Index]]。
- **来源**: 使用 `BV1bKTk69EDD` source card 与 raw transcript，并用 MCP、Claude Code overview、Claude Code skills、Vercel AI SDK 官方文档交叉验证 Agent-ready 软件接口、skills 和工具调用趋势。
- **初步结果**: GUI 不应被简单否定；AI 应用的关键分层正在变成 human UI、agent interface 和 workflow assets。投资/职业判断应同时评估界面信任层、工具接口、上下文资产、权限审计和 skill/workflow 复用能力。
- **限制**: 视频中关于飞书、Google Workspace、Supabase、MongoDB、瑞幸、KFC、微信等具体产品开放 CLI/MCP 的说法尚未逐项核验，暂作为访谈观点和后续验证任务。

## [2026-07-05] ingest | Bilibili AI/具身智能每日视频采集

- **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-05|Bilibili AI Daily Run 2026-07-05]]；处理 3 个 Bilibili 视频 source packet。
- **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
- **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

## [2026-07-05] synthesis | Bilibili 单视频深研三篇

- **变更**: 新增 [[_syntheses/bilibili-hapmorph-haptic-feedback-deep-dive-2026-07-05|HapMorph 触觉反馈视频深度调研]]、[[_syntheses/bilibili-physical-ai-time-scale-deep-dive-2026-07-05|Physical AI 时间尺度视频深度调研]] 和 [[_syntheses/bilibili-vla-tutorial-deep-dive-2026-07-05|VLA 入门教程视频深度调研]]；更新 [[_syntheses/bilibili-ai-daily-run-2026-07-05|Bilibili AI Daily Run 2026-07-05]]、[[index|Knowledge Index]]、[[robotics-embodied-ai/sources|机器人来源表]] 和机器人来源抽取 manifest。
- **来源**: 只综合本次自动化中 `status=processed` 的 `BV12XTM6sEGF`、`BV1y3T46NEUf`、`BV1ifTp62EaV`；用 arXiv `2509.05433` / `SRC-robotics-233` 校验 HapMorph 触觉反馈关键指标，并复用既有 VLA、数据集、评测和工程平台来源。
- **初步结果**: 触觉反馈的关键问题是多属性反馈、人类可辨识与任务闭环价值；Physical AI 需要按多时间尺度系统理解；VLA 学习应从模型扩展到数据 schema、benchmark、真机部署和失败回流。
- **限制**: Bilibili 仍为 B 级线索；GelSight、DIGIT 360、RT-1、RT-2、RoboFlamingo、MDT、RDT、LAPA 等模型/硬件名需要后续补独立 source card 后再推广为事实。

## [2026-07-06] research | 家庭养老机器人公司与方案调研

- **变更**: 新增 [[robotics-embodied-ai/research-notes/home-elderly-care-robots-2026-07-06|家庭养老机器人公司与方案调研]]；更新 [[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]] 和 [[index|Knowledge Index]]。
- **来源**: 复用中国人口老龄化、`机器人+`、北京/上海医疗康养和家庭场景政策来源；在线核验 ElliQ、Hyodol、Joy for All、LOVOT、Labrador、傅利叶、1X、Figure 和 Tesla 官方页面，并用 arXiv `2410.12205`、`2302.12686` 补充老年人采用偏好研究。Weave Isaac 与优必选 UWorld U1 仅作为媒体线索列入待验证。
- **初步结果**: 家庭养老机器人应分为陪伴提醒、远程巡视、移动载物、康复护理和通用家务五层；2026 年更可行的是“AI 照护终端 + 家属 App + IoT + 社区/护理服务”闭环，而不是直接售卖昂贵全能人形机器人。
- **限制**: 本轮未系统抓取中国地方养老机器人招投标、真实家庭部署数量、价格带和留存数据；国内智能家居/IoT 厂商在养老闭环中的角色需下一轮补公司级来源。

## [2026-07-06] research | 中国养老行业头部公司与科技创新创业公司

- **变更**: 新建 `eldercare` 行业工作区；新增 [[eldercare/00-index|养老服务与银发科技研究入口]] 和 [[eldercare/04-companies|中国养老行业头部公司与科技创新创业公司]]；更新 [[index|Knowledge Index]]、[[README|Knowledge README]] 和 `tools/industry_registry.json`。
- **来源**: 复用国家统计局 2025 年公报；核验泰康之家、椿萱茂、安康通、金牌护士、亲和源、万物云官网；补充 arXiv 中国社区养老科技研究和毫米波人体感知综述；复用前序家庭养老机器人调研。
- **初步结果**: 养老行业头部应按保险系医养社区、连锁养老运营、居家/社区/机构服务、智慧养老平台、互联网护理和智能硬件分层看；科技创新的近期重点在长护险履约、上门护理、智慧养老指挥中心、无感监测、社区空间科技和康复/护理机器人。
- **限制**: 太保家园、国寿嘉园、大家的家、梧桐人家、九如城、光大养老、福寿康、青松康护、小柏家护等头部候选仍需下一轮补官方项目、床位、城市、收入或招投标证据；本轮不做硬排名。

## [2026-07-06] automation | Bilibili AI/具身智能每日视频采集

- **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-07-06|Bilibili AI Daily Run 2026-07-06]]；更新 [[index|Knowledge Index]]。
- **来源**: 运行 `uv run python tools/bilibili_ai_daily_research.py --limit 20 --json` 获取默认收藏夹最新 20 个候选。
- **结果**: 20 个候选全部为 `skipped_duplicate`；`needs_model_review=0`、模型选中 0、`processed=0`、`failed=0`，因此未进入第二阶段、未新增 transcript、source card 或单视频深研页。
- **限制**: 本轮没有新视频内容可综合；后续运行继续只处理 selected + processed 视频。

## [2026-07-06] synthesis | VLA&世界模型数据基建平台系统设计

- **变更**: 新增 [[robotics-embodied-ai/research-notes/vla-world-model-data-infrastructure-platform-design-2026-07-06|VLA&世界模型数据基建平台系统调研与设计]]；更新 [[index|Knowledge Index]]。
- **来源**: 以 [[_sources/bilibili-bv1zftq6pea3-vla|BV1ZFTq6pEA3 source card]] 和 `raw/_inbox/transcripts/2026-07-02-bilibili-bv1zftq6pea3-vla.json` 的 15 阶段 SOP 为主线，复用 [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]、[[robotics-embodied-ai/research-notes/airspeed-data-production-platform-2026-06-23|AIRSPEED 调研]]、[[robotics-embodied-ai/research-notes/robot-training-data-value-evaluation-2026-06-29|训练数据价值评估框架]]、[[robotics-embodied-ai/research-notes/open-embodied-ai-datasets-comparison-2026-06-11|开源具身数据集对比]] 和 [[robotics-embodied-ai/research-notes/dora-1-vs-ros2-2026-06-23|dora vs ROS 2]]。
- **初步结果**: 平台应定位为具身智能数据生产操作系统，核心对象是 episode 和数据飞轮；MVP 应优先做任务契约、采集接入、同步缓存、自动质检、episode builder、多格式导出、dataset registry、baseline 评测和失败补采闭环。
- **限制**: Bilibili 视频仍为 B 级线索；具体性能、成本、QC 阈值、dora/AIRSPEED 复用程度和真实客户 ROI 需要用小规模实采和代码级复现继续验证。

## [2026-07-06] governance | 行业完整调研文档存放规则修正

- **变更**: 将 [[robotics-embodied-ai/research-notes/vla-world-model-data-infrastructure-platform-design-2026-07-06|VLA&世界模型数据基建平台系统调研与设计]] 放入机器人行业 `research-notes/`；更新 [[index|Knowledge Index]]、[[robotics-embodied-ai/00-index|机器人研究入口]]、[[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]] 和 `AGENTS.md`。
- **规则**: 后续完整行业调研文档应写入对应 `knowledge/<industry>/research-notes/`，而不是默认放入 `knowledge/_syntheses/`；`_syntheses/` 主要用于跨行业综合、迁移计划或无明确产业归属的高价值输出。

## [2026-07-07] ingest | Bilibili AI/具身智能每日视频采集

- **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-07|Bilibili AI Daily Run 2026-07-07]]；处理 5 个 Bilibili 视频 source packet。
- **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
- **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

## [2026-07-07] synthesis | Bilibili 单视频深研五篇

- **变更**: 新增 [[_syntheses/bilibili-physical-ai-productivity-revolution-deep-dive-2026-07-07|Physical AI 生产力革命播客视频深度调研]]、[[_syntheses/bilibili-isaac-sim-tutorial-deep-dive-2026-07-07|Isaac Sim 教程视频深度调研]]、[[_syntheses/bilibili-multiview-embodied-perception-deep-dive-2026-07-07|多目具身感知视频深度调研]]、[[_syntheses/bilibili-do-as-i-do-dexterous-video-data-deep-dive-2026-07-07|Do As I Do 灵巧操作视频数据深度调研]] 和 [[_syntheses/bilibili-abot-m05-world-action-model-deep-dive-2026-07-07|ABot-M0.5 世界动作模型视频深度调研]]；更新 [[_syntheses/bilibili-ai-daily-run-2026-07-07|Bilibili AI Daily Run 2026-07-07]]、[[index|Knowledge Index]]、AI/机器人 sources.csv、source cards 和 source capture manifest。
- **来源**: 只综合本次自动化中 `status=processed` 的 `BV17eTk6vETX`、`BV1G8kBBvEzR`、`BV1j9jd6aE7c`、`BV1WfTk6EEZ8`、`BV1F7Ts6WEYj`；用 NVIDIA Isaac Sim/Isaac Lab 官方文档、arXiv `2606.19333` 和 arXiv `2607.00678` 交叉验证关键技术事实。
- **初步结果**: Physical AI 需要按系统工程和产业链分层理解；Isaac Sim 的价值在多传感器仿真、ROS2、synthetic data 和 RL 工具链；多目感知选型应匹配任务和模型目标；Do As I Do 强调观察性视频到机器人轨迹需要严格筛选和重定向；ABot-M0.5 把移动操作 WAM 的瓶颈明确为时间粒度、动作空间和训练/推理条件三层错配。
- **限制**: Bilibili 仍为 B 级线索；摩尔线程 Lambda 平台、高德/AMAP 后续产品化、ABot 代码开放状态、多目设备真实 BOM 和工厂采集 ROI 仍需一级来源或实测验证。

## [2026-07-08] automation | Bilibili AI/具身智能每日视频采集

- **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-07-08|Bilibili AI Daily Run 2026-07-08]]；更新 [[index|Knowledge Index]]。
- **来源**: 运行 `uv run python tools/bilibili_ai_daily_research.py --limit 20 --json` 获取默认收藏夹最新 20 个候选。
- **结果**: 20 个候选全部为 `skipped_duplicate`；`needs_model_review=0`、模型选中 0、`processed=0`、`failed=0`，因此未进入第二阶段、未新增 transcript、source card 或单视频深研页。
- **限制**: 本轮没有新视频内容可综合；后续运行继续只处理 selected + processed 视频。

## [2026-07-08] automation | Bilibili AI/具身智能每日视频采集补跑

- **变更**: 更新 [[_syntheses/bilibili-ai-daily-run-2026-07-08|Bilibili AI Daily Run 2026-07-08]]，新增 [[_sources/bilibili-bv1mgja6cebk-200|千寻智能 Bilibili source card]] 和 [[_syntheses/bilibili-qianxun-intelligence-deep-dive-2026-07-08|千寻智能具身智能公司视频深度调研]]；补充 `knowledge/ai/sources.csv` 与 `knowledge/robotics-embodied-ai/sources.csv`。
- **来源**: 第一阶段候选池 20 个，模型选中 `BV1mgja6CEbK`、`BV1q3TE6AE4b`、`BV1Z7jA6LE8s`；其中仅 `BV1mgja6CEbK` 生成 `raw/_inbox/transcripts/2026-07-08-bilibili-bv1mgja6cebk-200.json` 和 source card。
- **限制**: `BV1q3TE6AE4b` 与 `BV1Z7jA6LE8s` 外部 ASR subprocess 长时间不返回，已中断，未写 source card 或单视频深研页；`BV1mgja6CEbK` 的公司估值、营收、客户、数据规模、Spirit VLA 和政策 claim 均为 B 级线索，需一级来源验证。

## [2026-07-08] tooling | Bilibili ASR/TOS 上传诊断优化

- **变更**: 更新 `tools/bilibili_ai_daily_research.py`、`tools/volcengine_asr.py`、`tools/tos_upload.py` 和 `docs/bilibili_daily_research_automation.md`，为每日 Bilibili 自动化增加 TOS 今日目录检查、上传后 URL 可达性验证、上传失败重试和外部 ASR 进程组超时清理。
- **原因**: 今日补跑中 `BV1q3TE6AE4b` 与 `BV1Z7jA6LE8s` 卡在 external ASR，人工检查 TOS 今日目录只有一个音频文件，说明失败视频可能未成功上传且主脚本缺少明确上传失败反馈。
- **验证**: `uv run python -m unittest tests.test_volcengine_asr tests.test_bilibili_ai_daily_research tests.test_tos_upload` 通过。

## [2026-07-08] governance | Bilibili 失败 case 自主排查规则

- **变更**: 更新 `docs/bilibili_daily_research_automation.md`，新增 `Failed Case Handling And Self-Repair` 规则，要求每日任务对 selected 视频的失败 case 自主定位失败边界、保留证据、bounded retry、能修则修并补测试，只有外部状态不可控时才作为人工 blocker 报告。
- **约束**: 失败视频仍不得伪造 transcript、source card 或单视频深研页；只有 `status=processed` 才进入 durable synthesis。

## [2026-07-08] ingest | Bilibili AI/具身智能每日视频采集

- **变更**: 新增或更新 [[_syntheses/bilibili-ai-daily-run-2026-07-08|Bilibili AI Daily Run 2026-07-08]]；处理 2 个 Bilibili 视频 source packet。
- **来源**: `raw/_inbox/transcripts/` 与 `knowledge/_sources/` 中的 Bilibili 视频转录产物。
- **限制**: 脚本只完成候选筛选、去重、转录和 source card 交接；行业判断仍需 Codex 后续综合，并对关键事实做一级来源交叉验证。

## [2026-07-08] tooling | Bilibili 失败 case 补跑修复

- **变更**: 修复 `tools/bilibili_ai_daily_research.py` 的 dry-run JSON report path 问题、失败日志误触发重复检测问题、TOS 列目录候选检查 runner；修复 `tools/tos_upload.py` 的 SDK list-prefix 路径；同步更新 `docs/bilibili_daily_research_automation.md` 的 TOS 检查命令。
- **原因**: `BV1q3TE6AE4b` 与 `BV1Z7jA6LE8s` 初始重试被 `knowledge/log.md` 中的失败记录误判为 `skipped_duplicate`；TOS 前缀检查落到 S3-compatible fallback signer 时返回 `Unsupported Authorization Type`。
- **验证**: 两个 BV 的 dry-run 均恢复为 `selected` 且 TOS 今日前缀检查返回 3 个对象、无错误；`uv run python -m unittest tests.test_volcengine_asr tests.test_bilibili_ai_daily_research tests.test_tos_upload` 通过 33 个测试。

## [2026-07-08] synthesis | Bilibili 失败 case 单视频深研补齐

- **变更**: 新增 [[_syntheses/bilibili-boden-intelligence-data-infrastructure-deep-dive-2026-07-08|博登智能 Physical AI 数据基建视频深度调研]] 和 [[_syntheses/bilibili-qianxun-intelligence-bv1z7-deep-dive-2026-07-08|千寻智能 BV1Z7jA6LE8s 视频深度调研]]；更新 [[_syntheses/bilibili-ai-daily-run-2026-07-08|Bilibili AI Daily Run 2026-07-08]]、[[index|Knowledge Index]]、AI/机器人 sources.csv。
- **来源**: 只综合本次补跑中 `status=processed` 的 `BV1q3TE6AE4b` 和 `BV1Z7jA6LE8s`；复用 OpenVLA、Open X-Embodiment、NVIDIA GR00T N1 等一级技术来源验证“真实机器人数据 + VLA/动作模型”的行业逻辑。
- **初步结果**: 博登智能视频提供“真实场景网络 + 数据引擎 + 验证体系”的具身数据基建线索；千寻智能 `BV1Z7jA6LE8s` 独立页补充融资、团队、墨子一硬件、Spirit VLA 和客户落地线索。
- **限制**: 两条视频中的公司估值、融资、客户、营收、数据规模、机器人数量、模型指标和订单均未找到足够一级来源支撑，全部保留为 `待验证`。

## [2026-07-08] synthesis | 博登智能商业与技术综述

- **变更**: 新增 [[robotics-embodied-ai/research-notes/boden-intelligence-business-technology-overview-2026-07-08|博登智能商业逻辑、商业计划与技术方案综述]]；更新 [[index|Knowledge Index]]、[[robotics-embodied-ai/00-index|机器人研究入口]] 和 [[robotics-embodied-ai/research-notes/README|机器人研究中间笔记]]。
- **来源**: 基于 [[_syntheses/bilibili-boden-intelligence-data-infrastructure-deep-dive-2026-07-08|博登智能 Physical AI 数据基建视频深度调研]]、[[_sources/bilibili-bv1q3te6ae4b-10-ai|BV1q3TE6AE4b source card]] 和 `raw/_inbox/transcripts/2026-07-08-bilibili-bv1q3te6ae4b-10-ai.json`，并复用 [[robotics-embodied-ai/research-notes/vla-world-model-data-infrastructure-platform-design-2026-07-06|VLA&世界模型数据基建平台系统调研与设计]] 的 episode-first 数据平台框架。
- **初步结果**: 将博登智能叙事整理为“自动化标注现金流 + 真实场景训练基地 + 跨本体数据采集 + 数据资产治理 + 现实验证闭环”的 Physical AI 数据工厂商业计划，并拆解 BASE、BreakRobot、Blink、BIBOT 四类产品角色。
- **限制**: 本文仍不新增一级来源验证；公司主体、产品名、融资、客户、基地规模、产能、数据交易和订单 claim 均保持 `待验证`。

## [2026-07-09] automation | Bilibili AI/具身智能每日视频采集

- **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-07-09|Bilibili AI Daily Run 2026-07-09]]；更新 [[index|Knowledge Index]]。
- **来源**: 运行 `uv run python tools/bilibili_ai_daily_research.py --limit 20 --json` 获取默认收藏夹最新 20 个候选。
- **结果**: 20 个候选全部为 `skipped_duplicate`；`needs_model_review=0`、模型选中 0、`processed=0`、`failed=0`，因此未进入第二阶段、未新增 transcript、source card 或单视频深研页。
- **限制**: 本轮没有新视频内容可综合；后续运行继续只处理 selected + processed 视频。

## [2026-07-10] automation | Bilibili AI/具身智能每日视频采集

- **变更**: 新增 [[_syntheses/bilibili-ai-daily-run-2026-07-10|Bilibili AI Daily Run 2026-07-10]]；更新 [[index|Knowledge Index]]。
- **来源**: 运行 `uv run python tools/bilibili_ai_daily_research.py --limit 20 --json` 获取默认收藏夹最新 20 个候选。
- **结果**: 20 个候选全部为 `skipped_duplicate`；`needs_model_review=0`、模型选中 0、`processed=0`、`failed=0`，因此未进入第二阶段、未新增 transcript、source card 或单视频深研页。
- **限制**: 本轮没有新视频内容可综合；后续运行继续只处理 selected + processed 视频。
