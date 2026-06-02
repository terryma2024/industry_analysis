---
title: 具身智能数据采集和服务公司对比
type: synthesis
date_created: 2026-06-02
last_updated: 2026-06-02
sources:
  - https://www.agibot.com/article/231/detail/54.html
  - https://huggingface.co/datasets/agibot-world/AgiBotWorld-Alpha
  - https://www.wondercv.com/xiaozhao/agibot-2026-intern-shanghai-shenzhen-7150-291a6c/
  - https://www.sohu.com/a/1017597949_99919085
  - https://cn.chinadaily.com.cn/a/202512/29/WS695222e7a310942cc4999198.html
  - https://www.ithome.com/0/927/552.htm
  - https://www.wondercv.com/xiaozhao/tars-robotics-shanghai-2026-spring-9018-c6cedb/
  - https://cn.genrobot.com/
  - https://cn.genrobot.com/why
  - https://www.tmtpost.com/7813011.html
  - https://www.maxinsights.ai/
  - https://tolacapital.com/portfolio/maxinsights
  - https://www.x2robot.com/
  - https://www.stdaily.com/web/gdxw/2025-06/23/content_359003.html
  - https://sasac.tj.gov.cn/GZJG8342/JGDT5617/202507/t20250701_6970780.html
  - https://www.ctdsb.net/c1476_202603/2689670.html
  - https://cn.linkedin.com/jobs/view/%E5%85%B7%E8%BA%AB%E6%99%BA%E8%83%BD%E7%AE%97%E6%B3%95%E6%80%BB%E7%9B%91-at-%E5%B8%95%E8%A5%BF%E5%B0%BC%E6%84%9F%E7%9F%A5%E7%A7%91%E6%8A%80-4416783283
tags:
  - industry/robotics-embodied-ai
  - data
  - company-analysis
  - embodied-ai
status: draft
---

# 具身智能数据采集和服务公司对比

> [!summary]
> 本页对用户指定的 7 家具身智能数据采集和服务相关公司做横向分析。结论先行：**智元、它石、自变量更像“模型/本体公司自带数据闭环”；简智、Maxinsights、补天石更像“中立数据基础设施”；帕西尼是“触觉传感器/灵巧手/本体公司外溢出的全模态数据工厂”。** 因此不能只用“数据外包公司”框架看待它们。

## 一句话结论

| 区域 | 公司 | 当前定位 | 数据服务强度 | 证据置信度 | 核心判断 |
|---|---|---:|---:|---:|---|
| 上海 | 智元 | 整机/模型/开放数据生态 | 高 | 高 | 以整机和模型为主，数据开放和数采工厂是生态入口与模型训练底座，不一定是独立 DaaS 收入主线。 |
| 上海 | 补天石 | 具身数据 Infra 初创 | 高 | 低-中 | 方向最像“机器人版自动驾驶数据闭环/MLOps”，但公开资料少，需工商、招聘、客户验证。 |
| 上海 | 它石 | 全栈具身模型+本体+Human-centric 数据 | 高 | 中-高 | 以 WIYH/SenseHub/AWE 形成“数据-模型-本体”闭环，人才配置明显偏全栈研发而非纯运营数采。 |
| 苏州 | 简智 GenRobot | 中立数据基建/采集设备/数据治理 | 极高 | 中-高 | 最纯的数据基础设施玩家之一，打法是 wearable/无本体采集 + Gen Matrix 治理 + 分级 DaaS。 |
| 苏州 | Maxinsights | 全球化 Physical AI 数据平台 | 高 | 中 | 海外客户和全球采集网络叙事强，岗位显示算法/平台能力，但中国主体和苏州落点需继续核验。 |
| 深圳 | 自变量 | 端到端具身模型+轮式双臂本体 | 中 | 高 | 数据是其 WALL-A/QUANTA 的内生训练资源，不是公开数据服务商；适合作为数据客户/对标模型公司。 |
| 深圳 | 帕西尼 | 触觉硬件+灵巧手/人形+超级数据工厂 | 极高 | 高 | 最强差异化是触觉真值和 PMEC/Soma Redirect 路线，规模化工厂领先，但需验证数据质量、开放程度和商业授权。 |

## 行业位置

具身智能数据服务的核心不是“采视频”，而是**把真实物理交互转成可训练、可复现、可迁移的数据资产**。最小闭环包括：

1. 任务和场景设计：家庭、商超、工业、物流、康养、办公等。
2. 采集终端：真机遥操作、第一视角、手套/动捕、触觉传感器、UMI-like 工具。
3. 数据治理：时间同步、轨迹还原、清洗、切片、标注、失败/恢复片段、质量报告。
4. 标准格式：LeRobot、HDF5、Zarr、MCAP、RLDS/OXE 等。
5. 模型验证：模仿学习、VLA、[[../../_concepts/vision-language-tactile-action|Vision-Language-Tactile-Action (VLTA/VTLA)]]、RL、Sim2Real、真机回放。

这 7 家公司的差异主要体现在：谁拥有本体、谁拥有采集终端、谁拥有数据治理平台、谁能把数据喂回模型并在真机场景验证。

### 术语：Vision-Language-Tactile-Action

Vision-Language-Tactile-Action 是一种面向机器人操作的多模态模型/数据范式：把视觉、语言指令、触觉/力觉反馈和动作轨迹放在同一个训练闭环里，让机器人不仅能“看懂并执行”，还可以根据接触、滑移、压力、力矩等反馈微调动作。按英文首字母更严格应写作 **VLTA**；部分公司或媒体也写作 **VTLA**，本页在引用公司资料时保留原文写法，概念上统一指向 [[../../_concepts/vision-language-tactile-action|Vision-Language-Tactile-Action]]。

和 VLA 相比，VLTA/VTLA 的增量在 tactile：它更适合插接、柔性物体整理、拧盖、擦拭、装配、灵巧手抓握等“接触状态决定成败”的任务。对数据公司来说，这意味着竞争不只是采集更多视频，而是要提供触觉/力觉标定、时间同步、接触事件切片、失败/恢复标签和可训练 action 表示。

## 上海

### 智元机器人

**发展历史。** 智元是上海具身智能整机与生态公司，已有远征 A2、灵犀/X 系列、G 系列、D 系列、C5、OmniHand、VR Teleoperation Kit 等产品线。官网披露上海浦东、北京、深圳、上海奉贤制造工厂和上海浦东 Giga Data Factory 地址。其 AgiBot World Alpha 在 Hugging Face 上 2024-12-30 发布，后续持续更新；AGIBOT WORLD 2026 则进一步强调真实场景、数字孪生和分阶段开放。

**解决方案/产品。** 数据侧核心是 AgiBot World / AGIBOT WORLD 2026：真机数据、仿真数据、层级标注、错误恢复轨迹、开源数据集。硬件侧包含 G2 采集平台、Swift Picker、OmniHand、VR 遥操作套件等。官方产品菜单中也直接列出“Integrated Data-solution for Embodied AI”和“Data Service”。

**技术路线。** 智元走“真机遥操作 + 工业级数据处理 + 开源生态”的路线。AGIBOT WORLD 2026 官网称数据包含 RGB(D)、触觉、LiDAR、IMU、全身关节状态，并经过清洗验证；AgiBot World Alpha 卡片显示 10 万+ trajectories、100 台机器人、100+ real-world scenarios，并提供转换到 LeRobot format 的脚本。

**岗位/人才投入。** 2026 实习招聘覆盖具身基础模型、感知融合、多模态动作生成和机器人数据驱动算法。具身基础模型岗要求参与 VLM/VLA/VideoGen 预训练、后训练、RL、触觉/动作融合、数据配方和 scaling law；数据驱动算法实习生负责运动及操作数据采集、标注、处理与模型分析。这说明智元的数据团队不是低端采集外包，而是和 foundation model 训练/评测强耦合。

**优势。** 整机、本体、遥操作、数据集、模型训练和开源社区联动；公开数据和 LeRobot 兼容降低外部研究者使用门槛；Giga Data Factory 提供规模化叙事。

**劣势/风险。** 数据开放集与内部商业数据的差异待验证；数据服务是否独立变现尚不清晰；开源数据多使用非商业许可时，对商业客户可复用性有限；整机公司容易优先服务自家模型路线。

### 补天石科技

**发展历史。** 公开资料目前主要来自新智驾/搜狐转载。报道称上海补天石科技有限公司于 2025-11 成立，创始人为前蔚来 AI 平台负责人白宇利，首轮融资由红杉领投。白宇利曾在 Momenta、蔚来从事 AI 基础设施、算力与数据闭环建设。

**解决方案/产品。** 公开报道把补天石定位为“具身数据 Infra”：为机器人模型训练提供数据采集、处理、标注到模型训练调度的工程体系，让机器人公司不必从零搭建数据管线。尚未看到官网、产品页、客户案例、数据样例或标准格式披露。

**技术路线。** 推测更接近“自动驾驶数据闭环迁移到机器人”：任务调度、采集管线、标注/质检、训练调度、数据版本和模型迭代。该推测来自创始人履历和报道中的 Infra 描述，需以官方资料验证。

**岗位/人才投入。** 报道提到正在招募具身算法系统研发工程师、机器人底软研发工程师。岗位指向“系统软件 + 机器人基础软件 + 数据/训练平台”，而不是单纯采集员，说明公司早期重点可能是先搭工程中台。

**优势。** 自动驾驶数据闭环经验可迁移；若能做成中立 Infra，客户面可覆盖多家整机/模型公司；资本背书有助于抢早期人才。

**劣势/风险。** 公开证据薄弱，核心产品、客户、团队规模、融资金额、采集场地、数据格式全部待验证；具身数据与自动驾驶数据不同，动作空间、触觉、接触动力学和跨本体迁移更难；早期公司容易停留在平台叙事。

### 它石智航 TARS

**发展历史。** 公开资料称它石智航由陈亦伦、李震宇等创立，2025 年完成 1.2 亿美元天使轮和 1.22 亿美元天使+轮，招聘页称两轮累计 2.42 亿美元。创始团队背景来自清华 AIR、华为自动驾驶、百度智能驾驶等。

**解决方案/产品。** 它石的数据侧是 WIYH 数据集、TARS Datacore 数据引擎、SenseHub 商用级 Human-centric 数据解决方案；模型侧是 AWE 系列具身大模型；本体侧有 A/T 系列机器人和精细操作展示。中国日报报道 WIYH 为 Vision-Language-Tactile-Action 多模态数据集，包含 10 万条以上真实人类操作视频、40+ 任务类型、100+ 人类技能、520+ 物品和 10 类核心场景。

**技术路线。** 它石明确反复强调 Human-centric：先记录人的高质量物理交互，再通过 TARS Datacore 做标定、深度、动作、指令、COT、mask、tactile 等自动化标注，最后服务 AWE 模型和机器人落地。SenseHub 包含 TARS-Vision 和 TARS-Glove，核心是让机器人“看人之所看，感人之所感”。

**岗位/人才投入。** 2026 春招覆盖机器人强化学习、感知、具身 VLA、SLAM、端到端算法、运动控制、嵌入式、软件、机械、电子硬件等；实习岗位还包括 UX/工业设计、招聘品牌、财务采购。岗位组合显示公司在全栈快速扩张，研发重点集中在算法、本体和系统工程，数据只是三位一体路径的一环。

**优势。** 融资强、创始团队强、数据-模型-本体叙事完整；Human-centric 路线避开纯遥操作的成本瓶颈；WIYH 开源和 SenseHub 商用产品形成生态与商业入口。

**劣势/风险。** 大量能力来自公司宣传和媒体报道，实际可复现性、数据许可、客户付费和模型泛化需要第三方验证；Human-centric 到机器人 action 的 retargeting 是关键难点；全栈路线烧钱且组织复杂度高。

## 苏州

### 简智 GenRobot

**发展历史。** 官网主体为简智新创（北京）机器人科技有限公司，披露北京海淀地址，但联系方式含 0512 电话，用户将其归入苏州，可能与运营/产线/团队所在地有关，需工商和招聘进一步核验。钛媒体报道称简智机器人 2025-12 完成第三轮融资，成立 4 个月完成 3 轮融资，总额超 2 亿元，投资方包括 BV 百度风投、Momenta、九识、星海图、速腾聚创、顺为、初心等。

**解决方案/产品。** 官网披露 Gen DAS 采集设备矩阵：DAS Ego、DAS Dex、DAS Fingers、DAS Gripper、DAS Controller；数据资产 Gen EgoData；治理平台 Gen Matrix；并提供 Pro/Max/Ultra 分级数据服务，从原始数据到 AI-ready 数据集。

**技术路线。** 简智是最典型的“无本体/Human-centric 数据基建”路线。官网称覆盖头、手、全身，家庭/工厂/物流等场景，50+ 应用场景、10000+ 小时、100TB+ 数据量。钛媒体报道进一步披露 Gen DAS 重量 470g、图像/触觉/关节角度等多模态、误差小于 1cm、多设备时间误差小于 1ms、数据压缩至原大小 2%、采集后 2 小时内交付高质量加工数据等。

**岗位/人才投入。** 官网“加入我们”强调与全球顶尖 AI/机器人人才合作，100+ 团队成员、10+ 覆盖国家、远程办公友好；但公开岗位详情不如智元/它石完整。结合产品路线，人才投入应集中在硬件采集设备、视觉/触觉/轨迹还原、SLAM/环境重建、数据治理平台、AI 标注、众包产线运营和客户交付。

**优势。** 中立数据供应商定位清晰，不与客户本体路线强绑定；“产品+产线+治理平台”完整度高；无本体采集有成本和场景覆盖优势；产业投资方包括机器人公司，说明客户协同可能较强。

**劣势/风险。** 官网口径和融资稿中的数据规模需要样例/客户/合同验证；标准导出格式、LeRobot/HDF5/MCAP/RLDS 支持尚未充分公开；无本体数据到机器人动作的映射质量是成败关键；若客户最终自建数据闭环，中立供应商议价能力会受压。

### Maxinsights

**发展历史。** 官网披露 Maxinsights 的使命是为 Physical AI 建设数据基础，通过全球采集网络提供规模化、高质量数据。Tola Capital 投资组合页称其面向 Robotics Foundation Model 公司，通过 end-to-end data-solution platform 提供 massive、high-quality、scalable training data，并由自动驾驶和机器人连续创业者/研究人员创立。Tola 页面列出 CEO Yuguang Yong、总部 San Francisco，Tola 2025 年投资。用户将其列入苏州，公开检索中只找到 LinkedIn 个体位于苏州的线索，主体和中国办公室待验证。

**解决方案/产品。** 官网信息非常克制，仅披露 global capture network、research partners 和 early access。Tola 页面披露“端到端数据解决方案平台”与“几乎所有领先机器人企业/AI 实验室合作”的口径。

**技术路线。** 从招聘页检索可见，Maxinsights 平台集成视觉驱动 AI 模型，做 egocentric、embodiment、human-to-robot 数据解决方案；机器人实习岗位涉及目标检测、语义分割、3D 重建、pose optimization、多传感器融合、3D human pose/shape、ROS/ROS2；后端岗位涉及机器人 telemetry、多模态流、数据管线、dashboard、cloud-native infra。这说明其不是传统外包采集，而是“全球采集网络 + 视觉/3D/人到机器人转换 + 云端数据平台”。

**岗位/人才投入。** 公开岗位集中在 Robotics Intern、Backend Software Intern 等，技术栈包括 Python/C++、ROS/ROS2、SLAM、3D reconstruction、geometric deep learning、Kubernetes/Docker、data pipeline、visualization。这是典型平台型团队配置。

**优势。** 全球采集网络和海外研究伙伴叙事强；自动驾驶/机器人背景与数据平台匹配；面向海外 foundation model 客户时更容易获得多地域、多文化、多场景数据。

**劣势/风险。** 官网披露少，客户、数据样例、格式、合规、价格都不透明；中国主体和苏州落点未清晰；“几乎所有领先企业合作”属于投资方口径，需客户背书核验；全球采集会带来隐私、跨境数据和劳动组织复杂度。

## 深圳

### 自变量机器人 X Square Robot

**发展历史。** 自变量机器人科技（深圳）有限公司官网显示其总部在深圳南山区，聚焦自研通用具身智能大模型，采用端到端路径实现 WALL-A 操作大模型，并研发 QUANTA 轮式仿人机器人和五指灵巧手。官网新闻披露 2026-01 获字节、红杉等 10 亿元投资相关报道。

**解决方案/产品。** 产品包括 QUANTA X1、QUANTA X2、ArtiXon Hand，解决方案覆盖居家服务、科研教育、商业清洁、物流分拣。其核心不是对外数据服务，而是以 WALL-A 操作大模型驱动自有本体执行多步骤复杂任务。

**技术路线。** 自变量强调完全端到端、统一大模型、百亿级参数、跨任务跨场景泛化、少样本学习、强化学习、柔性物体长序列复杂操作、具身思维链、高自由度灵巧手。官网给出的任务包括切菜、制作饮品、分拣快递、工业组装、拉拉链、晾衣服、工业线束整理、酒店纸巾换新、房间杂物收纳等。

**岗位/人才投入。** 官网只有社会招聘/校园招聘入口，未公开抓到完整官方 JD。第三方招聘聚合显示 2026 校招岗位分为“机器人大脑”和“机器人本体”两大类，包含多模态生成算法、强化学习、SLAM、运动控制、机器人开发、系统工程、线束、电机等。结合官网产品，人才重心是大模型算法、本体工程、灵巧操作与场景落地。

**优势。** 模型中心路线明确；软硬一体和深圳供应链结合紧密；如果 WALL-A 真能跨任务泛化，内部数据闭环价值极高；面向服务/物流/家庭等高频场景，有机会积累部署数据。

**劣势/风险。** 不是中立数据服务商，外部客户难以直接购买其数据能力；官网能力多为宣传，缺少公开数据集、benchmark 和可复现模型卡；端到端大模型对数据规模、标注质量和真机安全要求很高，短期商业化验证压力大。

### 帕西尼 PaXini

**发展历史。** 帕西尼成立于 2021 年，总部深圳。公开资料称其拥有“传感器-灵巧手-人形机器人”完整多维触觉产品矩阵，并构建从硬件封装、数据采集、算法集成到 VTLA 模型的全栈体系。2025-06 天津 Super EID Factory 投用，2026-03 又宣布新增四座超级数据工厂，形成五厂联动。

**解决方案/产品。** 硬件包括 6D 霍尔阵列式多维触觉传感技术、DexH13 四指仿生灵巧手、TORA-ONE 人形机器人、PMEC 数据采集手套/终端。数据侧是 Super EID Factory、MotionSharing DB 向 OmniSharing DB 升级、全模态数据采集矩阵。

**技术路线。** 帕西尼核心差异是“触觉真值”。天津工厂 12000 平方米，15+N 场景矩阵、千种任务、百万工序、150 个标准化采集单元，预计年产近 2 亿条高维训练数据。武汉东西湖工厂报道提到 PMEC 手套、数千颗 ITPU 多维触觉传感单元与视觉矩阵，提升采集效率 3-6 倍；21 财经报道还提到 Soma Redirect 可向不同型号机器人输出，试图解决跨本体泛化。

**岗位/人才投入。** LinkedIn/猎聘岗位“具身智能算法总监”月薪 6-9 万，职责包括设计视觉、触觉、运动、交互数据的采集/清洗/增强策略，建立数据闭环；构建高保真仿真环境，支持大规模 RL 和 Sim2Real；开发灵巧手模仿学习/强化学习、任务规划、行为决策和真实机器人部署。这是非常直接的“数据-仿真-RL-灵巧手落地”岗位信号。天津国资报道还提到河西区协助收集 800 余份简历、启动大规模面试，说明数据工厂运营也需要大量现场采集和工程人员。

**优势。** 触觉传感器和灵巧手硬件带来稀缺模态；超级数据工厂规模化强；地方政府合作提供场地、招聘和政策支持；硬件、数据、模型、应用场景闭环完整。

**劣势/风险。** “近 2 亿条/近百亿条”属于产能口径，需验证有效 episode、质量指标、可训练格式和真实客户采用；传感器/灵巧手/人形/数据工厂/模型多线并进，组织复杂度高；数据产品开放范围、商业许可和跨本体效果仍需第三方验证。

## 横向比较

### 发展阶段

| 公司 | 阶段 | 最关键证据 | 下一步验证 |
|---|---|---|---|
| 智元 | 商业化+生态开放 | 官网产品矩阵、AgiBot World、招聘 JD、Giga Data Factory 地址 | 付费数据服务客户、开放集 license、内部训练效果 |
| 补天石 | 早期组建 | 媒体报道、创始人履历、早期岗位 | 官网/工商/融资公告/客户/产品 demo |
| 它石 | 高融资快速扩张 | 融资报道、WIYH、SenseHub、AWE3.0、春招 | 数据集访问、benchmark、客户和线束装配真实 ROI |
| 简智 | 数据基建快速融资 | 官网产品、Gen Matrix、融资稿、投资方背书 | 数据样例、格式、客户合同、苏州主体 |
| Maxinsights | 海外平台早期扩张 | 官网、Tola 投资页、岗位线索 | 中国办公室、客户名单、样例、数据合规 |
| 自变量 | 模型/本体商业化探索 | 官网 WALL-A/QUANTA、融资新闻、招聘入口 | 公开 benchmark、真实客户、数据闭环规模 |
| 帕西尼 | 数据工厂规模化 | 天津/武汉工厂、政府报道、算法总监 JD | 有效数据质量、客户采用、商业授权、真实模型收益 |

### 人才投入信号

| 公司 | 算法/模型 | 机器人系统 | 数据平台 | 采集运营 | 商业/生态 |
|---|---:|---:|---:|---:|---:|
| 智元 | 很强 | 很强 | 强 | 强 | 强 |
| 补天石 | 中-强 | 中 | 强 | 待验证 | 待验证 |
| 它石 | 很强 | 很强 | 强 | 中-强 | 强 |
| 简智 | 强 | 中 | 很强 | 很强 | 强 |
| Maxinsights | 强 | 中-强 | 很强 | 强 | 中 |
| 自变量 | 很强 | 很强 | 中 | 中 | 中 |
| 帕西尼 | 强 | 很强 | 强 | 很强 | 强 |

## 投资/合作视角

**最像中立供应链的公司：** 简智、Maxinsights、补天石。它们理论上可以服务多家整机/模型公司，商业模式更接近数据基础设施、数据产线和工具链。风险是客户会自建核心数据闭环。

**最有真实本体闭环的公司：** 智元、它石、自变量、帕西尼。它们能把数据直接喂回自家模型和机器人，验证速度更快。风险是对外数据服务可能只是生态宣传，不一定是独立业务。

**最有差异化模态的公司：** 帕西尼。触觉数据是当前具身智能短板，如果触觉传感器成本和一致性真实成立，壁垒强于普通视频/第一视角数据。

**最需要尽调的公司：** 补天石、Maxinsights。二者方向诱人，但公开证据最少，应该优先查工商、招聘、客户、样例和融资文件。

## 对职业机会的含义

如果目标是进入“具身智能数据采集和服务”赛道，不要只看数据采集员岗位。更有成长性的岗位族包括：

| 角色 | 适合公司 | 能力关键词 |
|---|---|---|
| 数据平台/MLOps | 补天石、简智、Maxinsights、智元、它石 | 多模态数据流、版本管理、训练调度、评测、云原生、可观测性 |
| 数据治理/标注算法 | 简智、它石、智元、帕西尼 | 自动切片、轨迹还原、mask、3D/2D 标注、COT、失败/恢复标签 |
| 机器人学习/VLA/VLTA | 智元、它石、自变量、帕西尼 | VLA、VLTA、模仿学习、RL、Diffusion Policy、ACT、OpenVLA、pi0 |
| 触觉/灵巧操作 | 帕西尼、智元、它石、自变量 | 触觉传感、力控、灵巧手、接触丰富操作、Sim2Real |
| 采集设备/嵌入式 | 简智、Maxinsights、帕西尼、它石 | wearable、手套、相机、IMU、同步、ROS/ROS2、低延迟 |
| 训练场/数据工厂运营 | 帕西尼、智元、简智 | SOP、场景搭建、人员培训、质检、交付报告、安全合规 |

## 需要继续核验的问题

1. 各家是否公开或可试用数据样例，格式是否支持 LeRobot/HDF5/MCAP/RLDS。
2. 数据许可：研究、商业、二次训练、模型分发是否允许。
3. 有效 episode 定义：一条数据是 clip、frame、轨迹还是完整任务。
4. 质量指标：同步误差、轨迹误差、丢帧率、标注一致性、失败标签覆盖。
5. 客户真实性：是采购硬件、采购数据、联合研发，还是展示合作。
6. 对模型的实际收益：同一模型架构下，加入其数据前后成功率、泛化、长程任务稳定性如何变化。
7. 合规：家庭/工厂/人体第一视角/触觉数据的隐私、授权和跨境流通。

## 来源映射

| 公司 | 关键来源 |
|---|---|
| 智元 | [AGIBOT WORLD 2026 官网公告](https://www.agibot.com/article/231/detail/54.html)、[AgiBot World Alpha Hugging Face](https://huggingface.co/datasets/agibot-world/AgiBotWorld-Alpha)、[2026 实习招聘](https://www.wondercv.com/xiaozhao/agibot-2026-intern-shanghai-shenzhen-7150-291a6c/) |
| 补天石 | [新智驾/搜狐报道](https://www.sohu.com/a/1017597949_99919085) |
| 它石 | [WIYH 数据集报道](https://cn.chinadaily.com.cn/a/202512/29/WS695222e7a310942cc4999198.html)、[AWE3.0/SenseHub 发布报道](https://www.ithome.com/0/927/552.htm)、[2026 春招](https://www.wondercv.com/xiaozhao/tars-robotics-shanghai-2026-spring-9018-c6cedb/)、[天使+轮融资](https://news.pedaily.cn/202507/552059.shtml) |
| 简智 | [GenRobot 官网](https://cn.genrobot.com/)、[GenRobot 关于页](https://cn.genrobot.com/why)、[钛媒体融资报道](https://www.tmtpost.com/7813011.html) |
| Maxinsights | [Maxinsights 官网](https://www.maxinsights.ai/)、[Tola Capital 投资组合页](https://tolacapital.com/portfolio/maxinsights) |
| 自变量 | [自变量官网](https://www.x2robot.com/) |
| 帕西尼 | [科技日报天津数据工厂](https://www.stdaily.com/web/gdxw/2025-06/23/content_359003.html)、[天津国资报道](https://sasac.tj.gov.cn/GZJG8342/JGDT5617/202507/t20250701_6970780.html)、[极目新闻武汉工厂](https://www.ctdsb.net/c1476_202603/2689670.html)、[LinkedIn/猎聘算法总监岗位](https://cn.linkedin.com/jobs/view/%E5%85%B7%E8%BA%AB%E6%99%BA%E8%83%BD%E7%AE%97%E6%B3%95%E6%80%BB%E7%9B%91-at-%E5%B8%95%E8%A5%BF%E5%B0%BC%E6%84%9F%E7%9F%A5%E7%A7%91%E6%8A%80-4416783283) |

## 关联连接

- [[07-training-data|机器人（具身智能） - 训练数据生产与处理]]
- [[09-training-data-deep-dive|机器人训练数据深度调研]]
- [[_concepts/robot-training-data|Robot Training Data]]
- [[_concepts/embodied-ai|Embodied AI]]
- [[_concepts/vision-language-tactile-action|Vision-Language-Tactile-Action]]
- [[_entities/Agibot|Agibot]]
