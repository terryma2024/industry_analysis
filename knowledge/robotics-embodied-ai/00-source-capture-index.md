---
title: 机器人（具身智能） - 来源抽取索引
date: 2026-06-08
last_updated: 2026-07-11
tags:
  - industry/robotics-embodied-ai
  - sources
  - raw-capture
  - obsidian/moc
aliases:
  - 具身智能来源抽取索引
  - Robotics Source Capture Index
---

# 机器人（具身智能） - 来源抽取索引

> [!summary]
> 本页是 [[00-index|机器人（具身智能）]] 的来源抽取 MOC。来源编号仍以 [[sources.csv]] 为准；原文/清洗件保存在 `raw/robotics-embodied-ai/documents/`，抽取状态见 [source_capture_manifest.csv](../../raw/robotics-embodied-ai/documents/source_capture_manifest.csv)。

## 当前状态

| 状态 | 数量 | 含义 |
|---|---:|---|
| `exists` | 108 | 既有 Markdown/PDF raw artifact。 |
| `ok` | 28 | 已成功抽取的 raw artifact。 |
| `fallback_html` | 8 | 正文抽取失败但已保存 HTML 或 raw sidecar。 |
| `manual_parse` | 1 | 本轮因 defuddle 失败，从网页内嵌结构化数据生成 Markdown。 |
| `manual_capture` | 1 | 手工 curl 保存 HTML，未生成清洗 Markdown。 |
| `failed` | 5 | defuddle 与 HTML fallback 都失败，需要浏览器、官方 PDF 或手工补采。 |

## 快速定位

- 来源总表：[[sources.csv]]
- 抽取 manifest：[source_capture_manifest.csv](../../raw/robotics-embodied-ai/documents/source_capture_manifest.csv)
- 示例：[`SRC-robotics-060`](../../raw/robotics-embodied-ai/documents/SRC-robotics-060-mimicgen-a-data-generation-system-for-scalable-robot-learning-using-human-demons.md) 的 raw extract 在 [SRC-robotics-060 MimicGen](../../raw/robotics-embodied-ai/documents/SRC-robotics-060-mimicgen-a-data-generation-system-for-scalable-robot-learning-using-human-demons.md)

## 需要补采的来源

> [!warning]
> 以下来源被站点限制、JS 渲染或 SSL/403 阻断。知识笔记可以暂用 `sources.csv` 的 URL，但关键结论需要后续补 raw 证据。

| SRC | 状态 | 原因 | 下一步 |
|---|---|---|---|
| `SRC-robotics-017` | `failed` | NVIDIA investor 页面 403，HTML fallback 也被拒。 | 寻找 NVIDIA 官方新闻镜像、开发者页或 PDF。 |
| `SRC-robotics-019` | `failed` | Tesla 页面 403，HTML fallback 也被拒。 | 用浏览器登录/手工保存，或改用 Tesla 官方可访问页面。 |
| `SRC-robotics-085` | `failed` | 深圳科创局页面 defuddle fetch failed，HTML fallback SSL BAD_ECPOINT。 | 用浏览器手工保存原文，或寻找深圳市政府/政策 PDF 镜像。 |
| `SRC-robotics-105` | `failed` | TRON 1 用户手册 PDF 官网证书过期，自动下载失败。 | 用浏览器手工保存 PDF，或寻找新版下载地址。 |
| `SRC-robotics-190` | `failed` | dora guides URL 自动抽取返回 404。 | 改用 GitHub raw docs、官网 `/book` 路径或浏览器手工保存后再核验。 |

## 已保存 fallback HTML 的来源

| SRC | raw sidecar | 说明 |
|---|---|---|
| [`SRC-robotics-015`](../../raw/robotics-embodied-ai/documents/SRC-robotics-015-agibot-a2-product-page.md) | [AGIBOT A2](../../raw/robotics-embodied-ai/documents/SRC-robotics-015-agibot-a2-product-page.md) | defuddle 500，但已保存 HTML。 |
| [`SRC-robotics-016`](../../raw/robotics-embodied-ai/documents/SRC-robotics-016-agibot-products-page.md) | [AGIBOT products](../../raw/robotics-embodied-ai/documents/SRC-robotics-016-agibot-products-page.md) | defuddle 500，但已保存 HTML。 |
| [`SRC-robotics-044`](../../raw/robotics-embodied-ai/documents/SRC-robotics-044-agibot-open-agibot-world-2026.md) | [AGIBOT WORLD 2026](../../raw/robotics-embodied-ai/documents/SRC-robotics-044-agibot-open-agibot-world-2026.md) | defuddle 500，但已保存 HTML。 |
| [`SRC-robotics-048`](../../raw/robotics-embodied-ai/documents/SRC-robotics-048-firstmove-egocentric-data-engine-for-robotics.md) | [FirstMove](../../raw/robotics-embodied-ai/documents/SRC-robotics-048-firstmove-egocentric-data-engine-for-robotics.md) | JS 页面无正文，但已保存 HTML。 |
| [`SRC-robotics-049`](../../raw/robotics-embodied-ai/documents/SRC-robotics-049-source.md) | [ModelScope/BAAI](../../raw/robotics-embodied-ai/documents/SRC-robotics-049-source.md) | defuddle URL 解析失败，但已保存 HTML。 |
| [`SRC-robotics-087`](../../raw/robotics-embodied-ai/documents/SRC-robotics-087-source.md) | [杭州强链补链政策解读](../../raw/robotics-embodied-ai/documents/SRC-robotics-087-source.md) | defuddle 无正文，但已保存 HTML。 |
| [`SRC-robotics-120`](../../raw/robotics-embodied-ai/documents/SRC-robotics-120-maniskill-official-website.md) | [ManiSkill](../../raw/robotics-embodied-ai/documents/SRC-robotics-120-maniskill-official-website.md) | defuddle 无正文，但已保存 HTML。 |
| [`SRC-robotics-122`](../../raw/robotics-embodied-ai/documents/SRC-robotics-122-moveit-2-documentation.md) | [MoveIt 2](../../raw/robotics-embodied-ai/documents/SRC-robotics-122-moveit-2-documentation.md) | defuddle 无正文，但已保存 HTML。 |
| [`SRC-robotics-123`](../../raw/robotics-embodied-ai/documents/SRC-robotics-123-agibot-genie-studio.md) | [Agibot Genie Studio](../../raw/robotics-embodied-ai/documents/SRC-robotics-123-agibot-genie-studio.md) | defuddle 无正文，但已保存 HTML。 |

## 手工/论文来源捕获

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-233`](../../raw/robotics-embodied-ai/documents/SRC-robotics-233-hapmorph-a-pneumatic-framework-for-multi-dimensional-haptic-property-rendering.md) | [HapMorph arXiv 摘要页](../../raw/robotics-embodied-ai/documents/SRC-robotics-233-hapmorph-a-pneumatic-framework-for-multi-dimensional-haptic-property-rendering.md) | 用于校验 `BV12XTM6sEGF` 触觉反馈视频中的 21g、50-104mm、4.7N/mm 和 89.4% 等关键指标。 |
| [`SRC-robotics-125`](../../raw/robotics-embodied-ai/documents/roboalign-r1-2605.03821.pdf) | [RoboAlign-R1 PDF](../../raw/robotics-embodied-ai/documents/roboalign-r1-2605.03821.pdf) | arXiv PDF 已保存；摘要页 sidecar 为 [HTML](../../raw/robotics-embodied-ai/documents/roboalign-r1-2605.03821-arxiv.html)。 |
| [`SRC-robotics-126`](../../raw/robotics-embodied-ai/documents/modelscope-roboalign-r1-434219.md) | [ModelScope RoboAlign-R1 Markdown](../../raw/robotics-embodied-ai/documents/modelscope-roboalign-r1-434219.md) | defuddle 因 ModelScope `og:url` protocol-relative metadata 失败；已从 `window.__detail_data__` 生成 Markdown，并保存 [HTML](../../raw/robotics-embodied-ai/documents/modelscope-roboalign-r1-434219.html)。 |

## 2026-07-11 Bilibili 交叉验证来源

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-243`](../../raw/robotics-embodied-ai/documents/SRC-robotics-243-wall-b.md) | [自变量机器人官网](../../raw/robotics-embodied-ai/documents/SRC-robotics-243-wall-b.md) | 核验自变量公司身份、WALL-A/WALL-B、端到端方向和多地布局；不用于确认视频中的估值、营收或客户。 |
| [`SRC-robotics-244`](../../raw/robotics-embodied-ai/documents/SRC-robotics-244-vision-pretraining-for-dense-spatial-perception.md) | [LingBot-Vision 论文](../../raw/robotics-embodied-ai/documents/SRC-robotics-244-vision-pretraining-for-dense-spatial-perception.md) | 核验 LingBot-Vision 与 LingBot-Depth 2.0 的稠密空间感知/深度补全定位；benchmark 数字仍为作者报告。 |

## AIRSPEED 数据生产平台来源

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-183`](../../raw/robotics-embodied-ai/documents/SRC-robotics-183-airspeed-project-page.html) | [AIRSPEED project page HTML](../../raw/robotics-embodied-ai/documents/SRC-robotics-183-airspeed-project-page.html) | 官网页面；web extraction 不稳定，改用 curl 保存 HTML。 |
| [`SRC-robotics-184`](../../raw/robotics-embodied-ai/documents/SRC-robotics-184-airspeed-technical-report.pdf) | [AIRSPEED technical report PDF](../../raw/robotics-embodied-ai/documents/SRC-robotics-184-airspeed-technical-report.pdf) / [TXT](../../raw/robotics-embodied-ai/documents/SRC-robotics-184-airspeed-technical-report.txt) | 技术报告，已用 `pdftotext -layout` 生成文本 sidecar。 |
| [`SRC-robotics-185`](../../raw/robotics-embodied-ai/documents/SRC-robotics-185-eai-data-engineering-survey.pdf) | [EAI data engineering survey PDF](../../raw/robotics-embodied-ai/documents/SRC-robotics-185-eai-data-engineering-survey.pdf) / [TXT](../../raw/robotics-embodied-ai/documents/SRC-robotics-185-eai-data-engineering-survey.txt) | EAI 数据工程综述，已生成文本 sidecar。 |
| [`SRC-robotics-186`](../../raw/robotics-embodied-ai/documents/SRC-robotics-186-airspeed-technology-transfer-report.pdf) | [Technology transfer report PDF](../../raw/robotics-embodied-ai/documents/SRC-robotics-186-airspeed-technology-transfer-report.pdf) / [TXT](../../raw/robotics-embodied-ai/documents/SRC-robotics-186-airspeed-technology-transfer-report.txt) | 英文技术转移报告，商业化 claim 需独立验证。 |
| [`SRC-robotics-187`](../../raw/robotics-embodied-ai/documents/SRC-robotics-187-airspeed-technology-transfer-report-cn.pdf) | [中文技术转移报告 PDF](../../raw/robotics-embodied-ai/documents/SRC-robotics-187-airspeed-technology-transfer-report-cn.pdf) / [TXT](../../raw/robotics-embodied-ai/documents/SRC-robotics-187-airspeed-technology-transfer-report-cn.txt) | 中文技术转移报告，包含客户、融资、标准参与等待验证 claim。 |
| [`SRC-robotics-188`](../../raw/robotics-embodied-ai/documents/SRC-robotics-188-airspeed-github-readme.md) | [AIRSPEED GitHub README](../../raw/robotics-embodied-ai/documents/SRC-robotics-188-airspeed-github-readme.md) | 当前 v1.3 开源能力边界，用于校正官网/论文完整架构表述。 |

## UMI 设备购买线索来源

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-127`](../../raw/robotics-embodied-ai/documents/SRC-robotics-127-aifitlab-umi-gripper-collection.md) | [AIFITLAB UMI Gripper collection](../../raw/robotics-embodied-ai/documents/SRC-robotics-127-aifitlab-umi-gripper-collection.md) | LUMOS FastUMI Pro/Ego/Go 商品聚合页。 |
| [`SRC-robotics-128`](../../raw/robotics-embodied-ai/documents/SRC-robotics-128-aifitlab-lumos-fastumi-pro-product-page.md) | [LUMOS FastUMI Pro](../../raw/robotics-embodied-ai/documents/SRC-robotics-128-aifitlab-lumos-fastumi-pro-product-page.md) | FastUMI Pro 公开价格、配置、backorder 和技术参数。 |
| [`SRC-robotics-129`](../../raw/robotics-embodied-ai/documents/SRC-robotics-129-aifitlab-lumos-fastumi-go-product-page.md) | [LUMOS FastUMI Go](../../raw/robotics-embodied-ai/documents/SRC-robotics-129-aifitlab-lumos-fastumi-go-product-page.md) | 背包式双手 UMI 数采设备公开价格与配置。 |
| [`SRC-robotics-130`](../../raw/robotics-embodied-ai/documents/SRC-robotics-130-aifitlab-lumos-fastumi-ego-product-page.md) | [LUMOS FastUMI Ego](../../raw/robotics-embodied-ai/documents/SRC-robotics-130-aifitlab-lumos-fastumi-ego-product-page.md) | 第一人称无本体采集设备公开价格与传感器参数。 |
| [`SRC-robotics-131`](../../raw/robotics-embodied-ai/documents/SRC-robotics-131-mego.md) | [觅蜂 MEgo 量产发货](../../raw/robotics-embodied-ai/documents/SRC-robotics-131-mego.md) | MEgo Gripper 量产发货、480g 和 1 mm 轨迹重建线索。 |
| [`SRC-robotics-132`](../../raw/robotics-embodied-ai/documents/SRC-robotics-132-awe2026-fastumi.md) | [鹿明 AWE2026 FastUMI 发布](../../raw/robotics-embodied-ai/documents/SRC-robotics-132-awe2026-fastumi.md) | FastUMI 全家桶发布与陆续上线京东线索。 |
| [`SRC-robotics-133`](../../raw/robotics-embodied-ai/documents/SRC-robotics-133-beingbeyond-launches-u1-realdexumi.md) | [BeingBeyond U1 RealDexUMI](../../raw/robotics-embodied-ai/documents/SRC-robotics-133-beingbeyond-launches-u1-realdexumi.md) | U1 / RealDexUMI 官方发布。 |
| [`SRC-robotics-134`](../../raw/robotics-embodied-ai/documents/SRC-robotics-134-realdexumi-wearable-universal-manipulation-interface-paper.md) | [RealDexUMI arXiv](../../raw/robotics-embodied-ai/documents/SRC-robotics-134-realdexumi-wearable-universal-manipulation-interface-paper.md) | RealDexUMI 论文摘要页。 |

## dora / ROS 2 中间件专题来源

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-189`](../../raw/robotics-embodied-ai/documents/SRC-robotics-189-dora-1-0-official-website.md) | [Dora 1.0 official website](../../raw/robotics-embodied-ai/documents/SRC-robotics-189-dora-1-0-official-website.md) | defuddle 超时，已保存官网 HTML；用于核验 dora 1.0/RC 与性能主张。 |
| `SRC-robotics-190` | 无 | dora guides URL 自动抽取失败，不作为关键结论依据。 |
| [`SRC-robotics-191`](../../raw/robotics-embodied-ai/documents/SRC-robotics-191-dora-github-readme.md) | [Dora GitHub README](../../raw/robotics-embodied-ai/documents/SRC-robotics-191-dora-github-readme.md) | GitHub raw README，成功 direct-download。 |
| [`SRC-robotics-192`](../../raw/robotics-embodied-ai/documents/SRC-robotics-192-dora-pypi-package-dora-rs.md) | [dora-rs PyPI](../../raw/robotics-embodied-ai/documents/SRC-robotics-192-dora-pypi-package-dora-rs.md) | PyPI 页面，记录 `0.5.0` 稳定版。 |
| [`SRC-robotics-193`](../../raw/robotics-embodied-ai/documents/SRC-robotics-193-dora-github-release-v0-5-0.md) | [Dora GitHub release v0.5.0](../../raw/robotics-embodied-ai/documents/SRC-robotics-193-dora-github-release-v0-5-0.md) | GitHub release tag fallback HTML，记录 `v0.5.0` 为 Latest。 |
| [`SRC-robotics-194`](../../raw/robotics-embodied-ai/documents/SRC-robotics-194-dora-dataflow-oriented-robotic-architecture-paper.md) | [DORA arXiv paper](../../raw/robotics-embodied-ai/documents/SRC-robotics-194-dora-dataflow-oriented-robotic-architecture-paper.md) | 论文摘要页，说明 DORA 的低延迟/低 CPU overhead 目标。 |
| [`SRC-robotics-195`](../../raw/robotics-embodied-ai/documents/SRC-robotics-195-dora-robotic-dataflow-benchmark-repository.md) | [dora benchmark repository](../../raw/robotics-embodied-ai/documents/SRC-robotics-195-dora-robotic-dataflow-benchmark-repository.md) | benchmark README，包含 CPU bulk data 与 CUDA IPC 对比和 caveat。 |
| [`SRC-robotics-196`](../../raw/robotics-embodied-ai/documents/SRC-robotics-196-ros-2-releases-official-documentation.md) | [ROS 2 releases docs](../../raw/robotics-embodied-ai/documents/SRC-robotics-196-ros-2-releases-official-documentation.md) | raw `.rst` 以 fallback sidecar 保存；记录 Lyrical Luth、Jazzy、Humble 等发行版。 |
| [`SRC-robotics-197`](../../raw/robotics-embodied-ai/documents/SRC-robotics-197-ros-2-nodes-official-documentation.md) | [ROS 2 nodes docs](../../raw/robotics-embodied-ai/documents/SRC-robotics-197-ros-2-nodes-official-documentation.md) | raw `.rst` 以 fallback sidecar 保存；用于节点/话题/服务/动作概念。 |
| [`SRC-robotics-198`](../../raw/robotics-embodied-ai/documents/SRC-robotics-198-ros-2-qos-official-documentation.md) | [ROS 2 QoS docs](../../raw/robotics-embodied-ai/documents/SRC-robotics-198-ros-2-qos-official-documentation.md) | raw `.rst` 以 fallback sidecar 保存；用于 DDS QoS 能力对比。 |
| [`SRC-robotics-199`](../../raw/robotics-embodied-ai/documents/SRC-robotics-199-ros-2-design-architecture-and-uses-in-the-wild.md) | [ROS 2 overview paper](../../raw/robotics-embodied-ai/documents/SRC-robotics-199-ros-2-design-architecture-and-uses-in-the-wild.md) | ROS 2 架构和真实部署综述论文摘要页。 |

## 2026-07-07 Bilibili 深研一级校验来源

| SRC | raw artifact | 说明 |
|---|---|---|
| [`SRC-robotics-238`](../../raw/robotics-embodied-ai/documents/SRC-robotics-238-nvidia-isaac-sim-4-5-documentation.md) | [NVIDIA Isaac Sim 4.5 documentation](../../raw/robotics-embodied-ai/documents/SRC-robotics-238-nvidia-isaac-sim-4-5-documentation.md) | 用于校验 Isaac Sim 的 GPU PhysX、多传感器 RTX 渲染、digital twin、Replicator、Isaac Lab 和 ROS/ROS2 bridge。 |
| [`SRC-robotics-239`](../../raw/robotics-embodied-ai/documents/SRC-robotics-239-nvidia-isaac-sim-4-5-system-requirements.md) | [Isaac Sim 4.5 requirements](../../raw/robotics-embodied-ai/documents/SRC-robotics-239-nvidia-isaac-sim-4-5-system-requirements.md) | 用于校验视频提到的 Isaac Sim 硬件/系统门槛。 |
| [`SRC-robotics-240`](../../raw/robotics-embodied-ai/documents/SRC-robotics-240-nvidia-isaac-lab-binary-installation-documentation.md) | [Isaac Lab binary installation](../../raw/robotics-embodied-ai/documents/SRC-robotics-240-nvidia-isaac-lab-binary-installation-documentation.md) | 用于校验 Isaac Lab clone、symlink、`isaaclab.sh` 和环境管理流程。 |
| [`SRC-robotics-241`](../../raw/robotics-embodied-ai/documents/SRC-robotics-241-do-as-i-do-dexterous-manipulation-data-from-everyday-human-videos.md) | [Do as I Do arXiv HTML](../../raw/robotics-embodied-ai/documents/SRC-robotics-241-do-as-i-do-dexterous-manipulation-data-from-everyday-human-videos.md) | 用于校验 `BV1WfTk6EEZ8` 中 monocular RGB reconstruction、retargeting、71% success rate 和 video filtering playbook。 |
| [`SRC-robotics-242`](../../raw/robotics-embodied-ai/documents/SRC-robotics-242-abot-m0-5-unified-mobility-and-manipulation-world-action-model.md) | [ABot-M0.5 arXiv HTML](../../raw/robotics-embodied-ai/documents/SRC-robotics-242-abot-m0-5-unified-mobility-and-manipulation-world-action-model.md) | 用于校验 `BV1F7Ts6WEYj` 中 intermediate latent actions、D-MoT、Dream Forcing 和 WAM limitations。 |

## 后续流程

- 新增来源后先更新 [[sources.csv]]，再运行 `uv run python tools/extract_sources_with_defuddle.py --industry robotics-embodied-ai`。
- 对知识笔记中的关键判断，使用 `SRC-*` 编号引用，并在需要时链接到 raw extract。
- 对 failed/fallback 来源，优先寻找官方 PDF、GitHub raw、论文 arXiv、监管/公告页等更稳定来源替换。
