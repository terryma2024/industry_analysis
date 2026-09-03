---
title: 机器人（具身智能） - 研究中间笔记
date: 2026-05-27
tags:
  - industry/robotics-embodied-ai
  - research-notes
  - obsidian/moc
aliases:
  - 具身智能研究中间笔记
last_updated: 2026-09-02
---

# 机器人（具身智能） - 研究中间笔记

> [!info]
> 本目录保存专题深度调研的中间笔记。结论成熟后再汇总进入上层知识笔记，如 [[07-training-data|训练数据生产与处理]] 和 [[09-training-data-deep-dive|训练数据深度调研]]。

## 2026-08-26 可靠性、模型规模与按结果付费

- [[embodied-ai-reliability-scaling-and-outcome-pricing-2026-08-26]]: 按 R07 主分类、R04/R03 次分类，把原子技能可靠性、陌生分布覆盖、长程任务 SLA、模型 scaling 与结果计价放在同一商业化框架中；`99%`、两个 `80%`、`7B`、万卡和毛利数字均保留证据边界，并给出按任务/合格件计费的验收与创业切口。

## 2026-09-02 宇树科技上市供应链公司

- [[unitree-listed-supply-chain-public-companies-2026-09-02]]: 按 R09 主分类、R02/R03 次分类，只纳入有上市公司公告、年报或官方投资者互动直接确认的 5 家 A 股供应链公司；比较业务、关系阶段、2026-08-31 股价/市值、近一个月与上市日走势，并明确未披露宇树收入占比的估值边界。

## 2026-08-12 EtherCAT 与 TCP/IP 机器人控制时延

- [[ethercat-vs-tcp-ip-robot-control-latency-2026-08-12]]: 按 R04 主分类、R05 次分类，解释 EtherCAT 的单帧多节点、ESC on-the-fly、统一过程映像、DC 和 WKC 为什么比普通 TCP/UDP socket 更适合多轴周期控制；同时证明“更快”不等于峰值吞吐量更高，并给出 6/12 轴 A/B PoC。

## 2026-08-11 具身智能模型数据处理闭环

- [[embodied-ai-model-data-processing-pipeline-2026-08-11]]: 按 R02 主分类、R05 次分类，从微信从业者文章提炼问题地图，再用 LeRobot/OXE/DROID/HIL 一手资料限定边界；形成采集前契约、raw 保真、同步/标定、自动质量门、episode/事件、分层标注、schema/action 编译、无泄漏切分、训练时增强、真实 holdout 和部署回流的十层闭环。

## 2026-08-10 onshape-to-robot CAD 转机器人描述

- [[onshape-to-robot-usage-selection-deep-dive-2026-08-10]]: 按 R05 主分类、R04 次分类，拆解 Onshape 顶层装配与 mate connector 约定、API 认证、版本锁定、URDF/SDF/MuJoCo、processors、示例和 open-issue 风险；结论是适合 Onshape-first 团队做版本化 CAD→机器人描述编译，但不能替代 ROS 2/MoveIt/控制、碰撞和动力学验证。

## 2026-08-09 EtherCAT 实时工业以太网

- [[ethercat-technology-ecosystem-engineering-deep-dive-2026-08-09]]: 按 R04 主分类、R05/R07 次分类，拆解 on-the-fly、FMMU、Distributed Clocks、CoE/CiA 402、FSoE、MainDevice/SubDevice 实现与许可，给出机器人分层架构、竞品边界、商业/创业机会和 6/12 轴 PoC。

## 2026-08-09 DexCap 灵巧操作数采

- [[dexcap-dexterous-mocap-data-collection-deep-dive-2026-08-09]]: 拆解 DexCap/DexIL 的穿戴动捕、跨本体重定向、点云 Diffusion Policy、人工纠偏、六任务证据、硬件/代码边界，以及中国数据服务的可验证切口。

## 2026-08-06 Unity 机器人与具身智能调研

- [[unity-in-robotics-and-embodied-ai-2026-08-06]]: 按 R04 主分类、R05/R06 次分类，拆解 Unity 的 ROS/URDF、ML-Agents、合成数据、室内具身世界、VR 示教、自动驾驶/UAV/多机器人应用，核验 23 个项目、16 篇论文及代码—引擎—资产分层许可，并与 UE/专用机器人模拟器对照。

## 2026-08-06 Unreal Engine 机器人与具身智能调研

- [[unreal-engine-in-robotics-and-embodied-ai-2026-08-06]]: 按 R04 主分类、R05/R06 次分类，拆解 UE 的场景/传感器/ROS/数字孪生/混合物理位置，核验 20 个公开项目或研究交付物与 18 篇论文；区分仓库可见、完整开源、许可证可商用和实际可复现，并给出 4 周 PoC、商业应用与创业边界。

## 2026-08-06 3D 仿真资产生产管线调研

- [[3d-simulation-asset-production-pipelines-comparison-2026-08-06]]: 按 R05 主分类、R04/R02 次分类，比较 DCC、CAD/BIM、摄影测量、LiDAR/RGB-D、NeRF/3DGS、程序化、生成式 3D、资产库和混合式资产工厂；给出 SimAsset 合同、SimReady L1 规范/L2 运行时/L3 任务三级验收、机器可读清单、六周 PoC、商业应用与中小创业机会。

## 2026-08-06 光轮智能同类创业公司扫描

- [[lightwheel-peer-companies-business-model-comparison-2026-08-06]]: 按 R06 主分类、R03/R07 次分类，用六层能力矩阵比较 12 家中国/海外候选；区分中立基础设施、纵向一体化和数据/评测局部供应商，并输出机器可读 CSV 与下一轮商业尽调问题。

## 2026-08-06 光轮智能公司与商业模式调研

- [[lightwheel-company-and-commercial-model-deep-dive-2026-08-06]]: 按 R03 主分类、R07 次分类，核验团队、产品栈、开源资产、NVIDIA/吉利部署、5.5 亿元订单与密集融资；结论是技术和资本势能强，但收入确认、回款、毛利、客户集中和复购仍需财务与合同尽调。

## 2026-08-05 Jetson Thor 与替代平台选型

- [[jetson-thor-and-alternatives-spec-price-comparison-2026-08-05]]: 按 R05 主分类、R06 次分类，对比 Thor/T5000/T4000、AGX Orin、IQ-9075、DGX Spark、Ryzen AI Max+ 395、Hailo/Atlas/征程 6 的规格、当前价格、生态、TCO 与 PoC；明确不同 TOPS 精度/稀疏口径不可直接横排。

## 2026-07-28 RoboVerse 平台与真实数据增益

- [[roboverse-platform-and-real-data-deep-dive-2026-07-28]]: 按 R05 主分类、R04/R07 次分类审阅 RSS 2025 论文、固定提交仓库/文档和数据格式，区分平台、仿真底座与基础模型，形成真实数采数据接入契约、增益路径、A/B 验收和商业/创业判断。

## 2026-07-20 MATRiX 仿真平台深研

- [[zsibot-matrix-robotics-simulator-deep-dive-2026-07-20]]: 对 `zsibot/matrix` 做固定提交、发行包、代码、文档、issue/PR、上游和政策证据审计；结论为“适合四足导航/感知联调的限定 PoC，尚不足以替代通用仿真底座”，并给出商业应用与中小创业边界。

## 2026-07-14 机器人仿真平台选型

- [[isaac-sim-vs-gazebo-vs-mujoco-2026-07-14]]: 基于 2026-07 官方版本、许可与后端资料，对比 Isaac Sim、Gazebo、MuJoCo 的物理、渲染、传感器、ROS 2、RL/IL、资产格式和商业边界；新增国产 GPU/AI 加速器支持矩阵、异构组合架构与采购 PoC 清单。

## 2026-07-14 Ego 视频到灵巧手训练数据

- [[ego-video-to-dexterous-hand-training-data-system-design-2026-07-14]]: 区分手骨架识别、手物 4D 重建和机器人可执行动作，比较 Do As I Do、HaWoR、DexCap、DexUMI/RealDexUMI、UniDex、EgoScale、GeoRT 与 SPIDER，并给出系统架构、数据 schema、质量门和 PoC 路线。

## 2026-07-13 SRT 软体机器人公司调研

- [[srt-soft-robot-tech-company-deep-dive-2026-07-13]]: 调研 SRT 的软体执行器产品化、技术壁垒、业务模式、融资股权、竞争格局、十五五关联、创始团队迁移与投前尽调清单。

## 2026-05-27 并行调研

- [[training-data-company-verification-2026-05-27]]: 公司/方案交叉验证。
- [[local-policy-data-platforms-2026-05-27]]: 地方政策、公共训练场、数据工厂和测评中心。
- [[dataset-schema-comparison-2026-05-27]]: OXE、DROID、RoboMIND、AgiBot World、LeRobot schema 横向。
- [[failure-intervention-data-2026-05-27]]: 失败轨迹和人工接管数据。
- [[umi-hardware-localization-2026-05-27]]: UMI 硬件 BOM、许可证、可采购性和国产替代。

## 2026-05-28 UMI v0 模板补全

- [[umi-v0-sop-schema-data-package-2026-05-28]]: UMI-like v0 采集 SOP、UMI/Zarr 与 LeRobot schema 对照、客户数据包样例目录。
- [[lerobot-beginner-guide-2026-05-28]]: LeRobot 初学者教学，解释 LeRobotDataset、数据目录、UMI/Zarr 转换和 ToB 数据服务意义。

## 2026-06-09 职业方向与业务落地入口

- [[career-direction-business-landing-knowhow-2026-06-09]]: 基于 Thinking Partner 对话沉淀的职业方向锚点，聚焦通过具身智能业务落地 know-how 解决企业决策者的成本、收入或风险痛点。

## 2026-06-10 线下零售门店场景验证

- [[retail-store-robotics-entry-scan-2026-06-10]]: 对“中国零售销售额前 10 大型零售公司是否超过一半已有线下门店机器人合作”的第一轮外部调研初扫。
- [[cross-scenario-near-term-landing-candidate-pool-2026-06-10]]: 跨全部具身智能/机器人应用场景，按 1 年内真实订单或试点转生产证据建立短期落地候选池。

## 2026-06-10 平台工程师 JD 入场验证

- [[platform-engineer-jd-entry-scan-2026-06-10]]: 用“通用软件平台能力是硬要求、机器人领域知识可补齐”作为第一筛选门槛，初扫具身智能/机器人平台工程、后端、数据管线、仿真平台和运营系统岗位。

## 2026-06-11 仿真评测平台

- [[libero-lifelong-robot-learning-platform-2026-06-11]]: LIBERO 终身学习仿真/评测平台调研，拆解任务套件、数据、baseline、平台工程价值、局限和 2025-2026 年鲁棒性批评。
- [[open-embodied-ai-datasets-comparison-2026-06-11]]: 开源具身智能训练与评估数据集横向调研，按预训练、真实微调、特定能力和仿真 benchmark 比较格式、任务完整度与模型适配。

## 2026-06-23 数据生产平台

- [[airspeed-data-production-platform-2026-06-23]]: AIRSPEED 具身智能数据生产平台调研，区分当前 GitHub v1.3 开源采集核心、论文/官网三服务架构和技术转移报告中的商业化叙事。

## 2026-06-23 机器人中间件与 dataflow runtime

- [[dora-1-vs-ros2-2026-06-23]]: 对比 dora 1.0 能力主张与 ROS 2 生态底座，重点拆解版本状态、性能、QoS、ROS 2 bridge、平台工程选型和职业学习路径。

## 2026-06-29 LiDAR 世界模型训练

- [[lidar-world-model-training-2026-06-29]]: 调研激光雷达数据如何通过点云/range/ray token、BEV/occupancy、camera-LiDAR unified latent 和 JEPA 进入世界模型训练，并给出自动驾驶、传感器仿真、多模态生成和移动机器人导航的工程方案。

## 2026-06-29 训练数据价值评估

- [[robot-training-data-value-evaluation-2026-06-29]]: 面向采集前立项、采集中质检和采后验证的具身智能训练数据价值评估框架，核心是边际能力提升、复用性、可信度与全成本风险比。

## 2026-07-03 世界模型与物理理解评估

- [[embodied-model-physical-understanding-evaluation-2026-07-03]]: 区分具身大模型的动作生成、语义泛化、动作条件预测和规划可用世界模型，提出反事实预测、minimal physical pairs、forward/inverse dynamics、闭环 A/B 和多模态约束的评估框架。

## 2026-07-06 家庭养老机器人

- [[home-elderly-care-robots-2026-07-06]]: 家庭养老机器人公司与方案调研，按陪伴提醒、远程巡视、移动载物、康复护理和通用家务机器人分层，比较国内外代表公司、落地阶段和中国方案机会。

## 2026-07-06 VLA 与世界模型数据基建

- [[vla-world-model-data-infrastructure-platform-design-2026-07-06]]: 基于 `BV1ZFTq6pEA3` 的 15 阶段数据生产 SOP，设计 VLA&世界模型数据基建平台，覆盖 episode-first 架构、自动质检、多格式导出、dataset registry、baseline 评测和失败补采闭环。

## 2026-07-08 博登智能商业与技术综述

- [[boden-intelligence-business-technology-overview-2026-07-08]]: 基于 `BV1q3TE6AE4b` 视频深研和 ASR 原文，整理博登智能作为 Physical AI 数据基建公司的商业逻辑、商业计划、产品收入结构、三层技术方案和一级来源待验证清单。

## 2026-07-09 遥操数据成本与占比

- [[teleoperation-training-data-cost-and-share-2026-07-09]]: 调研遥操/teleoperation 训练数据的有效小时成本和在训练数据中的占比，区分人类视频、UMI-like 示教、单臂机器人遥操、双臂/人形/灵巧手遥操和 VLA 训练混合口径。
- [[embodied-ai-training-data-hour-requirements-2026-07-09]]: 调研具身智能训练数据需求量与有效小时数，按 demo、单任务泛化、客户场景产品化、跨任务策略模型和前沿 VLA/foundation model 分层估算。
