---
title: Microduck 双足机器鸭复刻方案深度拆解
type: source
date_created: 2026-09-02
last_updated: 2026-09-02
source_urls:
  - https://mp.weixin.qq.com/s/vahOiKWnEYOh-PNTxYs5SQ
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-558-microduck.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-559-microduck-official-press-kit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-560-microduck-runtime-official-repository-at-commit-2c61dcc.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-561-microduck-rl-official-repository-at-commit-badc4e7.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-562-dynamixel-xl330-m288-t-e-manual.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-563-dynamixel-xl-series-official-price-page.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-564-radxa-zero-3w-official-product-page.md
evidence_grade: C
tags:
  - source/wechat
  - industry/robotics-embodied-ai
  - microduck
  - reinforcement-learning
  - sim-to-real
  - diy-robot
status: active
aliases:
  - Microduck DIY 复刻文章来源卡
  - 十字透镜 Microduck 拆解
---

# Microduck 双足机器鸭复刻方案深度拆解

> [!summary]
> 文章适合作为 Microduck 的 BOM、供电、控制、结构和 sim-to-real 问题清单，但不适合作为可直接照做的复刻说明。官方资料确认了 `25 cm`、不足 `800 g`、15 个舵机、RK3566、相机、8×8 ToF、两个 IMU、50 Hz 策略循环和 399 美元预售价；关节分配、双 IMU 用途、完整硬件开源、Python/JS SDK、RT 内核必要性、1–2 天调通和成本优势等叙述需要校正或保留为待验证。

## 来源元数据

| 字段 | 内容 |
|---|---|
| 标题 | Microduck 双足机器鸭 — 复刻方案深度拆解 |
| 平台 | 微信公众号 |
| 公众号 / 署名 | 十字透镜 |
| 发布日期 | 待验证；正文自述“分析日期：2026-08-31” |
| 入库日期 | 2026-09-02 |
| 提取方式 | Defuddle Markdown，正文成功捕获 |
| 证据等级 | C：二次拆解与 DIY 估算，没有逐项列出一级来源 |
| 原文 | [微信链接](https://mp.weixin.qq.com/s/vahOiKWnEYOh-PNTxYs5SQ) |
| 原始抽取 | [`SRC-robotics-558`](../../raw/robotics-embodied-ai/documents/SRC-robotics-558-microduck.md) |

## 原文主张地图

- **硬件**：文章给出 15 个 XL330、Radxa ZERO 3W、两个 IMU、VL53L5CX、相机、NFC 与 NP-F550 的推测 BOM，并尝试从结构图恢复关节分配。
- **复刻路线**：提出忠实、混合与极限降本三条路线，把舵机替换、传感器适配和结构打印作为主要工作。
- **软件**：把官方软件描述为 Python/JS SDK、仿真与训练栈，并称兼容硬件可直接刷镜像、1–2 天调通。
- **风险**：把峰值电流、双 IMU 融合、50 Hz 实时性列为 P0，机械精度、ToF 标定和散热列为 P1。
- **结论**：判断忠实复刻约需人民币 3460 元、4–6 周，DIY 成本接近整机但教育价值较高。

## 事实校正

| 主题 | 官方或固定提交证据 | 入库判断 |
|---|---|---|
| 产品状态 | 官方于 2026-08-27 开放 399 美元预售，首批交付目标是 2026 年圣诞节前；规格仍有未定项 | 截至 2026-09-02 仍是预售阶段，不能声称已有普遍“开箱运行”经验 |
| 开源边界 | 官方 press kit 明确只开源软件，机械与电子设计文件不开放 | 不是开源硬件；仿真模型不能替代制造 CAD、PCB、线束、BOM 与装配公差 |
| 关节分配 | runtime 固定提交列出：左腿 5 + 头颈/嘴 5 + 右腿 5；嘴不进入 14 维策略动作 | 原文“双腿各约 6–7、头部 2”不成立；应使用官方 15 关节表 |
| 软件架构 | runtime 是 Rust 多 daemon + Unix socket JSON-RPC；RL 栈是 Python、MuJoCo/mjlab、PPO、ONNX | 原文把 SDK 归为 Python/JS 且链接 `huggingface/lerobot`，与当前官方实现不符 |
| 50 Hz | 官方配置说明 50 Hz 继承自原型，并未在 Radxa 上重新推导；官方仓库记录一次非 RT 内核硬件运行达到 50.0 Hz | 50 Hz 是当前策略循环目标，不是 DYNAMIXEL TTL 的协议“硬约束”；RT-PREEMPT 不是已证明的必要条件 |
| 两个 IMU | 官方仅确认头部和机身各一个 IMU；当前策略观测使用躯干陀螺与重力方向 | “振动补偿、状态融合、失效接管”是原文推断，尚无官方算法或失效切换证据 |
| ToF | 官方只承诺 8×8 ToF；runtime 同时支持 VL53L5CX 与 VL53L8CX | 不能把所有量产机固定写成 VL53L5CX；具体代次需按实机探测 |
| 电池 | 官方写 NP-F550、2600 mAh、约 1 小时；原文写约 2200 mAh | 容量口径冲突，以最终量产清单和实机标签为准 |
| 成本 | ROBOTIS US 2026-09-02 报价为 XL330-M288-T 每个 27.49 美元，15 个合计 412.35 美元 | 单舵机零售价合计已高于 399 美元整机预售价；忠实复刻没有零售 BOM 成本优势 |

## 可取之处

- 把复刻拆成执行器、计算、传感、供电、结构、软件和验证阶段，适合作为工程尽调骨架。
- 提醒不要把廉价 PWM 舵机视为 XL330 的即插即用替代；协议、反馈、尺寸、动力学与训练模型都会改变。
- 把电源压降、关节间隙、传感器外参、热与线束当作 sim-to-real 的系统问题，而不是只讨论策略网络。

## 下游编译

本文按 `R05 产品、平台与工具选型调研` 主分类、`R08 数量/成本与单位经济性` 和 `R04 技术原理与前沿` 次分类，编译为 [[robotics-embodied-ai/research-notes/microduck-diy-replication-feasibility-2026-09-02|Microduck DIY 复刻可行性与教学平台选型]]；产品事实汇总于 [[Microduck]]。

## 商业应用可能性

Microduck 当前最可信的用途是高校课程、实验室 RL/sim-to-real 教学、开发者社区和消费级编程玩具，而不是工业生产或开放家庭劳动。使用者通常是学生、教师、研究者与 maker，付款者是个人、实验室或教育机构；规模采购仍需等首批交付、可靠性、备件、售后和课程效果验证。

## 中小型创业者的机会

- **可立即验证**：中文课程、仿真实验、策略评测、测试夹具、非结构性配件和本地化技术支持。
- **需要条件成熟**：首批交付后开展维修、备件、校准、课程认证和小批量教学套件服务。
- **不建议进入**：依赖官方非商业 3D 模型直接销售克隆硬件，或在缺少机械/电子设计文件时承诺“忠实复刻”。

## 知识冲突

- 原文称结构图/CAD、电路图或 PCB 至少部分开源；官方 press kit 明确说机械和电子设计文件不开放。RL 仓库内的仿真模型采用 `CC BY-SA-NC`，也不能等同于可商业制造的开源硬件资料。
- 原文把 50 Hz 与实时内核列为 P0；官方仓库记录非 RT 内核已达到当前循环目标，但这只是开发方一次硬件记录，不是跨批次 SLA。
- 原文认为忠实复刻与整机成本接近；按官方美国零售价，15 个 XL330 本身已超过整机预售价。中国渠道价与批量采购价仍应重新询价。

## 关联连接

- [[Microduck]]
- [[robotics-embodied-ai/00-index|机器人（具身智能）]]
- [[robotics-embodied-ai/02-technology-and-products|机器人技术与产品]]
- [[robotics-embodied-ai/research-notes/onshape-to-robot-usage-selection-deep-dive-2026-08-10|onshape-to-robot 用法与选型调研]]
- [[embodied-ai|Embodied AI]]
- [[BillOfMaterials|BOM]]
