---
title: 机器人（具身智能） - 产业链地图
date: 2026-04-28
tags:
  - industry/robotics-embodied-ai
  - industry-map
aliases:
  - 具身智能产业链
  - 人形机器人产业链
---

# 机器人（具身智能） - 产业链地图

## 行业边界

具身智能是让 AI 系统通过机器人本体感知、决策并作用于真实物理世界的产业方向。它和传统机器人产业高度重叠，但核心差异在于：传统机器人更多依赖预编程、固定工位和确定性任务，具身智能强调多模态感知、泛化决策、数据闭环和跨场景任务执行。

本研究将行业边界定义为：

- 包含：人形机器人、轮式双臂机器人、协作机器人、AMR/移动操作机器人、四足/特种机器人、工业机器人、核心零部件、感知传感、运动控制、仿真训练、具身大模型和场景解决方案。
- 不包含：纯消费电子玩具、仅软件聊天机器人、与机器人无明确关联的通用大模型应用。
- 邻近行业：AI 大模型、工业自动化、智能制造、低空经济、汽车零部件、传感器、半导体、云计算和边缘计算。

## 产业链总览

| 环节 | 核心价值 | 代表公司/机构 | 关键壁垒 | 证据 |
|---|---|---|---|---|
| 上游机械与执行 | 决定成本、寿命、精度和负载能力 | 绿的谐波、双环传动、中大力德、步科股份、鸣志电器、秦川机床、贝斯特、五洲新春 | 精密加工、良率、批量一致性、客户验证周期 | [`SRC-robotics-034`](../../raw/robotics-embodied-ai/documents/SRC-robotics-034-2025-121-42.md) [`SRC-robotics-036`](../../raw/robotics-embodied-ai/documents/SRC-robotics-036-2025.md) |
| 上游感知与传感 | 让机器人获得空间、力觉、触觉和环境信息 | 奥比中光、柯力传感、东华测试、汉威科技、速腾聚创、禾赛科技、舜宇光学 | 传感精度、稳定性、算法融合、成本下降 | [`SRC-robotics-037`](../../raw/robotics-embodied-ai/documents/SRC-robotics-037-2026.md) [`SRC-robotics-038`](../../raw/robotics-embodied-ai/documents/SRC-robotics-038-2025-6-85-1-73.md) [`SRC-robotics-039`](../../raw/robotics-embodied-ai/documents/SRC-robotics-039-source.md) |
| 上游控制与算力 | 运动控制、伺服驱动、边缘计算和开发平台 | 汇川技术、固高科技、NVIDIA、华为昇腾、地平线、黑芝麻智能 | 实时控制、可靠性、生态工具链、软硬协同 | [[00-source-capture-index|SRC-robotics-017]] [`SRC-robotics-018`](../../raw/robotics-embodied-ai/documents/SRC-robotics-018-nvidia-isaac-gr00t-developer-page.md) [`SRC-robotics-040`](../../raw/robotics-embodied-ai/documents/SRC-robotics-040-2026-12-98-23-39.md) [`SRC-robotics-041`](../../raw/robotics-embodied-ai/documents/SRC-robotics-041-2025.md) |
| 中游整机 | 将软硬件集成为可交付机器人 | 优必选、宇树、智元、逐际、星动、银河、自变量、魔法原子、越疆、节卡、新松、埃斯顿、埃夫特 | 系统工程、供应链、成本、数据闭环、场景交付 | [`SRC-robotics-009`](../../raw/robotics-embodied-ai/documents/SRC-robotics-009-ubtech-robotics-hkex-issuer-announcements-page.md) [`SRC-robotics-012`](../../raw/robotics-embodied-ai/documents/SRC-robotics-012-unitree-g1-humanoid-robot-product-page.md) [`SRC-robotics-015`](../../raw/robotics-embodied-ai/documents/SRC-robotics-015-agibot-a2-product-page.md) [`SRC-robotics-020`](../../raw/robotics-embodied-ai/documents/SRC-robotics-020-limx-dynamics-official-website.md) |
| 中游软件与数据 | 训练、仿真、调度、运维、远程遥操作、任务编排 | NVIDIA Isaac/GR00T、智元、宇树 G1-D、优艾智合、极智嘉、快仓 | 数据获取、仿真到现实、评测体系、云边协同 | [`SRC-robotics-014`](../../raw/robotics-embodied-ai/documents/SRC-robotics-014-unitree-g1-d-end-to-end-platform-for-humanoid-robot.md) [[00-source-capture-index|SRC-robotics-017]] [`SRC-robotics-018`](../../raw/robotics-embodied-ai/documents/SRC-robotics-018-nvidia-isaac-gr00t-developer-page.md) [`SRC-robotics-031`](../../raw/robotics-embodied-ai/documents/SRC-robotics-031-youibot-official-website.md) |
| 下游应用 | 为机器人付费并提供真实数据 | 汽车、3C、新能源、半导体、仓储物流、能源巡检、医疗养老、商业服务 | ROI、可靠性、安全责任、集成成本、售后体系 | [`SRC-robotics-003`](../../raw/robotics-embodied-ai/documents/SRC-robotics-003-source.md) [`SRC-robotics-029`](../../raw/robotics-embodied-ai/documents/SRC-robotics-029-geek-company-page.md) [`SRC-robotics-030`](../../raw/robotics-embodied-ai/documents/SRC-robotics-030-quicktron-official-website.md) |

## 价值流

- 谁付钱：
  - 近期：工业制造、仓储物流、科研教育、政府示范、特种作业客户。
  - 中期：商业服务、医疗康养、公共服务、能源巡检。
  - 远期：家庭服务和个人消费。
- 谁获益：
  - 早期更确定：核心零部件、传感/视觉、运动控制、工业/仓储解决方案。
  - 高弹性但高风险：人形整机厂、具身大模型和数据平台。
  - 稳定但弹性较低：传统工业机器人、自动化系统集成商。
- 成本主要在哪里：
  - 硬件：关节执行器、减速器、电机、丝杠、传感器、计算单元、电池、结构件。
  - 软件：数据采集、标注、仿真、模型训练、控制算法、云端调度、现场部署。
  - 交付：客户工位改造、集成调试、运维、售后和安全责任。
- 利润池集中在哪里：
  - 当前：具备技术壁垒和批量供货能力的核心零部件。
  - 商业化放量期：整机厂和场景解决方案公司。
  - 长期：数据闭环、仿真平台、机器人操作系统和生态工具链。

## 关键瓶颈

| 瓶颈 | 说明 | 影响 |
|---|---|---|
| 供给瓶颈 | 高精密减速器、丝杠、空心杯/无框电机、六维力传感器、灵巧手仍需验证批量一致性。 | 决定成本下降和规模交付。 |
| 技术瓶颈 | 长周期任务泛化、复杂环境稳定性、灵巧操作、仿真到现实迁移仍未完全解决。 | 决定能否从 demo 走向真实替代。 |
| 数据瓶颈 | 真实机器人数据昂贵且稀缺，场景差异大。 | 决定具身大模型迭代速度。 |
| 商业化瓶颈 | 客户更关心 ROI、稳定工作时长、维护成本和安全责任。 | 决定订单是否复购。 |
| 监管瓶颈 | 人机协同、安全认证、数据合规、责任划分仍在完善。 | 决定公共和家庭场景开放速度。 |
| 渠道瓶颈 | 工业客户需要现场交付能力，服务机器人需要售后网络。 | 决定整机厂能否规模化。 |
| 人才瓶颈 | 机器人需要机械、控制、AI、软件、供应链、现场工程复合团队。 | 决定公司组织效率和交付质量。 |

## 投资含义

产业链越上游，短期确定性越高，但弹性可能受估值约束；越靠近整机和应用，弹性越大，但商业化和现金流不确定性更高。第一阶段投资研究应优先跟踪“多客户复用 + 财务可验证 + 机器人收入占比上升”的公司，详见 [[05-investment-view]] 和 [[05a-portfolio-draft-2026-04-28]]。
