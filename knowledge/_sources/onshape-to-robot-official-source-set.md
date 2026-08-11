---
title: onshape-to-robot 官方仓库、文档、示例与问题来源集
type: source
date_created: 2026-08-10
last_updated: 2026-08-10
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-516-onshape-to-robot-official-repository-at-commit-7d0803d.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-517-onshape-to-robot-getting-started-documentation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-518-onshape-to-robot-design-time-conventions.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-519-onshape-to-robot-config-documentation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-520-onshape-to-robot-urdf-exporter-documentation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-521-onshape-to-robot-sdf-exporter-documentation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-522-onshape-to-robot-mujoco-exporter-documentation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-523-onshape-to-robot-processors-documentation.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-524-onshape-to-robot-examples-repository-at-commit-7e40fd6.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-525-onshape-to-robot-pypi-package.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-526-onshape-to-robot-issue-170-onshape-api-rate-limit.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-527-onshape-to-robot-issue-76-dof-in-nested-subassemblies.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-528-onshape-to-robot-issue-206-retrieve-convert-config-behavior.md
tags:
  - source/github
  - source/documentation
  - industry/robotics-embodied-ai
  - cad-to-robot
status: active
---

# onshape-to-robot 官方仓库、文档、示例与问题来源集

> [!summary]
> 本来源集以官方仓库固定提交 `7d0803db16c99efa0bd59482f2dc81f9558aa7ba`、官方文档、官方示例固定提交 `7e40fd653205caa2f195d453fa495d9ef5179202` 和具体 GitHub issue 为证据，区分“工具明确支持的工作流”“源码实际行为”和“尚未由维护者确认的用户问题”。综合结论见 [[robotics-embodied-ai/research-notes/onshape-to-robot-usage-selection-deep-dive-2026-08-10|onshape-to-robot 用法与选型调研]]。

## 核心来源

| SRC | 等级 | 用途 | 边界 |
|---|---:|---|---|
| [`SRC-robotics-516`](../../raw/robotics-embodied-ai/documents/SRC-robotics-516-onshape-to-robot-official-repository-at-commit-7d0803d.md) | S | 代码边界、三类 exporter、CLI、处理器、MIT 许可证 | raw 文件保存 README；实现判断另以同一 commit 的源码路径核对 |
| [`SRC-robotics-517`](../../raw/robotics-embodied-ai/documents/SRC-robotics-517-onshape-to-robot-getting-started-documentation.md) | S | 安装、认证、最小配置、导出与 smoke test | latest 文档跟随 master，可能领先 PyPI |
| [`SRC-robotics-518`](../../raw/robotics-embodied-ai/documents/SRC-robotics-518-onshape-to-robot-design-time-conventions.md) | S | Onshape 装配、link、DoF、frame、闭环和多根节点约定 | 设计约定不等于任意 CAD 可无修改导出 |
| [`SRC-robotics-519`](../../raw/robotics-embodied-ai/documents/SRC-robotics-519-onshape-to-robot-config-documentation.md) | S | 全局 `config.json` 参数 | 当前页一处漏列 `sdf`，已用源码纠正 |
| [`SRC-robotics-520`](../../raw/robotics-embodied-ai/documents/SRC-robotics-520-onshape-to-robot-urdf-exporter-documentation.md) | S | URDF 专用参数 | 不含 ros2_control、SRDF、传动和真机标定 |
| [`SRC-robotics-521`](../../raw/robotics-embodied-ai/documents/SRC-robotics-521-onshape-to-robot-sdf-exporter-documentation.md) | S | SDF、`model.config`、geometry override | master 有晚于 v1.8.2 的 SDF 修复，须做版本化 PoC |
| [`SRC-robotics-522`](../../raw/robotics-embodied-ai/documents/SRC-robotics-522-onshape-to-robot-mujoco-exporter-documentation.md) | S | MuJoCo actuator、site、equality 和 scene | 默认执行器、接触参数不是实机辨识结果 |
| [`SRC-robotics-523`](../../raw/robotics-embodied-ai/documents/SRC-robotics-523-onshape-to-robot-processors-documentation.md) | S | retrieve → processors → exporter 架构 | `robot.pkl` 只应在可信工作区使用 |
| [`SRC-robotics-524`](../../raw/robotics-embodied-ai/documents/SRC-robotics-524-onshape-to-robot-examples-repository-at-commit-7e40fd6.md) | S | 两轮车、机械臂、四足、人形、闭环、环境示例 | 示例不是通用兼容矩阵；重导出需拥有对应 Onshape 文档权限 |
| [`SRC-robotics-525`](../../raw/robotics-embodied-ai/documents/SRC-robotics-525-onshape-to-robot-pypi-package.md) | S | PyPI v1.8.2 元数据 | Defuddle 超时，已保留原 HTML；版本/依赖另由 PyPI JSON 与固定 `pyproject.toml` 交叉核验 |

## 风险线索

| SRC | 等级 | 线索 | 使用方式 |
|---|---:|---|---|
| [`SRC-robotics-526`](../../raw/robotics-embodied-ai/documents/SRC-robotics-526-onshape-to-robot-issue-170-onshape-api-rate-limit.md) | B | 约 1000 parts 用户模型遭遇 HTTP 429 | 作为大装配拆分、版本缓存和请求预算 PoC 的触发条件，不外推为固定阈值 |
| [`SRC-robotics-527`](../../raw/robotics-embodied-ai/documents/SRC-robotics-527-onshape-to-robot-issue-76-dof-in-nested-subassemblies.md) | B | 重复嵌套子装配 DoF 未被识别 | 在采购/迁移前用真实嵌套结构回归测试 |
| [`SRC-robotics-528`](../../raw/robotics-embodied-ai/documents/SRC-robotics-528-onshape-to-robot-issue-206-retrieve-convert-config-behavior.md) | B | 修改 `joint_properties` 后复用 `robot.pkl` 未生效 | 当前 workaround 是重新 retrieve；等待维护者确认根因与修复 |

## 审阅快照

- 审阅时间：2026-08-10（Asia/Shanghai）。
- PyPI 最新稳定版：`1.8.2`，发布于 2026-03-27；Python 要求 `>=3.9`。
- 默认分支固定提交：`7d0803d`，提交于 2026-06-19；相对 `v1.8.2` 多出一次合并，改动包括 OAuth 文档、gear relation 空值保护和 SDF pose 格式修复。
- 仓库未归档，许可证为 MIT。GitHub 动态计数只能表示关注度和维护表面信号，不能代表工业验证或支持 SLA。
- 固定提交源码可通过 Python `compileall`；本轮没有 Onshape 密钥，因此未执行真实 API 导出，也没有把静态检查写成端到端复现。
- 固定提交树中未发现测试目录或 pytest/tox/nox 配置；GitHub Actions 仅见发布构建流程。应以目标装配回归测试补足上游自动化验证缺口。

## 关联连接

- [[robotics-embodied-ai/research-notes/onshape-to-robot-usage-selection-deep-dive-2026-08-10|onshape-to-robot 用法与选型调研]]
- [[robotics-embodied-ai/research-notes/3d-simulation-asset-production-pipelines-comparison-2026-08-06|3D 仿真资产生产管线]]
- [[robotics-embodied-ai/research-notes/isaac-sim-vs-gazebo-vs-mujoco-2026-07-14|机器人仿真平台选型]]
- [[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]]
