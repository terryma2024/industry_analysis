---
title: 门与抽屉可交互重建代码核查来源集
type: source
date_created: 2026-11-10
last_updated: 2026-11-10
sources:
  - knowledge/robotics-embodied-ai/sources.csv
  - raw/robotics-embodied-ai/data/door-drawer-code-audit-provenance-2026-11-10.json
tags: [interactive-scene, articulation, code-audit, sources]
status: active
---

# 门与抽屉代码核查来源集

R05/R04/R06。仅场景重建、物理与交互，不含策略训练或真机部署。

## 本轮来源

| 编号 | 内容 | 归档 |
|---|---|---|
| SRC-robotics-758 | DISCOVERSE door drawer original MJCF | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-758-discoverse-door-drawer-original-mjcf.md) |
| SRC-robotics-759 | DISCOVERSE cabinet door example source | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-759-discoverse-cabinet-door-example-source.md) |
| SRC-robotics-760 | DISCOVERSE drawer example source | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-760-discoverse-drawer-example-source.md) |
| SRC-robotics-761 | GaussianRenderer MuJoCo body pose bridge | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-761-gaussianrenderer-mujoco-body-pose-bridge.md) |
| SRC-robotics-762 | GaussianRenderer 0.2 dependency manifest | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-762-gaussianrenderer-0-2-dependency-manifest.md) |
| SRC-robotics-763 | GaussianRenderer MIT license | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-763-gaussianrenderer-mit-license.md) |
| SRC-robotics-764 | DISCOVERSE core optional dependencies | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-764-discoverse-core-optional-dependencies.md) |
| SRC-robotics-765 | PhiRIE MJCF rigid object export implementation | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-765-phirie-mjcf-rigid-object-export-implementation.md) |
| SRC-robotics-766 | RialTo GUI joint authoring implementation | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-766-rialto-gui-joint-authoring-implementation.md) |
| SRC-robotics-767 | RialTo USD physics joint exporter | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-767-rialto-usd-physics-joint-exporter.md) |
| SRC-robotics-768 | RialTo GUI package metadata license boundary | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-768-rialto-gui-package-metadata-license-boundary.md) |
| SRC-robotics-769 | DISCOVERSE Real2Sim rasterizer research license | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-769-discoverse-real2sim-rasterizer-research-license.md) |
| SRC-robotics-770 | DISCOVERSE cabinet parent scene compiler contract | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-770-discoverse-cabinet-parent-scene-compiler-contract.md) |
| SRC-robotics-771 | Door drawer code audit and isolated probes | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-771-door-drawer-code-audit.md) |
| SRC-robotics-772 | GaussianRenderer gsplat backend implementation | [归档](../../raw/robotics-embodied-ai/documents/SRC-robotics-772-gaussianrenderer-gsplat-backend-implementation.md) |

## 版本与许可

- DISCOVERSE `d67f47c084aba0e0cf422a8725235f8b9238655a`，MIT；Real2Sim `1fd9ecdbb02fe3b28bce5db28a3b968b4d3d4d57`，独立工具链许可分开。
- GaussianRenderer `577efdb50c3891f46db3971dc0b7c4129146dd16`，声明0.2.0／MIT，核心依赖gsplat；不能外推为全部Real2Sim组件MIT。
- PhiRIE `a03543f6472451ffc079502417a48d64c2a6e7f1`，MIT；完整编辑后台见复用750／756。
- RialToGUI `9f0191453d7884d6eaf301a12e6f1cdb24a0ae28`，根tree与package未见明确许可。额外检查到同组织RialTo同名仓库以项目网站资源为主，没有将其网站许可套到GUI软件。

## 捕获与验证边界

14网页源：769自动Markdown抽取ok，另外13项为无.md后缀纯文本fallback_html；正文与独立GitHub连接器副本逐一匹配（去掉尾部空白），不把状态伪改ok。771为本地静态／探针包，包含4个完整未截断tree、固定源码、依赖／许可证和结果JSON。运行在隔离MuJoCo4.0.0，不是现有项目依赖资格测试。

探针证实原柜子模型两个关节可编译／前向变换／短施力步进，以及真实body pose可被原renderer映射方法送入截获适配器。GPU Gaussian变换、rasterization、图形UI、完整候选运行、限位与真实物性精度均未验收。没有机器人、策略或远程操作。

## 关联连接

- [[robotics-embodied-ai/research-notes/door-drawer-interactive-reconstruction-code-audit-2026-11-10|三项目深查与推荐路线]]
- [[robotics-embodied-ai/research-notes/interactive-room-sim-reconstruction-alternatives-2026-11-10|场景重建主报告]]
