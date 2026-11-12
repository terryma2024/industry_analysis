---
title: "Atlas 重建与机器人仿真落地｜来源集"
type: source
date_created: 2026-11-12
last_updated: 2026-11-12
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-777-atlas-developer-api-quickstart.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-778-how-to-use-atlas.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-779-atlas-cameras-and-posed-images.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-780-atlas-build-a-scene-from-images.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-781-atlas-using-video-footage.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-782-atlas-images-to-posed-rgbd-guide.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-783-atlas-generate-views-walkthrough.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-784-atlas-posed-images-to-splats-guide.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-785-atlas-splat-best-practices.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-786-atlas-billing.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-787-atlas-rate-limits.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-788-atlas-blender-integration.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-789-atlas-general-best-practices.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-790-atlas-splats2mesh-openapi-schema.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-791-atlas-posedimages2splats-openapi-schema.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-792-atlas-images2posedrgbd-openapi-schema.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-793-atlas-atlasgenerate-openapi-schema.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-794-atlaschisel-scene-editing-tutorial.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-795-atlas-terms-of-service.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-796-atlas-data-processing-addendum.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-797-building-worlds-that-train-robots-r2s2r.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-798-marble-available-models.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-799-marble-world-api-pricing.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-800-mujoco-xml-reference-snapshot-2026-11-12.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-801-isaac-sim-physics-simulation-fundamentals.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-802-atlas-schema-health-audit.md
tags: [industry/robotics-embodied-ai, atlas, real2sim, source-set]
status: active
---

# Atlas 重建与机器人仿真落地｜来源集

> [!summary]
> 本次新增 SRC-robotics-777–802：20项官方Markdown文档、5项网页和1项本地有限核查。详见 [[robotics-embodied-ai/research-notes/atlas-3d-reconstruction-robot-simulation-deployment-2026-11-12|R05/R04/R07落地报告]]。文档证明存在明确资产合同，不证明本账号已可调用或场景达到物理验收。

## 来源与抓取状态

| 编号 | 来源与等级 | 保存状态／用途 |
|---|---|---|
| [777](../../raw/robotics-embodied-ai/documents/SRC-robotics-777-atlas-developer-api-quickstart.md) | World Labs／Atlas Developer API Quickstart；S | ok；生产端点、项目鉴权与任务工作流 |
| [778](../../raw/robotics-embodied-ai/documents/SRC-robotics-778-how-to-use-atlas.md) | World Labs／How to use Atlas；S | ok；任务分工；账号可用性独立 |
| [779](../../raw/robotics-embodied-ai/documents/SRC-robotics-779-atlas-cameras-and-posed-images.md) | World Labs／Atlas cameras and posed images；S | ok；c2w、XYZW、坐标轴、深度及尺度 |
| [780](../../raw/robotics-embodied-ai/documents/SRC-robotics-780-atlas-build-a-scene-from-images.md) | World Labs／Atlas build a scene from images；S | ok；小组视角检查后再做较长工序 |
| [781](../../raw/robotics-embodied-ai/documents/SRC-robotics-781-atlas-using-video-footage.md) | World Labs／Atlas using video footage；S | ok；视频先抽帧；冻结时间不等于连续4D |
| [782](../../raw/robotics-embodied-ai/documents/SRC-robotics-782-atlas-images-to-posed-rgbd-guide.md) | World Labs／Atlas images to posed RGBD guide；S | ok；估计端点输入/输出与网格对齐 |
| [783](../../raw/robotics-embodied-ai/documents/SRC-robotics-783-atlas-generate-views-walkthrough.md) | World Labs／Atlas generate views walkthrough；S | ok；RGBD context、相机与输出深度 |
| [784](../../raw/robotics-embodied-ai/documents/SRC-robotics-784-atlas-posed-images-to-splats-guide.md) | World Labs／Atlas posed images to splats guide；S | ok；SPZ流程、费用/耗时说明；draft存在冲突 |
| [785](../../raw/robotics-embodied-ai/documents/SRC-robotics-785-atlas-splat-best-practices.md) | World Labs／Atlas splat best practices；S | ok；重复物体、薄结构、白墙/玻璃等反例 |
| [786](../../raw/robotics-embodied-ai/documents/SRC-robotics-786-atlas-billing.md) | World Labs／Atlas billing；S | ok；Atlas积分与会话计费；完整任务价待平台 |
| [787](../../raw/robotics-embodied-ai/documents/SRC-robotics-787-atlas-rate-limits.md) | World Labs／Atlas rate limits；S | ok；配额未最终公布、共享容量与重试 |
| [788](../../raw/robotics-embodied-ai/documents/SRC-robotics-788-atlas-blender-integration.md) | World Labs／Atlas Blender integration；S | ok；Blender集成指引；指定版本未实机核验 |
| [789](../../raw/robotics-embodied-ai/documents/SRC-robotics-789-atlas-general-best-practices.md) | World Labs／Atlas general best practices；S | ok；流程状态与旧API不兼容 |
| [790](../../raw/robotics-embodied-ai/documents/SRC-robotics-790-atlas-splats2mesh-openapi-schema.md) | World Labs／Atlas splats2Mesh OpenAPI schema；S | ok；GLB、碰撞盒、取样相机和提取分辨率 |
| [791](../../raw/robotics-embodied-ai/documents/SRC-robotics-791-atlas-posedimages2splats-openapi-schema.md) | World Labs／Atlas posedImages2Splats OpenAPI schema；S | ok；请求字段不含refine且禁止额外字段 |
| [792](../../raw/robotics-embodied-ai/documents/SRC-robotics-792-atlas-images2posedrgbd-openapi-schema.md) | World Labs／Atlas images2PosedRGBD OpenAPI schema；S | ok；估计输入拒绝camera/depth/mask的schema描述 |
| [793](../../raw/robotics-embodied-ai/documents/SRC-robotics-793-atlas-atlasgenerate-openapi-schema.md) | World Labs／Atlas atlasGenerate OpenAPI schema；S | ok；RGBD与目标相机schema |
| [794](../../raw/robotics-embodied-ai/documents/SRC-robotics-794-atlaschisel-scene-editing-tutorial.md) | World Labs／AtlasChisel scene editing tutorial；S | ok；深度条件外观与带mask编辑的区分 |
| [795](../../raw/robotics-embodied-ai/documents/SRC-robotics-795-atlas-terms-of-service.md) | World Labs／Atlas Terms of Service；S | ok；输出用途、内容使用、访问及竞争性用途边界 |
| [796](../../raw/robotics-embodied-ai/documents/SRC-robotics-796-atlas-data-processing-addendum.md) | World Labs／Atlas Data Processing Addendum；S | ok；数据处理合同原文；不作客户具体适用认定 |
| [797](../../raw/robotics-embodied-ai/documents/SRC-robotics-797-building-worlds-that-train-robots-r2s2r.md) | World Labs／Building Worlds That Train Robots R2S2R；A | ok；专有R2S2R公司实验；非Atlas公开API成果证明 |
| [798](../../raw/robotics-embodied-ai/documents/SRC-robotics-798-marble-available-models.md) | World Labs／Marble available models；S | ok；Marble模型族与Atlas分开 |
| [799](../../raw/robotics-embodied-ai/documents/SRC-robotics-799-marble-world-api-pricing.md) | World Labs／Marble World API pricing；S | ok；旧World API积分口径，不能套入Atlas |
| [800](../../raw/robotics-embodied-ai/documents/SRC-robotics-800-mujoco-xml-reference-snapshot-2026-11-12.md) | Google DeepMind MuJoCo／MuJoCo XML reference snapshot 2026-11-12；S | ok；新日期快照；mesh凸包/导入及关节语义 |
| [801](../../raw/robotics-embodied-ai/documents/SRC-robotics-801-isaac-sim-physics-simulation-fundamentals.md) | NVIDIA／Isaac Sim physics simulation fundamentals；S | ok；碰撞、刚体、关节与视觉层分开 |
| [802](../../raw/robotics-embodied-ai/documents/SRC-robotics-802-atlas-schema-health-audit.md) | Analyst／Atlas schema inspection and public health check 2026-11-12；S | ok；四份schema静态解析＋无认证health200；无生成 |

## 提取与版本边界

- 文档均在 2026-11-12 读取；没有发布日期的保留待验证，不以访问日替代。777–796按官方`.md`直接下载，797–801经项目Defuddle脚本；25项新网络来源均ok。脚本退出1来自历史failed记录，未重写旧来源正文。
- 800与既有708使用同一MuJoCo live stable URL，是本次重新核查的日期快照，旧文件保留。latest/stable文档会变化，当前依赖仍需固定实际运行版本。
- 802是本地原始有限观察：四份schema的版本、字段、hash和公开health响应，另有[JSON](../../raw/robotics-embodied-ai/documents/SRC-robotics-802-atlas-schema-health-audit.json)。该证据的S级只适用于自己的检查过程，不给模型精度背书。
- 公司R2S2R为A；其它官方技术文档为S。均不把公司宣传、演示或schema存在当作独立重现。
- 未听校现场视频、未读取评测图上的完整数值；正文采用R2S2R网页的文字协议，不重建曲线、相关系数或置信区间。未登录、安装、上传、付费生成、仿真或真机。

## 知识冲突

1. **指南与schema**：784描述`refine:false`的便宜draft，791请求schema无此字段且禁止extra；不提供未经核实的草稿调用模板，实际服务行为待验。
2. **访问状态**：前轮博客是early-access/closed-beta叙述，本次发现公开v2文档与资产输出；文档开放不证明账号权限或一般可用，也不说明上线日期。
3. **视频能力**：781限制当前工作流为静态帧/冻结时间；现场4D展示不能直接视为API连续时间控制。
4. **积分口径**：Atlas billing与旧Marble World API使用不同兑换关系，按各自产品记录，不静默合并。

## 关联连接

- [[robotics-embodied-ai/research-notes/atlas-3d-reconstruction-robot-simulation-deployment-2026-11-12|落地方案与验收]]
- [[_sources/wechat-corl-atlas-feifei-li-lisa-su|起始文章来源卡]]
- [[news/2026-11-12-corl-atlas-feifei-li-lisa-su|文章八个要点]]
- [[robotics-embodied-ai/00-source-capture-index|机器人来源索引]]
- [[robotics-embodied-ai/00-index|机器人研究入口]]
