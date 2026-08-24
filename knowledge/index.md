---
title: Knowledge Index
type: index
date_created: 2026-05-29
last_updated: 2026-08-24
tags:
  - wiki
  - index
  - llm-wiki
---

# Knowledge Index

本页是 LLM 维护本仓库知识库时优先读取的全局目录。`knowledge/README.md` 面向人类导航；本页面向 ingest/query/lint 工作流，所有重要页面都应在这里登记，并附一句话说明。

## Sources

- [[_sources/bilibili-bv1dxg36sen1-2026-8|人形机器人研究方法及心得 2026.8]] — 已综合为 [[_syntheses/bilibili-humanoid-investment-research-method-deep-dive-2026-08-14|人形机器人研究方法与投资验证深研]]；视频数字维持 B 级待验证。
- [[_sources/bilibili-bv1ucjj62eq4-ethercat|EtherCAT通讯原理讲解]] — 已综合为 [[_syntheses/bilibili-ethercat-robotics-control-network-deep-dive-2026-08-14|EtherCAT 机器人控制网络深研]]；协议机制经 ETG 资料核验。
- [[_sources/bilibili-bv1hnu26zebe-talk-144-vla-harness-vla|Harness VLA 记忆增强执行框架]] — 已综合为 [[_syntheses/bilibili-harness-vla-deep-dive-2026-08-14|Harness VLA 视频深研]]；真机商业化边界待 PoC。
- [[_sources/bilibili-bv1cu3b6vec4-bilibili-video|李飞飞空间智能访谈]] — 已综合为 [[_syntheses/bilibili-world-labs-spatial-intelligence-deep-dive-2026-08-14|World Labs 空间智能视频深研]]；R2S2R 为公司路线，待真机验证。
- [[_sources/bilibili-bv1di546yefr-bilibili-video|具身领域三大代表性数据集]] — 已综合为 [[_syntheses/bilibili-embodied-dataset-landscape-deep-dive-2026-08-14|具身数据集视频深研]]；RoboMIND 2.0 核心数据以论文为准。
- [[_sources/bilibili-bv1ftu96zeng-ros2|ROS2 运行在机器人的哪里？]] — 已综合为 [[_syntheses/bilibili-ros2-compute-layering-deep-dive-2026-08-13|ROS 2 实时控制边界深研]]。
- [[_sources/bilibili-bv1o5ud6ke7g-codex-ros2|具身探索-CodeX控制ROS2机器人]] — 已综合为 [[_syntheses/bilibili-codex-ros2-mcp-robot-control-deep-dive-2026-08-12|CodeX、ROS MCP 与 ROS 2 深研]]。
- [[_sources/bilibili-bv19kxhbme5f-bilibili-video|FlexiTac 开源触觉系统]] — 已综合为 [[_syntheses/bilibili-flexitac-open-tactile-system-deep-dive-2026-08-11|FlexiTac 触觉系统深研]]。
- [[_sources/bilibili-bv1cuuj6ce5b-icml-2025-sam2act|SAM2Act 记忆机器人操作]] — 已综合为 [[_syntheses/bilibili-sam2act-memory-robot-manipulation-deep-dive-2026-08-11|SAM2Act 深研]]。
- [[_sources/bilibili-bv14fmk6qecv-arxiv-2026-turbovla-1-gb-rtx-4090-32-hz|TurboVLA 实时 VLA]] — 已综合为 [[_syntheses/bilibili-turbovla-real-time-vla-deep-dive-2026-08-11|TurboVLA 深研]]。
- [[_sources/bilibili-bv1iynr68emq-bilibili-video|光模块工位机器人与人类数据路线]] — 已综合为 [[_syntheses/bilibili-optical-module-robotic-workcell-commercial-validation-deep-dive-2026-08-11|光模块工位机器人深研]]。
- [[_sources/bilibili-bv1r3yiz4e2s-b-2025-isaac-lab-nvidia-isaac-lab|Isaac Lab 教程]] — 已综合为 [[_syntheses/bilibili-isaac-lab-empty-scene-tutorial-deep-dive-2026-08-11|Isaac Lab 空场景教程深研]]。

- [[_sources/wechat-embodied-data-processing-roadmap|具身数据 RoadMap 微信文章来源卡]] — C 级从业者文章的问题地图；已把动作表征、时间对齐、质量门、标注、训练配比和部署回流编译为 [[robotics-embodied-ai/research-notes/embodied-ai-model-data-processing-pipeline-2026-08-11|具身智能模型数据处理闭环]]，毛利、单价、`50 ms` 与周期数字保持待验证。

- [[_sources/onshape-to-robot-official-source-set|onshape-to-robot 官方仓库、文档、示例与问题来源集]] — 固定提交核验 CAD→URDF/SDF/MuJoCo 工作流、装配命名约定、配置、processors、版本差异、示例和 open-issue 风险；综合于 [[robotics-embodied-ai/research-notes/onshape-to-robot-usage-selection-deep-dive-2026-08-10|onshape-to-robot 用法与选型调研]]。

- [[_sources/ethercat-technology-implementation-policy-source-set|EtherCAT 技术、实现、生态与政策来源集]] — ETG 官方技术/标准/许可/实现、IETF TCP/UDP 标准、SOEM/IgH、ODVA 竞品与工信部政策证据；综合于 [[robotics-embodied-ai/research-notes/ethercat-technology-ecosystem-engineering-deep-dive-2026-08-09|EtherCAT 深度调研]]和 [[robotics-embodied-ai/research-notes/ethercat-vs-tcp-ip-robot-control-latency-2026-08-12|EtherCAT vs TCP/IP 时延专题]]。

- [[_sources/dexcap-paper-project-code-source-set|DexCap 论文、官网与代码来源集]] — RSS 2024 论文、官方项目页与固定提交代码；综合于 [[robotics-embodied-ai/research-notes/dexcap-dexterous-mocap-data-collection-deep-dive-2026-08-09|DexCap 深度调研]]，并区分研究成功率、复现条件和商业真实性。

- [[_sources/unreal-engine-robotics-embodied-ai-source-set|Unreal Engine 机器人与具身智能来源集]] — Epic 许可与 Chaos、20 个公开项目或研究交付物、18 篇论文及 GitHub 维护快照；区分 UE 场景/传感器层、专用物理层、代码开放和商业许可。
- [[_sources/unity-robotics-embodied-ai-source-set|Unity 机器人与具身智能来源集]] — Unity 当前条款、机器人接入、学习/合成数据、室内具身环境和垂直模拟器的 39 项一级来源；区分项目代码、引擎、资产、数据和云服务许可。

- [[_sources/3d-simulation-asset-production-pipeline-source-set|3D 仿真资产生产技术管线来源集]] — OpenUSD/UsdPhysics/SimReady、Isaac/Datasmith、COLMAP/ReCap/Nerfstudio、Infinigen-Sim、Hunyuan3D/TRELLIS、MuJoCo/URDF/Houdini 官方来源；补充 SimReady 2026.04.1 Profile、validator、stamp 和 MUST/SHOULD 验收边界。

- [[_sources/lightwheel-peer-physical-ai-data-simulation-companies-source-set|光轮智能同类物理 AI 数据、仿真与评测公司来源集]] — 汇总 Applied Intuition、Duality AI、Parallel Domain、求之科技、极佳视界等 12 家候选的官方产品证据、抓取状态与商业证据限制。

- [[_sources/lightwheel-company-technology-commercial-source-set|光轮智能公司、技术与商业化来源集]] — 汇总公司产品、NVIDIA/吉利部署、开源代码与数据、订单交付口径及融资证据；明确订单不等于收入、合作案例不等于规模复购。

- [[_sources/jetson-thor-edge-ai-compute-platform-source-set|Jetson Thor 与边缘 AI 计算平台来源集]] — NVIDIA/Qualcomm/AMD/Hailo/Huawei/Horizon 官方规格、当前官方价格及动态库存证据；综合于 [[robotics-embodied-ai/research-notes/jetson-thor-and-alternatives-spec-price-comparison-2026-08-05|Jetson Thor 选型调研]]。

- [[_sources/bilibili-bv1z33l6ge9y-bilibili-video|开源机器人与机械臂成套方案选型调研]] — 已综合为 [[_syntheses/bilibili-open-robot-arm-platform-selection-deep-dive-2026-07-28|开源机器人与机械臂选型深研]]；视频价格/性能保持 B 级待验证。

- [[_sources/bilibili-bv1uwgf6veeh-2026-rlinf-ppo|2026智源大会丨清华于超主讲：具身智能为什么需要强化学习？面向具身智能的高灵活大规模强化学习框架RLinf！—具身智能机器人/PPO算法]] — 已综合为 [[_syntheses/bilibili-rlinf-embodied-reinforcement-learning-infrastructure-deep-dive-2026-07-28|RLinf 具身强化学习基础设施深研]]；仅将官方仓库/论文支持的机制视为事实。

- [[_sources/bilibili-bv1dkmt6hevk-dyna-york-yang|对话DYNA机器人联创York Yang]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; pending synthesis.

- [[_sources/bilibili-bv17dolbjebt-pi0-7-memoryvla-vla|PI0.7再次引用MemoryVLA，聊一聊 VLA 中的“记忆"]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; pending synthesis.

- [[_sources/bilibili-bv17oosb2e93-bilibili-video|人形机器人运控算法概览]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; pending synthesis.

- [[_sources/bilibili-bv1pnku6de3v-vincent-koc-openclaw-agent-b-x-waic-ai-101|对话Vincent Koc：OpenClaw的反思与进化，与Agent的下一步 | B站 x WAIC AI会客厅【101视频播客】]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; pending synthesis.

- [[_sources/bilibili-bv1q7ny6te8v-77k-star-ai|🔥77K Star！一句话生成模版！ai设计工具他来了]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; pending synthesis.

- [[_sources/bilibili-bv1ktky6rexa-superpowers-mattpocock-skills|模型越强， Superpowers 和 MattPocock-Skills 应该删除谁？]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; pending synthesis.

- [[_sources/bilibili-bv1crk86zepq-scale-up|蚂蚁灵波沈宇军具身原生模型访谈]] — B 级访谈 source packet；已用 LingBot-VLA 官方仓库与技术报告限定其技术主张。

- [[_sources/bilibili-bv1x45w6yeng-vla|【教程】具身智能实操，蚂蚁灵波VLA上手体验]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; pending synthesis.

- [[_sources/zsibot-matrix-robotics-simulator-source-set|zsibot/matrix（MATRiX）机器人仿真平台来源集]] — 固定提交 README、v0.1.2、GitHub API/issue/PR/tag、上游项目与政策证据；综合于 [[robotics-embodied-ai/research-notes/zsibot-matrix-robotics-simulator-deep-dive-2026-07-20|MATRiX 深度调研]]。

- [[_sources/roboverse-platform-dataset-benchmark-source-set|RoboVerse 平台、数据集与基准来源集]] — RSS 2025 论文、固定提交仓库/文档、数据格式、学习工作流、维护信号与官方竞品资料；综合于 [[robotics-embodied-ai/research-notes/roboverse-platform-and-real-data-deep-dive-2026-07-28|RoboVerse 深度调研]]。

- [[_sources/orb-slam3-paper-code-benchmark-source-set|ORB-SLAM3 论文、代码与 benchmark 来源集]] — T-RO/arXiv 论文、固定提交官方仓库/校准/依赖、2026-08-05 GitHub 快照、EuRoC/TUM-VI 与 VINS-Fusion/OpenVINS/RTAB-Map/cuVSLAM 官方对照；综合于 [[robotics-embodied-ai/research-notes/orb-slam3-technology-engineering-commercial-deep-dive-2026-08-05|ORB-SLAM3 深度调研]]。

- [[_sources/rtabmap-cuvslam-openvins-source-set|RTAB-Map、cuVSLAM、OpenVINS 论文、文档与代码来源集]] — 三套系统的一手论文、固定提交文档/许可证、2026-08-05 GitHub 审计与性能证据边界；综合于 [[robotics-embodied-ai/research-notes/rtabmap-cuvslam-openvins-comparative-deep-dive-2026-08-05|三方案深度调研]]。

- [[_sources/wechat-embodied-intelligence-robotics-core-technology-overview|一文速览具身智能机器人相关核心技术体系]] — 古月居 / 机器人小毛的 C 级入门综述；可作感知—决策—执行—反馈—学习概念地图，企业、政策、市场与产业主张均保留为待验证线索。

- [[_sources/bilibili-bv17wnv6gero-bilibili-video|途见科技：国家认证的“皮肤级”触觉方案]] — 已综合为 [[_syntheses/bilibili-tachin-flexible-electronic-skin-deep-dive-2026-07-20|途见科技柔性电子皮肤视频深度调研]]；产品定位有官方材料，融资、订单、量产和性能主张仍待验证。

- [[_sources/bilibili-bv1b2kc6heyx-pi-ai-7-18-13-survey-2026|PI 机器人 AI 创业公司 · 7 位创始人 · 18 个月 · 13 项产出【Survey 2026】]] — 已综合为 [[_syntheses/bilibili-physical-intelligence-vla-experience-loop-deep-dive-2026-07-19|PI VLA 与经验闭环深研]]；关键模型主张以一手论文校验。

- [[_sources/bilibili-bv13ykv6gek8-bilibili-video|做具身智能一定要几十万吗？我们带着答案拿了个冠军]] — 已综合为 [[_syntheses/bilibili-low-cost-embodied-robot-project-deep-dive-2026-07-19|低成本具身机器人项目深研]]；成本与开源交付物仍待验证。

- [[_sources/bilibili-bv1jhnc6ze8x-gpt-5-6-sol-blender-mcp|GPT 5.6 Sol 操控 Blender 有多强？社区案例、MCP 安装与真实实测]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; pending synthesis.

- [[_sources/bilibili-bv1hkkg69eed-jim-fan-robottt-8k|李飞飞、Jim Fan新作！RoboTTT把上下文拉到8K，机器人终于不再转头就忘]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; pending synthesis.

- [[_sources/bilibili-bv152ne6qeuf-18-ai-ai|18岁年薪百万，AI抢人大战开始了！AI天才的收入有多疯狂？]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; pending synthesis.

- [[_sources/bilibili-bv1wlja6gewq-ai-ai-ai|AI自己做科研了，那么人干嘛？#AI #AI科研 #英伟达 #人工智能 #科技改变生活]] — Bilibili source packet; synthesized after ENPIRE primary-source verification.

- [[_sources/bilibili-bv1qdjh64eeo-2026-docker-slam-diffusion-policy|公认2026具身智能天花板教程！一套吃透大模型机器人，Docker、SLAM、Diffusion Policy、扩散学习全覆盖]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; pending synthesis.

- [[_sources/bilibili-bv1sbtx6keh5-al-for-engineering|子虔科技Al For Engineering 具身智能机器人一体化设计平台]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; pending synthesis.

- [[_sources/bilibili-bv1c5nj6ve6y-icra-2026-ken-goldberg-agentic-coding-va-agentic-robot|【ICRA 2026 】伯克利机器人学教授 Ken Goldberg：Agentic Coding能弥合机器人鸿沟吗？新应用范式VA/Agentic Robot]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; pending synthesis.

- [[_sources/bilibili-bv1hdpnzte6d-cvpr-26|CVPR'26 | 浙江大学×宇树科技：首个具身智能终身学习的全生命周期闭环框架]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; pending synthesis.

- [[_sources/bilibili-bv17ud6bzeqc-kimodo|Kimodo，全新且免费的生成式动画工具，人人可用！]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; pending synthesis.

- [[_sources/bilibili-bv1y6m767e9x-2026-mujoco-python-ai|MuJoCo 具身智能建模教程]] — Bilibili source packet; installation instructions require official-document verification.
- [[_sources/bilibili-bv1ekmn6megs-ego|Ego 无机器人数据采集平台拆解]] — Bilibili source packet on synchronized sensor data for robot training.
- [[_sources/bilibili-bv15pmb68eb5-lingbot-depth-2-0|LingBot-Depth 2.0：反光与透明物体深度补全]] — Bilibili source packet; synthesized with the primary LingBot-Vision paper.
- [[_sources/bilibili-bv1utnj6ge75-200|自变量机器人：估值200亿，真智能还是真泡沫？]] — Bilibili source packet; company direction cross-checked against its official website.

- [[_sources/xiaohongshu-6a2667410000000006031e64-3|本周，最值得关注的3个基础设施资料项目]] — Xiaohongshu note source packet captured by the daily AI/embodied research pipeline; C-grade discovery evidence pending synthesis.

- [[_sources/xiaohongshu-6a44a669000000001101bdc2-xiaohongshu-note|未来不必生成视频，但要可评估、记忆和行动]] — Xiaohongshu note source packet captured by the daily AI/embodied research pipeline; C-grade discovery evidence pending synthesis.

- [[_sources/bilibili-bv1z7ja6le8s-200|成立两年半，估值200亿，千寻智能凭什么？]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; pending synthesis.

- [[_sources/bilibili-bv1q3te6ae4b-10-ai|博登智能：估值超10亿，AI卖铲人闷声发大财]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; synthesized in [[_syntheses/bilibili-boden-intelligence-data-infrastructure-deep-dive-2026-07-08|博登智能 Physical AI 数据基建视频深度调研]] and [[robotics-embodied-ai/research-notes/boden-intelligence-business-technology-overview-2026-07-08|博登智能商业逻辑、商业计划与技术方案综述]].

- [[_sources/bilibili-bv1mgja6cebk-200|成立两年半，估值200亿，千寻智能凭什么？]] — Bilibili 千寻智能 source packet; synthesized in [[_syntheses/bilibili-qianxun-intelligence-deep-dive-2026-07-08|千寻智能具身智能公司视频深度调研]].

- [[_sources/bilibili-bv1f7ts6weyj-abot-m0-5|高德杀进具身智能！ABot-M0.5：一个模型同时搞定导航+操作，还能自己"做梦"训练？]] — Bilibili ABot-M0.5 source packet; synthesized in [[_syntheses/bilibili-abot-m05-world-action-model-deep-dive-2026-07-07|ABot-M0.5 世界动作模型视频深度调研]].

- [[_sources/bilibili-bv1wftk6eez8-do-as-i-do|伯克利重磅Do As I Do！全网普通人视频，直接训练灵巧操作机器人]] — Bilibili Do As I Do source packet; synthesized in [[_syntheses/bilibili-do-as-i-do-dexterous-video-data-deep-dive-2026-07-07|Do As I Do 灵巧操作视频数据深度调研]].

- [[_sources/bilibili-bv1j9jd6ae7c-bilibili-video|具身感知升级逻辑：双目抓物体，多目构建完整空间世界模型]] — Bilibili multiview embodied perception source packet; synthesized in [[_syntheses/bilibili-multiview-embodied-perception-deep-dive-2026-07-07|多目具身感知视频深度调研]].

- [[_sources/bilibili-bv1g8kbbvezr-b-2025-isaac-sim-nvidia-isaac-sim|B站强推！2025公认最通俗易懂的【 Isaac Sim】教程，草履虫都能看懂！全套付费课程（附资料） NVIDIA_Isaac_Sim]] — Bilibili Isaac Sim tutorial source packet; synthesized in [[_syntheses/bilibili-isaac-sim-tutorial-deep-dive-2026-07-07|Isaac Sim 教程视频深度调研]].

- [[_sources/bilibili-bv17etk6vetx-ai|【播客】物理AI：新一轮生产力革命序章（第七期）]] — Bilibili Physical AI investment/research source packet; synthesized in [[_syntheses/bilibili-physical-ai-productivity-revolution-deep-dive-2026-07-07|Physical AI 生产力革命播客视频深度调研]].

- [[_sources/bilibili-bv1iftp62eav-2026-vla-rt-1-roboflamingo-mdt-rdt-lapa|【2026最新具身智能VLA入门教程】一口气讲透 RT-1、RoboFlamingo、MDT、RDT、LAPA 等核心算法]] — Bilibili VLA course source packet; synthesized in [[_syntheses/bilibili-vla-tutorial-deep-dive-2026-07-05|VLA 入门教程视频深度调研]].

- [[_sources/bilibili-bv1y3t46neuf-ai-ai|到底什么是物理AI，与数字AI核心区别是时间尺度不一样]] — Bilibili source packet on Physical AI time-scale differences; synthesized in [[_syntheses/bilibili-physical-ai-time-scale-deep-dive-2026-07-05|Physical AI 时间尺度视频深度调研]].

- [[_sources/bilibili-bv12xtm6segf-bilibili-video|机器触觉反馈，是不是就是一个伪命题？]] — Bilibili source packet on HapMorph wearable haptic feedback; synthesized in [[_syntheses/bilibili-hapmorph-haptic-feedback-deep-dive-2026-07-05|HapMorph 触觉反馈视频深度调研]].

- [[_sources/bilibili-bv1bktk69edd-agent-500-gui|【此话当真】Agent 元年第 500 天：什么在消失，什么在诞生，为什么我们不该再投资 GUI 思维的软件？]] — Bilibili source packet on Agent-era GUI/headless software, CLI/MCP/skills and agentic economy; synthesized in [[_syntheses/bilibili-agent-gui-headless-software-deep-dive-2026-07-04|Agent 时代 GUI 与 Headless 软件视频深度调研]].

- [[_sources/bilibili-bv1pcja6bei4-bilibili-video|还写什么单片机代码啊？直接微信聊天就行！]] — Bilibili source packet on ESP Cloud / ESP32 natural-language scripting; summarized in [[_syntheses/bilibili-ai-embodied-signals-2026-07-03|Bilibili AI 与具身智能线索 2026-07-03]].

- [[_sources/bilibili-bv1v17y6ae2l-science-robotics|浙大高飞发起 | 登顶《Science Robotics》封面背后的数学问题！]] — Bilibili source packet on numerical optimization as robotics career skill; summarized in [[_syntheses/bilibili-ai-embodied-signals-2026-07-03|Bilibili AI 与具身智能线索 2026-07-03]].

- [[_sources/bilibili-bv1ur7h6dey5-2026-slam-ai-slam-ai|【2026最新机器人视觉SLAM】保姆级全套课程！AI大佬带你十节课从零到一快速掌握SLAM理论直接速通具身智能机器人必备入门知识点！AI/机器人/具身智能]] — Bilibili source packet on SLAM/ROS/传感器融合基础栈; summarized in [[_syntheses/bilibili-ai-embodied-signals-2026-07-03|Bilibili AI 与具身智能线索 2026-07-03]].

- [[_sources/bilibili-bv1cl7p6veh9-b-vla-vla-rt-1-openvla-unipi|绝对是B站最好的具身智能VLA入门教程，对新手超级友好！仿真、隐式端到端VLA、RT-1、OpenVLA、UniPi—机械臂、具身智能机器人]] — Bilibili source packet on VLA model/data/evaluation/deployment basics; summarized in [[_syntheses/bilibili-ai-embodied-signals-2026-07-03|Bilibili AI 与具身智能线索 2026-07-03]].

- [[_sources/bilibili-bv1wctu6nef2-genie-sim-3-0-vla|深度探索-基于智元GENIE SIM 3.0的VLA闭环仿真（上）]] — Bilibili source packet on GENIE SIM 3.0 VLA closed-loop simulation; summarized in [[_syntheses/bilibili-ai-embodied-signals-2026-07-03|Bilibili AI 与具身智能线索 2026-07-03]].

- [[_sources/bilibili-bv1optq6senp-bilibili-video|人形机器人究竟怎么进家庭？这是我听过最好的答案]] — Bilibili source packet on home humanoid robot product definition; summarized in [[_syntheses/bilibili-ai-embodied-signals-2026-07-03|Bilibili AI 与具身智能线索 2026-07-03]].

- [[_sources/bilibili-bv12ptq6qecg-physisforcing|机械臂一碰就穿模？北大英伟达 PhysisForcing 纠正视频生成物理盲区]] — Bilibili source packet on PhysisForcing / physical-consistency video world models; summarized in [[_syntheses/bilibili-ai-embodied-signals-2026-07-03|Bilibili AI 与具身智能线索 2026-07-03]].

- [[_sources/bilibili-bv1bbtv6ueaf-5-skill-codex-matlab|安了这5个skill，让Codex自动控制matlab]] — Bilibili video source packet captured by the daily AI/embodied research pipeline; synthesized in [[_syntheses/matlab-simulink-agentic-ai-tools-bilibili-2026-07-02|MATLAB/Simulink Agentic AI 工具链视频调研]].
- [[_sources/bilibili-bv1ortv62e2j-26-vla-zr-0|智谱入局具身智能，26亿参数VLA模型ZR-0]] — Bilibili source packet for a ZR-0/VLA cross-embodiment transfer explainer; summarized as B-grade leads in [[_syntheses/bilibili-embodied-ai-signals-2026-07-02|Bilibili 具身智能与 AI 工具链线索 2026-07-02]].
- [[_sources/bilibili-bv1zftq6pea3-vla|VLA&世界模型数据基建]] — Bilibili source packet describing an observation/action/language/QC-to-episode data pipeline; summarized in [[_syntheses/bilibili-embodied-ai-signals-2026-07-02|Bilibili 具身智能与 AI 工具链线索 2026-07-02]].
- [[_sources/bilibili-bv1ywtg6te1k-genie-sim-3-0-vla|GENIE SIM 3.0 VLA 闭环仿真试用]] — Bilibili source packet on real-video-to-Isaac-Sim asset generation limits; summarized in [[_syntheses/bilibili-embodied-ai-signals-2026-07-02|Bilibili 具身智能与 AI 工具链线索 2026-07-02]].
- [[_sources/bilibili-bv19pt36resn-leworldmodel-github-4k-star-jepa-1gb|LeWorldModel / JEPA 世界动作模型讲解]] — Bilibili source packet for latent world-model learning and robot control education; summarized in [[_syntheses/bilibili-embodied-ai-signals-2026-07-02|Bilibili 具身智能与 AI 工具链线索 2026-07-02]].
- [[_sources/bilibili-bv1ck7n66epd-forceband|ForceBand 力数据采集]] — Bilibili source packet on sEMG/IMU-assisted force labels for robot demonstrations; summarized in [[_syntheses/bilibili-embodied-ai-signals-2026-07-02|Bilibili 具身智能与 AI 工具链线索 2026-07-02]].

- [[_sources/karpathy-llm-wiki-pattern|Karpathy LLM Wiki Pattern]] — LLM Wiki 的原始理念和 Jason 文章中的实践化解读。
- [[ai/00-source-capture-index|AI Source Capture Index]] — AI 行业来源抽取状态，包含 Scale AI 与中国 AI 数据基础设施对标调研的 raw artifact 入口。
- [[news/2026-05-29-us-productivity-miracle|美国正在爆发一场生产力奇迹]] — 关于美国生产率加速、AI 时滞、能源优势和经济灵活性的新闻摘要。
- [[_sources/roboalign-r1-reward-aligned-robot-video-world-models|RoboAlign-R1 - Reward-Aligned Robot Video World Models]] — arXiv `2605.03821` 论文卡片，聚焦机器人视频世界模型的多模态奖励对齐、RobotWorldBench、RoboAlign-Judge 和 SWR。
- [[_sources/airspeed-open-source-data-production-platform|AIRSPEED - Open-source Data Production Platform for Embodied AI]] — AIRSPEED 来源组，覆盖官网、技术报告、EAI 数据工程综述、技术转移报告和 GitHub README。

## Entities

- [[_entities/DexCap|DexCap]] — RSS 2024 便携式灵巧手动作采集系统与 DexIL 学习链路；强项是自然人类动作吞吐，商业化仍受力觉、跨本体、原 BOM 生命周期和真机增益验证约束。

- [[_entities/LightwheelAI|光轮智能]] — 中国物理 AI 数据、仿真与评测基础设施公司；已形成 SimReady、EgoSuite、RoboFinals 与 Real2Sim2Real 产品链，财务质量仍待验证。

- [[_entities/RoboVerse|RoboVerse]] — MetaSim 之上的任务、资产、数据集、benchmark 与学习工作流层；可用于多后端仿真、IL/VLA/RL、Real2Sim 和 sim-to-real 研究，但不是基础模型或企业真机数据湖。
- [[_entities/MATRiXSimulator|MATRiX Simulator]] — GENISOM.AI / zsibot 面向四足机器人开发的 MuJoCo + Unreal Engine 仿真工具；当前开源仓库主要是脚本、配置、教程和二进制分发入口，适合经 PoC 后用于导航/感知联调与演示，不宜直接视为成熟训练基础设施。
- [[_entities/SRTSoftRobotTech|SRT 软体机器人]] — 中国气动柔性末端执行器与行业自动化公司；已完成软体夹爪产品化和医疗康复延伸，当前重点跟踪财务透明度与 2026 年创始团队迁移。
- [[_entities/AndrejKarpathy|Andrej Karpathy]] — LLM Wiki 理念提出者，强调把知识管理从 RAG 转向持续编译。
- [[_entities/ScaleAI|Scale AI]] — 美国 AI 数据基础设施公司，从自动驾驶标注扩展到大模型后训练、评测和政府 AI，并于 2025 年获得 Meta 战略投资。
- [[_entities/HuggingFaceLeRobot|Hugging Face LeRobot]] — 机器人学习数据、加载、训练与评测工具链，也是 UMI 数据包可复现交付的重要格式入口。
- [[_entities/README|Entities Layer]] — 人物、公司、工具、产品和 UMI 技术术语实体索引。
- [[_entities/UniversalManipulationInterface|Universal Manipulation Interface]] — 低成本手持夹爪示教路线，把人类操作转成机器人可训练轨迹数据。
- [[_entities/SLAM|SLAM]] — UMI-like 数据采集中的位姿恢复与轨迹质量核心模块。
- [[_entities/ORBSLAM3|ORB-SLAM3]] — 稀疏特征视觉/视觉惯性、多地图 SLAM 经典库；适合作研究基线、轨迹恢复和限定 PoC，但官方上游为 ROS1-era、GPLv3，且不是稠密语义导航产品。
- [[_entities/RTABMap|RTAB-Map]] — 可接视觉/LiDAR/外部里程计的长期 graph-SLAM、数据库与 ROS 2 地图集成；适合 AMR/Nav2 和 2D/3D occupancy，需管理参数、退化与大图资源。
- [[_entities/cuVSLAM|cuVSLAM]] — NVIDIA CUDA 多模式、多相机 VO/VIO/VSLAM SDK；适合 Jetson/Isaac ROS，商业许可限定 NVIDIA Platforms。
- [[_entities/OpenVINS|OpenVINS]] — MSCKF/EKF visual-inertial estimation 研究平台；强于标定、仿真和可解释状态估计，不是默认长期地图/导航栈，许可证 GPL-3.0。
- [[_entities/DiffusionPolicy|Diffusion Policy]] — UMI 常用的机器人模仿学习策略模型基线。
- [[_entities/ActionChunkingTransformer|ACT]] — 用 Transformer 一次预测动作 chunk 的模仿学习基线。
- [[_entities/DataPackage|Data Package]] — ToB 机器人数据服务的交付资产包概念。
- [[_entities/QualityControl|Quality Control]] — 机器人训练数据从原始采集走向可训练交付的质检流程。
- [[_entities/LiDAR|LiDAR 激光雷达]] — 机器人与自动驾驶空间感知传感器，在 UMI 数据闭环和世界模型训练中对应点云/range/ray token、BEV/occupancy、跨模态对齐和几何评测。
- [[_entities/UnitreeRobotics|Unitree Robotics]] — 中国具身智能/机器人公司，现有研究中用于跟踪整机与数据平台线索。
- [[_entities/LimXDynamics|LimX Dynamics]] — 逐际动力，中国人形机器人与具身智能公司，当前研究重点是“机器人本体 + 运动控制小脑 + 具身大脑/工具链”的开发者平台路线。
- [[_entities/Agibot|Agibot]] — 中国具身智能公司，现有研究中用于跟踪开放数据集和整机生态。
- [[_entities/IOAI|IO-AI]] — 中国具身数据基础设施公司，现有研究中用于跟踪遥操作、数据标注管理与格式导出。
- [[_entities/AIRSPEED|AIRSPEED]] — AIRS/AIRSPEED 具身智能数据生产平台项目，当前开源核心偏 ROS2/YAML/HDF5 数据采集，论文/报告目标覆盖采集、仿真生成和数据集构建。
- [[_entities/MonteCarloTreeSearch|Monte Carlo Tree Search（MCTS）]] — 以选择、扩展、模拟和回传循环搜索大规模决策树，并通过 UCT 平衡已知高分分支与低访问分支。

## Concepts

- [[_concepts/llm-wiki|LLM Wiki]] — 以 Markdown wiki 作为 LLM 可维护的持久知识编译层。
- [[_concepts/knowledge-compilation|Knowledge Compilation]] — 把原始来源在摄入阶段编译为可复用、可链接、可审计的知识资产。
- [[_concepts/source-traceability|Source Traceability]] — 本仓库的核心质量约束：重要判断必须能回到原始来源。
- [[_concepts/embodied-ai|Embodied AI]] — AI 进入物理世界的机器人产业化方向。
- [[_concepts/robot-training-data|Robot Training Data]] — 具身智能训练数据、采集前契约、raw/canonical/model-view 分层、episode、schema、质检、真实 holdout 与部署回流体系。
- [[_concepts/vision-language-tactile-action|Vision-Language-Tactile-Action]] — 视觉、语言、触觉/力觉和动作轨迹融合的具身模型/数据范式。
- [[_concepts/universal-manipulation-interface|Universal Manipulation Interface]] — UMI-like 采集设备和机器人示教数据包路线。
- [[_concepts/lerobot-dataset-schema|LeRobot Dataset Schema]] — LeRobot v3 及相关机器人数据格式概念。
- [[_concepts/joint-embedding-predictive-architecture|Joint-Embedding Predictive Architecture]] — Yann LeCun 提出的非生成式自监督世界模型路线，在 latent space 预测目标表示而非重建像素/token。

## Claims

- [[_claims/README|Claims Index]] — 原子化、可溯源判断的登记区；当前先建规则，后续在研究深化时逐条抽取。

## Syntheses

- [[_syntheses/bilibili-ai-daily-run-2026-08-24|Bilibili AI Daily Run 2026-08-24]] — 20 个候选、18 个重复；其余两条经模型复核均无关，未进行下载、ASR 或深研。
- [[_syntheses/bilibili-ai-daily-run-2026-08-23|Bilibili AI Daily Run 2026-08-23]] — 20 个候选、18 个重复；其余两条经模型复核均无关，未进行下载、ASR 或深研。
- [[_syntheses/bilibili-ai-daily-run-2026-08-22|Bilibili AI Daily Run 2026-08-22]] — 20 个候选、18 个重复；其余两条经模型复核均无关，未进行下载、ASR 或深研。
- [[_syntheses/bilibili-ai-daily-run-2026-08-21|Bilibili AI Daily Run 2026-08-21]] — 20 个候选、18 个重复；其余两条经模型复核均无关，未进行下载、ASR 或深研。
- [[_syntheses/bilibili-ai-daily-run-2026-08-20|Bilibili AI Daily Run 2026-08-20]] — 20 个候选、18 个重复；其余两条经模型复核均无关，未进行下载、ASR 或深研。
- [[_syntheses/bilibili-ai-daily-run-2026-08-19|Bilibili AI Daily Run 2026-08-19]] — 20 个候选、18 个重复；其余两条经模型复核均无关，未进行下载、ASR 或深研。
- [[_syntheses/bilibili-ai-daily-run-2026-08-18|Bilibili AI Daily Run 2026-08-18]] — 20 个候选、18 个重复；其余两条经模型复核均无关，未进行下载、ASR 或深研。
- [[_syntheses/bilibili-ai-daily-run-2026-08-17|Bilibili AI Daily Run 2026-08-17]] — 20 个候选、18 个重复；其余两条经模型复核均无关，未进行下载、ASR 或深研。
- [[_syntheses/bilibili-ai-daily-run-2026-08-16|Bilibili AI Daily Run 2026-08-16]] — 20 个候选、18 个重复；其余两条经模型复核均无关，未进行下载、ASR 或深研。
- [[_syntheses/bilibili-ai-daily-run-2026-08-15|Bilibili AI Daily Run 2026-08-15]] — 20 个候选、18 个重复；其余两条经模型复核均无关，未进行下载、ASR 或深研。
- [[_syntheses/bilibili-ai-daily-run-2026-08-14|Bilibili AI Daily Run 2026-08-14]] — 收藏夹候选拉取失败：OpenCLI Browser Bridge 未连接；未处理本日视频。
- [[_syntheses/bilibili-humanoid-investment-research-method-deep-dive-2026-08-14|人形机器人研究方法与投资验证视频深研]] — R09/R07：以订单、回款、连续运行和单位经济性替代展示与出货叙事。
- [[_syntheses/bilibili-ethercat-robotics-control-network-deep-dive-2026-08-14|EtherCAT 机器人控制网络视频深研]] — R05/R02：按周期、互操作、安全和 TCO 选型。
- [[_syntheses/bilibili-harness-vla-deep-dive-2026-08-14|Harness VLA 记忆增强执行框架视频深研]] — R04/R05：planner 编排不等于可绕过低层安全闭环。
- [[_syntheses/bilibili-world-labs-spatial-intelligence-deep-dive-2026-08-14|World Labs 空间智能与机器人训练场视频深研]] — R04/R07：R2S2R 需要真机 holdout 证实价值。
- [[_syntheses/bilibili-embodied-dataset-landscape-deep-dive-2026-08-14|具身三类代表性数据集视频深研]] — R06/R04：按可用 episode、质量与真实增益选择数据资产。
- [[_syntheses/bilibili-ai-daily-run-2026-08-13|Bilibili AI Daily Run 2026-08-13]] — 20 个候选、12 个重复；六条已处理并完成单视频深研。
- [[_syntheses/bilibili-ros2-compute-layering-deep-dive-2026-08-13|ROS 2 机器人计算分层与实时控制边界深研]] — R05/R04：高层 ROS 2 与独立安全控制链需分别验收。
- [[_syntheses/bilibili-ai-daily-run-2026-08-12|Bilibili AI Daily Run 2026-08-12]] — CodeX—ROS 2 视频成功处理并完成 R05/R07 深研。
- [[_syntheses/bilibili-codex-ros2-mcp-robot-control-deep-dive-2026-08-12|CodeX、ROS MCP Server 与 ROS 2 机器人控制视频深研]] — R05/R07：MCP 应受策略约束且安全闭环独立留在车端。
- [[_syntheses/bilibili-ai-daily-run-2026-08-11|Bilibili AI Daily Run 2026-08-11]] — 五条成功转录并完成独立深研。
- [[_syntheses/bilibili-flexitac-open-tactile-system-deep-dive-2026-08-11|FlexiTac 触觉系统深研]] — R02/R04：以接触任务损伤、接管和 TCO 验收触觉价值。
- [[_syntheses/bilibili-sam2act-memory-robot-manipulation-deep-dive-2026-08-11|SAM2Act 深研]] — R04/R07：记忆模块需在反马尔可夫任务做真机 AB。
- [[_syntheses/bilibili-turbovla-real-time-vla-deep-dive-2026-08-11|TurboVLA 深研]] — R04/R05：模型推理延迟不等于端到端闭环延迟。
- [[_syntheses/bilibili-optical-module-robotic-workcell-commercial-validation-deep-dive-2026-08-11|光模块工位机器人与人类数据路线深研]] — R07/R04/R02：以工位 ROI、连续运行与订单核验。
- [[_syntheses/bilibili-isaac-lab-empty-scene-tutorial-deep-dive-2026-08-11|Isaac Lab 空场景教程深研]] — R05/R04：空场景 smoke test 不等于 sim-to-real 成功。

- [[robotics-embodied-ai/research-notes/ethercat-vs-tcp-ip-robot-control-latency-2026-08-12|EtherCAT 为什么在机器人实时控制中通常比 TCP/IP 更快]] — R04 主分类、R05 次分类：EtherCAT 的实时优势来自单帧多节点、ESC on-the-fly、固定周期、DC 和 WKC，而不是峰值带宽；TCP 的可靠有序语义适合通用数据，丢包时却会增加控制尾时延。

- [[robotics-embodied-ai/research-notes/embodied-ai-model-data-processing-pipeline-2026-08-11|具身智能模型数据处理闭环]] — R02 主分类、R05 次分类：将数据处理定义为从采集前契约到部署问题回流的十层闭环，给出同步/标定、自动质量门、分层标注、action/schema 编译、无泄漏切分、训练时增强、真实 holdout、交付物与创业边界。

- [[robotics-embodied-ai/research-notes/onshape-to-robot-usage-selection-deep-dive-2026-08-10|onshape-to-robot 用法、工程边界与选型调研]] — R05 主分类、R04 次分类：适合 Onshape-first 团队把版本化装配编译成 URDF/SDF/MuJoCo，但必须补齐模型 CI、ROS 2/MoveIt/控制、碰撞、动力学与真实 API PoC；报告含最小配置、故障定位、安全边界和创业机会。

- [[robotics-embodied-ai/research-notes/ethercat-technology-ecosystem-engineering-deep-dive-2026-08-09|EtherCAT 技术原理、产业生态与机器人工程选型深度调研]] — R04 主分类、R05/R07 次分类：EtherCAT 适合作为机器人确定性内环，但总线实时不等于整机硬实时；选型需联合验证 OS、主站、NIC、驱动器、安全和故障恢复。

- [[robotics-embodied-ai/research-notes/unreal-engine-in-robotics-and-embodied-ai-2026-08-06|Unreal Engine 在机器人与具身智能中的应用、开源项目和论文调研]] — R04 主分类、R05/R06 次分类：UE 最适合作为高真实感世界、观测、人机交互和数字孪生层；接触操作与控制优先采用 UE + MuJoCo/专用物理 + ROS 2，并以真机 holdout 验收。
- [[robotics-embodied-ai/research-notes/unity-in-robotics-and-embodied-ai-2026-08-06|Unity 在机器人与具身智能中的应用、开源项目和论文调研]] — R04 主分类、R05/R06 次分类：Unity 强项是可编程交互世界、ML-Agents、AI2-THOR 家庭具身任务、VR 示教和 ROS/垂直模拟器；项目开源不代表 Unity/资产可商用。

- [[robotics-embodied-ai/research-notes/3d-simulation-asset-production-pipelines-comparison-2026-08-06|3D 仿真资产生产技术管线综合调研]] — R05 主分类、R04/R02 次分类：比较九条资产生产路线，推荐“多源输入 + OpenUSD 规范化 + 物理/语义编译 + 多仿真器 adapter + 任务证据”的混合资产工厂；补充 Profile 版本冻结、零失败规范门、L1/L2/L3 三级验收与机器可读清单。

- [[robotics-embodied-ai/research-notes/lightwheel-peer-companies-business-model-comparison-2026-08-06|光轮智能同类创业公司与商业模式对比调研]] — R06 主分类、R03/R07 次分类：Applied Intuition 是最接近的平台商业对标，Parallel Domain 最接近 Real2Sim 资产飞轮，求之科技是中国产品覆盖最相似候选，但商业质量均需合同、回款与复购穿透。

- [[robotics-embodied-ai/research-notes/lightwheel-company-and-commercial-model-deep-dive-2026-08-06|光轮智能公司与商业模式深度调研]] — R03 主分类、R07 次分类：判断其已越过概念与单一 Demo，但 5.5 亿元新增订单、150 万小时交付和复售率仍需用合同、收入、回款、毛利及复购穿透验证。

- [[robotics-embodied-ai/research-notes/jetson-thor-and-alternatives-spec-price-comparison-2026-08-05|Jetson Thor 与同类替代平台规格、价格及选型调研]] — R05/R06：当前 Thor 开发套件已为 US$5,499；以真实模型 p95、内存、功耗、I/O、迁移与量产 TCO 比较 T5000/T4000、Orin、IQ-9075、DGX Spark、AMD 128GB 和降档 NPU。

- [[robotics-embodied-ai/research-notes/orb-slam3-technology-engineering-commercial-deep-dive-2026-08-05|ORB-SLAM3 技术原理、工程选型与商业落地深度调研]] — R04 主分类、R05/R07 次分类：判断其仍是经典而强的多地图 V/VI-SLAM 基线，但 2026 年商业选型必须先过目标场景失败率、ROS 2 维护、GPL 许可与下游 ROI 四道门。
- [[robotics-embodied-ai/research-notes/rtabmap-cuvslam-openvins-comparative-deep-dive-2026-08-05|RTAB-Map、cuVSLAM、OpenVINS 技术与工程选型深度调研]] — R05 主分类、R04/R07 次分类：区分长期导航 SLAM、NVIDIA 多相机 VSLAM SDK 与 MSCKF VIO 研究平台，给出统一选型、许可边界和任务级 PoC。

- [[_syntheses/bilibili-ai-daily-run-2026-07-28|Bilibili AI Daily Run 2026-07-28]] — 20 个候选、17 个重复；模型选中并成功转录 RLinf 和开源机械臂选型两条视频。
- [[_syntheses/bilibili-rlinf-embodied-reinforcement-learning-infrastructure-deep-dive-2026-07-28|RLinf 具身强化学习基础设施视频深度调研]] — R04 主分类、R07 次分类：应以任务级安全/成本/收益的 A/B 验收来判断 RL 后训练基础设施，而非采用视频 benchmark 或采用方叙事。
- [[_syntheses/bilibili-open-robot-arm-platform-selection-deep-dive-2026-07-28|开源机器人与机械臂成套方案选型视频深度调研]] — R05 主分类、R07 次分类：平台选型先审 BOM、控制、数据、部署、许可证与安全闭环，再做单臂 PoC，不能按视频价格/展示排名。

- [[_syntheses/bilibili-ai-daily-run-2026-07-26|Bilibili AI Daily Run 2026-07-26]] — 20 个候选、18 个重复；选中 DYNA 机器人访谈但字幕与有界 ASR 诊断均未成功，未创建 source packet 或深研。

- [[_syntheses/bilibili-ai-daily-run-2026-07-25|Bilibili AI Daily Run 2026-07-25]] — 20 个候选、19 个重复；唯一模型复核项为无关个人感悟内容，未选中、未转录或深研。

- [[_syntheses/bilibili-humanoid-motion-control-algorithms-deep-dive-2026-07-24|人形机器人运控算法概览视频深度调研]] — R04 主分类、R07 次分类：运控应按安全伺服、模型控制、学习策略和高层任务模型分层验收；仿真动作与展示不能外推为真机商业可靠性。

- [[_syntheses/bilibili-memoryvla-temporal-memory-deep-dive-2026-07-24|MemoryVLA 时序记忆视频深度调研]] — R04 主分类、R07 次分类：MemoryVLA 可缓解历史不可见操作混淆，但论文结果不等于跨客户或跨 episode 的产品化记忆。

- [[_syntheses/bilibili-ai-daily-run-2026-07-24|Bilibili AI Daily Run 2026-07-24]] — 20 个候选、17 个重复；模型选择两条具身智能视频并均成功转录、完成单视频深研。

- [[_syntheses/bilibili-robbyant-native-embodied-model-strategy-deep-dive-2026-07-23|蚂蚁灵波具身原生模型战略访谈深度调研]] — R03 主分类、R04/R07 次分类：开源技术资产可核验，组织、数据联盟、商业化与竞争叙事仍待一手证据。

- [[_syntheses/bilibili-lingbot-vla-hands-on-deep-dive-2026-07-23|LingBot-VLA 上手教程视频深度调研]] — R05 主分类、R04/R07 次分类：开源 VLA 的价值在可审计的后训练与部署工具链；模型分数不能替代目标工位的闭环成功率、人工干预与单位任务成本。

- [[_syntheses/bilibili-ai-daily-run-2026-07-23|Bilibili AI Daily Run 2026-07-23]] — 20 个候选、13 个重复；模型判断 6 条相关，成功转写 1 条并完成单视频深研，余 5 条因 Volcengine 音频时长配额耗尽未启动。

- [[_syntheses/bilibili-ai-daily-run-2026-07-22|Bilibili AI Daily Run 2026-07-22]] — 20 个候选、15 个重复；模型选中 4 个 AI/具身智能相关视频，但首个外部 ASR 调用上传音频后无输出，未产生可综合的 source packet。
- [[robotics-embodied-ai/research-notes/roboverse-platform-and-real-data-deep-dive-2026-07-28|RoboVerse 能力边界与具身数采数据增益深度调研]] — R05 主分类、R04/R07 次分类：区分 RoboVerse 与 MetaSim/基础模型/真机数据平台，给出六类真实数据增益路径、L0–L4 接入等级、四组 A/B 和商业/创业边界。
- [[robotics-embodied-ai/research-notes/zsibot-matrix-robotics-simulator-deep-dive-2026-07-20|zsibot/matrix（MATRiX）机器人仿真平台深度调研]] — R05 主分类、R04/R07 次分类：审计架构、发行包、代码开放边界、维护活跃度、文档漂移、许可与商业落地；结论是“值得做限定 PoC，不宜未经验证替换通用仿真底座”。
- [[_syntheses/bilibili-ai-daily-run-2026-07-20|Bilibili AI Daily Run 2026-07-20]] — 20 个候选、19 个重复；唯一模型选中的柔性电子皮肤视频已完成转录与 R03/R07 单视频深研。
- [[_syntheses/bilibili-tachin-flexible-electronic-skin-deep-dive-2026-07-20|途见科技柔性电子皮肤视频深度调研]] — R03 主分类、R07 次分类：区分可确认的产品方向/共同展示与未验证的融资、供应、性能、订单和规模化叙事。
- [[_syntheses/bilibili-ai-daily-run-2026-07-19|Bilibili AI Daily Run 2026-07-19]] — 20 个候选、18 个重复；模型选择并成功转录低成本具身机器人项目与 Physical Intelligence 调研两条视频，均完成单视频深研。
- [[_syntheses/bilibili-low-cost-embodied-robot-project-deep-dive-2026-07-19|低成本具身智能机器人项目视频深度调研]] — R05 主分类、R07 次分类：把“低成本”拆回可复现实验闭环、工程总拥有成本与待开源验证项。
- [[_syntheses/bilibili-physical-intelligence-vla-experience-loop-deep-dive-2026-07-19|Physical Intelligence VLA 与经验闭环视频深度调研]] — R04 主分类、R07 次分类：一手论文支持 π0、π0.5 与 RECAP 的研究结论，但不支持把视频中的全部版本、公司与商业化叙事当成事实。
- [[_syntheses/bilibili-ai-daily-run-2026-07-18|Bilibili AI Daily Run 2026-07-18]] — 20 个候选，18 个重复；模型选中并成功转录 RoboTTT 机器人长上下文与 Codex/Blender MCP 两条视频，均已完成单视频深研。
- [[_syntheses/bilibili-robottt-long-context-robot-policy-deep-dive-2026-07-18|RoboTTT 长上下文机器人策略视频深度调研]] — R04 主分类：一手预印本支持 8K 时间步、fast weights 与论文内任务增益，但尚不等同于现场商业可靠性。
- [[_syntheses/bilibili-codex-blender-mcp-toolchain-deep-dive-2026-07-18|Codex 与 Blender MCP 工具链视频深度调研]] — R05 主分类：确认 BlenderMCP 的工具架构，保留视频 ASR 中模型品牌、质量、耗时与成本主张为待验证。
- [[_syntheses/bilibili-ai-talent-market-and-career-path-deep-dive-2026-07-16|AI 人才市场与职业路径视频深度调研]] — 将 AI 抢人视频分类为 R10 职业路径调研；政策支持长期人才建设，但视频中的薪资、岗位量和市场数字均保留为待核验线索。
- [[_syntheses/bilibili-ai-daily-run-2026-07-16|Bilibili AI Daily Run 2026-07-16]] — 20 个候选，19 个重复；唯一模型选中的 AI 人才市场视频已成功转录并完成单视频深研。
- [[_syntheses/bilibili-ai-daily-run-2026-07-17|Bilibili AI Daily Run 2026-07-17]] — 20 个候选均为重复；未进入模型复核、转录或单视频深研。

- [[_syntheses/bilibili-ai-daily-run-2026-07-15|Bilibili AI Daily Run 2026-07-15]] — 20 candidates: 19 duplicates; one AI-research video processed successfully.
- [[_syntheses/bilibili-enpire-physical-autoresearch-deep-dive-2026-07-15|ENPIRE 真实世界机器人自我改进视频深度调研]] — 将短视频的“AI 自己做科研”叙事校正为真实世界、受任务和安全边界约束的 agentic policy-improvement 闭环。
- [[robotics-embodied-ai/research-notes/isaac-sim-vs-gazebo-vs-mujoco-2026-07-14|Isaac Sim vs Gazebo vs MuJoCo 机器人仿真平台选型]] — 基于 2026-07 官方版本、许可与加速后端资料，区分高保真感知/合成数据、ROS 2 系统联调和控制/RL 三类需求；新增摩尔线程、沐曦、海光、昇腾、寒武纪、壁仞、天数智芯的支持矩阵、解耦式国产算力架构与 PoC 清单。
- [[_syntheses/bilibili-ai-daily-run-2026-07-14|Bilibili AI Daily Run 2026-07-14]] — 20 candidates: 19 duplicates; the selected UMI/SLAM/Diffusion Policy tutorial was transcribed successfully.
- [[_syntheses/bilibili-umi-diffusion-policy-robotics-tutorial-deep-dive-2026-07-14|UMI、SLAM 与 Diffusion Policy 具身智能教程视频深度调研]] — 以一手 UMI/Diffusion Policy 资料校验最小操作闭环，并保留视频中未核验的公司、规格和实时性主张。
- [[_syntheses/bilibili-ai-daily-run-2026-07-13|Bilibili AI Daily Run 2026-07-13]] — 20 candidates: 19 duplicates; the sole model-review item was unrelated, so none was processed.
- [[_syntheses/bilibili-ai-daily-run-2026-07-12|Bilibili AI Daily Run 2026-07-12]] — 20 candidates: 15 duplicates; four model-selected and processed.
- [[_syntheses/bilibili-kimodo-controllable-motion-deep-dive-2026-07-12|Kimodo 可控动作生成视频深度调研]] — NVIDIA primary documentation separates controllable motion generation from executable robot control.
- [[_syntheses/bilibili-rkda-embodied-lifelong-learning-deep-dive-2026-07-12|RKDA 具身终身学习闭环视频深度调研]] — Lifecycle architecture is useful, but the claimed CVPR 2026 paper remains to be located and verified.
- [[_syntheses/bilibili-graph-as-policy-agentic-robotics-deep-dive-2026-07-12|Graph-as-Policy 智能体机器人视频深度调研]] — GaP primary paper supports modular agentic robotics with simulation-gated iteration.
- [[_syntheses/bilibili-zixel-cloud-cad-embodied-engineering-deep-dive-2026-07-12|子虔科技云原生 CAD 与具身工程闭环视频深度调研]] — CAD/PDM should bind design versions to simulation, manufacturing and test evidence.

- [[_syntheses/bilibili-ai-daily-run-2026-07-11|Bilibili AI Daily Run 2026-07-11]] — 20 candidates: 15 duplicates; four model-selected and processed.
- [[_syntheses/bilibili-variable-robotics-deep-dive-2026-07-11|自变量机器人视频深度调研]] — Official model direction separated from unverified finance and commercial claims.
- [[_syntheses/bilibili-lingbot-depth-2-deep-dive-2026-07-11|LingBot-Depth 2.0 视频深度调研]] — Depth-completion signal with sensor-truth and safety boundaries.
- [[_syntheses/bilibili-ego-data-capture-deep-dive-2026-07-11|Ego 无机器人数据采集平台视频深度调研]] — The value of timestamp, calibration and IMU alignment over video-only capture.
- [[_syntheses/bilibili-mujoco-tutorial-deep-dive-2026-07-11|MuJoCo 教程视频深度调研]] — Simulation-learning path and installation-risk correction checklist.
- [[robotics-embodied-ai/research-notes/srt-soft-robot-tech-company-deep-dive-2026-07-13|SRT 软体机器人公司深度调研]] — 拆解 SRT 的柔性末端执行器技术、业务结构、融资与股权、竞争格局、十五五关联、创始团队迁移风险和投前核验清单。

- [[_syntheses/xiaohongshu-wam-robotics-infrastructure-deep-dive-2026-07-10|小红书 WAM 与具身智能基础设施线索深度调研]] — 基于两条小红书收藏、PAIWorld/WVM/WAM-TTT arXiv 和三个 GitHub Awesome 项目，判断具身智能竞争重心从单模型转向数据、记忆、评测和操作闭环基础设施。

- [[_syntheses/bilibili-ai-daily-run-2026-07-10|Bilibili AI Daily Run 2026-07-10]] — 每日收藏夹候选池 20 个视频全部为重复，未进入模型复核、转录或单视频深研。

- [[_syntheses/bilibili-ai-daily-run-2026-07-09|Bilibili AI Daily Run 2026-07-09]] — 每日收藏夹候选池 20 个视频全部为重复，未进入模型复核、转录或单视频深研。

- [[_syntheses/bilibili-ai-daily-run-2026-07-08|Bilibili AI Daily Run 2026-07-08]] — 每日收藏夹补跑后 3 个模型选中 AI/具身智能相关视频均完成 source packet 和单视频深研；TOS 今日前缀检查恢复正常并确认 3 个音频对象。
- [[_syntheses/bilibili-qianxun-intelligence-deep-dive-2026-07-08|千寻智能具身智能公司视频深度调研]] — 对 `BV1mgja6CEbK` 做单视频深研，将千寻智能相关估值、数据规模、Spirit VLA、工业客户和开源策略全部标为待一级来源验证。
- [[_syntheses/bilibili-boden-intelligence-data-infrastructure-deep-dive-2026-07-08|博登智能 Physical AI 数据基建视频深度调研]] — 对 `BV1q3TE6AE4b` 做单视频深研，提取真实世界数据基建、训练基地、数据资产化和重资产风险线索，全部公司指标待一级来源验证。
- [[robotics-embodied-ai/research-notes/boden-intelligence-business-technology-overview-2026-07-08|博登智能商业逻辑、商业计划与技术方案综述]] — 基于博登智能视频深研和 ASR 原文，系统整理其 Physical AI 数据工厂叙事、收入结构、客户分层、三层技术方案与待验证风险。
- [[_syntheses/bilibili-qianxun-intelligence-bv1z7-deep-dive-2026-07-08|千寻智能 BV1Z7jA6LE8s 视频深度调研]] — 对 `BV1Z7jA6LE8s` 做独立单视频深研，补充融资、创始团队、墨子一硬件、Spirit VLA 和客户落地待验证清单。
- [[_syntheses/bilibili-ai-daily-run-2026-07-07|Bilibili AI Daily Run 2026-07-07]] — 每日收藏夹候选池 20 个，模型选中并成功处理 5 个 AI/具身智能相关视频。
- [[_syntheses/bilibili-physical-ai-productivity-revolution-deep-dive-2026-07-07|Physical AI 生产力革命播客视频深度调研]] — 对 `BV17eTk6vETX` 做单视频深研，拆解 Physical AI 产业链、算力/仿真/数据/本体分层和投资风险。
- [[_syntheses/bilibili-isaac-sim-tutorial-deep-dive-2026-07-07|Isaac Sim 教程视频深度调研]] — 对 `BV1G8kBBvEzR` 做单视频深研，用 NVIDIA Isaac Sim/Isaac Lab 官方文档校验仿真、ROS2、RL 和硬件门槛。
- [[_syntheses/bilibili-multiview-embodied-perception-deep-dive-2026-07-07|多目具身感知视频深度调研]] — 对 `BV1j9jd6aE7c` 做单视频深研，形成双目/多目/多传感器数据采集选型框架。
- [[_syntheses/bilibili-do-as-i-do-dexterous-video-data-deep-dive-2026-07-07|Do As I Do 灵巧操作视频数据深度调研]] — 对 `BV1WfTk6EEZ8` 做单视频深研，并用 arXiv `2606.19333` 校验视频到灵巧操作数据 pipeline。
- [[_syntheses/bilibili-abot-m05-world-action-model-deep-dive-2026-07-07|ABot-M0.5 世界动作模型视频深度调研]] — 对 `BV1F7Ts6WEYj` 做单视频深研，并用 arXiv `2607.00678` 校验移动操作 WAM 的三层对齐框架。
- [[_syntheses/bilibili-ai-daily-run-2026-07-06|Bilibili AI Daily Run 2026-07-06]] — 每日收藏夹候选池 20 个视频全部为重复，未进入模型复核、转录或单视频深研。
- [[robotics-embodied-ai/research-notes/vla-world-model-data-infrastructure-platform-design-2026-07-06|VLA&世界模型数据基建平台系统调研与设计]] — 基于 `BV1ZFTq6pEA3` 的 15 阶段数据生产 SOP，并对照 AIRSPEED、LeRobot、机器人平台和数据价值框架，设计具身智能数据生产平台。
- [[_syntheses/bilibili-hapmorph-haptic-feedback-deep-dive-2026-07-05|HapMorph 触觉反馈视频深度调研]] — 对 `BV12XTM6sEGF` 做单视频深研，并用 arXiv `2509.05433` 校验 21g、50-104mm、4.7N/mm 和 89.4% 等 HapMorph 触觉反馈指标。
- [[_syntheses/bilibili-physical-ai-time-scale-deep-dive-2026-07-05|Physical AI 时间尺度视频深度调研]] — 对 `BV1y3T46NEUf` 做单视频深研，沉淀 Physical AI 与数字 AI 在实时性、视觉主模态和跨本体部署上的差异。
- [[_syntheses/bilibili-vla-tutorial-deep-dive-2026-07-05|VLA 入门教程视频深度调研]] — 对 `BV1ifTp62EaV` 做单视频深研，梳理 VLA 模型、数据、仿真、评测和真机部署学习路线。

- [[_syntheses/bilibili-agent-gui-headless-software-deep-dive-2026-07-04|Agent 时代 GUI 与 Headless 软件视频深度调研]] — 对 `BV1bKTk69EDD` 做单视频深研，并用 MCP、Claude Code skills 和 Vercel AI SDK 官方文档校验 Agent-ready 软件接口、skills 与 GUI/Headless 分层趋势。

- [[_syntheses/bilibili-ai-embodied-signals-2026-07-03|Bilibili AI 与具身智能线索 2026-07-03]] — 从每日收藏夹成功转录的视频中抽取物理一致世界模型、家用机器人产品定义、VLA 工程闭环、GENIE SIM、SLAM/ROS、数值优化和 ESP32 AI 工具链线索。
- [[_syntheses/karpathy-wiki-migration-plan|Karpathy Wiki Migration Plan]] — 本仓库从行业分析工作区升级为 LLM Wiki 的迁移设计。
- [[ai/research-notes/scale-ai-company-history-2026-06-02|Scale AI 公司发展史]] — Scale AI 从 2016 年人力任务 API、自动驾驶数据标注、大模型后训练到 2025 年 Meta 战略投资的完整复盘。
- [[ai/research-notes/scale-ai-and-china-data-infrastructure-peers-2026-06-02|Scale AI 发展历程与中国对标公司]] — Scale AI 从人力任务 API 到 Meta 战略投资的路径，以及中国 AI 数据基础设施公司对标。
- [[ai/research-notes/google-mediapipe-comprehensive-guide-2026-07-14|Google MediaPipe 全面调研：功能、原理与使用方法]] — 拆解 Tasks、Framework、Models 与 LiteRT 的边界，系统说明感知任务、计算图、检测—跟踪、时序同步、跨端用法、工程选型和维护状态。
- [[robotics-embodied-ai/research-notes/ego-video-to-dexterous-hand-training-data-system-design-2026-07-14|Ego 视频到灵巧手训练数据：技术路线、系统设计与落地方案]] — 区分手骨架、手物 4D 重建和机器人动作，比较 Do As I Do、HaWoR、DexCap、DexUMI/RealDexUMI、UniDex、EgoScale、GeoRT 与 SPIDER，并给出数据 schema、质量门和 PoC。
- [[robotics-embodied-ai/09-training-data-deep-dive|机器人训练数据深度调研]] — 具身智能训练数据、地方政策、schema、失败轨迹和 UMI-like 业务路线综合。
- [[robotics-embodied-ai/08-umi-gripper-research-and-business-plan|UMI Gripper 研究与业务计划]] — UMI-like 数据采集硬件、学习路径与 ToB 落地方案。
- [[robotics-embodied-ai/11-embodied-ai-data-service-companies-2026-06-02|具身智能数据采集和服务公司对比]] — 对智元、补天石、它石、简智、Maxinsights、自变量、帕西尼的数据采集/服务路线、岗位和优劣势做横向分析。
- [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]] — 对机器人数据、训练、评测、部署、真机推理平台做分层拆解，并比较 LeRobot、FluxVLA、Isaac、OpenPI、Unitree G1-D、EmbodiFlow 等选项。
- [[robotics-embodied-ai/13-robot-company-product-comparison-2026-06-08|机器人公司产品型号全景对比]] — 汇总 `04-companies` 主表机器人公司的产品型号、参数、技术路线、优缺点和待验证事项。
- [[robotics-embodied-ai/research-notes/career-direction-business-landing-knowhow-2026-06-09|具身智能业务落地 know-how 职业方向思考]] — 基于 Thinking Partner 对话沉淀的职业方向锚点，聚焦用具身智能业务落地 know-how 解决企业成本、收入或风险痛点。
- [[robotics-embodied-ai/research-notes/retail-store-robotics-entry-scan-2026-06-10|线下零售门店机器人合作验证初扫]] — 验证大型零售公司线下门店机器人合作是否超过 5/10；第一轮公开检索未通过，需继续补实权威排名与公告/年报全文。
- [[robotics-embodied-ai/research-notes/cross-scenario-near-term-landing-candidate-pool-2026-06-10|具身智能短期落地跨场景候选池]] — 按 1 年内真实订单或试点转生产证据，建立跨场景短期落地候选池，暂不排序。
- [[robotics-embodied-ai/research-notes/platform-engineer-jd-entry-scan-2026-06-10|具身智能平台工程师 JD 快速入场扫描]] — 用“通用软件平台能力是硬要求、机器人领域知识可补齐”作为第一筛选门槛，初扫平台工程、后端、数据管线、仿真平台和运营系统岗位。
- [[robotics-embodied-ai/research-notes/libero-lifelong-robot-learning-platform-2026-06-11|LIBERO 终身学习仿真平台调研]] — 拆解 LIBERO 的 lifelong robot learning benchmark 定位、任务/数据/baseline、VLA/IL 评测价值、平台工程作品集方向和鲁棒性局限。
- [[robotics-embodied-ai/research-notes/open-embodied-ai-datasets-comparison-2026-06-11|开源具身智能训练与评估数据集横向调研]] — 按预训练、真实机器人微调、特定能力和仿真 benchmark 横向比较开源具身数据集的格式、任务完整度、模型/算法适配和缺口。
- [[robotics-embodied-ai/research-notes/robot-training-data-value-evaluation-2026-06-29|具身智能训练数据价值评估框架]] — 面向数据采集立项、现场质检和采后验证，提出以边际能力提升、复用性、可信度和全成本风险比衡量机器人训练数据价值。
- [[robotics-embodied-ai/research-notes/teleoperation-training-data-cost-and-share-2026-07-09|遥操训练数据每小时成本与训练数据占比快速调研]] — 按有效可训练小时估算遥操/示教数据成本，并区分机器人 action 数据和 VLA foundation model 总训练混合中的遥操占比。
- [[robotics-embodied-ai/research-notes/embodied-ai-training-data-hour-requirements-2026-07-09|具身智能训练数据需求量与小时数分层估算]] — 按有效可训练小时估算从 demo、单任务泛化、客户场景产品化到跨任务 VLA/foundation model 的训练数据需求量。
- [[robotics-embodied-ai/research-notes/airspeed-data-production-platform-2026-06-23|AIRSPEED 具身智能数据生产平台调研]] — 系统拆解 AIRSPEED 当前开源采集核心、论文三服务架构、技术转移叙事、性能 claim 和中国具身数据基础设施启发。
- [[robotics-embodied-ai/research-notes/dora-1-vs-ros2-2026-06-23|dora 1.0 vs ROS 2 调研]] — 对比 dora 的 AI dataflow runtime 路线与 ROS 2 机器人生态底座，拆解版本状态、性能、QoS、桥接架构和职业学习路径。
- [[robotics-embodied-ai/research-notes/lidar-world-model-training-2026-06-29|激光雷达数据融合进入世界模型训练论文与方案调研]] — 梳理 LiDAR 原生生成、BEV/occupancy、多模态 camera-LiDAR latent、JEPA 和移动机器人导航 world model 路线，并给出工程方案。
- [[robotics-embodied-ai/research-notes/home-elderly-care-robots-2026-07-06|家庭养老机器人公司与方案调研]] — 按陪伴提醒、远程巡视、移动载物、康复护理和通用家务机器人五层路线，比较国内外代表公司、商业化阶段、风险约束与中国落地方案。
- [[eldercare/04-companies|中国养老行业头部公司与科技创新创业公司]] — 新建养老服务与银发科技行业公司扫描，分层梳理保险系医养社区、连锁养老运营、居家护理、智慧养老平台、社区空间科技和养老智能硬件玩家。
- [[robotics-embodied-ai/research-notes/embodied-model-physical-understanding-evaluation-2026-07-03|具身智能大模型物理理解能力评估框架]] — 区分动作生成、语义泛化、动作条件预测和规划可用世界模型，提出反事实预测、minimal physical pairs、闭环 A/B 与多模态约束的评估方法。
- [[ai/research-notes/jepa-core-principles-2026-06-11|JEPA 核心原理快速调研]] — 系统拆解 JEPA、I-JEPA、V-JEPA、V-JEPA 2 与世界模型/机器人规划的核心原理、差异和局限。
- [[_syntheses/china-umi-gripper-purchase-scan-2026-06-08|中国可购买 UMI 夹爪设备检索]] — 追踪 LUMOS FastUMI、觅蜂 MEgo Gripper、BeingBeyond U1 等 UMI-like 数采设备在中国的购买状态、价格线索和待验证事项。
- [[integrated-circuits/07-ai-chip-global-supply-chain-and-stock-screen-2026-06-11|AI 芯片全球上市公司、供应链关系与股票初筛]] — 第一版全球 AI 芯片及上下游上市公司池，记录主营业务、公开供应链关系、近一年市值变化、筛选框架和待补证据。
- [[_syntheses/matlab-simulink-agentic-ai-tools-bilibili-2026-07-02|MATLAB/Simulink Agentic AI 工具链视频调研]] — 基于 Bilibili 视频和 MathWorks 官方 GitHub 项目，分析工程软件 Agent 化的工具层、技能层和反馈闭环。
- [[_syntheses/bilibili-embodied-ai-signals-2026-07-02|Bilibili 具身智能与 AI 工具链线索 2026-07-02]] — 从每日收藏夹成功转录的视频中抽取 VLA、世界模型、机器人数据基建、仿真资产、家庭机器人 PMF、ForceBand、ROS2/LiDAR 和 TensorRT 的 B 级研究线索。
- [[_syntheses/bilibili-ai-embodied-signals-2026-07-03|Bilibili AI 与具身智能线索 2026-07-03]] — 从每日收藏夹成功转录视频中抽取 PhysisForcing 物理一致世界模型和 ESP Cloud 自然语言驱动嵌入式开发的 B 级线索。
- [[_syntheses/bilibili-physisforcing-world-simulator-deep-dive-2026-07-03|PhysisForcing 物理一致世界模拟器视频深度调研]] — 对 `BV12pTq6qECg` 做单视频深研，并用 arXiv `2606.28128` 校验物理一致视频/机器人世界模型 claim。
- [[_syntheses/bilibili-esp-claw-embedded-ai-deep-dive-2026-07-03|ESP-Claw 自然语言驱动嵌入式开发视频深度调研]] — 对 `BV1PCjA6bEi4` 做单视频深研，并用乐鑫 ESP-Claw 官网、文档和 GitHub 校验项目形态。

## Industries

- [[6g/00-index|6G]] — 6G 初步调研入口，覆盖 IMT-2030、通感一体、空天地一体和运营商/设备商链条。
- [[aerospace/00-index|航空航天]] — 航空航天初步调研入口，覆盖商业航天、卫星互联网、发射与空间基础设施。
- [[ai/00-index|AI]] — AI 总行业研究入口，覆盖算力、基础模型、数据/评测、应用/Agent、监管安全和职业/投资视角。
- [[biopharma/00-index|生物医药]] — 生物医药初步调研入口，覆盖创新药、生物经济、CXO/CDMO 和未来健康。
- [[brain-computer-interface/00-index|脑机接口]] — 脑机接口初步调研入口，覆盖非侵入/侵入式 BCI、医疗康复和神经信号解码。
- [[eldercare/00-index|养老服务与银发科技]] — 养老服务、医养结合、长护险、智慧养老、居家护理、养老社区和银发科技行业研究入口。
- [[future-energy/00-index|未来能源]] — 未来能源初步调研入口，覆盖新型能源体系、储能、氢能、智能电网和聚变期权。
- [[integrated-circuits/00-index|集成电路]] — 集成电路行业研究入口。
- [[low-altitude-economy/00-index|低空经济]] — 低空经济初步调研入口，覆盖无人机、eVTOL、低空基础设施和监管平台。
- [[quantum-technology/00-index|量子科技]] — 量子科技初步调研入口，覆盖量子计算、量子通信和量子精密测量。
- [[robotics-embodied-ai/00-index|机器人与具身智能]] — 机器人与具身智能行业研究入口。

## News

- [[news/00-index|新闻速记]] — ad hoc 新闻/文章/视频摘要入口；每条摘要独立成文。
- [[news/2026-07-14-harness-engineering-self-improvement-deep-dive|Harness Engineering for Self-Improvement 深度研读与公式通俗解释]] — 梳理 harness 从上下文、工作流到自改进代码的研究谱系，逐式解释 MCE 与 STOP，并校正 STOP 元效用公式中的重复归一化记号。
- [[news/2026-06-05-nvidia-cosmos-3-getting-started-plan|NVIDIA Cosmos 3 上手调研与计划]] — NVIDIA 2026 年发布的 Cosmos 3 omnimodal world model 调研、关键事实与两周上手计划。

## Operations

- [Xiaohongshu AI Daily Research Automation](../docs/xiaohongshu_daily_research_automation.md) — 小红书 `AI/具身智能调研` 收藏夹采集流程，复用 Bilibili 每日研究的候选筛选、去重、图文 OCR、视频字幕/ASR、source packet、source card 和 Codex handoff 模式。
- [[log|Wiki Log]] — append-only 操作日志，记录 ingest/query/lint/migration。
- [[README|Knowledge README]] — 面向人类的 Obsidian vault 首页。
