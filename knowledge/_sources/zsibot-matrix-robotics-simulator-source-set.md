---
title: "zsibot/matrix（MATRiX）机器人仿真平台来源集"
type: source
date_created: 2026-07-20
last_updated: 2026-07-20
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-310-matrix-repository-readme-at-audited-commit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-311-matrix-v0-1-2-release-and-package-manifest.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-312-matrix-github-maintenance-and-issue-audit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-313-genisom-ai-official-open-source-catalog.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-314-mujoco-unreal-engine-plugin-upstream-repository.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-315-unreal-robotics-lab-a-high-fidelity-robotics-simulator-with-advanced-physics-and.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-316-2026.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-317-source.md
tags:
  - source/github
  - industry/robotics-embodied-ai
  - simulation
status: active
aliases:
  - MATRiX GitHub 来源摘要
---

# zsibot/matrix（MATRiX）机器人仿真平台来源集

> [!summary]
> 本来源集把 `zsibot/matrix` 的 pinned README、v0.1.2 Release、GitHub API/issue/PR/tag 快照、公司开源目录、上游插件、同类论文和政策来源编译为可审计证据。结论见 [[robotics-embodied-ai/research-notes/zsibot-matrix-robotics-simulator-deep-dive-2026-07-20|MATRiX 深度调研]]。

## 提取方式

- README：按主分支审阅提交 `918fae3` 直接下载 Markdown。
- Release、官网、上游仓库、论文和政策：Defuddle 清洗为 Markdown。
- GitHub 维护元数据：API 查询后人工整理为结构化快照；原始 endpoint 保留在 source artifact。
- 代码：克隆公开仓库后做静态文件、脚本、文档、版本和路径审阅；未运行完整 Ubuntu/ROS/GPU 发行包。

## 核心来源

| SRC | 内容 | 证据等级 | 关键用途 |
|---|---|---|---|
| [`SRC-robotics-310`](../../raw/robotics-embodied-ai/documents/SRC-robotics-310-matrix-repository-readme-at-audited-commit.md) | pinned README | S | 产品定位、安装、系统要求、功能目录。 |
| [`SRC-robotics-311`](../../raw/robotics-embodied-ai/documents/SRC-robotics-311-matrix-v0-1-2-release-and-package-manifest.md) | v0.1.2 Release | S | 版本新增、运行包、地图与 bug fixes。 |
| [`SRC-robotics-312`](../../raw/robotics-embodied-ai/documents/SRC-robotics-312-matrix-github-maintenance-and-issue-audit.md) | GitHub API/issue/PR/tag 审计 | S/B | stars、forks、提交、下载、问题、版本异常和代码边界。 |
| [`SRC-robotics-313`](../../raw/robotics-embodied-ai/documents/SRC-robotics-313-genisom-ai-official-open-source-catalog.md) | GENISOM 官网 | A | MATRiX 在硬件、导航、VLN 和 SDK 生态中的位置。 |
| [`SRC-robotics-314`](../../raw/robotics-embodied-ai/documents/SRC-robotics-314-mujoco-unreal-engine-plugin-upstream-repository.md) | 被致谢的上游 PoC | S | 技术来源与许可证尽调。 |
| [`SRC-robotics-315`](../../raw/robotics-embodied-ai/documents/SRC-robotics-315-unreal-robotics-lab-a-high-fidelity-robotics-simulator-with-advanced-physics-and.md) | Unreal Robotics Lab 论文 | S | 同类路线、benchmark 与“全球首个”反证。 |
| [`SRC-robotics-316`](../../raw/robotics-embodied-ai/documents/SRC-robotics-316-2026.md) | 2026 实景实训专项行动 | S | 商业验收与政策位置。 |
| [`SRC-robotics-317`](../../raw/robotics-embodied-ai/documents/SRC-robotics-317-source.md) | 训练平台国家标准计划 | S | 标准化窗口和合规方向。 |

## 关键边界

- GitHub 下载数不等于活跃用户、安装成功或付费客户。
- issue 是真实用户信号，但不是可控实验。
- 公司官网是官方自述，不是第三方性能证明。
- 未下载完整运行包，因此不声称运行、性能、传感器精度或 sim-to-real 已复现。

## 关联连接

- [[MATRiXSimulator|MATRiX Simulator]]
- [[robotics-embodied-ai/research-notes/zsibot-matrix-robotics-simulator-deep-dive-2026-07-20|MATRiX 深度调研]]
- [[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]]
- [[robotics-embodied-ai/00-index|机器人（具身智能）研究入口]]
