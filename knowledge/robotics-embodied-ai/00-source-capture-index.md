---
title: 机器人（具身智能） - 来源抽取索引
date: 2026-06-08
last_updated: 2026-09-02
tags:
  - industry/robotics-embodied-ai
  - sources
  - raw-capture
  - obsidian/moc
aliases:
  - 具身智能来源抽取索引
  - Robotics Source Capture Index
---

# 机器人（具身智能） - 来源抽取索引

> [!summary]
> 本页是 [[00-index|机器人（具身智能）]] 的来源抽取 MOC。来源编号仍以 [[sources.csv]] 为准；原文/清洗件保存在 `raw/robotics-embodied-ai/documents/`，抽取状态见 [source_capture_manifest.csv](../../raw/robotics-embodied-ai/documents/source_capture_manifest.csv)。

## 2026-08-26 WRC 具身大脑可靠性、规模与商业模式来源

| SRC | raw artifact | 用途与边界 |
|---|---|---|
| [`SRC-robotics-534`](../../raw/robotics-embodied-ai/documents/SRC-robotics-534-wrc.md) | 微信文章 Defuddle 全文 | 提取可靠性、模型 scaling 与“物理 Token”问题框架；C 级二次转述，发布日期和关键数字待验证。 |
| [`SRC-robotics-535`](../../raw/robotics-embodied-ai/documents/SRC-robotics-535-token-wrc-2026.md) | 雷峰网 WRC 演讲整理 | 支持星海图商业路径的公开归因；B 级媒体编辑稿，不验证毛利、成功率或单位经济性。 |
| [`SRC-robotics-536`](../../raw/robotics-embodied-ai/documents/SRC-robotics-536-waic-ceo-99.md) | 量子位/AITNT 访谈 | 支持苏度把 `99%+` 视为部署前提的公开归因；B 级，缺 trial protocol 与客户验收。 |

- 来源卡：[[_sources/wechat-wrc-embodied-ai-reliability-scaling-token-business|WRC 可靠性、模型规模与物理 Token 微信文章来源卡]]。
- 下游编译：[[research-notes/embodied-ai-reliability-scaling-and-outcome-pricing-2026-08-26|具身智能可靠性、模型规模与按结果付费的商业化门槛]]。

## 2026-09-02 宇树上市供应链公司来源

| SRC | raw artifact | 用途与边界 |
|---|---|---|
| `SRC-robotics-541`–`544` | [新洁能年报](../../raw/robotics-embodied-ai/documents/SRC-robotics-541-2025.pdf)、[蔚蓝锂芯业绩会](../../raw/robotics-embodied-ai/documents/SRC-robotics-542-2024.pdf)、[创世纪调研记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-543-2025-3-2.pdf)、[丰立智能发行预案](../../raw/robotics-embodied-ai/documents/SRC-robotics-544-2025-a.pdf) | 核验批量、持续供货、重要供应商和验证/小批量阶段；PDF 已保存，自动抽取因代理依赖失败，正文由本地 `pdftotext` 复核。 |
| `SRC-robotics-545` | [长盛轴承互动易归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-545-source.md) | 核验合作产品为自润滑轴承；动态页面只形成 fallback HTML/Markdown。 |
| `SRC-robotics-546`–`550` | [统一行情底表](../../raw/robotics-embodied-ai/data/unitree-public-supply-chain-market-snapshot-2026-08-31.csv) | 2026-08-31 收盘价、市值、近一个月和上市日表现；B 级聚合行情，部分动态页未形成完整 raw 正文，交易前需用券商终端复核。 |

- 来源卡：[[_sources/unitree-listed-supply-chain-source-set|宇树科技上市供应链公司来源集]]。
- 下游编译：[[research-notes/unitree-listed-supply-chain-public-companies-2026-09-02|宇树科技上市供应链 A 股公司调研]]。

## 2026-08-12 EtherCAT 与 TCP/IP 实时控制对照来源

| SRC | raw artifact | 用途与边界 |
|---|---|---|
| [`SRC-robotics-530`](../../raw/robotics-embodied-ai/documents/SRC-robotics-530-rfc-9293-transmission-control-protocol-tcp.md) | IETF RFC 9293 TCP 标准 | 核验可靠、有序字节流、ACK、重传、动态 RTO 和拥塞控制；不代表具体机器人 TCP 实现的实测性能。 |
| [`SRC-robotics-531`](../../raw/robotics-embodied-ai/documents/SRC-robotics-531-rfc-768-user-datagram-protocol.md) | IETF RFC 768 UDP 标准 | 核验最小 datagram 机制及不保证送达/去重/有序；UDP 仍不自动提供 DC、过程映像和 WKC。 |

- 与 `SRC-robotics-505` 的 ETG on-the-fly、ESC、DC、WKC 一手说明合并为 [[research-notes/ethercat-vs-tcp-ip-robot-control-latency-2026-08-12|EtherCAT vs TCP/IP 机器人控制时延专题]]。
- 本轮无统一硬件 A/B benchmark；不提供协议性能倍数。

## 2026-08-11 微信具身数据处理 RoadMap

| SRC | raw artifact | 用途与边界 |
|---|---|---|
| [`SRC-robotics-529`](../../raw/robotics-embodied-ai/documents/SRC-robotics-529-50-vs-ego-roadmap.md) | [微信文章 Defuddle 全文](../../raw/robotics-embodied-ai/documents/SRC-robotics-529-50-vs-ego-roadmap.md) | 提炼多模态采集、动作表征、同步、标注、质量筛选、训练配比和部署回流问题；C 级文章，发布日期、毛利、价格、`50 ms` 与周期数字均待验证。 |

- 来源卡：[[_sources/wechat-embodied-data-processing-roadmap|具身数据 RoadMap 微信文章来源卡]]。
- 下游编译：[[research-notes/embodied-ai-model-data-processing-pipeline-2026-08-11|具身智能模型数据处理闭环]]。

## 2026-08-10 onshape-to-robot 官方来源

- [[_sources/onshape-to-robot-official-source-set|onshape-to-robot 官方仓库、文档、示例与问题来源集]]：固定主仓库 commit `7d0803d`、示例 commit `7e40fd6`，并捕获安装、设计约定、config、URDF/SDF/MuJoCo、processors 和三个具体 issue。
- `SRC-robotics-516`–`524`、`526`–`528` 已形成可读 raw Markdown；`SRC-robotics-525` PyPI 页面 Defuddle 超时，已保留 HTML，版本/依赖由 PyPI JSON 与固定 `pyproject.toml` 交叉核验。
- 综合于 [[research-notes/onshape-to-robot-usage-selection-deep-dive-2026-08-10|onshape-to-robot 用法与选型调研]]；本轮未使用 Onshape 密钥，真实 API 导出仍待 PoC。

## 2026-08-09 EtherCAT 技术与生态来源

| SRC | raw artifact | 用途与边界 |
|---|---|---|
| `SRC-robotics-505`–`510` | ETG 技术、标准化、许可、Implementation Guide、EtherCAT G/TSN | 核验协议机制、IEC、许可、一致性和扩展；`508` 官方 PDF 已用 PyMuPDF4LLM 捕获；ETG 性能数字不作为任意产品 SLA。 |
| `SRC-robotics-511`–`512` | SOEM 与 IgH 官方资料 | 核验两条开源 MainDevice 实现路线；未在实时内核/机器人台架运行。 |
| `SRC-robotics-513` | ODVA CIP Motion 官方页 | 竞品机制对照；未做统一硬件性能横评。 |
| `SRC-robotics-514`–`515` | 工信部人形机器人及工业互联网政策 | 限定十五五关联；政策未点名 EtherCAT。 |

## 2026-08-09 DexCap 灵巧操作数采来源

| SRC | raw artifact | 用途与边界 |
|---|---|---|
| [`SRC-robotics-277`](../../raw/robotics-embodied-ai/documents/SRC-robotics-277-dexcap-scalable-and-portable-mocap-data-collection-system-for-dexterous-manipula.md) | RSS 2024 / arXiv 论文 | 核验硬件、DexIL、六任务结果和三项明确限制；均为作者实验。 |
| [`SRC-robotics-502`](../../raw/robotics-embodied-ai/documents/SRC-robotics-502-dexcap-project-page.md) | 官方项目页 | 核验演示、工作流与 human-in-the-loop；不作为商业客户证据。 |
| [`SRC-robotics-504`](../../raw/robotics-embodied-ai/documents/SRC-robotics-504-dexcap-official-code-repository-at-commit-4b0bed0.md) | 固定提交 README | 核验采集、处理、HDF5、训练和 MIT 许可；未编译，第三方许可另审。 |

## 当前状态

| 状态 | 数量 | 含义 |
|---|---:|---|
| `exists` | 116 | 既有 Markdown/PDF raw artifact。 |
| `ok` | 292 | 已成功抽取的 raw artifact。 |
| `fallback_html` | 18 | 正文抽取失败但已保存 HTML 或 raw sidecar。 |
| `manual_parse` | 14 | defuddle、静态网页或自动 PDF 抽取不能承载审计信息时，由本地 PDF 文本、网页内嵌结构化数据、GitHub API 或固定提交文本复核。 |
| `manual_capture` | 1 | 手工 curl 保存 HTML，未生成清洗 Markdown。 |
| `failed` | 20 | defuddle 与 HTML fallback 都失败，或正文质量经复核不可用，需要浏览器、官方 PDF 或手工补采。 |

## 2026-08-06 Unreal Engine 机器人与具身智能来源

| SRC | raw artifact | 用途与边界 |
|---|---|---|
| `SRC-robotics-426`–`430` | Epic 许可/Chaos、UnrealCV、Gym-UnrealCV | 定义 UE proprietary license、游戏物理和可编程视觉世界边界；Epic licensing 自动抽取 403，保留失败记录并以官方页面实时核验。 |
| `SRC-robotics-431`–`439` | AirSim、Project AirSim、Cosys-AirSim、CARLA、CARLA-Air | 核验 UAV、道路、SIL/HIL、ROS 2 和空地协同；CARLA-Air 为非商业许可，AirSim release 与 archived 标志分开处理。 |
| `SRC-robotics-440`–`445` | Unreal Robotics Lab、SPEAR、SimWorld-Robotics | 核验 UE + MuJoCo、通用 UE Python 控制和城市具身 benchmark；论文性能不跨项目排名。 |
| `SRC-robotics-446`–`455` | rclUE、ROSIntegration、UnrealROX、RobotriX、UNav-Sim、HoloOcean、NDDS | 覆盖 ROS 接口、室内视觉、海洋机器人和历史合成数据；NDDS 为 CC BY-NC-SA 且长期不活跃。 |
| `SRC-robotics-456`–`462` | HERCULES、HEROES、数字孪生、3DGS、VirtualEnv、SimWorld Studio | 覆盖多机器人、灾害、协作机械臂和 Agent 生成世界；多项仍是论文确认而非完整仓库审计。 |

## 2026-08-06 Unity 机器人与具身智能来源

| SRC | raw artifact | 用途与边界 |
|---|---|---|
| [`SRC-robotics-463`](../../raw/robotics-embodied-ai/documents/SRC-robotics-463-unity-plans-pricing-and-editor-software-terms.md)–[`469`](../../raw/robotics-embodied-ai/documents/SRC-robotics-469-unity-perception-official-repository-readme.md) | Unity 条款、Robotics Hub、ROS/URDF、ML-Agents、Perception | 核验引擎与代码许可分层、官方机器人接入和学习/合成数据工具；Perception 已明确停更。 |
| [`SRC-robotics-470`](../../raw/robotics-embodied-ai/documents/SRC-robotics-470-ros2-for-unity-official-repository-readme.md)–[`472`](../../raw/robotics-embodied-ai/documents/SRC-robotics-472-ros-sharp-official-repository-readme.md) | ros2-for-unity、Robotec GPU LiDAR、ROS# | 核验原生 ROS 2、GPU LiDAR 与历史 C#/rosbridge 接入；部署兼容和组件许可另验。 |
| [`SRC-robotics-473`](../../raw/robotics-embodied-ai/documents/SRC-robotics-473-ai2-thor-official-repository-readme.md)–[`484`](../../raw/robotics-embodied-ai/documents/SRC-robotics-484-teach-task-driven-embodied-agents-that-chat.md) | AI2-THOR、RoboTHOR、ProcTHOR、ManipulaTHOR、Holodeck、ALFRED、TEACh | 覆盖室内交互、sim-to-real、程序化世界、移动操作、语言任务与对话；离散动作不外推为真机控制。 |
| [`SRC-robotics-485`](../../raw/robotics-embodied-ai/documents/SRC-robotics-485-virtualhome-official-repository-readme.md)–[`490`](../../raw/robotics-embodied-ai/documents/SRC-robotics-490-threedworld-a-platform-for-interactive-multi-modal-physical-simulation.md) | VirtualHome、VRKitchen、ThreeDWorld | 覆盖家庭活动程序、VR 示教、多模态和物理交互；TDW 已进入 LTS。 |
| [`SRC-robotics-491`](../../raw/robotics-embodied-ai/documents/SRC-robotics-491-flightmare-official-repository-readme.md)–[`501`](../../raw/robotics-embodied-ai/documents/SRC-robotics-501-dmava-distributed-multi-autonomous-vehicle-architecture-using-autoware.md) | Flightmare、AWSIM、SVL、AutoDRIVE、CLOiSim、分布式 AWSIM | 覆盖 UAV、自动驾驶、多机器人和 HIL；AWSIM 代码/资产异许可，SVL 已 sunset。 |

`SRC-robotics-474` 与 `484` 自动正文抽取退化为 HTML fallback，但已保留页面和元数据；其论文事实同时由 arXiv 当前页面核验。

## 2026-08-06 3D 仿真资产生产管线调研来源

| SRC | raw artifact | 用途与边界 |
|---|---|---|
| [`SRC-robotics-407`](../../raw/robotics-embodied-ai/documents/SRC-robotics-407-openusd-introduction-and-composition-model.md)–[`409`](../../raw/robotics-embodied-ai/documents/SRC-robotics-409-simready-foundation-specification-and-validation-framework.md) | OpenUSD、UsdPhysics、SimReady Foundation | 定义组合式 canonical asset、刚体物理 schema 和机器可检查质量门；不证明跨引擎数值等价。 |
| [`SRC-robotics-410`](../../raw/robotics-embodied-ai/documents/SRC-robotics-410-nvidia-isaac-sim-current-asset-ingestion-overview.md)–[`413`](../../raw/robotics-embodied-ai/documents/SRC-robotics-413-unreal-engine-datasmith-cad-import-and-tessellation-workflow.md) | Isaac Sim/URDF/Replicator 与 Datasmith CAD | 核验多源导入、合成数据和 CAD tessellation 工作流；导入成功不等于任务可信。 |
| [`SRC-robotics-414`](../../raw/robotics-embodied-ai/documents/SRC-robotics-414-colmap-structure-from-motion-and-multi-view-stereo-pipeline.md)–[`416`](../../raw/robotics-embodied-ai/documents/SRC-robotics-416-nerfstudio-gaussian-splatting-implementation-and-export-limits.md) | COLMAP、ReCap、Nerfstudio | 对照摄影测量、LiDAR scan-to-mesh 和 3DGS appearance 表示；均需额外物理/语义编译。 |
| [`SRC-robotics-417`](../../raw/robotics-embodied-ai/documents/SRC-robotics-417-infinigen-sim-procedural-articulated-simulation-assets.md)–[`419`](../../raw/robotics-embodied-ai/documents/SRC-robotics-419-trellis-structured-3d-latent-asset-generation.md) | Infinigen-Sim、Hunyuan3D、TRELLIS | 核验程序化 articulated asset 与生成式 mesh/PBR/Gaussian 能力；作者指标不外推为 metric/physics 保证。 |
| [`SRC-robotics-420`](../../raw/robotics-embodied-ai/documents/SRC-robotics-420-mujoco-model-asset-collision-and-inertia-documentation.md)–[`422`](../../raw/robotics-embodied-ai/documents/SRC-robotics-422-houdini-solaris-procedural-usd-workflow.md) | MuJoCo、ROS 2 URDF、Houdini Solaris | 区分 visual/collision/inertial，并核验程序化 USD 资产工厂入口。 |
| [`SRC-robotics-423`](../../raw/robotics-embodied-ai/documents/SRC-robotics-423-simready-foundation-profile-validation-workflow-2026-04-1.md)–[`425`](../../raw/robotics-embodied-ai/documents/SRC-robotics-425-simready-foundation-requirement-severity-conventions-2026-04-1.md) | SimReady 2026.04.1 profile、validator、severity | 定义 Profile 选型、零失败规范门、JSON/stamp 证据和 MUST/SHOULD 边界；运行时与任务级另行验收。 |

## 2026-08-05 RTAB-Map、cuVSLAM、OpenVINS 深度调研来源

| SRC | raw artifact | 用途与边界 |
|---|---|---|
| [`SRC-robotics-350`](../../raw/robotics-embodied-ai/documents/SRC-robotics-350-rtab-map-large-scale-and-long-term-lidar-and-visual-slam-paper-full-pdf.md)–[`353`](../../raw/robotics-embodied-ai/documents/SRC-robotics-353-rtab-map-github-repository-release-and-maintenance-audit.md) | RTAB-Map 论文、core README/许可证与 GitHub 审计 | 核验 WM/LTM、回环/图/occupancy、当前 release/head 与 BSD；论文旧硬件数值不外推。 |
| [`SRC-robotics-354`](../../raw/robotics-embodied-ai/documents/SRC-robotics-354-cuvslam-cuda-accelerated-visual-odometry-and-mapping-paper-full-pdf.md)–[`356`](../../raw/robotics-embodied-ai/documents/SRC-robotics-356-cuvslam-github-repository-release-and-maintenance-audit.md) | cuVSLAM 论文、NVIDIA Community License 与 GitHub 审计 | 核验 CUDA/multi-camera/VIO、作者 benchmark、v17 和 NVIDIA Platforms 限定；不视作现场 SLA。 |
| [`SRC-robotics-357`](../../raw/robotics-embodied-ai/documents/SRC-robotics-357-openvins-research-platform-for-visual-inertial-estimation-paper-full-pdf.md)–[`361`](../../raw/robotics-embodied-ai/documents/SRC-robotics-361-openvins-gpl-3-0-license-at-audited-commit.md) | OpenVINS 论文、官方架构/标定、GitHub 审计与 GPL | 核验 MSCKF、标定、回环边界、head/tag；GPL 解释不构成法律意见。 |

## 2026-08-05 ORB-SLAM3 深度调研来源

| SRC | raw artifact | 用途与边界 |
|---|---|---|
| [`SRC-robotics-338`](../../raw/robotics-embodied-ai/documents/SRC-robotics-338-orb-slam3-full-paper.md) | [ORB-SLAM3 完整论文](../../raw/robotics-embodied-ai/documents/SRC-robotics-338-orb-slam3-full-paper.md) | 核验系统架构、MAP 视觉惯性初始化、Atlas、多数据关联、EuRoC/TUM-VI 作者实验、timing 和低纹理失败；不外推为现场 SLA。 |
| [`SRC-robotics-339`](../../raw/robotics-embodied-ai/documents/SRC-robotics-339-orb-slam3-official-repository-readme-at-audited-commit.md)–[`342`](../../raw/robotics-embodied-ai/documents/SRC-robotics-342-orb-slam3-dependency-and-license-inventory-at-audited-commit.md) | 官方固定提交 README、GitHub 审计、校准和依赖 | 核验支持模式、ROS1-era 环境、当前 head/release、坐标/标定与 GPL/依赖许可；动态社区计数不可视为采用或质量。 |
| [`SRC-robotics-343`](../../raw/robotics-embodied-ai/documents/SRC-robotics-343-vins-fusion-official-repository-readme-at-audited-commit.md)–[`346`](../../raw/robotics-embodied-ai/documents/SRC-robotics-346-nvidia-cuvslam-official-repository-readme-at-audited-commit.md) | VINS-Fusion、OpenVINS、RTAB-Map ROS2、cuVSLAM | 官方替代方案边界对照；未做统一硬件性能排名。 |
| [`SRC-robotics-347`](../../raw/robotics-embodied-ai/documents/SRC-robotics-347-tum-vi-benchmark-official-dataset-page.md)–[`348`](../../raw/robotics-embodied-ai/documents/SRC-robotics-348-euroc-mav-dataset-official-page.md) | TUM-VI 与 EuRoC 官方 benchmark | 限定论文数据的传感器、同步、ground-truth 和场景口径。 |
| [`SRC-robotics-349`](../../raw/robotics-embodied-ai/documents/SRC-robotics-349-rtab-map-ros2-bsd-3-clause-license-at-audited-commit.md) | RTAB-Map ROS2 固定提交许可证 | 核验 BSD-3-Clause 对照；不覆盖依赖、数据和机器人集成许可。 |

## 2026-08-05 微信具身智能技术综述

| SRC | raw artifact | 用途与边界 |
|---|---|---|
| [`SRC-robotics-337`](../../raw/robotics-embodied-ai/documents/SRC-robotics-337-source.md) | [微信文章 Defuddle 全文](../../raw/robotics-embodied-ai/documents/SRC-robotics-337-source.md) | 用于建立感知—决策—执行—反馈—学习入门地图；作者署名“机器人小毛”、公众号“古月居”，发布日期待验证。无一级引用的公司、政策、市场与性能主张不作为已验证事实。 |

## 2026-07-28 RLinf 与开源机械臂视频深研来源

| SRC | raw artifact | 用途与边界 |
|---|---|---|
| `SRC-robotics-323` | RLinf official repository | 核验 RLinf 的开源定位、工作流、集成与许可；仓库自述的采用/性能不作为独立商业或可靠性证据。 |
| `SRC-robotics-324` | π_RL preprint | 核验 Flow-Noise/Flow-SDE 方法、实验和作者报告的效率/效果边界；预印本不等同于现场部署证据。 |
| `SRC-robotics-325` | LeRobot SO-101 official docs | 核验 leader/follower 架构、组装与软件依赖；不核验视频中的人民币价格或任务成功率。 |
| `SRC-robotics-326` | OpenArm official repository | 核验公开硬件/软件/仿真范围和许可；当前售价、供货、维保和性能另行询价/实测。 |

## 2026-07-20 MATRiX 机器人仿真平台来源

| SRC | raw artifact | 用途与边界 |
|---|---|---|
| [`SRC-robotics-310`](../../raw/robotics-embodied-ai/documents/SRC-robotics-310-matrix-repository-readme-at-audited-commit.md) | [固定提交 README](../../raw/robotics-embodied-ai/documents/SRC-robotics-310-matrix-repository-readme-at-audited-commit.md) | 核验安装入口、支持机器人、演示与仓库自述；营销表述不作为独立性能证据。 |
| [`SRC-robotics-311`](../../raw/robotics-embodied-ai/documents/SRC-robotics-311-matrix-v0-1-2-release-and-package-manifest.md) | [v0.1.2 Release](../../raw/robotics-embodied-ai/documents/SRC-robotics-311-matrix-v0-1-2-release-and-package-manifest.md) | 核验公开稳定发行说明；实际包体、下载量与 tag 异常由 `SRC-robotics-312` 补充。 |
| [`SRC-robotics-312`](../../raw/robotics-embodied-ai/documents/SRC-robotics-312-matrix-github-maintenance-and-issue-audit.md) | [GitHub API 审计](../../raw/robotics-embodied-ai/documents/SRC-robotics-312-matrix-github-maintenance-and-issue-audit.md) | 2026-07-20 快照：提交、贡献者、stars/forks、发行资产、issue/PR 与 tag；动态指标不可视为永久事实。 |
| [`SRC-robotics-313`](../../raw/robotics-embodied-ai/documents/SRC-robotics-313-genisom-ai-official-open-source-catalog.md) | [GENISOM.AI 开源目录](../../raw/robotics-embodied-ai/documents/SRC-robotics-313-genisom-ai-official-open-source-catalog.md) | 核验 MATRiX 在 RoamerX、VLN、SDK 与 URDF 资源生态中的定位。 |
| [`SRC-robotics-314`](../../raw/robotics-embodied-ai/documents/SRC-robotics-314-mujoco-unreal-engine-plugin-upstream-repository.md) | [MuJoCo–UE 上游仓库](../../raw/robotics-embodied-ai/documents/SRC-robotics-314-mujoco-unreal-engine-plugin-upstream-repository.md) | 核验 MATRiX 致谢的上游项目和公开许可状态；不据此推断未公开代码关系。 |
| [`SRC-robotics-315`](../../raw/robotics-embodied-ai/documents/SRC-robotics-315-unreal-robotics-lab-a-high-fidelity-robotics-simulator-with-advanced-physics-and.md) | [Unreal Robotics Lab 预印本](../../raw/robotics-embodied-ai/documents/SRC-robotics-315-unreal-robotics-lab-a-high-fidelity-robotics-simulator-with-advanced-physics-and.md) | 证明 2025 年已有 UE + MuJoCo 公开系统与实验，限制“全球首个”类无限定营销说法。 |
| [`SRC-robotics-316`](../../raw/robotics-embodied-ai/documents/SRC-robotics-316-2026.md) | [2026 真实场景训练行动](../../raw/robotics-embodied-ai/documents/SRC-robotics-316-2026.md) | 核验四足机器人、成熟仿真平台和成功率/效率/安全/经济性等政策测量要求。 |
| [`SRC-robotics-317`](../../raw/robotics-embodied-ai/documents/SRC-robotics-317-source.md) | [机器人模型训练平台国家标准计划](../../raw/robotics-embodied-ai/documents/SRC-robotics-317-source.md) | 核验训练平台规范化与标准化方向；不能直接证明 MATRiX 已符合标准。 |

## Isaac Sim、Gazebo、MuJoCo 仿真平台来源

| 平台 | SRC | raw artifact | 用途 |
|---|---|---|---|
| Isaac Sim | `SRC-robotics-284`–`286` | [6.0.1 下载页](../../raw/robotics-embodied-ai/documents/SRC-robotics-284-nvidia-isaac-sim-6-0-1-download-and-release-page.md)、[系统要求](../../raw/robotics-embodied-ai/documents/SRC-robotics-285-nvidia-isaac-sim-6-0-1-system-requirements.md)、[License FAQ](../../raw/robotics-embodied-ai/documents/SRC-robotics-286-nvidia-isaac-sim-6-0-1-license-faq.md) | 当前版本、RTX/VRAM 门槛和商业交付许可边界。 |
| Gazebo | `SRC-robotics-287`–`290` | [版本生命周期](../../raw/robotics-embodied-ai/documents/SRC-robotics-287-gazebo-release-lifecycle.md)、[Jetty notes](../../raw/robotics-embodied-ai/documents/SRC-robotics-288-gazebo-jetty-release-notes.md)、[ROS 配套](../../raw/robotics-embodied-ai/documents/SRC-robotics-289-installing-gazebo-with-ros-compatibility-guide.md)、[官方仓库](../../raw/robotics-embodied-ai/documents/SRC-robotics-290-gazebo-sim-official-repository-features-and-license.md) | Jetty/Harmonic 选择、ROS 2 兼容、模块化能力与 Apache 2.0。 |
| MuJoCo | `SRC-robotics-291`–`295` | [changelog](../../raw/robotics-embodied-ai/documents/SRC-robotics-291-mujoco-changelog.md)、[overview](../../raw/robotics-embodied-ai/documents/SRC-robotics-292-mujoco-overview-and-key-features.md)、[MJX/Warp](../../raw/robotics-embodied-ai/documents/SRC-robotics-293-mujoco-xla-and-mujoco-warp-documentation.md)、[releases](../../raw/robotics-embodied-ai/documents/SRC-robotics-294-mujoco-official-releases.md)、[license](../../raw/robotics-embodied-ai/documents/SRC-robotics-295-mujoco-apache-2-0-license.md) | 3.9.0、控制/物理定位、GPU 后端与 Apache 2.0。 |

## 国产 GPU/AI 加速器适配来源

| 类别 | SRC | raw artifact | 用途 |
|---|---|---|---|
| 通用后端 | `SRC-robotics-296`–`298` | [JAX accelerator matrix](../../raw/robotics-embodied-ai/documents/SRC-robotics-296-jax-installation-and-accelerator-backend-support.md)、[Gazebo OGRE2 backends](../../raw/robotics-embodied-ai/documents/SRC-robotics-297-gazebo-rendering-installation-and-backend-guide.md)、[Gazebo EGL headless](../../raw/robotics-embodied-ai/documents/SRC-robotics-298-gazebo-headless-rendering-with-egl.md) | 区分 JAX/PJRT 计算后端与 OpenGL/Vulkan/EGL 图形驱动路径。 |
| 摩尔线程 | `SRC-robotics-299`–`300` | [MUSA SDK](../../raw/robotics-embodied-ai/documents/SRC-robotics-299-moore-threads-musa-sdk-software-stack.md)、[Moore Perf 图形 API](../../raw/robotics-embodied-ai/documents/SRC-robotics-300-moore-perf-system-graphics-api-support.md) | CUDA 迁移工具边界及 OpenGL/Vulkan PoC 依据。 |
| 海光 | `SRC-robotics-301` | [DCU ROCm 披露](../../raw/robotics-embodied-ai/documents/SRC-robotics-301-hygon-dcu-rocm-compatibility-disclosure.md) | 证明 ROCm 兼容声明；不把它外推为 JAX/MJX 认证。 |
| 国产 AI/通用计算栈 | `SRC-robotics-302`–`306` | [昇腾 CANN](../../raw/robotics-embodied-ai/documents/SRC-robotics-302-ascend-cann-8-3-rc1-documentation-index.md)、[沐曦 MXMACA](../../raw/robotics-embodied-ai/documents/SRC-robotics-303-metax-products-and-mxmaca-software-ecosystem.md)、[壁仞 BIRENSUPA](../../raw/robotics-embodied-ai/documents/SRC-robotics-304-birensupa-software-platform.md)、[天数智芯](../../raw/robotics-embodied-ai/documents/SRC-robotics-305-iluvatar-corex-software-stack.md)、[寒武纪 BANGPy](../../raw/robotics-embodied-ai/documents/SRC-robotics-306-cambricon-bangpy-developer-manual.md) | 核验各软件栈的公开定位，并界定图形渲染、仿真器直跑与 AI 推理旁路。 |

## 2026-07-18 RoboTTT 长上下文策略来源

| SRC | raw artifact | 用途与边界 |
|---|---|---|
| [`SRC-robotics-307`](../../raw/robotics-embodied-ai/documents/SRC-robotics-307-robottt-context-scaling-for-robot-policies.md) | [RoboTTT arXiv preprint](../../raw/robotics-embodied-ai/documents/SRC-robotics-307-robottt-context-scaling-for-robot-policies.md) | 核验 `BV1HkKG69EeD` 的 8K time-step、TTT/fast weights、论文内真机任务与作者报告指标；预印本不证明跨工厂部署、订单或中国商业化。 |

## 快速定位

- 来源总表：[[sources.csv]]
- 抽取 manifest：[source_capture_manifest.csv](../../raw/robotics-embodied-ai/documents/source_capture_manifest.csv)
- 示例：[`SRC-robotics-060`](../../raw/robotics-embodied-ai/documents/SRC-robotics-060-mimicgen-a-data-generation-system-for-scalable-robot-learning-using-human-demons.md) 的 raw extract 在 [SRC-robotics-060 MimicGen](../../raw/robotics-embodied-ai/documents/SRC-robotics-060-mimicgen-a-data-generation-system-for-scalable-robot-learning-using-human-demons.md)

## 需要补采的来源

> [!warning]
> 以下来源被站点限制、JS 渲染或 SSL/403 阻断。知识笔记可以暂用 `sources.csv` 的 URL，但关键结论需要后续补 raw 证据。

| SRC | 状态 | 原因 | 下一步 |
|---|---|---|---|
| `SRC-robotics-017` | `failed` | NVIDIA investor 页面 403，HTML fallback 也被拒。 | 寻找 NVIDIA 官方新闻镜像、开发者页或 PDF。 |
| `SRC-robotics-019` | `failed` | Tesla 页面 403，HTML fallback 也被拒。 | 用浏览器登录/手工保存，或改用 Tesla 官方可访问页面。 |
| `SRC-robotics-085` | `failed` | 深圳科创局页面 defuddle fetch failed，HTML fallback SSL BAD_ECPOINT。 | 用浏览器手工保存原文，或寻找深圳市政府/政策 PDF 镜像。 |
| `SRC-robotics-105` | `failed` | TRON 1 用户手册 PDF 官网证书过期，自动下载失败。 | 用浏览器手工保存 PDF，或寻找新版下载地址。 |
| `SRC-robotics-190` | `failed` | dora guides URL 自动抽取返回 404。 | 改用 GitHub raw docs、官网 `/book` 路径或浏览器手工保存后再核验。 |
| `SRC-robotics-266` | `failed` | 团体标准站点抽取结果只有“系统错误”。 | 从全国团体标准信息平台或中关村标准化协会补正式 PDF。 |
| `SRC-robotics-267` | `failed` | 高校页面只抽到导航，缺少新闻正文。 | 用浏览器手工保存或寻找学校/项目官方镜像。 |

## 已保存 fallback HTML 的来源

| SRC | raw sidecar | 说明 |
|---|---|---|
| [`SRC-robotics-015`](../../raw/robotics-embodied-ai/documents/SRC-robotics-015-agibot-a2-product-page.md) | [AGIBOT A2](../../raw/robotics-embodied-ai/documents/SRC-robotics-015-agibot-a2-product-page.md) | defuddle 500，但已保存 HTML。 |
| [`SRC-robotics-016`](../../raw/robotics-embodied-ai/documents/SRC-robotics-016-agibot-products-page.md) | [AGIBOT products](../../raw/robotics-embodied-ai/documents/SRC-robotics-016-agibot-products-page.md) | defuddle 500，但已保存 HTML。 |
| [`SRC-robotics-044`](../../raw/robotics-embodied-ai/documents/SRC-robotics-044-agibot-open-agibot-world-2026.md) | [AGIBOT WORLD 2026](../../raw/robotics-embodied-ai/documents/SRC-robotics-044-agibot-open-agibot-world-2026.md) | defuddle 500，但已保存 HTML。 |
| [`SRC-robotics-048`](../../raw/robotics-embodied-ai/documents/SRC-robotics-048-firstmove-egocentric-data-engine-for-robotics.md) | [FirstMove](../../raw/robotics-embodied-ai/documents/SRC-robotics-048-firstmove-egocentric-data-engine-for-robotics.md) | JS 页面无正文，但已保存 HTML。 |
| [`SRC-robotics-049`](../../raw/robotics-embodied-ai/documents/SRC-robotics-049-source.md) | [ModelScope/BAAI](../../raw/robotics-embodied-ai/documents/SRC-robotics-049-source.md) | defuddle URL 解析失败，但已保存 HTML。 |
| [`SRC-robotics-087`](../../raw/robotics-embodied-ai/documents/SRC-robotics-087-source.md) | [杭州强链补链政策解读](../../raw/robotics-embodied-ai/documents/SRC-robotics-087-source.md) | defuddle 无正文，但已保存 HTML。 |
| [`SRC-robotics-120`](../../raw/robotics-embodied-ai/documents/SRC-robotics-120-maniskill-official-website.md) | [ManiSkill](../../raw/robotics-embodied-ai/documents/SRC-robotics-120-maniskill-official-website.md) | defuddle 无正文，但已保存 HTML。 |
| [`SRC-robotics-122`](../../raw/robotics-embodied-ai/documents/SRC-robotics-122-moveit-2-documentation.md) | [MoveIt 2](../../raw/robotics-embodied-ai/documents/SRC-robotics-122-moveit-2-documentation.md) | defuddle 无正文，但已保存 HTML。 |
| [`SRC-robotics-123`](../../raw/robotics-embodied-ai/documents/SRC-robotics-123-agibot-genie-studio.md) | [Agibot Genie Studio](../../raw/robotics-embodied-ai/documents/SRC-robotics-123-agibot-genie-studio.md) | defuddle 无正文，但已保存 HTML。 |

## 手工/论文来源捕获

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-233`](../../raw/robotics-embodied-ai/documents/SRC-robotics-233-hapmorph-a-pneumatic-framework-for-multi-dimensional-haptic-property-rendering.md) | [HapMorph arXiv 摘要页](../../raw/robotics-embodied-ai/documents/SRC-robotics-233-hapmorph-a-pneumatic-framework-for-multi-dimensional-haptic-property-rendering.md) | 用于校验 `BV12XTM6sEGF` 触觉反馈视频中的 21g、50-104mm、4.7N/mm 和 89.4% 等关键指标。 |
| [`SRC-robotics-125`](../../raw/robotics-embodied-ai/documents/roboalign-r1-2605.03821.pdf) | [RoboAlign-R1 PDF](../../raw/robotics-embodied-ai/documents/roboalign-r1-2605.03821.pdf) | arXiv PDF 已保存；摘要页 sidecar 为 [HTML](../../raw/robotics-embodied-ai/documents/roboalign-r1-2605.03821-arxiv.html)。 |
| [`SRC-robotics-126`](../../raw/robotics-embodied-ai/documents/modelscope-roboalign-r1-434219.md) | [ModelScope RoboAlign-R1 Markdown](../../raw/robotics-embodied-ai/documents/modelscope-roboalign-r1-434219.md) | defuddle 因 ModelScope `og:url` protocol-relative metadata 失败；已从 `window.__detail_data__` 生成 Markdown，并保存 [HTML](../../raw/robotics-embodied-ai/documents/modelscope-roboalign-r1-434219.html)。 |

## 2026-07-11 Bilibili 交叉验证来源

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-271`](../../raw/robotics-embodied-ai/documents/SRC-robotics-271-wall-b.md) | [自变量机器人官网](../../raw/robotics-embodied-ai/documents/SRC-robotics-271-wall-b.md) | 核验自变量公司身份、WALL-A/WALL-B、端到端方向和多地布局；不用于确认视频中的估值、营收或客户。 |
| [`SRC-robotics-272`](../../raw/robotics-embodied-ai/documents/SRC-robotics-272-vision-pretraining-for-dense-spatial-perception.md) | [LingBot-Vision 论文](../../raw/robotics-embodied-ai/documents/SRC-robotics-272-vision-pretraining-for-dense-spatial-perception.md) | 核验 LingBot-Vision 与 LingBot-Depth 2.0 的稠密空间感知/深度补全定位；benchmark 数字仍为作者报告。 |

## SRT 软体机器人公司调研来源

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-254`](../../raw/robotics-embodied-ai/documents/SRC-robotics-254-srt.md) | [SRT 企业简介](../../raw/robotics-embodied-ai/documents/SRC-robotics-254-srt.md) | 公司边界、产品矩阵、发展历程和融资金额口径。 |
| [`SRC-robotics-256`](../../raw/robotics-embodied-ai/documents/SRC-robotics-256-sfg-snm2-n4049.md) | [SFG 产品页](../../raw/robotics-embodied-ai/documents/SRC-robotics-256-sfg-snm2-n4049.md) | 一个可核验型号的负载、节拍、寿命和工作压力。 |
| [`SRC-robotics-258`](../../raw/robotics-embodied-ai/documents/SRC-robotics-258-2024-3.md) | [北京市专精特新报告](../../raw/robotics-embodied-ai/documents/SRC-robotics-258-2024-3.md) | 政府侧公司资质、专利、国家和客户覆盖口径。 |
| [`SRC-robotics-259`](../../raw/robotics-embodied-ai/documents/SRC-robotics-259-source.md) | [北京经开区 2026 报道](../../raw/robotics-embodied-ai/documents/SRC-robotics-259-source.md) | 最新业务方向、产品覆盖和上市计划线索。 |
| [`SRC-robotics-260`](../../raw/robotics-embodied-ai/documents/SRC-robotics-260-source.md) | [上交所招股书抽取](../../raw/robotics-embodied-ai/documents/SRC-robotics-260-source.md) | 金石基金投资 SRT 的历史注册资本与持股比例；同时保存 PDF/JSON/key-info。 |
| [`SRC-robotics-263`](../../raw/robotics-embodied-ai/documents/SRC-robotics-263-ceo.md) | [高少龙再创业报道](../../raw/robotics-embodied-ai/documents/SRC-robotics-263-ceo.md) | 2026 年创始人及两名前高管迁移线索，需公司/工商进一步确认。 |
| [`SRC-robotics-264`](../../raw/robotics-embodied-ai/documents/SRC-robotics-264-onrobot-soft-gripper-official-product-announcement.md) | [OnRobot Soft Gripper](../../raw/robotics-embodied-ai/documents/SRC-robotics-264-onrobot-soft-gripper-official-product-announcement.md) | 国际软夹爪可比产品参数和食品级/无外接气源差异。 |

> [!warning]
> `SRC-robotics-266` 自动抽取仅得到站点“系统错误”，`SRC-robotics-267` 未抽到高校新闻正文；两者虽被脚本记为 `ok`，本次不作为关键事实的唯一依据，后续应更换官方 PDF/可访问页面。

## AIRSPEED 数据生产平台来源

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-183`](../../raw/robotics-embodied-ai/documents/SRC-robotics-183-airspeed-project-page.html) | [AIRSPEED project page HTML](../../raw/robotics-embodied-ai/documents/SRC-robotics-183-airspeed-project-page.html) | 官网页面；web extraction 不稳定，改用 curl 保存 HTML。 |
| [`SRC-robotics-184`](../../raw/robotics-embodied-ai/documents/SRC-robotics-184-airspeed-technical-report.pdf) | [AIRSPEED technical report PDF](../../raw/robotics-embodied-ai/documents/SRC-robotics-184-airspeed-technical-report.pdf) / [TXT](../../raw/robotics-embodied-ai/documents/SRC-robotics-184-airspeed-technical-report.txt) | 技术报告，已用 `pdftotext -layout` 生成文本 sidecar。 |
| [`SRC-robotics-185`](../../raw/robotics-embodied-ai/documents/SRC-robotics-185-eai-data-engineering-survey.pdf) | [EAI data engineering survey PDF](../../raw/robotics-embodied-ai/documents/SRC-robotics-185-eai-data-engineering-survey.pdf) / [TXT](../../raw/robotics-embodied-ai/documents/SRC-robotics-185-eai-data-engineering-survey.txt) | EAI 数据工程综述，已生成文本 sidecar。 |
| [`SRC-robotics-186`](../../raw/robotics-embodied-ai/documents/SRC-robotics-186-airspeed-technology-transfer-report.pdf) | [Technology transfer report PDF](../../raw/robotics-embodied-ai/documents/SRC-robotics-186-airspeed-technology-transfer-report.pdf) / [TXT](../../raw/robotics-embodied-ai/documents/SRC-robotics-186-airspeed-technology-transfer-report.txt) | 英文技术转移报告，商业化 claim 需独立验证。 |
| [`SRC-robotics-187`](../../raw/robotics-embodied-ai/documents/SRC-robotics-187-airspeed-technology-transfer-report-cn.pdf) | [中文技术转移报告 PDF](../../raw/robotics-embodied-ai/documents/SRC-robotics-187-airspeed-technology-transfer-report-cn.pdf) / [TXT](../../raw/robotics-embodied-ai/documents/SRC-robotics-187-airspeed-technology-transfer-report-cn.txt) | 中文技术转移报告，包含客户、融资、标准参与等待验证 claim。 |
| [`SRC-robotics-188`](../../raw/robotics-embodied-ai/documents/SRC-robotics-188-airspeed-github-readme.md) | [AIRSPEED GitHub README](../../raw/robotics-embodied-ai/documents/SRC-robotics-188-airspeed-github-readme.md) | 当前 v1.3 开源能力边界，用于校正官网/论文完整架构表述。 |

## UMI 设备购买线索来源

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-127`](../../raw/robotics-embodied-ai/documents/SRC-robotics-127-aifitlab-umi-gripper-collection.md) | [AIFITLAB UMI Gripper collection](../../raw/robotics-embodied-ai/documents/SRC-robotics-127-aifitlab-umi-gripper-collection.md) | LUMOS FastUMI Pro/Ego/Go 商品聚合页。 |
| [`SRC-robotics-128`](../../raw/robotics-embodied-ai/documents/SRC-robotics-128-aifitlab-lumos-fastumi-pro-product-page.md) | [LUMOS FastUMI Pro](../../raw/robotics-embodied-ai/documents/SRC-robotics-128-aifitlab-lumos-fastumi-pro-product-page.md) | FastUMI Pro 公开价格、配置、backorder 和技术参数。 |
| [`SRC-robotics-129`](../../raw/robotics-embodied-ai/documents/SRC-robotics-129-aifitlab-lumos-fastumi-go-product-page.md) | [LUMOS FastUMI Go](../../raw/robotics-embodied-ai/documents/SRC-robotics-129-aifitlab-lumos-fastumi-go-product-page.md) | 背包式双手 UMI 数采设备公开价格与配置。 |
| [`SRC-robotics-130`](../../raw/robotics-embodied-ai/documents/SRC-robotics-130-aifitlab-lumos-fastumi-ego-product-page.md) | [LUMOS FastUMI Ego](../../raw/robotics-embodied-ai/documents/SRC-robotics-130-aifitlab-lumos-fastumi-ego-product-page.md) | 第一人称无本体采集设备公开价格与传感器参数。 |
| [`SRC-robotics-131`](../../raw/robotics-embodied-ai/documents/SRC-robotics-131-mego.md) | [觅蜂 MEgo 量产发货](../../raw/robotics-embodied-ai/documents/SRC-robotics-131-mego.md) | MEgo Gripper 量产发货、480g 和 1 mm 轨迹重建线索。 |
| [`SRC-robotics-132`](../../raw/robotics-embodied-ai/documents/SRC-robotics-132-awe2026-fastumi.md) | [鹿明 AWE2026 FastUMI 发布](../../raw/robotics-embodied-ai/documents/SRC-robotics-132-awe2026-fastumi.md) | FastUMI 全家桶发布与陆续上线京东线索。 |
| [`SRC-robotics-133`](../../raw/robotics-embodied-ai/documents/SRC-robotics-133-beingbeyond-launches-u1-realdexumi.md) | [BeingBeyond U1 RealDexUMI](../../raw/robotics-embodied-ai/documents/SRC-robotics-133-beingbeyond-launches-u1-realdexumi.md) | U1 / RealDexUMI 官方发布。 |
| [`SRC-robotics-134`](../../raw/robotics-embodied-ai/documents/SRC-robotics-134-realdexumi-wearable-universal-manipulation-interface-paper.md) | [RealDexUMI arXiv](../../raw/robotics-embodied-ai/documents/SRC-robotics-134-realdexumi-wearable-universal-manipulation-interface-paper.md) | RealDexUMI 论文摘要页。 |

## dora / ROS 2 中间件专题来源

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-189`](../../raw/robotics-embodied-ai/documents/SRC-robotics-189-dora-1-0-official-website.md) | [Dora 1.0 official website](../../raw/robotics-embodied-ai/documents/SRC-robotics-189-dora-1-0-official-website.md) | defuddle 超时，已保存官网 HTML；用于核验 dora 1.0/RC 与性能主张。 |
| `SRC-robotics-190` | 无 | dora guides URL 自动抽取失败，不作为关键结论依据。 |
| [`SRC-robotics-191`](../../raw/robotics-embodied-ai/documents/SRC-robotics-191-dora-github-readme.md) | [Dora GitHub README](../../raw/robotics-embodied-ai/documents/SRC-robotics-191-dora-github-readme.md) | GitHub raw README，成功 direct-download。 |
| [`SRC-robotics-192`](../../raw/robotics-embodied-ai/documents/SRC-robotics-192-dora-pypi-package-dora-rs.md) | [dora-rs PyPI](../../raw/robotics-embodied-ai/documents/SRC-robotics-192-dora-pypi-package-dora-rs.md) | PyPI 页面，记录 `0.5.0` 稳定版。 |
| [`SRC-robotics-193`](../../raw/robotics-embodied-ai/documents/SRC-robotics-193-dora-github-release-v0-5-0.md) | [Dora GitHub release v0.5.0](../../raw/robotics-embodied-ai/documents/SRC-robotics-193-dora-github-release-v0-5-0.md) | GitHub release tag fallback HTML，记录 `v0.5.0` 为 Latest。 |
| [`SRC-robotics-194`](../../raw/robotics-embodied-ai/documents/SRC-robotics-194-dora-dataflow-oriented-robotic-architecture-paper.md) | [DORA arXiv paper](../../raw/robotics-embodied-ai/documents/SRC-robotics-194-dora-dataflow-oriented-robotic-architecture-paper.md) | 论文摘要页，说明 DORA 的低延迟/低 CPU overhead 目标。 |
| [`SRC-robotics-195`](../../raw/robotics-embodied-ai/documents/SRC-robotics-195-dora-robotic-dataflow-benchmark-repository.md) | [dora benchmark repository](../../raw/robotics-embodied-ai/documents/SRC-robotics-195-dora-robotic-dataflow-benchmark-repository.md) | benchmark README，包含 CPU bulk data 与 CUDA IPC 对比和 caveat。 |
| [`SRC-robotics-196`](../../raw/robotics-embodied-ai/documents/SRC-robotics-196-ros-2-releases-official-documentation.md) | [ROS 2 releases docs](../../raw/robotics-embodied-ai/documents/SRC-robotics-196-ros-2-releases-official-documentation.md) | raw `.rst` 以 fallback sidecar 保存；记录 Lyrical Luth、Jazzy、Humble 等发行版。 |
| [`SRC-robotics-197`](../../raw/robotics-embodied-ai/documents/SRC-robotics-197-ros-2-nodes-official-documentation.md) | [ROS 2 nodes docs](../../raw/robotics-embodied-ai/documents/SRC-robotics-197-ros-2-nodes-official-documentation.md) | raw `.rst` 以 fallback sidecar 保存；用于节点/话题/服务/动作概念。 |
| [`SRC-robotics-198`](../../raw/robotics-embodied-ai/documents/SRC-robotics-198-ros-2-qos-official-documentation.md) | [ROS 2 QoS docs](../../raw/robotics-embodied-ai/documents/SRC-robotics-198-ros-2-qos-official-documentation.md) | raw `.rst` 以 fallback sidecar 保存；用于 DDS QoS 能力对比。 |
| [`SRC-robotics-199`](../../raw/robotics-embodied-ai/documents/SRC-robotics-199-ros-2-design-architecture-and-uses-in-the-wild.md) | [ROS 2 overview paper](../../raw/robotics-embodied-ai/documents/SRC-robotics-199-ros-2-design-architecture-and-uses-in-the-wild.md) | ROS 2 架构和真实部署综述论文摘要页。 |

## 2026-07-07 Bilibili 深研一级校验来源

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-238`](../../raw/robotics-embodied-ai/documents/SRC-robotics-238-nvidia-isaac-sim-4-5-documentation.md) | [NVIDIA Isaac Sim 4.5 documentation](../../raw/robotics-embodied-ai/documents/SRC-robotics-238-nvidia-isaac-sim-4-5-documentation.md) | 用于校验 Isaac Sim 的 GPU PhysX、多传感器 RTX 渲染、digital twin、Replicator、Isaac Lab 和 ROS/ROS2 bridge。 |
| [`SRC-robotics-239`](../../raw/robotics-embodied-ai/documents/SRC-robotics-239-nvidia-isaac-sim-4-5-system-requirements.md) | [Isaac Sim 4.5 requirements](../../raw/robotics-embodied-ai/documents/SRC-robotics-239-nvidia-isaac-sim-4-5-system-requirements.md) | 用于校验视频提到的 Isaac Sim 硬件/系统门槛。 |
| [`SRC-robotics-240`](../../raw/robotics-embodied-ai/documents/SRC-robotics-240-nvidia-isaac-lab-binary-installation-documentation.md) | [Isaac Lab binary installation](../../raw/robotics-embodied-ai/documents/SRC-robotics-240-nvidia-isaac-lab-binary-installation-documentation.md) | 用于校验 Isaac Lab clone、symlink、`isaaclab.sh` 和环境管理流程。 |
| [`SRC-robotics-241`](../../raw/robotics-embodied-ai/documents/SRC-robotics-241-do-as-i-do-dexterous-manipulation-data-from-everyday-human-videos.md) | [Do as I Do arXiv HTML](../../raw/robotics-embodied-ai/documents/SRC-robotics-241-do-as-i-do-dexterous-manipulation-data-from-everyday-human-videos.md) | 用于校验 `BV1WfTk6EEZ8` 中 monocular RGB reconstruction、retargeting、71% success rate 和 video filtering playbook。 |
| [`SRC-robotics-242`](../../raw/robotics-embodied-ai/documents/SRC-robotics-242-abot-m0-5-unified-mobility-and-manipulation-world-action-model.md) | [ABot-M0.5 arXiv HTML](../../raw/robotics-embodied-ai/documents/SRC-robotics-242-abot-m0-5-unified-mobility-and-manipulation-world-action-model.md) | 用于校验 `BV1F7Ts6WEYj` 中 intermediate latent actions、D-MoT、Dream Forcing 和 WAM limitations。 |

## 2026-07-14 Ego 视频到灵巧手训练数据来源

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-275`](../../raw/robotics-embodied-ai/documents/SRC-robotics-275-hawor-world-space-hand-motion-reconstruction-from-egocentric-videos.md) | [HaWoR CVPR 2025](../../raw/robotics-embodied-ai/documents/SRC-robotics-275-hawor-world-space-hand-motion-reconstruction-from-egocentric-videos.md) | 第一人称视频世界坐标手部重建、自适应 Ego SLAM 与缺失轨迹补全。 |
| [`SRC-robotics-276`](../../raw/robotics-embodied-ai/documents/SRC-robotics-276-dexumi-using-human-hand-as-the-universal-manipulation-interface-for-dexterous-ma.md) | [DexUMI](../../raw/robotics-embodied-ai/documents/SRC-robotics-276-dexumi-using-human-hand-as-the-universal-manipulation-interface-for-dexterous-ma.md) | 可穿戴外骨骼、触觉反馈和机器人手图像修复；成功率为作者报告。 |
| [`SRC-robotics-277`](../../raw/robotics-embodied-ai/documents/SRC-robotics-277-dexcap-scalable-and-portable-mocap-data-collection-system-for-dexterous-manipula.md) | [DexCap](../../raw/robotics-embodied-ai/documents/SRC-robotics-277-dexcap-scalable-and-portable-mocap-data-collection-system-for-dexterous-manipula.md) | 便携、抗遮挡手部动捕，以及 IK + 点云模仿学习和人类在环修正。 |
| [`SRC-robotics-278`](../../raw/robotics-embodied-ai/documents/SRC-robotics-278-unidex-a-robot-foundation-suite-for-universal-dexterous-hand-control-from-egocen.md) | [UniDex 论文](../../raw/robotics-embodied-ai/documents/SRC-robotics-278-unidex-a-robot-foundation-suite-for-universal-dexterous-hand-control-from-egocen.md) | 50K+ 轨迹、8 种手、FAAS、UniDex-VLA 与 UniDex-Cap；规模和指标为作者报告。 |
| [`SRC-robotics-279`](../../raw/robotics-embodied-ai/documents/SRC-robotics-279-unidex-official-implementation.md) | [UniDex 官方实现](../../raw/robotics-embodied-ai/documents/SRC-robotics-279-unidex-official-implementation.md) | 数据准备、多手重定向、预训练和真机后训练代码与环境要求。 |
| [`SRC-robotics-280`](../../raw/robotics-embodied-ai/documents/SRC-robotics-280-egoscale-scaling-dexterous-manipulation-with-diverse-egocentric-human-data.md) | [EgoScale](../../raw/robotics-embodied-ai/documents/SRC-robotics-280-egoscale-scaling-dexterous-manipulation-with-diverse-egocentric-human-data.md) | 20,854 小时 Ego 视频、人类预训练 + 对齐中训练和 scaling 结论；指标为作者报告。 |
| [`SRC-robotics-281`](../../raw/robotics-embodied-ai/documents/SRC-robotics-281-spider-scalable-physics-informed-dexterous-retargeting.md) | [SPIDER 论文](../../raw/robotics-embodied-ai/documents/SRC-robotics-281-spider-scalable-physics-informed-dexterous-retargeting.md) | 将运动学人类动作转为动态可行机器人轨迹；性能和规模为作者报告。 |
| [`SRC-robotics-282`](../../raw/robotics-embodied-ai/documents/SRC-robotics-282-spider-official-implementation.md) | [SPIDER 官方实现](../../raw/robotics-embodied-ai/documents/SRC-robotics-282-spider-official-implementation.md) | 多本体、多数据集和多物理仿真器的人到机器人重定向工程底座。 |
| [`SRC-robotics-283`](../../raw/robotics-embodied-ai/documents/SRC-robotics-283-geometric-retargeting-a-principled-ultrafast-neural-hand-retargeting-algorithm.md) | [GeoRT](../../raw/robotics-embodied-ai/documents/SRC-robotics-283-geometric-retargeting-a-principled-ultrafast-neural-hand-retargeting-algorithm.md) | 无监督几何手部重定向；1 kHz 推理速度为作者报告。 |

## 2026-07-19 Physical Intelligence VLA 与经验闭环来源

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-308`](../../raw/robotics-embodied-ai/documents/SRC-robotics-308-0-5-a-vision-language-action-model-with-open-world-generalization.md) | [π0.5 arXiv HTML](../../raw/robotics-embodied-ai/documents/SRC-robotics-308-0-5-a-vision-language-action-model-with-open-world-generalization.md) | 用于核验异构机器人数据与多模态语义共训、未见住宅中的长程操作；实验结论不外推为商业部署。 |
| [`SRC-robotics-309`](../../raw/robotics-embodied-ai/documents/SRC-robotics-309-0-6-a-vla-that-learns-from-experience.md) | [π*0.6 / RECAP arXiv HTML](../../raw/robotics-embodied-ai/documents/SRC-robotics-309-0-6-a-vla-that-learns-from-experience.md) | 用于核验自主 rollout、人类遥操纠正、advantage conditioning 和论文内的吞吐/失败率效果边界。 |

## 2026-07-20 途见科技柔性电子皮肤视频一级校验来源

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-318`](../../raw/robotics-embodied-ai/documents/SRC-robotics-318-source.md) | [途见官网 raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-318-source.md) | 核验其自述的材料—器件—电路—算法定位与 EI-H/EI-B/EI-G 产品类别；不认作第三方性能/收入证明。 |
| `SRC-robotics-319` | 抽取失败（源站 TLS `BAD_ECPOINT`） | 深圳发改委托管报道：URL/正文已人工核验 2025 CES 共同展示与创始人供应链陈述；保留失败 manifest，不证明订单、收入或量产指标。 |
| [`SRC-robotics-320`](../../raw/robotics-embodied-ai/documents/SRC-robotics-320-2025.md) | [兆威年报 PDF sidecar](../../raw/robotics-embodied-ai/documents/SRC-robotics-320-2025.md) | 核验其仿生灵巧手研发/量产目标；PDF 已留存，文本转换失败待补；未点名途见，不能用于证明供应关系或投资。 |

## 2026-07-28 RoboVerse 平台、数据与真实数采增益来源

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-327`](../../raw/robotics-embodied-ai/documents/SRC-robotics-327-roboverse-towards-a-unified-platform-dataset-and-benchmark-for-scalable-and-gene.md) | [RoboVerse arXiv 元数据](../../raw/robotics-embodied-ai/documents/SRC-robotics-327-roboverse-towards-a-unified-platform-dataset-and-benchmark-for-scalable-and-gene.md) | 核验论文身份、总体定位与摘要；详细实验看 `SRC-robotics-336`。 |
| [`SRC-robotics-336`](../../raw/robotics-embodied-ai/documents/SRC-robotics-336-roboverse-rss-2025-paper-full-pdf.md) | [完整论文 Markdown](../../raw/robotics-embodied-ai/documents/SRC-robotics-336-roboverse-rss-2025-paper-full-pdf.md) / [PDF](../../raw/robotics-embodied-ai/documents/SRC-robotics-336-roboverse-rss-2025-paper-full-pdf.pdf) | 核验数据统计、DROID+RoboVerse 世界模型、Real2Sim、sim-to-real 与限制；均为作者实验。 |
| [`SRC-robotics-328`](../../raw/robotics-embodied-ai/documents/SRC-robotics-328-roboverse-repository-readme-at-audited-commit.md) | [固定提交 README](../../raw/robotics-embodied-ai/documents/SRC-robotics-328-roboverse-repository-readme-at-audited-commit.md) | 当前安装、后端/数据来源、Apache-2.0 根许可证和资产许可待补声明。 |
| [`SRC-robotics-329`](../../raw/robotics-embodied-ai/documents/SRC-robotics-329-roboverse-scope-and-architecture-documentation-at-audited-commit.md) | [范围与架构](../../raw/robotics-embodied-ai/documents/SRC-robotics-329-roboverse-scope-and-architecture-documentation-at-audited-commit.md) | 区分 RoboVerse 内容/学习层与 MetaSim simulator core。 |
| [`SRC-robotics-330`](../../raw/robotics-embodied-ai/documents/SRC-robotics-330-roboverse-multi-agent-trajectory-format-and-cross-simulator-replay-documentation.md) | [轨迹格式](../../raw/robotics-embodied-ai/documents/SRC-robotics-330-roboverse-multi-agent-trajectory-format-and-cross-simulator-replay-documentation.md) | robot-keyed PKL、双臂数据与 state replay 不等于 dynamics/task success 的边界。 |
| [`SRC-robotics-331`](../../raw/robotics-embodied-ai/documents/SRC-robotics-331-roboverse-smolvla-and-lerobot-data-pipeline-documentation.md) | [SmolVLA/LeRobot pipeline](../../raw/robotics-embodied-ai/documents/SRC-robotics-331-roboverse-smolvla-and-lerobot-data-pipeline-documentation.md) | 仿真 demo→LeRobot→训练→RoboVerse 评测工作流，不等于任意真机数据通用 importer。 |
| `SRC-robotics-332` | [GitHub API fallback HTML](../../raw/robotics-embodied-ai/documents/SRC-robotics-332-roboverse-github-repository-and-issue-audit.html) | 自动抽取失败后保留原始 API HTML；维护/issue 仅作工程信号。 |
| [`SRC-robotics-333`](../../raw/robotics-embodied-ai/documents/SRC-robotics-333-isaac-lab-official-framework-overview.md) | [Isaac Lab 官方概览](../../raw/robotics-embodied-ai/documents/SRC-robotics-333-isaac-lab-official-framework-overview.md) | 单一 NVIDIA/PhysX 生态对照。 |
| [`SRC-robotics-334`](../../raw/robotics-embodied-ai/documents/SRC-robotics-334-lerobotdataset-v3-official-specification.md) | [LeRobotDataset v3](../../raw/robotics-embodied-ai/documents/SRC-robotics-334-lerobotdataset-v3-official-specification.md) | 真机数据格式/共享层对照。 |
| [`SRC-robotics-335`](../../raw/robotics-embodied-ai/documents/SRC-robotics-335-maniskill-official-framework-documentation.md) | [ManiSkill 官方概览](../../raw/robotics-embodied-ai/documents/SRC-robotics-335-maniskill-official-framework-documentation.md) | manipulation GPU simulation 对照。 |

## 后续流程

## 2026-08-06 光轮智能公司、技术与商业化来源

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-377`](../../raw/robotics-embodied-ai/documents/SRC-robotics-377-lightwheel-official-company-and-product-overview.md)–[`SRC-robotics-378`](../../raw/robotics-embodied-ai/documents/SRC-robotics-378-lightwheel-platform-enterprise-workflow-and-capabilities.md) | 公司官网与企业平台 | 核验当前产品结构；不证明收入和独立性能。 |
| [`SRC-robotics-379`](../../raw/robotics-embodied-ai/documents/SRC-robotics-379-lightwheel-nvidia-customer-story-and-geely-factory-deployment.md)–[`SRC-robotics-380`](../../raw/robotics-embodied-ai/documents/SRC-robotics-380-geely-humanoid-real2sim2real-deployment-case.md) | NVIDIA/光轮吉利案例 | 核验 GR00T、Isaac 与工厂部署工作流；同一合作链不算完全独立双重验证。 |
| [`SRC-robotics-381`](../../raw/robotics-embodied-ai/documents/SRC-robotics-381-beijing-government-report-on-lightwheel-financing-orders-and-delivery-scale.md) | 政府平台报道 | 记录 5.5 亿元新增订单、150 万小时及复售率等公司口径；非审计财务。 |
| [`SRC-robotics-382`](../../raw/robotics-embodied-ai/documents/SRC-robotics-382-lw-benchhub-official-repository.md)–[`SRC-robotics-384`](../../raw/robotics-embodied-ai/documents/SRC-robotics-384-lightwheelocc-autonomous-driving-synthetic-dataset.md) | GitHub 与 Hugging Face | 可检查的代码、任务、资产与数据集；不等于企业版 SLA 或收入。 |
| [`SRC-robotics-385`](../../raw/robotics-embodied-ai/documents/SRC-robotics-385-lightwheel-early-angel-financing-and-initial-customer-status.md)–[`SRC-robotics-393`](../../raw/robotics-embodied-ai/documents/SRC-robotics-393-lightwheel-miracleplus-accelerator-company-profile.md) | 融资、团队、生态资料 | 形成融资和团队时间线；`SRC-robotics-390` 旧链接 404，已保留失败 manifest。 |

## 2026-08-06 光轮智能同类物理 AI 基础设施公司来源

| SRC | raw artifact / 状态 | 说明 |
|---|---|---|
| [`SRC-robotics-394`](../../raw/robotics-embodied-ai/documents/SRC-robotics-394-applied-intuition-end-to-end-physical-ai-platform.md)–[`SRC-robotics-397`](../../raw/robotics-embodied-ai/documents/SRC-robotics-397-scale-ai-physical-ai-data-engine.md) | Applied Intuition、Duality AI、Parallel Domain、Scale AI 官方页 | 核验海外平台、Real2Sim、数字孪生、数据与评测模块；财务和机器人业务拆分不公开。 |
| `SRC-robotics-398` | Rendered.ai 抓取失败 | Defuddle 与 fallback HTML 均返回 403；仅保留来源记录和公开搜索快照，待官方 PDF/文档补采。 |
| [`SRC-robotics-399`](../../raw/robotics-embodied-ai/documents/SRC-robotics-399-foretellix-data-driven-autonomy-verification-and-validation-toolchain.md)–[`SRC-robotics-400`](../../raw/robotics-embodied-ai/documents/SRC-robotics-400-discover-robotics-rsr-embodied-data-closed-loop-platform.md) | Foretellix 与求之科技 | 核验自动驾驶 V&V 和中国具身数据/仿真闭环产品；客户经济性待验证。 |
| [`SRC-robotics-401`](../../raw/robotics-embodied-ai/documents/SRC-robotics-401-gigaai-company-and-full-stack-physical-agi-platform.md)–[`SRC-robotics-402`](../../raw/robotics-embodied-ai/documents/SRC-robotics-402-gigaai-financing-and-industrial-deployment-report.md) | 极佳视界官网 fallback 与政府平台报道 | 核验全栈路线和公开融资/部署口径；公司披露不等于审计财务或独立 benchmark。 |
| [`SRC-robotics-403`](../../raw/robotics-embodied-ai/documents/SRC-robotics-403-51world-company-and-51sim-physical-ai-platform.md)–[`SRC-robotics-405`](../../raw/robotics-embodied-ai/documents/SRC-robotics-405-nexastar-real-world-interaction-data-infrastructure.md) | 51WORLD、IO-AI、NexaStar 官方页 | 区分仿真平台、真实数据平台和数据中心/交易模式；官网规模数字均需第三方及合同穿透。 |
| `SRC-robotics-406` | 具身智境抓取失败 | TLS 在安全握手前断开；保留官网来源记录，客户、产品和复购均待补证。 |

## 2026-07-23 LingBot-VLA 教程视频一级校验来源

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-321`](../../raw/robotics-embodied-ai/documents/SRC-robotics-321-lingbot-vla.md) | [LingBot-VLA 官方仓库](../../raw/robotics-embodied-ai/documents/SRC-robotics-321-lingbot-vla.md) | 核验开源权重/代码、Apache-2.0、LeRobot v3、数据映射、归一化、后训练与真机接口；README benchmark 不等于商业可靠性。 |
| [`SRC-robotics-322`](../../raw/robotics-embodied-ai/documents/SRC-robotics-322-a-pragmatic-vla-foundation-model.md) | [LingBot-VLA 技术报告](../../raw/robotics-embodied-ai/documents/SRC-robotics-322-a-pragmatic-vla-foundation-model.md) | 核验 20,000 小时、9 双臂本体、四平台/每任务 130 episode 的论文边界；不证明订单或可复制交付。 |

- 新增来源后先更新 [[sources.csv]]，再运行 `uv run python tools/extract_sources_with_defuddle.py --industry robotics-embodied-ai`。
- 对知识笔记中的关键判断，使用 `SRC-*` 编号引用，并在需要时链接到 raw extract。
- 对 failed/fallback 来源，优先寻找官方 PDF、GitHub raw、论文 arXiv、监管/公告页等更稳定来源替换。

## 2026-08-05 Jetson Thor 与边缘 AI 计算平台来源

| SRC | raw artifact / 状态 | 说明 |
|---|---|---|
| [`SRC-robotics-363`](../../raw/robotics-embodied-ai/documents/SRC-robotics-363-nvidia-jetson-thor-official-product-specifications.md) | [Thor 官方规格](../../raw/robotics-embodied-ai/documents/SRC-robotics-363-nvidia-jetson-thor-official-product-specifications.md) | T5000/T4000、128/64GB、功耗、I/O 与开发套件。 |
| [`SRC-robotics-364`](../../raw/robotics-embodied-ai/documents/SRC-robotics-364-nvidia-jetson-faq-current-pricing-and-lifecycle.md) | [Jetson 当前价格与生命周期](../../raw/robotics-embodied-ai/documents/SRC-robotics-364-nvidia-jetson-faq-current-pricing-and-lifecycle.md) | 2026-08-05 当前 MSRP、1KU+ 建议价和 dev kit/production module 边界。 |
| `SRC-robotics-366`–`371`、`373`、`375` | Defuddle 已捕获 | JetPack/benchmark、Qualcomm、AMD/MINISFORUM、Hailo 与 Journey 6 官方页面。 |
| `SRC-robotics-365`、`372` | 自动抽取超时 | NVIDIA Marketplace 动态价格由 2026-08-05 live page 核验；后续重试或保存浏览器快照。 |
| `SRC-robotics-374` | 旧页面 404；官方 PDF 已人工核验 | 8 INT8 TOPS、4GB ECC、24W 和接口来自 2025-03-04 官方 PDF；后续补 PDF raw artifact。 |
| [`SRC-robotics-376`](../../raw/robotics-embodied-ai/documents/SRC-robotics-376-jetson-agx-thor-china-channel-listing.md) | [中国渠道动态页](../../raw/robotics-embodied-ai/documents/SRC-robotics-376-jetson-agx-thor-china-channel-listing.md) | ¥40,999 含税报价仅作 B 级采购线索，需书面复核。 |

- 来源集：[[_sources/jetson-thor-edge-ai-compute-platform-source-set|Jetson Thor 与边缘 AI 计算平台来源集]]
- 数据表：[候选规格与价格 CSV](../../raw/robotics-embodied-ai/data/jetson-thor-alternatives-spec-price-2026-08-05.csv)
