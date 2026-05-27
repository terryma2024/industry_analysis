---
title: 具身智能训练数据公司/方案交叉验证深度调研
date: 2026-05-27
tags:
  - industry/robotics-embodied-ai
  - research-note
  - training-data
  - company-verification
aliases:
  - 具身智能数据公司交叉验证 2026-05-27
  - Training Data Company Verification Deep Dive
---

# 具身智能训练数据公司/方案交叉验证深度调研

> [!summary]
> 这份子报告只做公司/方案交叉验证，不改动主知识笔记。配套 CSV 草案见 [training_data_company_verification_deep_dive.csv](../../../raw/robotics-embodied-ai/data/training_data_company_verification_deep_dive.csv)。

## 结论先行

- **第一梯队：证据链较完整，适合进入主表二级字段。** 智元、宇树、IO-AI、星海图已经能从官方产品页/数据集/上市公司公告/论文或 Hugging Face/GitHub 交叉验证“数据采集/处理/训练闭环”的关键字段。
- **第二梯队：定位明确，但客户/融资/格式披露不足。** Robotin、FirstMove、灵初 Psi Data、GenRobot、禹纲数据需要继续用工商、招聘 JD、样例数据和客户案例核验。它们更像下一轮访谈/尽调候选。
- **第三梯队：工具链或生态型补充。** 穹彻智能 Noematrix、朔月智能 Menily、智域基石偏“工具链/数据层/数据编译基础设施”叙事，其中 Menily 和智域基石需要尤其注意主体与真实交付核验。
- **关键判断：** 国内具身数据供应链正在从“整机厂自采自用”分出三类 ToB 机会：遥操作/人体采集设备、数据治理与格式转换平台、垂直数据工厂/数据服务。真正有商业价值的不是“视频小时数”，而是能否交付可训练、可回放、可质检、可追溯、可复现实验结果的数据包。

## 字段核验表

| 公司 | 证据强度 | 可确认内容 | 仍需验证 |
|---|---:|---|---|
| 智元机器人 | 高 | AGIBOT WORLD 2026 真实场景采集、DaaS 质检、层级标注、Hugging Face LeRobot v2.1 结构。 | 数据许可、商业 DaaS 价格/客户、开放集与内部训练集差异。 |
| 宇树科技 | 高 | G1-D 把采集、处理、标注、审核、资产管理、训练、仿真、部署打包；IPO 文件确认算法/数据/生态重要性。 | 是否支持 LeRobot/HDF5/MCAP；平台是否已规模交付。 |
| IO-AI | 高 | TeleXperience、SenseXperience、EmbodiFlow；明确导出 LeRobot/HDF5/MCAP，客户 logo 多，腾讯云合作可交叉验证。 | 融资轮次、开源数据具体地址、客户 logo 对应合同范围。 |
| Robotin | 中 | 官网确认真实家庭/杂乱场景、穿戴式灵巧手套/夹爪、定制格式对齐。 | 融资、客户、样例数据、LeRobot/OXE 支持。 |
| FirstMove | 低-中 | 官网/搜索摘要确认第一视角数据引擎和面向云 AI 平台/机器人本体厂的定位。 | 主体、融资、团队、客户、传感器、可训练格式。 |
| 星海图 | 高 | 官网客户/融资/数据采集需求；OpenGalaxea 数据集公开 LeRobot schema；GitHub 公开 G0 VLA。 | B 轮需官方公告或工商核验；商业数据采集服务边界。 |
| 灵初 PsiBot | 中 | Psi Data 以外骨骼和自建采集场做灵巧操作真机数采，官网披露人效指标。 | SynData 官方入口、格式、客户、融资。 |
| GenRobot | 中 | 官网披露 50+ 场景、10000+ 小时、100TB+、Gen Matrix 数据治理和分级 DaaS。 | 数据资产真实性、客户、格式、融资。 |
| 禹纲数据 | 低-中 | 官网确认机器人/大模型数据痛点、AI 辅助标注。 | 主体、客户、模态、格式、交付案例。 |
| Noematrix | 中 | 工具链覆盖数据采集、数据管理、模型训练、部署，CoMiner 数据采集套件。 | CoMiner 子页细节、格式、客户与 API。 |
| Menily | 低-中 | 官网称 schema/toolkit 兼容 OXE/RLDS、HF Datasets，面向任务级示教数据。 | 主体、团队、开源活跃度、客户交付。 |
| 智域基石 | 低 | 媒体线索显示数据编译基础设施、采集工厂、时空对齐、技能原子化。 | 官网/工商/融资公告/JD，当前不能作为高置信标的。 |

## 公司要点

### 智元机器人

智元已经从“整机厂”进一步展示了数据平台属性。AGIBOT WORLD 2026 官方文章称数据来自 100% 真实环境，覆盖商业空间、酒店餐饮、家居、安防、工业物流等场景，并用精灵 G2、Swift Picker、OmniHand 采集 RGB(D)、触觉、LiDAR、IMU、全身关节状态、力传感器等多模态数据。官方还强调 DaaS 工业质检流水线、多轮筛查清洗、层级标注和错误修正过程轨迹。

Hugging Face 数据集页进一步把“能否训练”落到结构上：AgiBotWorld2026 遵循 LeRobot v2.1 目录结构，包含 `episodes.jsonl`、`info.json`、`tasks.jsonl`、`annotations.json` 等，并在 `info.json` 中扩展 `instruction_segments`、`key_frame`、`take_over`、`h5_path`、`camera_parameters` 等字段。上市公司公告还能交叉验证智元主体信息和经营范围，包括人工智能公共数据平台、人工智能基础资源与技术平台等。

**判断：** 智元是国内最强样本之一，适合在主表里新增字段：`lerobot_support=明确支持`、`sample_dataset=Hugging Face`、`data_qc=工业质检流水线`。

### 宇树科技

宇树 G1-D 产品页是“数据采集设备 + 数据平台 + 训练部署平台”的组合。页面明确写到 Streamlined Data Acquisition Tools 覆盖 acquisition、processing、labeling、review、data asset management；采集流程包括创建任务、任务编辑分配、采集标注、上传审核、存储、导出；平台支持多机器人和多末端执行器，并能输出或转换为主流训练格式。

训练侧，G1-D 页面称平台集成主流开源机器人模型，点名 PI 和 GROOT，并提供仿真评估、分布式训练、模型导出与部署。IPO 问询/回复文件也值得跟踪：文件明确把“算法、数据、生态及服务等软件要素”视为未来竞争点，并披露其通过大规模人体 Mocap 数据构建通用运动控制基础模型。

**判断：** 宇树不是纯数据服务商，但 G1-D 对国内 ToB 数采设备很重要。其短板是官网没有公开 LeRobot/HDF5/MCAP 等具体格式，适合标为 `mainstream format claimed, exact schema pending`。

### IO-AI

IO-AI 是当前最接近“独立具身数据基础设施公司”的样本。官网把产品拆成三层：TeleXperience 做机器人遥操作，SenseXperience 做人体动作/第一视角/UMI 风格真实世界数据采集，EmbodiFlow 做数据标注管理与导出。EmbodiFlow 页面明确支持图像、音频、IMU、触觉、动捕等多模态采集，兼容 LeRobot、ROS1/ROS2、自定义格式，并导出 LeRobot、HDF5、MCAP。

客户/伙伴证据也相对充足：官网列出智元、逐际、睿尔曼、比亚迪、中国移动、字节、清华、蚂蚁灵波等 logo；腾讯云开发者文章披露双方联合推出一站式数据平台，兼容 50+ 机器人形态，支持视觉、运动学、触觉、音频多模态同步采集，并把数据直接推送至客户 COS 存储桶。腾讯云文还称 IO-AI 已积累超 50 万条开源数据，但具体数据集入口仍需定位。

**判断：** IO-AI 应列为“重点跟踪/可访谈供应商”。它比整机厂更接近用户设想的 ToB 数据采集服务和设备提供商。

### Robotin

Robotin 官网证据能确认三件事：其主体为感进机器人（深圳）有限公司；定位是具身智能底层训练数据与全栈解决方案；方案围绕真实家庭/杂乱场景、多模态真机采集、穿戴式灵巧手套和夹爪、硬件本体格式定制与对齐。

但目前缺口也明显：官网未列客户名称，未公开融资，未披露 LeRobot/HDF5/MCAP/OXE 支持，也没有可下载样例数据。innoHere 公司页可以作为工商/融资入口线索，但完整信息需登录或转向企查查/天眼查/招聘平台。

**判断：** Robotin 是“新兴垂直数据服务商”观察对象，适合下一步用招聘 JD 和客户访谈验证真实交付。

### FirstMove

FirstMove 官网/搜索摘要显示其定位是 Egocentric Data Engine for Robotics，强调成为具身智能时代的数据基础设施，服务对象包括需要高质量具身数据的云 AI 平台和需要真实场景数据的机器人本体厂。已有 raw HTML 只保留 React/Manus 壳和 meta，无法从静态页面提取团队、主体、客户、格式。

**判断：** FirstMove 是“无本体/第一视角数据”路线的重要线索，但目前证据弱。下一步优先找招聘 JD、融资新闻、工商主体、团队成员公开演讲，验证它如何把人类第一视角数据转成机器人可执行 action。

### 星海图 Galaxea

星海图证据链正在从官网商业化披露延伸到开源数据集。官网称公司成立于 2023 年 9 月，服务包含斯坦福、Physical Intelligence、英伟达等在内的全球近百家客户，并明确客户需求包括算法开发、场景落地、数据采集。官网还披露 A 轮近 3 亿元、累计近 1 亿美元；Forbes China 进一步报道 10 亿元 B 轮，但这条仍需官方公告或工商交叉验证。

OpenGalaxea/Galaxea-Open-World-Dataset 的 Hugging Face 页面直接给出 LeRobot Dataset Schema：多路头部/腕部 RGB 视频，左右臂、躯干、底盘、IMU、夹爪、末端位姿等状态和动作字段，外加任务与质量索引。GitHub 也称 LeRobot Format Dataset 已可用。

**判断：** 星海图应从“整机+模型公司”升级为“整机+模型+数据资产”重点跟踪对象，尤其适合和智元做开放数据格式对比。

## 补充国内同类公司

### 灵初智能 Psi Data

灵初的 Psi Data 产品页强调“针对具身灵巧操作量身定做”，结合自研外骨骼设备、自建数据采集场，采集与标注人效 >500 条/天。它是“灵巧操作/人类数据/外骨骼采集”路线的重要补充。但官方页未披露格式、客户、公开样例；关于 SynData 在 Hugging Face Trending 的线索来自媒体，需要定位官方数据集页。

### GenRobot 简智新创

GenRobot 官网披露数据资产更激进：50+ 应用场景、10000+ 小时、100TB+，并提供 Gen EgoData、Gen Matrix 数据治理平台和从原始数据到 AI-ready 数据集的 Pro/Max/Ultra 分级服务。模态覆盖图像、语音、触觉、运动信息、磁编码器、IMU、轨迹、环境重建、深度、标注、3D/2D 分割。缺口是未列客户、未披露标准导出格式。

### 禹纲数据

禹纲数据官网强调解决机器人和大模型的数据痛点，依托自研具身机器人场景 AI 辅助模型提升标注效率。当前信息过少，应作为线索保留，待工商、客户、案例和格式验证后再决定是否进入主表。

### 穹彻智能 Noematrix

穹彻不是纯数据服务商，但官网的 Noematrix Toolchain 覆盖数据采集、数据管理、模型训练、功能部署闭环，且有 CoMiner 伴随式数据采集套件。适合作为“模型公司自带数据工具链”的对照组。

### Menily 朔月智能

Menily 官网披露任务级示教数据 schema 和 toolkit，声称兼容 Open X-Embodiment/RLDS、Hugging Face Datasets、NVIDIA SOMA/SOMA-X，并支持 Unitree G1/H1、Fourier GR-1 等 dof_map。这个方向很像“数据格式/语义层公司”，但主体、团队、客户和仓库活跃度都要进一步验证。

### 智域基石

当前只找到媒体转述：数千万元天使轮、四家机器人厂商参与、数据编译管线、真机采集工厂、全量质检、时空戳对齐、技能原子化、语义检索和标准化交付。因为没有官方站点/工商/招聘证据，建议只作为“待验证线索”，不能放进高置信主表。

## ToB 落地启示

如果国内要做具身智能数据采集设备和 ToB 数据服务，可以按下面的证据约束倒推产品：

1. **必须对齐 LeRobot/HDF5/MCAP/ROS。** IO-AI 和星海图已经公开打出 LeRobot；智元开放集也采用 LeRobot v2.1 结构。新进入者不能只交付视频，应交付可被训练脚本直接加载的数据包。
2. **必须提供质检和血缘。** 智元强调 DaaS 质检，IO-AI 强调审核、质检、权限、项目隔离、审计。ToB 交付要包括采集任务、操作者、设备、标定、失败原因、版本和质量报告。
3. **第一视角/人体数据是新机会，但动作映射是核心难点。** FirstMove、IO-AI SenseXperience、Menily、GenRobot 都在这个方向有信号。真正壁垒不在摄像头，而在时间对齐、手/物体/接触状态推断、retargeting 和可训练 action 表示。
4. **整机厂会自建数据闭环，独立供应商要避开“只卖给整机厂一次”。** 更好的切入是格式转换、数据质检、标注协作、私有化部署、垂直场景数据包、基准训练验证。
5. **公开样例是获客资产。** 智元、星海图通过 HF/GitHub 提升信任；Robotin/FirstMove/GenRobot 如果没有可下载样例，会很难被算法团队快速评估。

## 下一步验证清单

- 对 Robotin、FirstMove、GenRobot、禹纲数据做工商主体和招聘 JD 抓取：重点找“数据采集工程师、机器人遥操作、数据标注、LeRobot、HDF5、ROS bag、MCAP、Isaac、OpenPI、ACT、Diffusion Policy”等关键词。
- 下载 AgiBotWorld2026 和 Galaxea Open-World 的最小样例，做 schema 对照：视频编码、Parquet 字段、状态/动作维度、任务标注、质量索引、license。
- 对 IO-AI 的 LeRobot Studio/ROSView 做 GitHub 活跃度检查，看是否只是营销页面还是可运行工具。
- 对 FirstMove 用浏览器渲染抓取页面正文，补团队、客户、采集设备、合作入口。
- 把“支持 LeRobot”拆成三级：`native_dataset_schema`、`export_only`、`marketing_claim_unverified`，避免把格式兼容性说得过满。

## 来源 URL

- 智元 AGIBOT WORLD 2026：https://www.agibot.com.cn/article/315/detail/148.html
- AgiBotWorld2026 Hugging Face：https://huggingface.co/datasets/agibot-world/AgiBotWorld2026
- 同星科技对外投资公告（含智元主体信息）：https://static.cninfo.com.cn/finalpage/2025-10-09/1224703664.PDF
- 宇树 G1-D：https://www.unitree.com/G1-D/
- 宇树科创板问询/申请文件：https://static.sse.com.cn/stock/disclosure/announcement/c/202603/002178_20260320_OE27.pdf
- IO-AI 官网：https://io-ai.tech/
- IO-AI EmbodiFlow：https://io-ai.tech/zh/embodiflow/
- IO-AI 平台指南：https://io-ai.tech/platform/guides/
- IO-AI TeleXperience：https://io-ai.tech/zh/telexperience/
- IO-AI SenseXperience：https://io-ai.tech/zh/sensexperience/
- 腾讯云 x IO-AI：https://developer.cloud.tencent.com/article/2635361
- Robotin：https://robotin.cc/
- FirstMove：https://cn.thefirstmove.ai/
- 星海图官网：https://galaxea-ai.com/cn/about
- Galaxea Open-World Dataset：https://huggingface.co/datasets/OpenGalaxea/Galaxea-Open-World-Dataset
- GalaxeaVLA GitHub：https://github.com/OpenGalaxea/GalaxeaVLA
- 灵初 Psi Data：https://www.psibot.ai/products_zh/product_psi-data_zh/
- GenRobot：https://cn.genrobot.com/
- 禹纲数据：https://www.dayudata.cn/
- 穹彻智能：https://www.noematrix.ai/
- Menily：https://www.menily.ai/
- 智域基石媒体线索：https://www.firecat-web.com/daily-news/4138
