---
title: Wiki Log
type: log
date_created: 2026-05-29
last_updated: 2026-06-11
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
