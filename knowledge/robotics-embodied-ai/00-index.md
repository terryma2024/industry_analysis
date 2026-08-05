---
title: 机器人（具身智能） - 研究入口
type: industry
date_created: 2026-05-29
last_updated: 2026-08-05
status: active
tags:
  - industry/robotics-embodied-ai
  - embodied-ai
  - robotics
sources:
  - robotics-embodied-ai/sources.csv
---

# 机器人（具身智能） - 研究入口

## 当前摘要

- 一句话理解：具身智能是 AI 从数字世界进入物理世界的产业化方向，核心载体是各类机器人，近期最可验证的落点在工业、仓储、巡检和核心零部件。
- 当前判断：政策确定性强、长期空间大，但短期商业化分化剧烈。投资上不宜只押注人形整机，应优先跟踪核心零部件、传感/视觉、运动控制和真实工业/仓储场景公司。
- 关键不确定性：人形机器人能否从示范订单走向复购；核心零部件能否从送样进入批量；具身大模型能否在真实场景稳定泛化；估值是否已经透支 3-5 年乐观预期。
- 下一步优先问题：建立“整机厂 - 供应商 - 场景客户”映射表，并对核心股票池做财务和估值跟踪。

## 行业边界

- 包含：人形机器人、工业机器人、协作机器人、AMR/移动操作、四足/特种机器人、核心零部件、感知传感、运动控制、仿真训练、具身大模型和场景解决方案。
- 不包含：无明确机器人载体的通用大模型应用、纯消费电子玩具、与物理世界交互无关的软件工具。
- 相邻行业：AI 大模型、工业自动化、智能制造、汽车零部件、半导体、云计算、低空经济、传感器。

## 中国十五五定位

- 国家重视原因：具身智能连接 AI、先进制造、智能装备、人口老龄化和生产效率提升，是未来产业和新质生产力的重要载体。
- 对应战略方向：未来产业、智能制造、国产替代、工业自动化、服务机器人、特种机器人、安全生产和养老服务。
- 中国产业链位置：中国拥有全球最大工业机器人市场、完整制造供应链和快速迭代能力，2024 年工业机器人安装量约占全球 54%。证据：[`SRC-robotics-008`](../../raw/robotics-embodied-ai/documents/SRC-robotics-008-world-robotics-2025-report-industrial-robots.md)
- 关键短板：高端核心零部件、灵巧操作、具身数据、机器人基础模型、可靠性、安全标准和高端生态工具链。
- 政策受益环节：核心部组件、整机系统、机器人操作系统、标准测试、工业/仓储/医疗/养老/应急场景。
- 地方落地线索：北京、上海、深圳、浙江、安徽等地正在围绕机器人和具身智能建设产业集群，需继续建立地方政策表。

## 文件导航

- `00-source-acquisition-plan.md`: 信息获取路线、来源等级和已验证站点。
- `00-source-capture-index.md`: 来源抽取 MOC、raw artifacts、manifest 和补采状态。
- `01-industry-map.md`: 产业链和价值流。
- `02-technology-and-products.md`: 技术路线和产品形态。
- `03-market-and-policy.md`: 中国市场规模、十五五政策和监管。
- `04-companies.md`: 公司和竞争格局，含 [[_entities/LimXDynamics|逐际动力 LimX Dynamics]] 等重点整机/平台公司入口。
- `05-investment-view.md`: 投资逻辑和风险。
- `05a-portfolio-draft-2026-04-28.md`: 100 万 RMB 股票组合草案。
- `06-career-view.md`: 岗位地图和学习路径。
- `07-training-data.md`: 训练数据生产、处理、公司、解决方案和论文数据集。
- `08-umi-gripper-research-and-business-plan.md`: UMI Gripper 技术研究、学习计划、国内数据采集业务落地计划，以及 2026-05-28 下一步任务复核。
- `09-training-data-deep-dive.md`: 训练数据深度调研汇总页和并行研究入口，含 UMI v0 SOP/schema/客户数据包模板与 LeRobot 初学者教学入口。
- `12-robotics-engineering-platforms-2026-06-04.md`: 机器人工程平台综合调研，覆盖数据、训练、评测、部署、真机推理和选型框架。
- `13-robot-company-product-comparison-2026-06-08.md`: 主表机器人公司的产品型号全景对比，覆盖人形/轮式双臂、协作臂/工业机器人、AMR/移动操作的参数、技术路线、优缺点和待验证项。
- [[research-notes/zsibot-matrix-robotics-simulator-deep-dive-2026-07-20|zsibot/matrix（MATRiX）机器人仿真平台深度调研]]: 审计 MuJoCo + Unreal Engine 架构、四足机器人与 ROS 2 能力、发行包和开放边界，并给出商业应用、中小创业机会、PoC 验收与停用条件。
- [[research-notes/roboverse-platform-and-real-data-deep-dive-2026-07-28|RoboVerse 能力边界与具身数采数据增益深度调研]]: 拆解 RoboVerse/MetaSim 的平台边界、多后端任务/数据/学习能力，判断真实数采数据对数据集、仿真、benchmark 和模型的不同增益，并给出 L0–L4 接入契约与四组 A/B PoC。
- [[research-notes/orb-slam3-technology-engineering-commercial-deep-dive-2026-08-05|ORB-SLAM3 技术原理、工程选型与商业落地深度调研]]: R04 主分类、R05/R07 次分类；拆解 ORB 特征、视觉惯性 MAP 初始化、Atlas 多地图、论文 benchmark/失败模式、ROS 2 与 GPL 边界，对照 VINS-Fusion/OpenVINS/RTAB-Map/cuVSLAM，并给出 UMI 与商业 PoC。
- [[research-notes/rtabmap-cuvslam-openvins-comparative-deep-dive-2026-08-05|RTAB-Map、cuVSLAM、OpenVINS 技术与工程选型深度调研]]: R05 主分类、R04/R07 次分类；区分长期 ROS 2 导航/占据建图、NVIDIA 多相机 CUDA VSLAM 与 MSCKF 滤波 VIO，覆盖维护、许可、商业/创业机会和统一 PoC。
- [[research-notes/jetson-thor-and-alternatives-spec-price-comparison-2026-08-05|Jetson Thor 与同类替代平台规格、价格及选型调研]]: R05 主分类、R06 次分类；核验 2026-08-05 当前价格，按内存、功耗、机器人 I/O、软件迁移、量产生命周期与目标模型 PoC 比较 Thor、Orin、IQ-9075、DGX Spark、AMD 128GB 系统及降档方案。
- [[_sources/wechat-embodied-intelligence-robotics-core-technology-overview|一文速览具身智能机器人相关核心技术体系]]: 微信公众号 C 级入门综述来源卡；保留技术地图，并显式隔离未经一级来源验证的企业、政策、市场和产业主张。
- [[research-notes/isaac-sim-vs-gazebo-vs-mujoco-2026-07-14|Isaac Sim vs Gazebo vs MuJoCo 机器人仿真平台选型]]: 按高保真感知/合成数据、ROS 2 系统联调、控制/RL、硬件与商业许可拆解三者边界；包含国产 GPU/AI 加速器支持矩阵、组合架构与 PoC 验收项。
- [[research-notes/srt-soft-robot-tech-company-deep-dive-2026-07-13|SRT 软体机器人公司深度调研]]: 拆解柔性末端执行器技术、业务结构、融资与股权、竞争、十五五关联、创始团队迁移风险和投前尽调问题。
- [[research-notes/airspeed-data-production-platform-2026-06-23|AIRSPEED 具身智能数据生产平台调研]]: 系统拆解 AIRSPEED 的开源采集核心、论文三服务架构、技术转移叙事、性能 claim、版本边界和对中国具身数据基础设施的启发。
- [[research-notes/vla-world-model-data-infrastructure-platform-design-2026-07-06|VLA&世界模型数据基建平台系统调研与设计]]: 基于 `BV1ZFTq6pEA3` 的 15 阶段数据生产 SOP，设计面向 VLA、模仿学习和世界模型的数据生产平台，覆盖采集接入、同步缓存、自动质检、episode builder、多格式导出和失败补采闭环。
- [[research-notes/ego-video-to-dexterous-hand-training-data-system-design-2026-07-14|Ego 视频到灵巧手训练数据：技术路线、系统设计与落地方案]]: 比较普通单目视频、RGB-D/动捕、可穿戴/同构接口三条采集路线，给出手物 4D 重建、跨本体重定向、物理验收、数据 schema 和 6–8 周 PoC 方案。
- [[research-notes/teleoperation-training-data-cost-and-share-2026-07-09|遥操训练数据每小时成本与训练数据占比快速调研]]: 按有效可训练小时估算人类视频、UMI-like、单臂、双臂/人形/灵巧手遥操数据成本，并区分机器人 action 轨迹数据与 VLA foundation model 总训练混合中的遥操占比。
- [[research-notes/embodied-ai-training-data-hour-requirements-2026-07-09|具身智能训练数据需求量与小时数分层估算]]: 按有效可训练小时估算 demo、单任务泛化、客户场景产品化、跨任务策略模型和前沿 VLA/foundation model 所需数据量。
- [[research-notes/boden-intelligence-business-technology-overview-2026-07-08|博登智能商业逻辑、商业计划与技术方案综述]]: 基于 `BV1q3TE6AE4b` 视频深研和 ASR 原文，整理 Physical AI 数据基建公司的商业逻辑、收入结构、客户分层、三层技术方案和待验证风险。
 - [[research-notes/lidar-world-model-training-2026-06-29|激光雷达数据融合进入世界模型训练论文与方案调研]]: 横向梳理 LiDAR 原生生成、BEV/occupancy、多模态 camera-LiDAR latent、JEPA 和移动机器人导航 world model 论文，并给出工程落地方案。
- [[research-notes/home-elderly-care-robots-2026-07-06|家庭养老机器人公司与方案调研]]: 按陪伴提醒、远程巡视、移动载物、康复护理和通用家务机器人五层路线，比较 ElliQ、Hyodol、Labrador、傅利叶、1X、Figure、Tesla、优必选等公司与中国落地方案。
- [[research-notes/embodied-model-physical-understanding-evaluation-2026-07-03|具身智能大模型物理理解能力评估框架]]: 区分动作生成、语义泛化、动作条件预测和规划可用世界模型，提出用反事实预测、minimal physical pairs、闭环 A/B 和多模态约束评估模型是否真正理解物理规律。
- [[research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]]: 基于 Thinking Partner 对话沉淀的职业方向锚点，聚焦企业决策者的成本、收入或风险痛点，以及零售后场/餐饮后厨/酒店后台等早期验证场景。
- [[research-notes/retail-store-robotics-entry-scan-2026-06-10|线下零售门店机器人合作验证初扫]]: 验证中国大型零售公司是否已有足够多线下门店机器人/具身智能合作项目；第一轮结果为暂定样本 0/10，未通过 5/10 门槛但需继续补实公告/年报全文。
- [[research-notes/cross-scenario-near-term-landing-candidate-pool-2026-06-10|具身智能短期落地跨场景候选池]]: 按 1 年内真实订单或试点转生产证据，建立汽车制造、仓储物流、商业服务、电力/数据中心、医疗手术机器人等短期落地候选池。
- [[research-notes/platform-engineer-jd-entry-scan-2026-06-10|具身智能平台工程师 JD 快速入场扫描]]: 用“通用软件平台能力是硬要求、机器人领域知识可补齐”作为第一筛选门槛，初扫平台工程、后端、数据管线、仿真平台和运营系统岗位。
- [[research-notes/libero-lifelong-robot-learning-platform-2026-06-11|LIBERO 终身学习仿真平台调研]]: 拆解 LIBERO 的 lifelong robot learning benchmark 定位、4 个 task suites、130 个任务、baseline、VLA/IL 评测价值，以及 2025-2026 年对固定 benchmark 泛化性的批评。
- [[research-notes/open-embodied-ai-datasets-comparison-2026-06-11|开源具身智能训练与评估数据集横向调研]]: 按预训练/真实微调/特定能力/仿真 benchmark 对比 OXE、DROID、BridgeData、AgiBot、RoboMIND、ALOHA、UMI、LIBERO、ManiSkill、RoboCasa、RoboTwin 等数据集的格式、任务完整度和模型适配。
- [[research-notes/robot-training-data-value-evaluation-2026-06-29|具身智能训练数据价值评估框架]]: 把数据价值拆成边际能力提升、复用性、可信度和全成本风险比，给出采集前打分、采集中实时质检和采后 rollout 验证方法。
- [[research-notes/dora-1-vs-ros2-2026-06-23|dora 1.0 vs ROS 2 调研]]: 对比 dora 的 AI dataflow runtime 路线与 ROS 2 机器人生态底座，给出版本状态、性能、桥接架构和学习/选型建议。
- [[_syntheses/china-umi-gripper-purchase-scan-2026-06-08|中国可购买 UMI 夹爪设备检索]]: LUMOS FastUMI、觅蜂 MEgo Gripper、BeingBeyond U1 等 UMI-like 数采设备的购买状态、价格线索和采购问询清单。
- [[_entities/README|UMI 技术术语实体索引]]: UMI Gripper 初学者术语已拆分为实体页，覆盖 IMU、6DoF、SLAM、Zarr、LeRobot、Diffusion Policy 等概念。

## 关联连接

- [[index|Knowledge Index]]
- [[README|Knowledge README]]
- [[_concepts/embodied-ai|Embodied AI]]
- [[_concepts/robot-training-data|Robot Training Data]]
- [[_concepts/universal-manipulation-interface|Universal Manipulation Interface]]
- [[_entities/AIRSPEED|AIRSPEED]]
- [[_entities/SRTSoftRobotTech|SRT 软体机器人]]
- [[_entities/MATRiXSimulator|MATRiX Simulator]]
- [[_entities/RoboVerse|RoboVerse]]
