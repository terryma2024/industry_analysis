---
title: Niantic／Flexion 工作流、公开资产与项目适配来源集
type: source
date_created: 2026-11-10
last_updated: 2026-11-10
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-689-niantic-flexion-workflow-and-benchmark-recheck-2026-11-10.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-690-niantic-embodied-ai-product-availability-and-delivery.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-691-niantic-real2sim-sample-scene-dataset-card-pinned-f7ca594.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-692-niantic-sample-metadata.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-693-mvsanywhere-official-method-and-pose-scale.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-694-mvsanywhere-readme-fixed-commit-5bd49bb.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-695-mvsanywhere-license-fixed-commit-5bd49bb.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-696-isaac-sim-6-2-nurec-neural-volume-rendering.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-697-isaac-sim-6-2-nurec-rendering-utilities.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-698-isaac-sim-6-2-requirements.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-699-niantic-embodied-ai-plans-2026-11-10.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-700-niantic-places-library-2026-11-10.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-701-flexion-reflect-v1-0-architecture-and-limitations.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-702-niantic-sample-static-inspection.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-703-mvsanywhere-simple-demo-fixed-source.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-704-local-project-hash-recheck.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-705-mujoco-modeling-mesh-collision-semantics.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-706-flexion-copy-of-niantic-joint-workflow.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-707-mujoco-experimental-openusd-importing.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-708-mujoco-mesh-collision-xml-reference.md
tags:
  - industry/robotics-embodied-ai
  - source-set
  - real2sim
status: active
---

# Niantic／Flexion 工作流来源集

> [!summary]
> 支持 [[robotics-embodied-ai/research-notes/niantic-flexion-real2sim-zero-shot-project-fit-2026-11-10|R05/R04/R07研究报告]]。20项本轮资料涵盖联合发布、数据卡、固定源码、商业交付、Isaac/MuJoCo文档、静态样例和本地接口；使用前轮688快照作为本机对照。八个公开资产条目不是机器人示教数据。

## 来源登记与捕获

| ID | 来源与证据等级 | 原始工件 | 方法和状态 |
|---|---|---|---|
| SRC-robotics-689 | Niantic Flexion workflow and benchmark recheck 2026-11-10（A） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-689-niantic-flexion-workflow-and-benchmark-recheck-2026-11-10.md) | defuddle；ok |
| SRC-robotics-690 | Niantic embodied AI product availability and delivery（A） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-690-niantic-embodied-ai-product-availability-and-delivery.md) | defuddle；ok |
| SRC-robotics-691 | Niantic Real2Sim sample scene dataset card pinned f7ca594（S） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-691-niantic-real2sim-sample-scene-dataset-card-pinned-f7ca594.md) | direct-download；ok |
| SRC-robotics-692 | Niantic Real2Sim sample scene metadata pinned f7ca594（S） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-692-niantic-sample-metadata.md) | direct-download；ok |
| SRC-robotics-693 | MVSAnywhere official method and pose scale（S） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-693-mvsanywhere-official-method-and-pose-scale.md) | defuddle；ok |
| SRC-robotics-694 | MVSAnywhere README fixed commit 5bd49bb（S） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-694-mvsanywhere-readme-fixed-commit-5bd49bb.md) | direct-download；ok |
| SRC-robotics-695 | MVSAnywhere license fixed commit 5bd49bb（S） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-695-mvsanywhere-license-fixed-commit-5bd49bb.md) | defuddle；fallback_html |
| SRC-robotics-696 | Isaac Sim 6.2 NuRec neural volume rendering（S） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-696-isaac-sim-6-2-nurec-neural-volume-rendering.md) | defuddle；ok |
| SRC-robotics-697 | Isaac Sim 6.2 NuRec rendering utilities（S） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-697-isaac-sim-6-2-nurec-rendering-utilities.md) | defuddle；ok |
| SRC-robotics-698 | Isaac Sim 6.2 requirements（S） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-698-isaac-sim-6-2-requirements.md) | defuddle；ok |
| SRC-robotics-699 | Niantic embodied AI plans 2026-11-10（A） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-699-niantic-embodied-ai-plans-2026-11-10.md) | defuddle；ok |
| SRC-robotics-700 | Niantic Places Library 2026-11-10（A） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-700-niantic-places-library-2026-11-10.md) | defuddle；ok |
| SRC-robotics-701 | Flexion Reflect v1.0 architecture and limitations（A） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-701-flexion-reflect-v1-0-architecture-and-limitations.md) | defuddle；ok |
| SRC-robotics-702 | Niantic sample asset and benchmark evidence packet（S） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-702-niantic-sample-static-inspection.md) | bounded-http-range-and-openusd；ok |
| SRC-robotics-703 | MVSAnywhere simple demo fixed source（S） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-703-mvsanywhere-simple-demo-fixed-source.md) | github-connector-fixed-commit；ok |
| SRC-robotics-704 | Local project compatibility hash recheck for Niantic Flexion（S） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-704-local-project-hash-recheck.md) | local-sha256-recheck；ok |
| SRC-robotics-705 | MuJoCo modeling mesh collision semantics（S） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-705-mujoco-modeling-mesh-collision-semantics.md) | defuddle；ok |
| SRC-robotics-706 | Flexion copy of Niantic joint workflow（A） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-706-flexion-copy-of-niantic-joint-workflow.md) | defuddle；ok |
| SRC-robotics-707 | MuJoCo experimental OpenUSD importing（S） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-707-mujoco-experimental-openusd-importing.md) | defuddle；ok |
| SRC-robotics-708 | MuJoCo mesh collision XML reference（S） | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-708-mujoco-mesh-collision-xml-reference.md) | defuddle；ok |

## 核阅定位与版本

- 联合发布为2026-07-20；Niantic与Flexion副本是同一合作方披露，不算两个独立实验。正文、嵌入图表和现场演示分别归因。
- [原始HTML](../../raw/robotics-embodied-ai/documents/SRC-robotics-689-niantic-flexion-blog.html)保留`var SCENES`及图表字段；[基准JSON](../../raw/robotics-embodied-ai/data/niantic-flexion-benchmark-embedded-2026-11-10.json)、[8行基准CSV](../../raw/robotics-embodied-ai/data/niantic-flexion-navigation-benchmark-2026-11-10.csv)来自该结构。1024是每个条件的作者评测次数，原值比例已舍入，不反推精确整数分子。
- HF样例固定revision `f7ca59406bf15cdaf28e9c95bb99a317ebd7c83c`；[原始metadata.csv](../../raw/robotics-embodied-ai/documents/SRC-robotics-692-niantic-sample-metadata.csv)与API真实路径/bytes均保存；metadata部分Particle Field文件名省略后缀，衍生清单按tree。
- MVSAnywhere固定commit `5bd49bba0992aa56060e1aa3bb40b2150b04726f`：README、LICENSE及simple_demo。README/固定源码仅说明组件用法，不证明商用后端/导航训练全配方可复现。
- Isaac文档固定6.2.0；MVSAnywhere与资产版本分别绑定，避免用新版能力回填7月实验。
- MuJoCo stable已有实验性OpenUSD导入，需构建启用USD；支持文件格式不证明NuRec原生渲染或当前本地固定构建已支持。普通mesh凸包碰撞依据XMLreference，不能误把exact惯量模式当任意凹形碰撞。

## 捕获限制和补充

- 19项本轮capture为ok；695通用Defuddle对无扩展名纯文本LICENSE走网页解析后fallback。已用GitHub connector取得[完整固定版LICENSE补充](../../raw/robotics-embodied-ai/documents/SRC-robotics-695-mvsanywhere-license-github-supplement.txt)，保留原fallback、原错误和补充路径。
- MVSAnywhere源码条款明确非商业用途；样例资产数据卡为CC-BY-4.0；服务计划写training rights。三者对应不同产物，不能混用。
- 本轮脚本返回1受合并manifest历史failed项影响；具体以本轮source rows和补充路径为准，不把退出码解释成20项全部失败。
- 未取得该合作完整导航代码/权重、逐rollout原始日志、office复现实验资产或完整直播内容。未逐帧审核视频。

## 样例静态检查证据

- [局部HTTP Range与OpenUSD检查包](../../raw/robotics-embodied-ai/data/niantic-sample-asset-inspection-2026-11-10.json)：固定HF API信息、完整文件tree、ZIP成员目录、成员hash/CRC与网格API字段。
- [8项资产库存](../../raw/robotics-embodied-ai/data/niantic-sample-assets-inventory-2026-11-10.csv)：实际路径、bytes、API标示LFS SHA256。除Pondicherry部分成员外都只是元数据检查；没有本机验证完整LFS hash。
- 只读Pondicherry NuRec包三个成员，保存在`SRC-robotics-702-selected-usdz-members/`；未下载`sim.nurec`，未组成完整可渲染stage。mesh有碰撞API、不可见、259296点/499999面；几何与视觉对齐/物性/接触/吞吐均未测。
- 孤立mesh layer单位/轴值为未authored的fallback，不能据此声明100倍尺度bug；根stage1米/Z-up和局部变换须在完整composition下验证。
- OpenUSD工具由临时uv环境提供（0.26.11），有架构假设warning但成功解析。没有更改机器人项目依赖或启动模拟器。

## 本地接口复核

- [本轮复核JSON](../../raw/robotics-embodied-ai/data/niantic-flexion-local-project-recheck-2026-11-10.json)：前轮688的8份文件SHA256均一致；Microduck与SO-101 HEAD、Microduck本地uv.lock hash和4项版本另记录。
- Microduck锁文件有修改，SO-101有未跟踪文档；文件/设计的存在不证明运行资格、安装产物、远程环境或真机迁移。

## 知识冲突与边界

- 详细联合发布真机常规导航“on par”与产品页“outperformed”并列保存；只将特定难例和常规表现分别解释。
- 97.8%是仿真易场景；难场景75%且有16%超时/9%跌倒；没有独立真机分母。
- 一处现场训练后的真机zero-shot，不是无真实扫描/预训练数据或未知场地通用；MVSAnywhere的zero-shot是另一实验对象。
- “同源几何/外观”不排除共同偏差；“USD可读”不保证NuRec神经渲染和碰撞表示一致。
- Vary beta、回流roadmap与enterprise API/训练数据排除等计划条款，需要按客户实际合同核实。

## 关联连接

- [[robotics-embodied-ai/research-notes/niantic-flexion-real2sim-zero-shot-project-fit-2026-11-10|Niantic／Flexion研究报告]]
- [[_sources/vlk-paper-code-project-fit-source-set-2026-11-10|VLK来源集]]
- [[_sources/wechat-3dgs-robot-simulation-data-real2sim-vlk|前驱微信来源]]
- [[robotics-embodied-ai/00-source-capture-index|机器人来源抓取索引]]
