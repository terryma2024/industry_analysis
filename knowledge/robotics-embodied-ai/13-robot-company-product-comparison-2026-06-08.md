---
title: 机器人公司产品型号全景对比
type: synthesis
date_created: 2026-06-08
last_updated: 2026-06-08
sources:
  - robotics-embodied-ai/sources.csv
  - raw/robotics-embodied-ai/data/robot_company_product_models_2026-06-08.csv
  - raw/robotics-embodied-ai/documents/SRC-robotics-012-unitree-g1-humanoid-robot-product-page.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-013-unitree-h1-humanoid-robot-product-page.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-014-unitree-g1-d-end-to-end-platform-for-humanoid-robot.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-024-dobot-official-website.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-025-jaka-official-website.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-104-limx-tron-1-product-page.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-106-limx-oli-product-page.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-107-limx-tron-2-product-page.md
tags:
  - industry/robotics-embodied-ai
  - companies
  - products
  - comparison
status: draft
---

# 机器人公司产品型号全景对比

> [!important] 范围与读法
> 本页覆盖 [[04-companies|公司池]] 主表中的机器人整机、协作机器人、工业机器人、AMR/移动操作公司；零部件公司暂不展开 SKU。参数以 2026-06-08 可核验的官网、产品页、产品手册或已入库 raw artifact 为准。工业机器人、协作臂和 AMR 公司型号很多，本页先按“系列 + 已公开型号”梳理，精确到每个 SKU 的负载/臂展/重复定位精度需要继续从产品手册补齐。
>
> 可筛选数据表见 [robot_company_product_models_2026-06-08.csv](../../raw/robotics-embodied-ai/data/robot_company_product_models_2026-06-08.csv)。

## 一页结论

- **通用具身/人形路线分化明显**：宇树偏“低价标准化硬件 + 开发平台”，智元偏“整机矩阵 + 数据/开发平台”，优必选偏“工业场景交付 + 上市公司可验证订单”，逐际偏“运动控制本体 + VLA 工具链”，星动纪元偏“全尺寸人形 + 灵巧手 + 物流/制造 PMF”，银河通用/Galbot 与星海图/Galaxea 更偏轮式双臂、商业零售或科研数采。
- **工业可落地优先级不是人形优先**：对 2026 年真实 ROI，AMR/移动操作、协作臂、工业机器人和轮式双臂通常比双足人形更近；人形更像长期平台押注，短期适合看示范订单、数据闭环、可靠性和维护成本。
- **参数不能只看自由度和身高**：关键比较维度应是有效载荷、工作空间、续航/换电、感知配置、二次开发开放度、数据闭环、仿真/训练工具、场景客户与售后能力。
- **最值得继续深挖的公司**：优必选、宇树、智元、逐际、星动纪元、Galbot/Galaxea、越疆、节卡、极智嘉、快仓、优艾智合。它们分别代表人形交付、低价开发者平台、数据平台、VLA 工程工具、物流 PMF、轮式双臂、协作臂上探具身、AMR 场景数据等不同路线。

## 公司与产品矩阵

| 公司 | 已识别产品型号/系列 | 形态 | 技术路线 | 主要场景 | 证据 |
|---|---|---|---|---|---|
| 优必选 UBTECH | Walker S2、Walker S1、Walker S、Walker C、Walker X、Walker、Cruzr S2、熊猫机器人、教育机器人/UGOT/uKit 等 | 双足人形、商服轮式、教育硬件 | 全栈人形硬件、ROSA、U-SLAM/3D 语义导航、工业场景多机协同；S2 强调自主换电 | 汽车/3C/物流、商服、教育、家庭服务探索 | [`SRC-robotics-009`](../../raw/robotics-embodied-ai/documents/SRC-robotics-009-ubtech-robotics-hkex-issuer-announcements-page.md)、[`SRC-robotics-010`](../../raw/robotics-embodied-ai/documents/SRC-robotics-010-ubtech-latest-announcements-and-circulars.md)、[[00-source-capture-index|SRC-robotics-135]]-[[00-source-capture-index|SRC-robotics-139]] |
| 宇树 Unitree | G1、G1 EDU、G1-D Standard/Flagship、H1、H1-2 | 小型/全尺寸人形、轮式双臂数据平台 | 标准化本体、低价硬件、PMSM 关节、LiDAR+深度相机、端到端数据/训练平台、UnifoLM-WMA | 科研、开发者、教育、工业/服务探索 | [`SRC-robotics-012`](../../raw/robotics-embodied-ai/documents/SRC-robotics-012-unitree-g1-humanoid-robot-product-page.md)、[`SRC-robotics-013`](../../raw/robotics-embodied-ai/documents/SRC-robotics-013-unitree-h1-humanoid-robot-product-page.md)、[`SRC-robotics-014`](../../raw/robotics-embodied-ai/documents/SRC-robotics-014-unitree-g1-d-end-to-end-platform-for-humanoid-robot.md) |
| 智元 AGIBOT | A2、A2-W、A2-Max、G1、X1、X2、C5、Genie Studio、AgiBot World | 双足/轮式通用机器人、平台 | 整机 + 具身大模型/原子技能 + 数据采集/训练/部署平台 | 工业柔性制造、服务、科研、数据集 | [`SRC-robotics-015`](../../raw/robotics-embodied-ai/documents/SRC-robotics-015-agibot-a2-product-page.md)、[`SRC-robotics-016`](../../raw/robotics-embodied-ai/documents/SRC-robotics-016-agibot-products-page.md)、[`SRC-robotics-044`](../../raw/robotics-embodied-ai/documents/SRC-robotics-044-agibot-open-agibot-world-2026.md)、[`SRC-robotics-123`](../../raw/robotics-embodied-ai/documents/SRC-robotics-123-agibot-genie-studio.md)、[[00-source-capture-index|SRC-robotics-140]] |
| 逐际动力 LimX | Oli、TRON 1、TRON 2、FluxVLA | 全尺寸人形、多形态双足/轮腿平台 | 强运动控制、模块化脚端、Python/SDK/URDF/Sim2Real、VLA 数据-训练-推理工具链 | 科研开发、教育展示、巡检、工业操作探索 | [`SRC-robotics-104`](../../raw/robotics-embodied-ai/documents/SRC-robotics-104-limx-tron-1-product-page.md)、[`SRC-robotics-106`](../../raw/robotics-embodied-ai/documents/SRC-robotics-106-limx-oli-product-page.md)、[`SRC-robotics-107`](../../raw/robotics-embodied-ai/documents/SRC-robotics-107-limx-tron-2-product-page.md)、[`SRC-robotics-108`](../../raw/robotics-embodied-ai/documents/SRC-robotics-108-fluxvla-engine-documentation.md) |
| 星动纪元 RobotEra | L7、Q5、M7、XHAND 1、XHAND 1 Lite、ERA-42 | 双足人形、灵巧手、VLA | 全栈人形 + 灵巧手 + VLA 模型；L7 主打 55 DoF/171 cm/双臂 20 kg | 物流分拣、制造、接待、商场导购、教育/医疗导诊 | [`SRC-robotics-021`](../../raw/robotics-embodied-ai/documents/SRC-robotics-021-robotera-official-website.md)、[[00-source-capture-index|SRC-robotics-141]]、[[00-source-capture-index|SRC-robotics-142]] |
| 银河通用 Galbot | Galbot G1 | 轮式升降双臂通用机器人 | 轮式底盘 + 升降/折叠机构 + 长臂操作 + 多模态/具身大脑 | 零售、商业服务、仓储/货架操作 | [[00-source-capture-index|SRC-robotics-143]] |
| 星海图 Galaxea | R1 Pro、R1、R1 Lite、A1、G1 夹爪/开发文档 | 轮式双臂科研/数采平台 | 双臂 + 躯干升降 + 三舵轮底盘 + 多相机/LiDAR + Jetson Orin | 科研、数据采集、场景部署 | [`SRC-robotics-050`](../../raw/robotics-embodied-ai/documents/SRC-robotics-050-galaxea-company-about.md)、[`SRC-robotics-092`](../../raw/robotics-embodied-ai/documents/SRC-robotics-092-galaxea-open-world-dataset.md)、[[00-source-capture-index|SRC-robotics-144]] |
| 自变量 X2Robot | Quantum 2 / 量子 2、WALL-A 操作大模型 | 轮式仿人形机器人 + 模型 | 端到端操作大模型，百亿级参数，软硬件联合设计 | 工业操作、家庭/商业服务探索 | [`SRC-robotics-022`](../../raw/robotics-embodied-ai/documents/SRC-robotics-022-x2robot-official-website.md) |
| 魔法原子 MagicLab | MagicBot 系列、四足/人形产品线（型号待细化） | 人形、四足 | 具身智能 + 场景订单，强调表演/大健康/商业场景 | 工业、商业、大健康、展示 | [`SRC-robotics-023`](../../raw/robotics-embodied-ai/documents/SRC-robotics-023-magiclab-official-website.md) |
| 越疆 DOBOT | Atom、RoboPilot、X-Trainer、Hexplorer、Rover X1、CR 30H、CRA/CRAF/CRA-IP68、CR20A、Nova 2/5、MG400、M1 Pro、Magician E6/Magician | 人形、遥操作/数采、六足/四足、协作臂、SCARA/桌面机器人 | 协作臂制造 know-how 上探具身；CR/CRA 系列工业协作，Atom/Rover/X-Trainer 扩展具身形态 | 工业、商业、科研教育、家庭探索 | [`SRC-robotics-024`](../../raw/robotics-embodied-ai/documents/SRC-robotics-024-dobot-official-website.md)、[[00-source-capture-index|SRC-robotics-145]]、[[00-source-capture-index|SRC-robotics-146]] |
| 节卡 JAKA | EI Robot、Kargo、K1、Lumi、S3 移动作业机器人、EVO 平台、Zu3/5/7/12/18/20/30、Pro5/12/16、S5/S12、AL/A/Mini、Lens/力控组件 | 具身作业平台、协作臂、移动操作 | 协作臂 + 视觉/力控 + 移动作业，强调从点位编程到作业泛化 | 工业制造、3C、新能源、物流、科研教育 | [`SRC-robotics-025`](../../raw/robotics-embodied-ai/documents/SRC-robotics-025-jaka-official-website.md)、[[00-source-capture-index|SRC-robotics-147]]、[[00-source-capture-index|SRC-robotics-148]] |
| 遨博 AUBO | i3/i5/i10/i16/i20、iS/iH/C 等系列（手册待补） | 协作机器人 | 开放架构协作臂，3-20 kg 负载覆盖，部分系列高性能/高防护 | 3C、汽车、医疗、物流、教育 | [`SRC-robotics-026`](../../raw/robotics-embodied-ai/documents/SRC-robotics-026-aubo-robotics-official-website.md)、[[00-source-capture-index|SRC-robotics-149]] |
| 新松 SIASUN | SA/SCARA、SR 工业机器人、B/D/FP/P-T/G 系列移动机器人、重载/复合/输送 AMR | 工业机器人、AMR、复合机器人 | 传统工业机器人 + 移动机器人 + IMRS 2.0 调度平台 | 汽车、新能源、半导体、物流、光伏 | [`SRC-robotics-027`](../../raw/robotics-embodied-ai/documents/SRC-robotics-027-siasun-official-website.md)、[[00-source-capture-index|SRC-robotics-150]]、[[00-source-capture-index|SRC-robotics-151]] |
| 埃斯顿 ESTUN | ER 系列、iER 大负载、SCARA、UNO/协作探索 | 工业机器人 | 国产工业机器人本体 + 伺服/控制基础，3-1200 kg 负载覆盖 | 光伏、锂电、汽车、电子、重载搬运 | [[00-source-capture-index|SRC-robotics-155]] |
| 埃夫特 EFORT | ER8/10/12/15/20/25/35/50/70/150/210、ARC 系列、SCARA | 工业机器人 | 六轴工业机器人、弧焊/中小负载/中大负载和 SCARA 系列 | 汽车、3C、光伏、锂电、金属加工 | [`SRC-robotics-028`](../../raw/robotics-embodied-ai/documents/SRC-robotics-028-efort-official-website.md)、[[00-source-capture-index|SRC-robotics-154]] |
| 极智嘉 Geek+ | P 系列货到人、RoboShuttle/C200 系列、PopPick、拣选/分拣/搬运 AMR | 仓储 AMR、箱到人、货到人 | AMR + 仓储软件 + 多机器人调度，重在履约效率和存储密度 | 电商、零售、3PL、制造、汽车 | [`SRC-robotics-029`](../../raw/robotics-embodied-ai/documents/SRC-robotics-029-geek-company-page.md)、[[00-source-capture-index|SRC-robotics-152]] |
| 快仓 Quicktron | M-100、C-Series、Bin-to-Person 等产品线 | 仓储 AMR、料箱机器人 | AMR + 仓储系统，面向电商/零售/制造物流 | 电商、零售、汽车、医药、制造 | [`SRC-robotics-030`](../../raw/robotics-embodied-ai/documents/SRC-robotics-030-quicktron-official-website.md)、[[00-source-capture-index|SRC-robotics-153]] |
| 优艾智合 YOUIBOT | P200、巡检/复合移动机器人、半导体/能源/新能源解决方案 | 工业移动机器人、移动操作/巡检 | AMR + 机械臂/传感 + 工业软件系统 | 半导体、能源化工、新能源、3C | [`SRC-robotics-031`](../../raw/robotics-embodied-ai/documents/SRC-robotics-031-youibot-official-website.md) |

## 通用具身/人形与轮式双臂型号

| 公司 | 型号 | 关键公开参数 | 技术路线 | 优点 | 短板/待验证 |
|---|---|---|---|---|---|
| 优必选 | Walker S2 | 工业人形；自主热插拔换电，公开材料称 3 分钟内自主换电；双电池动态平衡 | 工业人形 + 自主补能 + 多机协同 | 解决“续航/补能”痛点，适合连续生产线叙事 | 具体负载、节拍、MTBF、单机成本和真实复购需用客户案例/年报验证 |
| 优必选 | Walker S / S1 | Walker S 约 1.7 m，41 个带力反馈伺服关节，多模态大模型决策、U-SLAM + 3D 点云语义导航、ROSA 2.0 | 工业制造人形 | 上市公司披露和汽车工厂试训线索较多 | 参数页仍偏营销，S1/S/S2 代际差异需产品手册验证 |
| 优必选 | Walker X | 130 cm，63 kg，41 DoF，最高步速 3 km/h，坡度 20 度、台阶 15 cm；7 DoF 手臂 + 6 DoF 力控仿人手 | 商服/家庭服务人形 | 感知交互能力完整，服务场景形象强 | 非工业交付主线，商业 ROI 更难验证 |
| 优必选 | Walker | 145 cm，77 kg，36 DoF，单臂伸展负载 1.5 kg，续航约 2 h，Ubuntu + Linux RT + ROS + Android | 早期人形服务机器人平台 | 技术积累和参数透明 | 代际较老，更多用于技术脉络而非当前采购 |
| 宇树 | G1 | 1320x450x200 mm，约 35 kg，23 DoF，单臂约 2 kg，9 Ah 电池约 2 h，深度相机 + 3D LiDAR，价格 from USD 13.5k | 低成本小型人形 | 价格透明、开发者门槛低、OTA | 商业场景载荷和稳定作业能力有限 |
| 宇树 | G1 EDU | 23-43 DoF，可选 Dex3-1 三指手、触觉阵列、Jetson Orin；膝关节最大 120 Nm，单臂约 3 kg | 开发/教育增强版 | 手部、腕部、算力可扩展 | 价格需销售确认，量产一致性和售后待验证 |
| 宇树 | H1 | 约 180 cm，47 kg，移动速度 3.3 m/s，潜在 >5 m/s，0.864 kWh 快换电池，最大关节扭矩 360 Nm | 全尺寸高动态人形 | 运动性能强，适合科研/演示 | 手部/操作能力不是核心强项 |
| 宇树 | H1-2 | 约 178 cm，70 kg，27 DoF，腿部最大 360 Nm，臂关节最大 120 Nm，臂额定约 7 kg/峰值约 21 kg | 全尺寸增强人形 | 载荷和上肢自由度较 H1 强 | 速度 <2 m/s，价格/交付周期待验证 |
| 宇树 | G1-D Standard/Flagship | Standard 约 50 kg/17 DoF；Flagship 约 80 kg/19 DoF；双 7 DoF 手臂、2 DoF 腰、可选二指/三指/五指末端，Orin NX 100 TOPS；Flagship 底盘 1.5 m/s，续航约 6 h | 轮式双臂数据与训练平台 | 面向数据采集/训练/部署，工作流完整 | 不是双足人形，价格和实际平台开放程度需验证 |
| 智元 | A2-W | 770x620x1630 mm，230 kg，2 kWh，充电 2 h，续航约 5 h，单臂 5 kg，每臂 7 DoF，操作高度 0-2 m，275T 算力 | 轮式双臂柔性制造机器人 | 参数接近工业落地，热插拔电池和一体化部署 | A2/A2-Max/G1/X 系列完整参数仍需官网手册补齐 |
| 智元 | A2/A2-Max/G1/X1/X2/C5 | 官网产品矩阵可见，A2 页面 raw 抓取失败 | 整机矩阵 + Genie Studio + AgiBot World 数据 | 具身数据、平台和整机联动强 | 非上市公司，客户、财务、交付节奏需交叉验证 |
| 逐际 | Oli | 165 cm 级全尺寸人形；31 DoF 线索来自已入库实体页；官网强调自研 6 轴 IMU、头/胸深度相机、双语语音、Python SDK、URDF | 运动控制 + 交互 + 开发平台 | 开箱、二次开发和展示/巡检友好 | 公开参数不完整，载荷/续航需规格页或手册 |
| 逐际 | TRON 1 | 多形态双足，点足/足底/轮足三模式；Python SDK、Isaac/Mujoco/Gazebo、URDF、可加机械臂/语音/感知套件 | 双足运动控制研究平台 | 强 RL/Sim2Real 教学和开发者定位 | 不是完整操作机器人，参数手册自动抓取失败待补 |
| 逐际 | TRON 2 | 双臂 + 轮足/足底，内置 VLA 数据采集、清洗、标注、训练、推理、任务管理；兼容 ROS1/ROS、ACT、Pi0.5 | 轮腿双臂 VLA 平台 | 与 FluxVLA 形成工具链闭环 | 公开参数缺少负载/尺寸/续航，仍偏开发平台 |
| 星动纪元 | L7 | 官网页显示 55 DoF、171 cm、双臂负载 20 kg；全尺寸双足 | 高自由度人形 + ERA-42 VLA | 物流/制造场景 PMF 叙事强，融资/顺丰合作线索多 | 真实性能、批量交付、维护成本需客户/合同验证 |
| 星动纪元 | XHAND 1 | 12 主动 DoF，1.1 kg，190.36x94x47 mm，整手最大握力 80 N，整手最大负载 25 kg，指尖 15 N/5 kg，最小抓握直径 16 mm | 全驱五指灵巧手 + 触觉可选 + ROS/SDK/遥操作 | 灵巧操作参数透明，适合搭配多本体 | 成本、寿命、触觉版量产一致性待验证 |
| 星动纪元 | Q5/M7/XHAND 1 Lite | 官网产品线可见，参数待补 | 服务/制造/灵巧操作产品线 | 产品矩阵完整 | 需要 PDF 或产品详情页补参数 |
| Galbot | G1 | 官方页披露 0-2.4 m 高度覆盖、机械臂水平触达可达 1.9 m、负载可达 10 kg、全向底盘、最多 8 h 运行 | 轮式升降双臂 + 多模态/具身大脑 | 商业零售/货架操作比双足更务实 | 规格页细节与客户案例仍需官方手册验证 |
| Galaxea | R1 Pro/R1/R1 Lite | R1 Pro/R1 高 1700 mm；R1 Lite 高 1455 mm；23-26 DoF；双臂负载额定 2-3.5 kg、最大 3.5-5 kg；底盘 1.5 m/s；Orin 32GB/200 TOPS，R1 文档称最高 550 TOPS | 轮式双臂科研/数采平台 | 参数公开、开发文档完整，适合 AI 开发 | 与“银河通用 Galbot”需区分；商业客户与量产需验证 |
| 自变量 | 量子 2 | 全身 20+ DoF、0-2 m 工作空间、轮式底盘；WALL-A 百亿级端到端操作模型 | 模型驱动轮式仿人形 | 模型路线鲜明，融资和大厂背书强 | 具体负载、续航、价格、开放接口待验证 |
| 魔法原子 | MagicBot/四足产品线 | 官网已有订单和春晚/大健康场景新闻，型号参数待补 | 人形/四足 + 场景方案 | 场景营销和订单新闻活跃 | 产品规格、交付验收、收入确认需要更硬证据 |

## 协作臂与工业机器人型号

| 公司 | 型号/系列 | 公开参数摘要 | 技术路线 | 优点 | 短板/待验证 |
|---|---|---|---|---|---|
| 越疆 | CR 30H | 官网称 30 kg 大负载、300 deg/s 行业高速 | 高负载六轴协作机器人 | 协作臂出货基础强，适合码垛/搬运/焊接 | 完整负载-臂展-精度需规格书 |
| 越疆 | CRA/CRAF/CRA-IP68/CR20A | CR20A：20 kg、1700 mm、TCP 2000 mm/s、重复定位 +/-0.05 mm、IP54；CRAF 5-20 kg/900-1700 mm，力控；CRA-IP68 高防护 | 工业协作臂 + 力控/高防护 | 工业 Know-how 和客户基础强 | 人形/具身业务占比待拆 |
| 越疆 | Nova 2/Nova 5 | Nova 2：11 kg、625 mm、+/-0.05 mm；Nova 5：14 kg、850 mm、+/-0.05 mm | 商业/服务协作臂 | 面向新零售/理疗等非传统工业 | 场景规模化待验证 |
| 越疆 | MG400/M1 Pro/Magician E6 | MG400 桌面四轴；M1 Pro SCARA 1.5 kg/400 mm/+/-0.02 mm；Magician 教育 | 桌面/教育/SCARA | 低门槛和教育生态 | 与通用具身关联弱 |
| 节卡 | Zu3/5/7/12/18/20/30 | Zu18：18 kg、1073 mm、+/-0.03 mm、6 轴、IP54；手册显示 Zu 系列覆盖 3-30 kg | 通用协作臂 | 型号覆盖完整，安全协作和性价比 | 各型号完整参数需产品选型手册 |
| 节卡 | Pro5/12/16 | IP68 防护，适合油污/粉尘/水环境 | 高防护协作臂 | 恶劣工业环境适配 | 参数待补 |
| 节卡 | S5/S12 | 内置高精度力传感器，强调智能力控 | 力控协作臂 | 适合装配、打磨、柔性操作 | 参数待补 |
| 节卡 | EI Robot/Kargo/K1/Lumi/S3/EVO | 具身作业机器人、移动作业机器人、工业具身平台 | 协作臂 + 移动/视觉/力控 + 作业泛化 | 从传统协作臂向具身落地过渡 | 具体参数和客户案例待补 |
| 遨博 | i3/i5/i10/i16/i20 | i3：3 kg/625 mm/+/-0.02 mm；i5：5 kg/886.5 mm/+/-0.02 mm；i 系列覆盖 3/5/10/16/20 kg | 协作机器人 | 开放架构、型号成熟 | 中国官网与海外资料需统一校验 |
| 新松 | SA/SCARA、SR 工业机器人 | SCARA 覆盖 4-20 kg；SR 系列覆盖 7-500 kg 级别，官网列多款重载型号 | 工业机器人本体 + 系统集成 | 产品线宽、项目经验深 | 传统集成业务周期性，具身关联需区分 |
| 埃斯顿 | ER/iER 系列 | ER 系列覆盖 3-1200 kg；例 iER170-2650：170 kg、2650 mm、+/-0.06 mm、6 轴 | 工业机器人 + 伺服/控制 | 国产工业机器人龙头，供应链基础强 | 产品数量多，需按应用细分深挖 |
| 埃夫特 | 小负载、弧焊、中负载、大负载、SCARA | 小型 8-12 kg、593-2025 mm、+/-0.02-0.03 mm；弧焊 10-15 kg、1400-2000 mm；中型 10-35 kg、1143-2295 mm；大负载 50-210 kg、2146-3160 mm | 工业机器人 + 工艺软件/系统集成 | 工艺覆盖广，上市公司可验证 | 毛利、海外子公司整合和周期性风险 |

## AMR、仓储与移动操作型号

| 公司 | 型号/系列 | 公开参数摘要 | 技术路线 | 优点 | 短板/待验证 |
|---|---|---|---|---|---|
| 极智嘉 | RoboShuttle/C200S/C200M、P40/P500/P800、PopPick 等 | C200S：约 950x702x2500/3400 mm、304 kg、自重、40 kg 载荷、最高举升 2915 mm、速度 2 m/s；C200M：470 kg、150 kg 载荷、最高 4865 mm、速度 1.5 m/s | 箱到人/货到人 AMR + 仓储系统 | 部署案例和仓储数据丰富，ROI 约 1-3 年叙事 | 向“具身操作”延伸仍需机械臂/抓取能力验证 |
| 快仓 | M-100、C-Series、Bin-to-Person 等 | 官网列产品线但本轮未补完整参数 | AMR + 仓储物流方案 | 客户基础和物流系统成熟 | 参数、海外/国内版本差异需补采 |
| 优艾智合 | P200、巡检/复合移动机器人 | P200 PDF 待补；公司定位半导体、能源化工、新能源、3C 工业移动机器人 | 移动底盘 + 操作/巡检 + 工业软件 | 工业场景明确，贴近具身落地 | 人形业务不是主线，需区分移动操作与人形叙事 |
| 新松 | B20S/B30S/D15S/D20S、FP85/FP95、P-T600D/T1000D/T1500D/T2000D/T3000D、G 系列、3T-80T 重载 | 标准/定制移动机器人覆盖叉车、料箱、清洁、潜伏举升、园区配送、重载、复合移动操作 | AMR/AGV + IMRS 2.0 平台 | 产品线最宽之一，可服务复杂工厂物流 | 非标项目多，毛利和交付周期风险 |

## 技术路线对比

| 路线 | 代表公司/型号 | 适合场景 | 优点 | 缺点 | 投资/职业观察点 |
|---|---|---|---|---|---|
| 双足人形 | UBTECH Walker S2/S1/S、Unitree H1/H1-2/G1、RobotEra L7、LimX Oli | 人类工位、展示、巡检、制造探索 | 可复用人类环境，叙事空间最大 | 成本高、稳定性/维护/安全难，短期 ROI 不确定 | 看订单是否从 demo 变复购，是否有明确工艺和节拍 |
| 轮式双臂/升降 | Agibot A2-W、Unitree G1-D、Galbot G1、Galaxea R1、X2Robot Quantum 2 | 工业柔性作业、零售货架、数据采集、科研 | 稳定性和续航通常优于双足，工作空间可控 | 不适合楼梯/复杂非结构地面，形态不如人形通用 | 更接近 2026-2028 落地，适合关注数据闭环和客户场景 |
| 协作臂上探具身 | DOBOT、JAKA、AUBO | 3C、汽车、食品、医疗、科研教育 | 真实产线基础、成本/维护可控 | 泛化能力弱，仍以工艺编程和集成为主 | 看视觉/力控/移动平台/数据训练是否产品化 |
| 工业机器人本体 | SIASUN、ESTUN、EFORT | 光伏、锂电、汽车、金属加工、重载搬运 | 成熟市场和财报可验证 | 与“通用具身智能”距离远，价格竞争强 | 更适合供应链和制造自动化视角 |
| AMR/仓储系统 | Geek+、Quicktron、YOUIBOT、SIASUN Mobile | 仓储、厂内物流、巡检、半导体搬运 | ROI 清晰、客户数据多、调度软件壁垒 | 主要是移动和物流，灵巧操作不足 | 看是否从“搬运”升级为“移动操作 + 抓取” |
| 灵巧手/末端执行器 | RobotEra XHAND 1、Unitree Dex3-1、Agibot/ Galaxea 夹爪 | 抓取、装配、数据采集 | 是具身操作的关键瓶颈 | 寿命、触觉、成本和控制难度高 | 看进入多家本体厂 BOM 的能力 |
| 数据/训练平台 | Agibot Genie Studio、Unitree G1-D、LimX FluxVLA、IO-AI EmbodiFlow | 具身模型训练、真机评测、部署 | 平台化和数据闭环决定长期学习速度 | 需要真实机器人和客户任务支撑 | 对软件/AI 工程职业最友好 |

## 优缺点总评

| 公司 | 主要优势 | 主要短板 | 下一步核验 |
|---|---|---|---|
| 优必选 | 上市公司、工业人形订单线索、S2 换电解决续航痛点 | 亏损和订单质量争议，产品参数部分不完整 | 2025 年报、Walker S2 客户验收、复购/维护成本 |
| 宇树 | 价格透明、硬件标准化、开发者生态强 | 商业场景收入结构不清，G1 操作负载有限 | G1/G1 EDU/H1-2 出货、售后、开发者案例 |
| 智元 | 产品矩阵和数据平台完整，AgiBot World/Genie Studio 形成闭环 | 非上市，客户与财务不透明 | A2-W/A2-Max 真实交付、平台开放度、数据质量 |
| 逐际 | 运动控制和工具链定位清晰，FluxVLA 开源信号强 | 更像工具/平台公司，直接场景交付少 | TRON 2 参数、FluxVLA 用户、实际数据/模型效果 |
| 星动纪元 | L7 + XHAND + 物流/制造 PMF 叙事强，融资热度高 | 批量交付和可靠性仍需硬证据 | 顺丰/物流场景合同、千台级交付进度、单机 TCO |
| Galbot/Galaxea | 轮式双臂路线务实，工作空间和续航更适合商业 | 公司名/产品线易混，参数来源需逐项校验 | Galbot G1 和 Galaxea R1 客户、价格、SDK/data license |
| DOBOT | 协作臂全球出货和场景 know-how 强，已扩展人形/四足/数采 | 具身新品商业占比不清 | Atom/Rover/X-Trainer 参数、订单、交付周期 |
| JAKA | 协作臂产品线完整，视觉/力控/移动作业向具身过渡 | 具身产品参数不足 | EI/Kargo/K1/Lumi/S3/EVO 规格和客户案例 |
| AUBO | 协作臂成熟，i 系列参数清晰 | 与具身智能距离较远 | iS/C/高防护系列官方手册和国内客户 |
| SIASUN/ESTUN/EFORT | 工业机器人基本盘和上市公司可验证性 | 更多是传统自动化，估值需防“人形概念”混淆 | 年报拆分机器人收入、毛利、订单周期 |
| Geek+/Quicktron/YOUIBOT | 场景数据和 ROI 更清晰，贴近真实物流/工业落地 | 通用操作能力不足，人形叙事弱 | 移动操作/抓取产品化、客户续约和软件收入 |

## 待补任务

- 为 [[00-source-capture-index|SRC-robotics-135]] 至 [[00-source-capture-index|SRC-robotics-155]] 执行正式 raw capture，更新 `source_capture_manifest.csv`。
- 从产品手册补齐：JAKA Zu/Pro/S/A/Mini 全型号参数，DOBOT CR/CRA/Nova/Atom/Rover/X-Trainer，AUBO i/iS/C 系列，Quicktron/YOUIBOT 型号参数。
- 为优必选、宇树、智元、逐际、星动、Galbot/Galaxea 各建或更新 entity 页，沉淀“产品矩阵 + 技术路线 + 商业化证据 + 待验证问题”。
- 继续维护 [robot_company_product_models_2026-06-08.csv](../../raw/robotics-embodied-ai/data/robot_company_product_models_2026-06-08.csv)，把后续手册抽取出的精确 SKU 参数补进去。

## 关联连接

- [[00-index|机器人与具身智能 - 研究入口]]
- [[04-companies|机器人公司与竞争]]
- [[02-technology-and-products|机器人技术与产品]]
- [[12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]
- [[_concepts/embodied-ai|Embodied AI]]
- [[_concepts/robot-training-data|Robot Training Data]]
