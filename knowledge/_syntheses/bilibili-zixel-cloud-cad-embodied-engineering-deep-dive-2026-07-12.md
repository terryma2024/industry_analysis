---
title: 子虔科技云原生 CAD 与具身工程闭环视频深度调研
type: synthesis
date_created: 2026-07-12
last_updated: 2026-07-12
sources:
  - knowledge/_sources/bilibili-bv1sbtx6keh5-al-for-engineering.md
  - raw/_inbox/transcripts/2026-07-12-bilibili-bv1sbtx6keh5-al-for-engineering.json
  - https://www.zcad.ai/helpcenter/launchpad
  - https://www.zixel3d.com/news/Zixel-zcad-yangtze-delta-launch
  - https://file.finance.sina.com.cn/211.154.219.97%3A9494/MRGG/CNSESH_STOCK/2025/2025-10/2025-10-10/11498213.PDF
tags: [bilibili, industrial-software, cloud-cad, robotics, embodied-ai]
status: active
---

# 子虔科技云原生 CAD 与具身工程闭环视频深度调研

> [!summary]
> 视频将子虔科技（ZIXEL）的云原生 3D CAD/PDM 描述为具身机器人“设计—仿真—训练—部署”闭环的数据底座。公司官网证实其产品组合包含 3D CAD、Viewer、Process Master、PDM 和几何搜索；公开上市公司公告证实浩辰软件与其签署 3D CAD 战略/OEM 框架。视频中的性能数字、客户数量和“国内领先”定位仍仅为 B 级陈述。

## 来源与视频主线

| 项目 | 内容 |
|---|---|
| 视频 | [子虔科技 AI For Engineering 具身智能机器人一体化设计平台](https://www.bilibili.com/video/BV1sBTX6kEH5) |
| 作者 / 文本 | 摩尔线程开发者；Volcengine ASR 原文见 `raw/_inbox/transcripts/2026-07-12-bilibili-bv1sbtx6keh5-al-for-engineering.json` |
| 关键一手来源 | [ZIXEL 工作台说明](https://www.zcad.ai/helpcenter/launchpad)、[子虔 2026 联合体公告](https://www.zixel3d.com/news/Zixel-zcad-yangtze-delta-launch)、[浩辰软件 OEM 合作公告](https://file.finance.sina.com.cn/211.154.219.97%3A9494/MRGG/CNSESH_STOCK/2025/2025-10/2025-10-10/11498213.PDF) |

视频提出：机器人不是单个模型，而涉及结构设计、感知/控制、训练、验证和制造；CAD 图文档应成为几何、约束、版本、BOM 和工艺信息的单一事实来源，再向云端批量仿真、训练和部署反馈闭环提供一致输入。该主张与产品定位相符，但“同一份设计文档即可消除信息丢失”的效果尚需看实际数据 schema、接口和客户项目验证。

## 事实、估计、判断与假设

| 类型 | 内容 | 证据边界 |
|---|---|---|
| 事实（公司官网） | ZIXEL 将 3D CAD、3D Viewer、3D Process Master、PDM、几何搜索和 3D Training 组织为云原生工程协作平台，并明确覆盖机器人与工业自动化。 | 一手产品材料 |
| 事实（上市公司公告） | 浩辰软件披露与上海子虔科技签订战略合作及 OEM 框架，涉及以 ZIXEL 3D CAD 为代表的制造业通用型 3D CAD；公告同时说明具体规模和业绩影响仍不确定。 | 交易所披露级公开公告 |
| 视频线索 | 云端 CAD/PDM 可统一图文档、BOM、版本/变更、委外协作、AI 搜索和 GPU/集群资源。 | B 级；功能范围需试用/合同核验 |
| 视频线索 | “3000+ 特征”“1500+ 特征两分钟更新”“0.01 纳米精度”等具体指标。 | 未找到对应测试协议；不得作选型依据 |
| 判断 | 对具身工程最关键的不是 CAD 是否上云，而是可追溯的设计版本能否映射到 URDF/网格、物理参数、传感器标定、仿真场景、BOM/供应商和真机测试结果。 | 工程判断 |
| 假设 | 统一数据底座可显著缩短机器人迭代周期。 | 需用 ECR 周期、仿真返工率、版本错配率、试制次数验证 |

## 产业、投资与职业启发

- 对中国具身智能：工业软件是“物理世界数据基础设施”的前端。若 CAD/PDM 能与机器人模型、仿真/训练数据和质量体系打通，价值在于降低设计—制造—验证之间的版本错配，而非仅提供可视化建模。
- 对投资：重点验收 API/导出格式、数据主权/权限、私有化部署、与 PLM/MES/ERP/仿真器的接口，以及实际工程变更闭环；上市公司合作框架不是收入或客户规模的证明。
- 对职业：机械/机器人平台工程师应掌握参数化 CAD、BOM/PDM、坐标系和资产版本控制，并能把设计变更连接到 URDF、仿真场景和测试报告。

## 风险与后续验证

1. 让供应商按指定机器人总成演示：CAD 改动如何自动追踪到装配、URDF/网格、仿真模型、BOM、工艺和回归测试。
2. 对性能数字要求给出硬件配置、模型规模、并发数和测试脚本；“云端/GPU 加速”不等于所有环节都线性提速。
3. 核验多组织协作的权限隔离、IP 水印/审计、离线备份和供应商退出时的数据可迁移性。

## 关联连接

- [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]
- [[robotics-embodied-ai/02-technology-and-products|机器人技术与产品]]
- [[ai/02-technology-and-products|AI 技术与产品]]
- [[integrated-circuits/00-index|集成电路]]
