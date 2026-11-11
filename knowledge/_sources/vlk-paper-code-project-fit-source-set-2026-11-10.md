---
title: VLK 论文、实现与本地项目适配来源集
type: source
date_created: 2026-11-10
last_updated: 2026-11-10
sources:
  - raw/robotics-embodied-ai/documents/SRC-robotics-680-vlk-paper-v1-full-text.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-681-vlk-paper-v1-pdf.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-682-vlk-author-project-recheck-2026-11-10.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-683-scenebot-author-project-and-demo-availability.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-684-scenebot-demo-readme-fixed-commit-430c29c.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-685-scenebot-fixed-source-inspection.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-686-vlk-website-readme-fixed-commit-fa01dab.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-687-chois-official-readme-fixed-commit-8ec585a.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-688-local-robot-project-compatibility.md
tags:
  - industry/robotics-embodied-ai
  - source-set
  - vlk
  - synthetic-data
status: active
---

# VLK 论文、实现与本地项目适配来源集

> [!summary]
> 支持 [[robotics-embodied-ai/research-notes/vlk-synthetic-data-zero-shot-project-fit-2026-11-10|VLK 深研报告]] 的九项一级资料与本地只读快照。论文全篇19页及附录已读；PDF第7/16/19页表1/3/4视觉核对。源码层只检查公开的SceneBot推理demo，不将其当VLK完整实现。

## 来源与捕获状态

| 编号 | 来源、等级与定位 | 原始工件 | 状态与限制 |
|---|---|---|---|
| SRC-robotics-680 | VLK paper v1 full text；S | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-680-vlk-paper-v1-full-text.md) | ok；正文、附录完整抽取；另存HTML保留接触自回归脚注。 |
| SRC-robotics-681 | VLK paper v1 PDF；S | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-681-vlk-paper-v1-pdf.md) | fallback_html；后缀缺少.pdf导致通用脚本走Defuddle，>5MB失败；fallback下载实际是PDF；原记录保留，已补PDF和逐页文本。 |
| SRC-robotics-682 | VLK author project recheck 2026-11-10；S | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-682-vlk-author-project-recheck-2026-11-10.md) | ok；本轮重新抓取，未覆盖679；Code入口仍为coming soon。 |
| SRC-robotics-683 | SceneBot author project and demo availability；S | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-683-scenebot-author-project-and-demo-availability.md) | ok；作者页仍标Code/Data Coming Soon；不能据此否认其repo已有推理demo。 |
| SRC-robotics-684 | SceneBot demo README fixed commit 430c29c；S | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-684-scenebot-demo-readme-fixed-commit-430c29c.md) | ok；固定430c29c；README性能陈述未运行验证。 |
| SRC-robotics-685 | SceneBot fixed source and repository inspection snapshot；S | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-685-scenebot-fixed-source-inspection.md) | ok；固定源码/元数据与文件树；未下载或运行ONNX。 |
| SRC-robotics-686 | VLK website README fixed commit fa01dab；S | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-686-vlk-website-readme-fixed-commit-fa01dab.md) | ok；固定fa01dab；只有网站，不是训练代码。 |
| SRC-robotics-687 | CHOIS official README fixed commit 8ec585a；S | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-687-chois-official-readme-fixed-commit-8ec585a.md) | ok；固定8ec585a；CHOIS前驱，不是G1适配。 |
| SRC-robotics-688 | Local Microduck and SO101 compatibility inspection 2026-11-10；S | [raw](../../raw/robotics-embodied-ai/documents/SRC-robotics-688-local-robot-project-compatibility.md) | ok；两个本地项目commit、逐文件SHA256与行号；设计不证明运行通过。 |

## PDF 补充与失败留痕

- [正式PDF副本](../../raw/robotics-embodied-ai/documents/SRC-robotics-681-vlk-paper-v1.pdf)：19页，7,605,284 bytes；SHA256 `5034ffea4a686e7ec3704fedf99b2f255106891659521e9baf4b32aee5d1aee4`。
- [逐页文本抽取](../../raw/robotics-embodied-ai/documents/SRC-robotics-681-vlk-paper-v1-pdf-extract.md) 与 [结构化JSON](../../raw/robotics-embodied-ai/documents/SRC-robotics-681-vlk-paper-v1-pdf-extract.json)：调用现有PDF脚本的pdftotext引擎；表格、公式以PDF复核，不把文本重排当原始布局。
- 通用捕获脚本的 `.html` fallback 实际为相同哈希PDF字节，保留原文件名及sidecar，不静默覆盖不可变源。manifest仍保留 `fallback_html`和原始>5MB错误，并记录成功补充路径。
- 脚本退出1还受合并manifest中的历史failed行影响；本轮680/682/683/684/686/687自动捕获为ok，685/688为手动一级快照ok，681有上述已恢复补充。

## 代码与本地证据边界

- VLK网站 `fa01dab376d81f1c361c203822437b6a2d8efe42`，源码树只含页面、样式、JS和展示素材。
- SceneBot作者demo `430c29c1801aceb813506d86f3a8cffeba250df3`；检查 `policy_runtime.js`、`contact_utils.js`、`loader.js`、`policy_meta.json`和局部LICENSE；不把元数据中的模型哈希当成本机核验结果。
- CHOIS `8ec585aa0200fd2a890ffb12897bcf69ae719463`；官方README仅用于前驱依赖/生成入口核验。
- 本地Microduck HEAD `29e887ecfbf5d37144759e5a9f8a176dfb83d547`，存在uv.lock修改；SO-101 HEAD `49119c1531c20a0928b5af0713738a729e629ae6`，存在未跟踪文档。仅哈希绑定的读取文件支持适配判断，无远端/安装产物/运行状态证据。
- 搜索中发现第三方 `project-instinct/omniretargeting` README自称re-implementation，未将其当论文官方OmniRetarget实现，亦未用于证明VLK管线可复现。

## 知识冲突

- P §4.3真机总数120与Table1行列合计240冲突；保留逐格计数。
- 每环境每模式4000条与10%留出、每模式1000条评测的对应未解释。
- 600GPU·h范围、31ms与63ms层次、Table4分项64.7ms与总项63ms存在口径/数值差异。
- 微信原文“真机微调”与作者论文/项目页的本工作设定不符；作者页“自动”也必须与手工场景标注区别。
- 完整讨论、证伪条件与下一步集中在报告，避免把文献不一致修成假事实。

## 派生数据

- [Table1逐格结果与分析者Wilson区间](../../raw/robotics-embodied-ai/data/vlk-experiment-table1-2026-11-10.csv)：24行，百分比和区间由原分子/分母计算；非独立实测。
- [数据链路与项目适配矩阵](../../raw/robotics-embodied-ai/data/vlk-pipeline-project-fit-2026-11-10.csv)：8阶段；SO-101/Microduck建议均为分析者判断。
- [成本参数和一致性复算](../../raw/robotics-embodied-ai/data/vlk-derived-cost-and-consistency-2026-11-10.json)：590.4GPU·h/环境等为算术估算，不包含全模型训练等成本。

## 关联连接

- [[robotics-embodied-ai/research-notes/vlk-synthetic-data-zero-shot-project-fit-2026-11-10|VLK 论文与实现深研]]
- [[news/2026-11-09-3dgs-robot-simulation-data-real2sim-vlk|前轮文章来源]]
- [[_sources/wechat-3dgs-robot-simulation-data-real2sim-vlk|微信来源卡]]
- [[robotics-embodied-ai/00-source-capture-index|来源抓取索引]]
