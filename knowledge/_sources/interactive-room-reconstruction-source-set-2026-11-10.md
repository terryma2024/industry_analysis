---
title: 可交互房间Sim重建来源集
type: source
date_created: 2026-11-10
last_updated: 2026-11-10
sources:
  - knowledge/robotics-embodied-ai/sources.csv
  - raw/robotics-embodied-ai/data/interactive-scene-reconstruction-provenance-2026-11-10.json
tags: [real2sim, interactive-scene, sources]
status: active
---

# 可交互房间重建来源集

范围只含场景、对象、物理与交互，不含策略训练或真机部署。以下是静态资料与局部源码证据，不代表在用户机器可运行。

| 编号 | 来源 | 归档 |
|---|---|---|
| SRC-robotics-742 | insait-institute/PhiRIE interactive reconstruction fixed README | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-742-insait-institute-phirie-interactive-reconstruction-fixed-readme.md) |
| SRC-robotics-743 | RunyiYang/PhysicalView interactive reconstruction fixed README | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-743-runyiyang-physicalview-interactive-reconstruction-fixed-readme.md) |
| SRC-robotics-744 | discoverse-dev/DISCOVERSE interactive reconstruction fixed README | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-744-discoverse-dev-discoverse-interactive-reconstruction-fixed-readme.md) |
| SRC-robotics-745 | discoverse-dev/DISCOVERSE-Real2Sim interactive reconstruction fixed README | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-745-discoverse-dev-discoverse-real2sim-interactive-reconstruction-fixed-readme.md) |
| SRC-robotics-746 | real-to-sim-to-real/RialToGUI interactive reconstruction fixed README | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-746-real-to-sim-to-real-rialtogui-interactive-reconstruction-fixed-readme.md) |
| SRC-robotics-747 | NVlabs/SimFoundry interactive reconstruction fixed README | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-747-nvlabs-simfoundry-interactive-reconstruction-fixed-readme.md) |
| SRC-robotics-748 | robosimstudio/robosimstudio interactive reconstruction fixed README | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-748-robosimstudio-robosimstudio-interactive-reconstruction-fixed-readme.md) |
| SRC-robotics-749 | InternRobotics/Re3Sim interactive reconstruction fixed README | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-749-internrobotics-re3sim-interactive-reconstruction-fixed-readme.md) |
| SRC-robotics-750 | PhiRIE interactive viewer dependencies | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-750-phirie-interactive-viewer-dependencies.md) |
| SRC-robotics-751 | PhiRIE phone video reconstruction entrypoint | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-751-phirie-phone-video-reconstruction-entrypoint.md) |
| SRC-robotics-752 | SimFoundry install and external service boundaries | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-752-simfoundry-install-path-failure-note.md)（404失败记录） |
| SRC-robotics-753 | PhiRIE data metric geometry and model inputs | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-753-phirie-data-metric-geometry-and-model-inputs.md) |
| SRC-robotics-754 | DISCOVERSE simulation and Gaussian state synchronization | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-754-discoverse-simulation-and-gaussian-state-synchronization.md) |
| SRC-robotics-755 | RoboSimStudio software dependencies | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-755-robosimstudio-software-dependencies.md) |
| SRC-robotics-756 | Interactive scene fixed license and dependency static review | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-756-interactive-scene-static-review.md) |
| SRC-robotics-757 | SimFoundry fixed third party license boundaries | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-757-simfoundry-fixed-third-party-license-boundaries.md) |

## 许可与缺口

- PhiRIE／PhiView MIT核心不等于PhiRoom兼容后台已能公开取得，750明确记录独立访问要求，当前公开树替代后台未验证。
- DISCOVERSE运行时MIT与Real2Sim工具／Gaussian依赖分开；没有用运行时许可外推所有仓库。
- SimFoundry默认Gemini和多项gated／自定义许可组件见747／757；752指向INSTALL.md但固定路径404，保留失败，不伪补成功。
- Re3Sim README为CC BY-NC 4.0；RialToGUI根许可未见明确覆盖。
- 14次自动来源抓取中：10项ok、3项纯文本fallback_html、1项failed；756静态包ok，757替代许可资料ok，总计12项ok／3项fallback／1项failed。
- 无模型推理、GPU兼容性、全房采集、模拟器交互或实时性能验收。

## 关联连接

- [[robotics-embodied-ai/research-notes/interactive-room-sim-reconstruction-alternatives-2026-11-10|场景优先报告]]
- [[robotics-embodied-ai/research-notes/so101-open-source-room-reconstruction-training-alternatives-2026-11-10|前轮广范围报告]]
