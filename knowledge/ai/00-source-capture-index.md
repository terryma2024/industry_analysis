---
title: AI Source Capture Index
type: index
date_created: 2026-06-02
last_updated: 2026-07-15
status: active
tags:
  - industry/ai
  - source-capture
sources:
  - ai/sources.csv
  - raw/ai/documents/source_capture_manifest.csv
---

# AI Source Capture Index

> [!summary]
> 本页登记 `knowledge/ai/sources.csv` 中网页来源的离线抓取状态。2026-06-02 已运行 `tools/extract_sources_with_defuddle.py --industry ai --timeout 60`：16 条 `ok`，7 条 `fallback_html`，1 条 `failed`。2026-06-29 追加 AI 总行业 analyst source notes（SRC-ai-033 至 SRC-ai-046）。2026-07-14 新增并成功捕获 19 条 MediaPipe/LiteRT 官方来源与原始论文（SRC-ai-061 至 SRC-ai-079）；2026-07-15 追加 ENPIRE 一手论文归档（SRC-ai-080）。

## 状态说明

- `ok`: defuddle 抽取到可读 Markdown。
- `fallback_html`: defuddle 失败或内容过短，但已保留原始 HTML 或 sidecar Markdown。
- `failed`: 未能抓取，需后续用浏览器、替代来源、官方 PDF 或手工摘录补证。

## Source Capture Manifest

| Source ID | Title | Status | Raw artifact | Follow-up |
|---|---|---|---|---|
| SRC-ai-001 | Scale YC company post | fallback_html | [raw](../../raw/ai/documents/SRC-ai-001-scale-yc-company-post.md) | 检查 fallback HTML 是否足够；必要时手工浏览器捕获。 |
| SRC-ai-002 | Scale announces Series B funding | ok | [raw](../../raw/ai/documents/SRC-ai-002-scale-announces-series-b-funding.md) | 无。 |
| SRC-ai-003 | Scale AI Series C | fallback_html | [raw](../../raw/ai/documents/SRC-ai-003-scale-ai-series-c.md) | Scale 官网超时，必要时重跑或手工捕获。 |
| SRC-ai-004 | Scale AI breaking even after it scaled back hiring | ok | [raw](../../raw/ai/documents/SRC-ai-004-scale-ai-breaking-even-after-it-scaled-back-hiring.md) | 无。 |
| SRC-ai-005 | Scale AI scores 325 million to grow AI solution | ok | [raw](../../raw/ai/documents/SRC-ai-005-scale-ai-scores-325-million-to-grow-ai-solution.md) | 无。 |
| SRC-ai-006 | Scale AI awarded 250M AI contract by Department of Defense | ok | [raw](../../raw/ai/documents/SRC-ai-006-scale-ai-awarded-250m-ai-contract-by-department-of-defense.md) | 无。 |
| SRC-ai-007 | Scale AI Series F | ok | [raw](../../raw/ai/documents/SRC-ai-007-scale-ai-series-f.md) | 无。 |
| SRC-ai-008 | Scale AI announces next phase of company evolution | ok | [raw](../../raw/ai/documents/SRC-ai-008-scale-ai-announces-next-phase-of-company-evolution.md) | 无。 |
| SRC-ai-009 | Customer trust and Scale Meta deal | ok | [raw](../../raw/ai/documents/SRC-ai-009-customer-trust-and-scale-meta-deal.md) | 无。 |
| SRC-ai-010 | Scale AI not winding down following Meta deal interim CEO says | fallback_html | [raw](../../raw/ai/documents/SRC-ai-010-scale-ai-not-winding-down-following-meta-deal-interim-ceo-says.md) | CNBC fetch failed，必要时用浏览器或替代来源核验。 |
| SRC-ai-011 | Meta restructures its AI unit under Superintelligence Labs | ok | [raw](../../raw/ai/documents/SRC-ai-011-meta-restructures-its-ai-unit-under-superintelligence-labs.md) | 无。 |
| SRC-ai-012 | Meta Scale AI deal analysis | failed | manifest only | Axios 403，需浏览器/manual capture 或替代来源。 |
| SRC-ai-013 | 海天瑞声官网 | ok | [raw](../../raw/ai/documents/SRC-ai-013-source.md) | 无。 |
| SRC-ai-014 | 数据堂官网 | ok | [raw](../../raw/ai/documents/SRC-ai-014-source.md) | 无。 |
| SRC-ai-015 | 数据堂关于我们 | ok | [raw](../../raw/ai/documents/SRC-ai-015-source.md) | 无。 |
| SRC-ai-016 | Testin 云测官网 | fallback_html | [raw](../../raw/ai/documents/SRC-ai-016-testin.md) | 页面超时，必要时浏览器捕获。 |
| SRC-ai-017 | 标贝科技数据服务 | ok | [raw](../../raw/ai/documents/SRC-ai-017-source.md) | 无。 |
| SRC-ai-018 | 曼孚科技官网 | ok | [raw](../../raw/ai/documents/SRC-ai-018-source.md) | 无。 |
| SRC-ai-019 | 龙猫数据关于我们 | ok | [raw](../../raw/ai/documents/SRC-ai-019-source.md) | 无。 |
| SRC-ai-020 | 龙猫数据 AutopilotGPT | ok | [raw](../../raw/ai/documents/SRC-ai-020-autopilotgpt.md) | 无。 |
| SRC-ai-021 | GOMAX LAB 官网 | fallback_html | [raw](../../raw/ai/documents/SRC-ai-021-gomax-lab.md) | defuddle 未抽到内容，必要时手工核验。 |
| SRC-ai-022 | Xpert Studio 官网 | fallback_html | [raw](../../raw/ai/documents/SRC-ai-022-xpert-studio.md) | defuddle 未抽到内容，必要时手工核验。 |
| SRC-ai-023 | Stardust AI smart education scenario | ok | [raw](../../raw/ai/documents/SRC-ai-023-stardust-ai-smart-education-scenario.md) | 无。 |
| SRC-ai-024 | 天衍奇点官网 | fallback_html | [raw](../../raw/ai/documents/SRC-ai-024-source.md) | 页面超时，必要时浏览器捕获。 |
| SRC-ai-033 | 中华人民共和国国民经济和社会发展第十四个五年规划和2035年远景目标纲要 | ok | [raw](../../raw/ai/documents/SRC-ai-033-source.md) | analyst source note，正式引用前可回到国务院页面核对原文。 |
| SRC-ai-034 | 国务院关于印发新一代人工智能发展规划的通知 | ok | [raw](../../raw/ai/documents/SRC-ai-034-source.md) | analyst source note，正式引用前可回到国务院页面核对原文。 |
| SRC-ai-035 | 2024年政府工作报告 | ok | [raw](../../raw/ai/documents/SRC-ai-035-source.md) | analyst source note，正式引用前可回到国务院页面核对原文。 |
| SRC-ai-036 | 生成式人工智能服务管理暂行办法 | ok | [raw](../../raw/ai/documents/SRC-ai-036-source.md) | analyst source note，正式引用前可回到国务院页面核对原文。 |
| SRC-ai-037 | 工业和信息化部等七部门关于推动未来产业创新发展的实施意见 | ok | [raw](../../raw/ai/documents/SRC-ai-037-source.md) | analyst source note，正式引用前可回到国务院页面核对原文。 |
| SRC-ai-038 | DeepSeek 官网 | ok | [raw](../../raw/ai/documents/SRC-ai-038-source.md) | analyst source note，跟踪模型、API 和开源版本时需增量更新。 |
| SRC-ai-039 | Qwen 官方文档站 | ok | [raw](../../raw/ai/documents/SRC-ai-039-source.md) | analyst source note，跟踪模型、API 和开源版本时需增量更新。 |
| SRC-ai-040 | 百度文心一言官网 | ok | [raw](../../raw/ai/documents/SRC-ai-040-source.md) | analyst source note，跟踪产品和企业服务时需增量更新。 |
| SRC-ai-041 | Kimi 官网 | ok | [raw](../../raw/ai/documents/SRC-ai-041-source.md) | analyst source note，跟踪产品和企业服务时需增量更新。 |
| SRC-ai-042 | 智谱 AI 官网 | ok | [raw](../../raw/ai/documents/SRC-ai-042-source.md) | analyst source note，跟踪模型、API 和企业服务时需增量更新。 |
| SRC-ai-043 | 腾讯混元产品页 | ok | [raw](../../raw/ai/documents/SRC-ai-043-source.md) | analyst source note，跟踪云 API 和生态应用时需增量更新。 |
| SRC-ai-044 | 华为昇腾官网 | ok | [raw](../../raw/ai/documents/SRC-ai-044-source.md) | analyst source note，跟踪国产算力生态时需增量更新。 |
| SRC-ai-045 | 寒武纪官网 | ok | [raw](../../raw/ai/documents/SRC-ai-045-source.md) | analyst source note，正式投资判断需叠加财报与公告。 |
| SRC-ai-046 | ModelScope 魔搭社区 | ok | [raw](../../raw/ai/documents/SRC-ai-046-source.md) | analyst source note，跟踪开源模型和开发者生态时需增量更新。 |
| SRC-ai-053 | NVIDIA Isaac Sim 4.5 documentation | ok | [raw](../../raw/ai/documents/SRC-ai-053-nvidia-isaac-sim-4-5-documentation.md) | 用于校验 Physical AI/Isaac Sim 视频中的仿真、数字孪生、多传感器和 ROS/ROS2 bridge 事实。 |
| SRC-ai-054 | NVIDIA Isaac Sim 4.5 system requirements | ok | [raw](../../raw/ai/documents/SRC-ai-054-nvidia-isaac-sim-4-5-system-requirements.md) | 用于校验 Isaac Sim 4.5 的 OS、RAM、GPU 和 VRAM 要求。 |
| SRC-ai-055 | NVIDIA Isaac Lab binary installation documentation | ok | [raw](../../raw/ai/documents/SRC-ai-055-nvidia-isaac-lab-binary-installation-documentation.md) | 用于校验 Isaac Lab 安装、symlink、`isaaclab.sh` 和 Python 环境约束。 |
| SRC-ai-056 | Do as I Do Dexterous Manipulation Data from Everyday Human Videos | ok | [raw](../../raw/ai/documents/SRC-ai-056-do-as-i-do-dexterous-manipulation-data-from-everyday-human-videos.md) | 用于校验 Do As I Do 视频中的论文方法、retargeting success rate 和数据筛选结论。 |
| SRC-ai-057 | ABot-M0.5 Unified Mobility-and-Manipulation World Action Model | ok | [raw](../../raw/ai/documents/SRC-ai-057-abot-m0-5-unified-mobility-and-manipulation-world-action-model.md) | 用于校验 ABot-M0.5 视频中的 WAM 架构、D-MoT、Dream Forcing 和限制。 |
| SRC-ai-061 | MediaPipe GitHub repository and README | ok | [raw](../../raw/ai/documents/SRC-ai-061-mediapipe-github-repository-and-readme.md) | 跟踪许可证、隐私声明、项目结构与最新仓库状态。 |
| SRC-ai-062 | MediaPipe Solutions guide | ok | [raw](../../raw/ai/documents/SRC-ai-062-mediapipe-solutions-guide.md) | 跟踪 Solutions 平台矩阵、Preview 标记和 Legacy 迁移状态。 |
| SRC-ai-063 | MediaPipe Tasks overview | ok | [raw](../../raw/ai/documents/SRC-ai-063-mediapipe-tasks-overview.md) | 与具体 Task 页面交叉核对平台支持，避免总览文案滞后。 |
| SRC-ai-064 | MediaPipe Framework concepts | ok | [raw](../../raw/ai/documents/SRC-ai-064-mediapipe-framework-concepts.md) | 用于 Graph、Calculator、Packet、Stream 与 Side Packet 原理。 |
| SRC-ai-065 | MediaPipe synchronization | ok | [raw](../../raw/ai/documents/SRC-ai-065-mediapipe-synchronization.md) | 用于时间戳同步、scheduler queue、executor、背压与确定性。 |
| SRC-ai-066 | MediaPipe GPU framework support | ok | [raw](../../raw/ai/documents/SRC-ai-066-mediapipe-gpu-framework-support.md) | 用于 GPU context、GpuBuffer 与 CPU/GPU 传输约束。 |
| SRC-ai-067 | MediaPipe Hand Landmarker guide | ok | [raw](../../raw/ai/documents/SRC-ai-067-mediapipe-hand-landmarker-guide.md) | 代表性 Task，用于检测—跟踪管线、输出和官方性能参考。 |
| SRC-ai-068 | MediaPipe: A Framework for Building Perception Pipelines | ok | [raw](../../raw/ai/documents/SRC-ai-068-mediapipe-a-framework-for-building-perception-pipelines.md) | 原始论文，用于核验框架设计目标与跨平台流水线定位。 |
| SRC-ai-069 | MediaPipe Model Maker overview | ok | [raw](../../raw/ai/documents/SRC-ai-069-mediapipe-model-maker-overview.md) | 已停止积极维护；若路线变化需更新选型建议。 |
| SRC-ai-070 | MediaPipe LLM Inference guide | ok | [raw](../../raw/ai/documents/SRC-ai-070-mediapipe-llm-inference-guide.md) | maintenance-only；持续跟踪 LiteRT-LM 迁移。 |
| SRC-ai-071 | LiteRT overview | ok | [raw](../../raw/ai/documents/SRC-ai-071-litert-overview.md) | 用于界定 MediaPipe Tasks 与底层通用端侧运行时的分工。 |
| SRC-ai-072 | MediaPipe Python setup guide | ok | [raw](../../raw/ai/documents/SRC-ai-072-mediapipe-python-setup-guide.md) | 开发前复核 Python 与操作系统支持版本。 |
| SRC-ai-073 | MediaPipe Web setup guide | ok | [raw](../../raw/ai/documents/SRC-ai-073-mediapipe-web-setup-guide.md) | 开发前复核 npm/CDN 包和浏览器支持。 |
| SRC-ai-074 | MediaPipe Android setup guide | ok | [raw](../../raw/ai/documents/SRC-ai-074-mediapipe-android-setup-guide.md) | 开发前复核 SDK、依赖版本、assets 与 delegate。 |
| SRC-ai-075 | MediaPipe iOS setup guide | ok | [raw](../../raw/ai/documents/SRC-ai-075-mediapipe-ios-setup-guide.md) | 与 Tasks 总览的 iOS 文案存在差异，应以具体 Task 为准。 |
| SRC-ai-076 | MediaPipe v0.10.35 release | ok | [raw](../../raw/ai/documents/SRC-ai-076-mediapipe-v0-10-35-release.md) | 截至 2026-07-14 的最新已核验正式版；后续需增量检查。 |
| SRC-ai-077 | MediaPipe Hand Landmarker Python guide | ok | [raw](../../raw/ai/documents/SRC-ai-077-mediapipe-hand-landmarker-python-guide.md) | 用于 IMAGE、VIDEO、LIVE_STREAM、时间戳和回调示例。 |
| SRC-ai-078 | AI Edge RAG guide | ok | [raw](../../raw/ai/documents/SRC-ai-078-ai-edge-rag-guide.md) | deprecated；不应作为新长期架构。 |
| SRC-ai-079 | AI Edge Function Calling guide | ok | [raw](../../raw/ai/documents/SRC-ai-079-ai-edge-function-calling-guide.md) | deprecated；官方建议迁移 LiteRT-LM。 |
| SRC-ai-080 | ENPIRE Agentic Robot Policy Self-Improvement in the Real World | ok | [raw](../../raw/ai/documents/SRC-ai-080-enpire-agentic-robot-policy-self-improvement-in-the-real-world.md) | 用于校验 ENPIRE 四模块、真实世界闭环、任务范围与 pass@8 指标边界。 |
| SRC-ai-081 | 国务院关于深入实施“人工智能+”行动的意见 | ok | [raw](../../raw/ai/documents/SRC-ai-081-source.md) | 用于校验 AI 人才培养、青年人才、期权激励与就业风险评估，不用于证明视频中的薪资或岗位数字。 |

## 关联连接

- [[00-index|AI 相关 - 研究入口]]
- [[sources.csv|AI sources.csv]]
- [[research-notes/scale-ai-and-china-data-infrastructure-peers-2026-06-02|Scale AI 发展历程与中国对标公司]]
- [[research-notes/google-mediapipe-comprehensive-guide-2026-07-14|Google MediaPipe 全面调研：功能、原理与使用方法]]
