---
title: AIRSPEED - Open-source Data Production Platform for Embodied AI
type: source
date_created: 2026-06-23
last_updated: 2026-06-23
source_urls:
  - https://airs.cuhk.edu.cn/en/airspeed
  - https://github.com/airs-cuhk/airspeed
  - https://airs.cuhk.edu.cn/sites/default/files/2025-10/AIRSPEED_arxiv.pdf
  - https://airs.cuhk.edu.cn/sites/default/files/2025-06/Survey_Arxiv.pdf
  - https://airs.cuhk.edu.cn/sites/default/files/2026-05/TechnologyTransferofOpen-SourceDataInfrastructureforEmbodiedAITheAIRSPEEDCase.pdf
  - https://airs.cuhk.edu.cn/sites/default/files/2026-05/TechnologyTransferofOpen-SourceDataInfrastructureforEmbodiedAITheAIRSPEEDCase-CN.pdf
evidence_grade: S/A
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-183-airspeed-project-page.html
  - raw/robotics-embodied-ai/documents/SRC-robotics-184-airspeed-technical-report.pdf
  - raw/robotics-embodied-ai/documents/SRC-robotics-184-airspeed-technical-report.txt
  - raw/robotics-embodied-ai/documents/SRC-robotics-185-eai-data-engineering-survey.pdf
  - raw/robotics-embodied-ai/documents/SRC-robotics-185-eai-data-engineering-survey.txt
  - raw/robotics-embodied-ai/documents/SRC-robotics-186-airspeed-technology-transfer-report.pdf
  - raw/robotics-embodied-ai/documents/SRC-robotics-186-airspeed-technology-transfer-report.txt
  - raw/robotics-embodied-ai/documents/SRC-robotics-187-airspeed-technology-transfer-report-cn.pdf
  - raw/robotics-embodied-ai/documents/SRC-robotics-187-airspeed-technology-transfer-report-cn.txt
  - raw/robotics-embodied-ai/documents/SRC-robotics-188-airspeed-github-readme.md
tags:
  - industry/robotics-embodied-ai
  - embodied-ai
  - data-platform
  - robot-training-data
  - open-source
status: active
aliases:
  - AIRSPEED source set
  - AIRSPEED 来源组
---

# AIRSPEED - Open-source Data Production Platform for Embodied AI

> [!summary]
> AIRSPEED 是深圳市人工智能与机器人研究院（AIRS）发布的具身智能数据生产平台来源组。官网和技术报告把它定位为覆盖真实数据采集、仿真数据生成、数据集自动构建的通用平台；GitHub README 则显示当前 v1.3 开源版本主要是 ROS2/YAML 驱动的数据采集核心，仿真生成和自动数据集构建仍列为未来计划。

## 来源信息

| SRC | 来源 | 类型 | 证据等级 | raw artifact |
|---|---|---|---|---|
| `SRC-robotics-183` | AIRSPEED project page | official project page | A | [HTML](../../raw/robotics-embodied-ai/documents/SRC-robotics-183-airspeed-project-page.html) |
| `SRC-robotics-184` | AIRSPEED technical report | paper / technical report | S | [PDF](../../raw/robotics-embodied-ai/documents/SRC-robotics-184-airspeed-technical-report.pdf), [TXT](../../raw/robotics-embodied-ai/documents/SRC-robotics-184-airspeed-technical-report.txt) |
| `SRC-robotics-185` | A Survey of Embodied AI Data Engineering | survey paper | S | [PDF](../../raw/robotics-embodied-ai/documents/SRC-robotics-185-eai-data-engineering-survey.pdf), [TXT](../../raw/robotics-embodied-ai/documents/SRC-robotics-185-eai-data-engineering-survey.txt) |
| `SRC-robotics-186` | Technology Transfer of Open-Source Data Infrastructure for Embodied AI | institutional report | A | [PDF](../../raw/robotics-embodied-ai/documents/SRC-robotics-186-airspeed-technology-transfer-report.pdf), [TXT](../../raw/robotics-embodied-ai/documents/SRC-robotics-186-airspeed-technology-transfer-report.txt) |
| `SRC-robotics-187` | 开源数据平台 AIRSPEED 技术转移报告 | institutional report | A | [PDF](../../raw/robotics-embodied-ai/documents/SRC-robotics-187-airspeed-technology-transfer-report-cn.pdf), [TXT](../../raw/robotics-embodied-ai/documents/SRC-robotics-187-airspeed-technology-transfer-report-cn.txt) |
| `SRC-robotics-188` | AIRSPEED GitHub README | code repository | S | [README](../../raw/robotics-embodied-ai/documents/SRC-robotics-188-airspeed-github-readme.md) |

## 核心事实

- AIRSPEED 的问题定义是：具身智能训练数据昂贵、数据格式和采集标准碎片化、真实场景/任务/机器人类型难以覆盖，且缺少判断数据集质量和潜在模型性能的统一方法。
- 官网和技术报告描述的完整架构包含三个服务：Data Collection Service、Data Generation Service、Dataset Construction Service。
- 论文设计中的数据集构建采用可配置金字塔结构，默认按 `Models-Tasks-Scenes-Executions` 组织数据；数据生成服务负责真实/仿真数据的时间、空间和物理单位对齐。
- GitHub README 显示当前 v1.3 开源实现包含 Teleoperation Interface、Robot Interface、Sensor Interface 和 Data Collection Service；Data Generation 与 automated Dataset Construction 被标注为 future releases。
- 当前开源数据采集核心基于 ROS2 topic contract、YAML 配置、AIRS HDF5 episode 文件，并提供到 Parquet、Zarr、LeRobot v3 和 JSON Lines 的转换工具。
- 技术报告实验声称：同构遥操作场景中真实数据集构建阶段效率提升 35.62x，整体效率提升 6.01x；光惯遥操作数据集构建阶段提升 23.5x；虚拟遥操作合成数据集构建阶段提升 7.67x。
- 技术报告给出的性能指标包括：数据采集端到端延迟最低 3ms，压缩吞吐至少 296 MB/s，数据生成对齐延迟最高 30ms。
- 中文技术转移报告声称项目 2025 年落地 3 家标杆客户付费试点、达到 TRL 6、完成 1000 万元 Pre-A 融资；这些商业化信息目前来自项目方报告，仍需工商、融资公告、客户访谈或合同级证据交叉验证。

## 研究意义

- 对 [[robotics-embodied-ai/09-training-data-deep-dive|机器人训练数据深度调研]]：AIRSPEED 是中国语境下“具身数据生产平台”从论文、开源代码到技术转移叙事的完整样本。
- 对 [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]：它强调接口、采集、格式转换、仿真扩增和数据集构建，而不是只做模型训练或仿真 benchmark。
- 对 [[_concepts/robot-training-data|Robot Training Data]]：它把数据工程上升为一条独立产业线，包括采集设备适配、时间同步、质量验证、格式转换、私有化部署和企业工作流。
- 对职业路径：AIRSPEED 对平台工程师、数据平台工程师、RobotOps/MLOps、仿真数据工程和数据基础设施产品经理都有参考价值。

## 待验证

- GitHub 仓库的许可证、release tag、活跃维护状态、issue/PR 生态和是否与 README 中 `StarChen-Cycler/airspeed-data-collection-zyc` 路径一致。
- 当前开源代码中真实支持的设备、机器人、ROS2 topic contract、HDF5 schema、LeRobot v3 转换器可用性。
- 技术转移报告中 20+ 遥操作设备、10+ 机器人、3 家付费试点、融资到账、标准参与等商业化 claim 的独立证据。
- 数据生成和数据集构建服务是否已有闭源商业版，或只是论文/报告中的规划能力。

## 关联连接

- [[_entities/AIRSPEED|AIRSPEED]]
- [[robotics-embodied-ai/research-notes/airspeed-data-production-platform-2026-06-23|AIRSPEED 具身智能数据生产平台调研]]
- [[robotics-embodied-ai/12-robotics-engineering-platforms-2026-06-04|机器人工程平台综合调研]]
- [[robotics-embodied-ai/09-training-data-deep-dive|机器人训练数据深度调研]]
- [[_concepts/robot-training-data|Robot Training Data]]
- [[_concepts/embodied-ai|Embodied AI]]
