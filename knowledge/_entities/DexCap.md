---
title: DexCap
type: entity
date_created: 2026-08-09
last_updated: 2026-08-09
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-277-dexcap-scalable-and-portable-mocap-data-collection-system-for-dexterous-manipula.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-502-dexcap-project-page.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-504-dexcap-official-code-repository-at-commit-4b0bed0.md
tags:
  - entity/project
  - industry/robotics-embodied-ai
  - robot-data
status: active
---

# DexCap

DexCap 是 Stanford 团队在 RSS 2024 发表的便携式灵巧手动作采集系统；DexIL 是其人到机器人重定向和点云模仿学习方法。系统组合电磁手套、腕部 SLAM tracking、胸前 RGB-D、fingertip IK、Diffusion Policy 与可选人工纠偏。

## 能力边界

- 强项：抗手指视觉遮挡、自然人类动作吞吐、同步三维环境与手部动作、可不依赖真机采集初始示教。
- 弱项：没有力/触觉；人手与机器人手差异仍造成 contact-rich 失败；原型续航约 40 分钟；2024 原 BOM 与软件栈需要现代化替代。
- 不是：商用数据平台、开箱即用的量产产品、机器人原生物理数据的完整替代品。
- 代码：官方仓库根许可证为 MIT；第三方软件、硬件 SDK、数据与依赖需另审。

## 关联连接

- [[_sources/dexcap-paper-project-code-source-set|DexCap 来源集]]
- [[robotics-embodied-ai/research-notes/dexcap-dexterous-mocap-data-collection-deep-dive-2026-08-09|DexCap 深度调研]]
- [[_concepts/robot-training-data|Robot Training Data]]
- [[_concepts/universal-manipulation-interface|Universal Manipulation Interface]]

