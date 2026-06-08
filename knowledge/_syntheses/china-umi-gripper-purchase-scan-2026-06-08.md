---
title: 中国可购买 UMI 夹爪设备检索
type: synthesis
date_created: 2026-06-08
last_updated: 2026-06-08
sources:
  - knowledge/robotics-embodied-ai/sources.csv
  - SRC-robotics-065
  - SRC-robotics-067
  - SRC-robotics-127
  - SRC-robotics-128
  - SRC-robotics-129
  - SRC-robotics-130
  - SRC-robotics-131
  - SRC-robotics-132
  - SRC-robotics-133
  - SRC-robotics-134
tags:
  - industry/robotics-embodied-ai
  - embodied-ai
  - umi
  - robot-training-data
  - procurement
status: active
---

# 中国可购买 UMI 夹爪设备检索

## 结论

截至 2026-06-08，可核实的结论是：在中国大陆供应链中，**最明确可直接下单或预订的 UMI-like 夹爪/数采设备是鹿明 LUMOS FastUMI 系列**；**觅蜂科技 MEgo Gripper 已宣布首批量产发货，但暂未检索到公开价格或电商下单页**；原版 [[_entities/UniversalManipulationInterface|Universal Manipulation Interface]] 是开源硬件和软件方案，不是官方成品 SKU。

## 设备清单

| 设备 | 购买状态 | 价格线索 | 关键事实 | 证据 |
|---|---:|---:|---|---|
| LUMOS FastUMI Pro | AIFITLAB 可下单/预订；具体配置显示 backordered | AIFITLAB 分类页显示 From USD 1,530；商品页单手便携配置显示 USD 19,200 | 更接近“UMI 夹爪”成品路线；约 600g；1-3 mm 定位精度；含鱼眼 RGB、深度、IMU、6DoF 轨迹等数据模态 | `SRC-robotics-127`、`SRC-robotics-128` |
| LUMOS FastUMI Go | AIFITLAB 可下单/预订；显示 backordered | USD 33,000 | 背包式双手 UMI 数采设备，含左右两套传感/夹爪单元、移动工作站、电源和背包 | `SRC-robotics-127`、`SRC-robotics-129` |
| LUMOS FastUMI Ego | AIFITLAB 可下单/预订；显示 backordered | USD 6,300 | 第一人称无本体采集设备，不是夹爪本体，但属于同一 UMI 数采产品线 | `SRC-robotics-127`、`SRC-robotics-130` |
| 觅蜂科技 MEgo Gripper | 已宣布 MEgo 系列首批量产发货；未找到公开下单页 | 未公开 | 无线 UMI 设备，机身 480g，可实现 1 mm 轨迹重建，支持户外自由场景数据采集 | `SRC-robotics-131`、`SRC-robotics-132` |
| BeingBeyond U1 / RealDexUMI | 已发布；未找到公开购买页 | 未公开 | 更偏灵巧手 UMI，而非二指夹爪。方案强调采集端与机器人末端执行器一致性、触觉和灵巧操作数据 | `SRC-robotics-133`、`SRC-robotics-134` |

## 购买优先级

1. **要马上买成品并开始实验**：优先联系鹿明或通过 AIFITLAB 订购 LUMOS FastUMI Pro。理由是它目前有公开商品页、价格、配置和下单入口，且产品形态最贴近 UMI 夹爪。
2. **要做数据工厂或双手任务**：看 LUMOS FastUMI Go，但要确认 backorder 周期、国内含税报价、SDK 权限、数据格式和售后。
3. **要接智元生态或 G2 Air 路线**：联系觅蜂科技询价 MEgo Gripper。公开报道显示已量产发货，但采购更像 B2B 商务流程。
4. **要研究灵巧手数据路线**：跟踪 BeingBeyond U1 / RealDexUMI。它可能代表 UMI 从夹爪向灵巧手迁移，但当前采购可得性不足。
5. **要低成本复现原版 UMI**：使用 Stanford UMI 开源硬件指南和 GitHub 仓库自建，国内可采购 GoPro、3D 打印件、传感器和夹爪零件，但这不是“直接购买成品”。

## 事实、判断与待验证

### 事实

- UMI 官方项目页将其定义为使用手持夹爪收集人类演示、再迁移到机器人策略的框架；硬件设计为手持平行夹爪并安装腕部 GoPro。`SRC-robotics-065`
- UMI GitHub 仓库提供安装、硬件指南、数据采集、SLAM、训练和真实部署说明，说明原版路线可自建。`SRC-robotics-067`
- AIFITLAB 的 UMI Gripper 分类页列出 LUMOS FastUMI Pro、Ego、Go 三个商品，并显示 in stock、价格和下单入口。`SRC-robotics-127`
- LUMOS FastUMI Pro 商品页披露配置、价格、backordered 状态、从中国发货、1-3 mm 定位精度、约 600g 等信息。`SRC-robotics-128`
- 鹿明在 AWE2026 发布 FastUMI 无本体数采产品“全家桶”，并宣布相关产品将陆续上线京东。`SRC-robotics-132`
- 觅蜂科技 MEgo 系列在 2026-05-26 宣布首批量产发货；MEgo Gripper 被描述为无线 UMI 设备。`SRC-robotics-131`

### 判断

- “可直接购买”的定义如果严格限定为国内电商现货，当前证据仍不足；如果接受国际站下单、从中国发货、B2B 预订，则 LUMOS FastUMI 系列最接近可买成品。
- LUMOS FastUMI Pro 适合快速进入 UMI-like 数据采集实验；MEgo Gripper 更像生态绑定较强的数据采集终端，可能需要厂商商务沟通和配套数据平台。
- BeingBeyond U1 / RealDexUMI 不是“夹爪”替代品，而是灵巧手数据采集范式，适合纳入下一代 UMI 设备观察池。

### 待验证

- 京东是否已经上线鹿明 FastUMI 系列的正式商品链接、售价和交付周期。
- AIFITLAB 对中国大陆地址是否提供本地发货、人民币报价、发票、售后和 SDK 授权。
- MEgo Gripper 是否对外销售单机硬件，还是只随数据服务项目交付。
- FastUMI Pro 的开箱内容、SDK license、数据格式、与 [[_entities/HuggingFaceLeRobot|LeRobot]] / Zarr / ROS 的兼容情况。
- 设备是否允许商业数据采集与再销售，尤其是采集隐私、场景授权和下游模型训练权利。

## 采购问询清单

- 是否可单独购买硬件，还是必须购买数据平台或服务包。
- 单手/双手配置、夹爪类型、触觉模块、头戴/背包模块分别多少钱。
- 交付周期、保修、国内发票、备件、二次开发支持。
- SDK 是否开放；是否支持导出 LeRobot、Zarr、HDF5、ROS bag 或 MCAP。
- 采集数据是否包含 RGB、深度、IMU、6DoF pose、夹爪开合、触觉/力觉和时间同步信息。
- 是否提供机器人端部署套件；支持 UR、Franka、xArm、Flexiv、智元、宇树等哪些平台。
- 商业使用、众包采集、隐私合规和数据再销售限制。

## 关联连接

- [[index|Knowledge Index]]
- [[robotics-embodied-ai/00-index|机器人（具身智能） - 研究入口]]
- [[robotics-embodied-ai/08-umi-gripper-research-and-business-plan|UMI Gripper 研究与业务计划]]
- [[robotics-embodied-ai/09-training-data-deep-dive|机器人训练数据深度调研]]
- [[_concepts/universal-manipulation-interface|Universal Manipulation Interface]]
- [[_concepts/robot-training-data|Robot Training Data]]
- [[_entities/UniversalManipulationInterface|Universal Manipulation Interface]]
- [[_entities/HuggingFaceLeRobot|Hugging Face LeRobot]]
