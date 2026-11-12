---
title: "Atlas 在 3D 重建与机器人仿真中的落地方案"
type: synthesis
date_created: 2026-11-12
last_updated: 2026-11-12
sources:
  - knowledge/_sources/atlas-reconstruction-simulation-source-set-2026-11-12.md
  - knowledge/news/2026-11-12-corl-atlas-feifei-li-lisa-su.md
tags: [industry/robotics-embodied-ai, atlas, world-model, 3d-reconstruction, simulation, real2sim]
status: active
---

# Atlas 在 3D 重建与机器人仿真中的落地方案

> [!summary]
> **选型结论：Atlas 已有值得做小样的资产生产接口，但目前不能作为“上传房间视频，即得到可开门、拉抽屉的机器人仿真”的现成系统。** 官方文档可追溯到 RGBD、SPZ、GLB mesh 和碰撞盒；对象分件、关节、物性与任务验证仍须补建。对本仓库，推荐保留实测结构＋MuJoCo 主线，把 Atlas 作为静态外观/背景资产候选；第二优先级是用已有物理场景的深度约束生成外观变化。文档与 schema 证据置信度高；本账号可用性、重建精度、时延和商业收益置信度低，尚未实测。

## 分类与研究边界

| 项目 | 内容 |
|---|---|
| 主分类 | R05 产品、平台与工具选型 |
| 次分类 | R04 技术原理；R07 商业落地验证 |
| 分类理由 | 从 CoRL 文章的生成/重建/仿真主张，追到实际输入、输出、接口与工程缺口，判断是否接入房间重建和机器人任务 |
| 截止日期 | 2026-11-12，Asia/Shanghai；未标日期的文档记录核查日，不当作发布日期 |
| 覆盖 | 官方 Atlas v2 文档、序列与坐标合同、mesh/碰撞资产、MuJoCo/Isaac 接口边界、三条落地路线、PoC 与成本 |
| 范围边界 | 当前房间场景需包含门与抽屉；训练/真机部署仍为后续阶段。本次只做公开资料、schema 静态检查和无认证健康检查，未安装 SDK、登录、上传房间、提交付费任务或运行仿真 |

来源起点为 [[news/2026-11-12-corl-atlas-feifei-li-lisa-su|微信文章八个要点]]，本次独立归档 25 项官方资料和 1 项本地核查记录；完整表见 [[_sources/atlas-reconstruction-simulation-source-set-2026-11-12|来源集]]。S 级文档证明接口被描述，不证明模型实际达到所需精度；公司 R2S2R 实验披露按 A 级处理。

## 1. 产品边界：五个东西分别选

| 名称 | 实际角色 | 对本任务的用途 | 尚不能据此认定 |
|---|---|---|---|
| Atlas 模型及 Developer API v2 | 相机/深度条件生成、重建、splat/mesh 等分步任务 | 可设计有资产输出的重建流水线 [777]、[778] | 账号已获权限、模型权重可下载、可本地部署 |
| Viewfinder / Atlas Studio | 构建与探索场景的界面 | 人工查看多视角、纠错和准备资产 | 现场录屏就是完整机器人仿真 |
| Frameboy | 云端生成帧的交互探索 | 快速看空间连贯性；适合演示 | 15 fps 是物理步频、机器人控制频率或导出资产本地帧率；见既有 SRC-robotics-775 |
| Marble / World API v1 | 另一个产品与旧 API 合同 | 可作为独立资产生成候选 | 旧模型名、请求或积分能直接用于 Atlas [798]、[799] |
| SceniX / World Labs R2S2R engine | 任务级重建、动力学对齐、训练与评测的专有系统 | 企业合作尽调候选 | 公开 Atlas API 已附送该系统、全部训练代码或任务资产 [797] |

**访问与部署事实**：Quickstart 给出生产 API 根 `https://api.atlas.worldlabs.ai/api/v2`，请求使用项目 key。文档仍在 `docs.atlas-beta.worldlabs.ai`，不要按文档域名自行推导服务地址。任务可用性依账号而定；没有取得本用户账户的功能清单。[777]、[778]

本次对上述生产根的 `/health` 发出一次无认证 GET，返回 HTTP 200 与 `status: ok`，仅证明**当前执行环境到该公开路由可达**。不证明授权、生成任务、付费能力或中国境内所有网络可用。[802]

## 2. 3D 重建的可执行工序

### 2.1 建议主流程

实拍照片/视频抽帧 → `images2PosedRGBD` → 检查相机、深度与尺度 → 必要时 `atlasGenerate` 补视角 → `posedImages2Splats` → SPZ → `splats2Mesh` → GLB / 碰撞盒 GLB → 本地分件、物理与仿真适配。

| 步骤 | 输入与输出 | 落地时的关键决定 |
|---|---|---|
| 采集 | 真实房间的透视照片；视频先抽成图像 | 官方建议单房间先用 8–16 张、相邻约 50% 内容重叠；是起点而非质量保证 [781]、[785] |
| 估计 | `images2PosedRGBD` 输出各帧 camera、RGB、线性深度 EXR 等 | 同一房间图像一起提交；若已有可信 D435i/COLMAP 位姿和深度，不能把它们塞给这个估计端点，应按下游 schema 组装 RGBD [782]、[792] |
| 几何检查 | 回投影、留出视角、实测长度对齐 | 先检查覆盖和结构，再决定是否补拍；不要优先依赖生成填补任务区证据 |
| 补视角（可选） | `atlasGenerate(contextFrames, targetCameras)`；后续需深度时开启 `returnDepth` | 请求内组织一组相机；大位移/越墙视角会增加虚构部分，序列上下文也不会自动跨独立请求共享 [780]、[783] |
| 构建外观 | `posedImages2Splats` 将 posed RGBD 转成 SPZ | 常见 refinement 本身还会生成/清理新视图；即使输入全是实拍，也不能称输出完全无生成补全 [784] |
| 提取表面 | `splats2Mesh` 输出 mesh；可加 `colliderBoxes` | 网格从所选视角渲染提取；没有视角看见的几何不会因此得到可信恢复 [790] |

**对真实重建的选择**：先保留“仅实拍输入”的版本；新增生成帧单独标注来源、相机、操作 ID 和审核结果，不能混成第二批真实测量。缺失的门背面、柜内、把手和接触面应补拍/实测。原图与生成图对应的错误，可能被后续 splat 放大，而不是自动修复。[784]、[785]

### 2.2 相机与尺度是接入中的第一道门槛

以下为官方合同中的关键点 [779]，实现时必须看完整页和 schema：

- 位姿是 **camera-to-world**；四元数是 **XYZW**。OpenCV world-to-camera 需先求逆；MuJoCo 四元数表示需按目标字段重新排列。
- `rub` 为相机右/上/后、朝 −Z；`rdf` 为右/下/前、朝 +Z。切换需要变换旋转基，不能只换字符串。Atlas 文档的 RUB 世界为 Y-up，Blender 常用 Z-up，世界轴也须转换。
- 内参使用像素单位；resize/crop 要同步修改内参和 RGB、mask、depth 的网格。
- EXR 是沿相机光轴的线性深度，不是射线长度；跳过 `NaN`，不能填成零表面。Three.js CPU 解码 EXR 时还要检查行方向。
- 多图恢复到共同坐标，并不自动得到实测米制尺度。要用已知尺寸或可信相机基线标定，并同步缩放相机平移与深度。

建议以实测点拟合整体相似变换：`p_sim = s · R · p_atlas + t`。`s` 是尺度；`R,t` 是轴向/原点对齐；相机位置、mesh、碰撞盒、关节锚点必须采用同一映射。**这是工程建议**，不是 Atlas 的误差指标。

### 2.3 输出合同和细节损失

`posedImages2Splats` guide 说明 refined 输入 2–512 帧，使用同一种受支持的图像网格；典型耗时 15–25 分钟是文档估计。SPZ 可供可视化或再提 mesh，不等于物理体。[784]

`splats2Mesh` 提供纹理/顶点色、目标面数、区域框与取样相机等配置；碰撞盒另作为 GLB 输出，盒子保持竖直，仅绕竖轴转动，降低盒子数会更松地包围几何。它们适合粗碰撞候选，不能直接推为薄门、把手或抽屉内部的精确碰撞。[790]

mesh 默认提取网格分辨率为区域最长边 512 格。**分析示例**：若区域长 5 m，单格约 9.8 mm；这只是离散网格尺度，不是精度承诺。整房 mesh 不宜承担毫米级操作接触；应按任务区拆分重建，并比较提取分辨率、耗时和细节。[790]、[802]

## 3. 三条落地方案

### 方案 A：Atlas 静态资产＋实测物理场景（当前推荐）

**适用**：先让自己的房间可浏览、可编辑、有碰撞和复位，门与抽屉可开合。

1. 选一个工作台及其旁边的柜体做小样；固定门/抽屉状态采集，多状态分成不同证据组。
2. 用 Atlas 产出静态外观、mesh 候选；用尺寸清单与独立留出照片检查。关键结构不合格时回到实测 CAD/传统重建。
3. 将墙地面、柜体、门板、抽屉、把手分开；从静态背景移除可动物，避免运动后原位置残留一份。
4. 在 MuJoCo 建 body 树、碰撞代理、门 `hinge`、抽屉 `slide`，录入真实轴、锚点、行程/限位、质量与阻尼。GLB 不能直接当作 MJCF mesh：按当前 mesh 入口转换为 OBJ/STL 等，纹理与变换另验。[800]
5. 先在 mesh 视图验收碰撞、开合、复位；再考虑逐 link splat 与物理 pose 同步。沿用既有 [[door-drawer-interactive-reconstruction-code-audit-2026-11-10|DISCOVERSE 核查]]；此前有限 body 映射探针不等于此处 SPZ 可直接接入。

**缺口**：本次 inspected API 没有提供可交付的门/抽屉 link 树、关节限位、质量/摩擦与机器人动作接口。若 mesh 是一个整体，仍须切分/重建；`atlasChisel` 改出一扇“打开的门”也不能替代关节定义。[790]、[791]、[792]、[793]、[794]、[802]

**引擎分支**：Isaac 可作为 USD 场景分支，但仍需添加 rigid body、collision、物理材料、joint 与 local frames。显示 mesh 和产生碰撞是不同层；动态凹形物体需要合适的碰撞近似。[801] 本次不增加第二套引擎的实施负担。

### 方案 B：已有物理场景＋Atlas 外观变化（第二优先）

**适用**：几何已可靠，希望生成不同材质、背景、光照风格，扩大视觉评测覆盖。

用实测/MuJoCo/Isaac 场景渲染固定相机的深度 → `atlasChisel` 深度条件生成 RGB → 多视角检查 → 离线视觉回放或后续训练数据。原始物理状态、动作与成功标签仍由物理任务产生。官方教程明确区分深度条件 restyle 和有 RGB/mask 的局部编辑。[794]

这条路径更容易保留可审计的几何源，但**深度条件不是像素级守恒证明**。需查物体轮廓、把手、遮挡、相机及动作可见性；生成过程改变目标或关键遮挡时，不应沿用原标签。逐帧生成也不能未经时序验收当作连续机器人视频。

建议先离线生成，不把网络生成放入刚性实时控制循环。若以后要做策略评测，分开比较：真实观测、原仿真渲染、Atlas 增强渲染；同一组任务状态，避免把几何变化误当成外观增强收益。是否涉及条款中的竞争性 benchmarking 需在实验范围确定时核对。[795]

### 方案 C：企业 R2S2R 合作（证据不足，条件分支）

公司目前公开了操作任务的 sim/real 对齐、长时运行展示和策略评测协议；ALOHA 评测描述每 checkpoint 2,000 次仿真、100 次真机，分 ID/OOD。[797] **这属于专有 R2S2R engine 的公司证据**，不能归到公开 `atlasGenerate` 的独立能力，也不能把所有材料自动归因为 Atlas。

若将来采购，需让供应方交付：具体机器人/传感器适配、可下载的场景与关节物性、相同开环动作回放、策略排名/失败边界、失败恢复和升级合同。现未取得本项目适配、报价、付费客户复购、完整实现和可复现实验资产，不作为当前首版依赖。

## 4. 导航与操作应用的不同验收

| 场景 | Atlas 可承担的部分 | 必须外补的部分 | 先测什么 |
|---|---|---|---|
| 房间/工位预览 | 多视角外观、静态 splat/mesh | 尺度及未观察区域标注 | 返回原视点是否一致，尺寸/通道是否失真 |
| 室内导航 | 背景、相机外观、粗静态碰撞候选 | 地面/台阶、机器人动力学、传感器、可通行地图 | 碰撞体是否封住真实通路，视觉与碰撞是否对齐 |
| 抓取/放置 | 场景外观及部分物体表面候选 | 手/物体精确几何、质量、摩擦、碰撞与控制 | 抓取点、接触面及状态标签可信度 |
| 开门/拉抽屉 | 柜体外观、可见表面 | 分件、背景去残影、轴与行程、内壁/背面、关节接触 | 全行程碰撞、开合/复位、物理与外观同步 |
| 线缆/柔性操作 | 研究展示线索 | 可复现柔性物理、接触参数与动作闭环 | 不由视频/外观相似性推断动态可靠性 |

导航侧可把 [[niantic-flexion-real2sim-zero-shot-project-fit-2026-11-10|Niantic/Flexion]] 作为公开场景流程参照，操作侧参考上述实测分件主线。二者均不是 Atlas 的即插即用依赖。本仓库当前优先完成场景层，不提前启动策略训练。

## 5. 最小验证计划与停止条件

以下数量、精度和预算均为**建议验收设计，未执行**。表格版见 [PoC 验收清单](../../../raw/robotics-embodied-ai/data/atlas-reconstruction-simulation-2026-11-12-acceptance.csv)。

| 阶段 | 交付与拟定门槛 | 未通过时怎么做 |
|---|---|---|
| P0 接口与使用条件 | 账号实际具有四项所需任务；确认费率、额度、内容设置、导出用途；保存服务/schema 版本 | 无权限或条款不适配则止于公开样例，不让项目依赖该服务 |
| P1 固定小样 | 一处工作台＋一扇门＋一个抽屉；8–16 张输入，另留至少 4 张不入模照片；测量至少 3 个独立尺寸 | 模糊/覆盖不足先补拍；保持门抽屉状态一致 |
| P2 几何检查 | 实拍输入优先；背景尺寸误差拟定 ≤1%；关键把手/间隙不用未经验证的生成几何 | 失败则减小区域/补拍，关键部分改实测 CAD |
| P3 静态仿真 | 可通行区域、桌面与碰撞重合；盒子不过度封堵；保存 mesh、碰撞、变换和来源清单 | 修碰撞代理，不用一个房间凸包封住整个室内空间 |
| P4 关节场景 | 门角误差拟定 ≤2°、抽屉行程误差 ≤3 mm；建议 20 次开合/复位，无数值发散和不可接受穿透 | 按任务公差收紧；物性/轴向未明先回测，不能用外观掩盖 |
| P5 视觉增量 | 固定相机和关节状态，审查静态/动态外观残影与标签；记录返工、人工小时和云成本 | 结构/标签被改变则淘汰该增强；总工时无收益则停用 Atlas 支路 |

关键接触结构的几何公差应小于任务允许间隙的一部分，不能用“整房 1%”代替；毫米级目标由实测建模承担。P4 是场景测试，不是已验证的机器人开门策略。

未来进入机器人训练/评测时，再增加真实留出任务、成功/碰撞/接管率、节拍和策略排名验证。闭环真实性不能由本次静态文档检查替代。

## 6. 成本、稳定性与运维

| 项目 | 2026-11-12 可引用口径 | 不能据此外推 |
|---|---|---|
| Atlas 积分 | 官方 billing：1 USD = 1,000 credits [786] | 不混用 World API 的 1,250 credits/USD [799] |
| Splat 构建 | guide 列 refined 5,000 credits / $5，draft 500 / $0.50；失败免费 [784] | 草稿 `refine:false` 与 schema 有冲突，未解决前不能写入预算执行方案 |
| Frameboy | 官方计费说明最长一分钟会话 500 credits / $0.50，有短会话/故障例外 [786] | 不等于重建一个房间只要 $0.50 |
| 单资产总价 | pose、生成视角、mesh 等实时价目待平台确认 | 不编造完整每房间报价或总工期 |
| 容量与服务 | rate limits 页未公开最终配额；按任务排队、保留 operation ID、幂等重试 [787] | 无法从网页并发或旧 API 配额承诺批量产能/SLA |

**分析预算公式**：`总成本 = API 实际账单 + 本地/云渲染与存储 + 采集/标定工时×费率 + 分件/物理/质检工时×费率 + 返工 + 维护`。PoC 可先给 Atlas 支路设 **$30 人工监控预算**，这是本报告建议上限，不是足额报价；费用未知时逐步提交，不保证账户限制精确阻断所有在途费用。[786]

按文档 refined 单次 $5 计算，2 次为 $10，6 次为 $30；**仅是 splat 工序算术**，不含 pose、生成、mesh、人工等。若反复重建已无几何/工时改善，就不应为了画面更漂亮继续扩大投入。

保存每次的请求摘要、operation/asset ID、下载文件 hash、相机/尺度变换、接受/拒绝原因和账单；调用完成只在 `done=true` 且没有 error 后使用输出。SDK/CLI 可选，当前不必安装才能完成方案尽调。[777]、[789]

## 7. 知识冲突、失败模式与反方证据

1. **“还没有可接入资料”的旧结论需细化**：前一轮按发布博客/现场文章判断资产链未核实；本次发现 v2 文档明确 SPZ、GLB 与碰撞盒。更新的是本仓库证据覆盖，不能写为 API 今日才上线。仍未证明本账号获准调用。
2. **草稿接口冲突**：guide 声称 `refine:false`；同日归档 `PosedImages2SplatsRequest` 仅有 `webhookUrl/purgeContentOnOperationCompletion/prompt/enhancePrompt/regionOfInterest/posedFrames`，`additionalProperties:false`。静态 schema 不接受教程字段；未向线上发错误请求，无法确认服务与文档谁先更新。见 [784]、[791] 和 [核查 JSON](../../../raw/robotics-embodied-ai/documents/SRC-robotics-802-atlas-schema-health-audit.json)。
3. **视频/4D 展示与公开工作流有边界**：视频指南当前要求抽静态帧；同步多机可冻结一个瞬间，但没有开放连续动态时间控制。单目走拍的不同时间帧，不能当作同时刻多视角。[781]
4. **生成一致性不足有官方反例**：文档展示桌子变形/重复并进入 splat，另有薄结构、窗玻璃、白墙和缺失地板等失真。不能把所有生成视图未经检查地回灌。[785]
5. **SPZ/GLB 导入与可交互并不等价**：API 的场景渲染/盒状碰撞不提供门轴辨识或可靠接触。MuJoCo 常规 mesh 碰撞用凸包；整房一块几何可能封死凹空间。[790]、[800]
6. **渲染集成仍有具体依赖**：官方 Blender 页的版本/原生 splat 支持尚未在本机验证；SPZ 不应改后缀冒充既有 PLY。当前逐 link 渲染器是否能读输出、深度合成与遮挡是否正确另验。[788]

**证伪条件与监测**：若明确提供了可用的分件/关节/物性导出，可上调自动化判断；若留出尺寸、开合测试或返工成本不达标，则只保留外观用途。监测服务/schema 变化、task 权限、每可用资产的 API/人工成本、几何误差、生成部分占比、碰撞封堵和复位失败。

## 8. 中国场景与商业应用可能性

**产业判断**：可复用的机器人仿真资产、验证工具与工业场景数据，契合本库 [[robotics-embodied-ai/03-market-and-policy|机器人应用与智能制造政策框架]]；本报告不据此推断 Atlas 获中国采购准入、政策补贴或国产化资格。中国团队的现场工程、机器人集成和垂直工艺知识可作为切口，闭源云服务、模型权限及任务数据出境条件则是依赖。

| 优先场景 | 使用者／决策和付款主体（待访谈确认） | 价值与成熟度 | 从试点到复制的门槛 |
|---|---|---|---|
| 工位/实验室资产制作 | 仿真工程师；研发负责人；研发/集成预算 | 降低场景准备和改版工时；Atlas 接口可设计 PoC，未见本项目实测 | 统一量测与导出合同、可动件正确、版本可维护 |
| 导航视觉回归与工位外观变体 | 感知/测试团队；测试负责人；研发/测试预算 | 扩大视觉覆盖；收益需真实失败案例验证 | 真实留出集、标签有效、每有效案例成本可控 |
| 高接触操作任务评测 | 策略/自动化团队；业务＋研发采购 | 专有 R2S2R 有公司展示；完整 Atlas 公共方案仍不足 | 接触动力学、真机预测能力、稳定交付和故障恢复 |

人工/传统 mesh 是主要替代方案。价值用“每个**验收合格**场景的总工时/费用、改版周转、可重复复位与发现真实回归的能力”衡量；生成速度或下载文件数不够。部署成本还包括数据采集、标定、模型服务版本、坐标/格式适配、人工分件、质检及现场复测。未获得付费试点、回款、复购或规模订单证据，不把 API 能力当成商业闭环。

**时间判断**：近期 1–2 年，静态资产辅助与视觉回归是中等置信度机会；精细交互的全自动重建为低置信度。中期 3–5 年，若对象化、物理辨识、服务可靠性与成本显著改善，可扩展到任务级仿真交付，置信度中低；此为情景判断，不是产品路线承诺。

**直接影响选型的条款**：当前 TOS 区分低档与合资格付费输出的用途，内容可能用于改进/训练、付费档有前瞻 opt-out 机制，并列出竞争性用途/benchmarking 限制；部分分享设置可能默认公开。企业实际权限、工厂资料处理及再交付权应按账户与 Order Form 核对。[795]、[796] 不应以公开文档代替本客户的具体许可，也未据此开展数据上传或竞品测试。

## 9. 中小型创业者的机会

以下是机会假设，尚未做客户访谈或验证收费。

| 分层 | 切口与最小交付 | 团队/资金/周期（建议） | 客户为何可能采购及复购 |
|---|---|---|---|
| 可立即验证 | 单工位“实拍＋尺度＋可开合资产＋验收报告”，先以本地方案交付，Atlas 作可替换插件 | 2–3 人，覆盖三维/仿真与现场测量；资金低到中，以人力为主；2–4 周访谈与样品周期 | 首批找机器人实验室/集成商；客户买可用场景与省下的工时；设备、布局与产品更新可产生复购 |
| 可立即验证 | SPZ/GLB→对象化碰撞/关节的检查、格式适配与版本报告 | 需要三维格式、MJCF/USD、自动校验和人工复核能力；预算先覆盖实际样品 | 基础模型不天然掌握客户门轴/工艺公差；集成经验与验收记录形成积累 |
| 需要条件成熟 | 有真实失败集的视觉/策略回归服务，或企业 R2S2R 的垂直集成 | 需要客户策略/场景访问、算力和试点合作，资金中等 | 只有当仿真筛查能减少客户硬件试错时才有持续预算 |
| 不建议进入 | 从零训练通用 Atlas 替代模型；无授权转售 API；承诺单图自动恢复全部物性与关节 | 资本/数据/研究周期高，或交付与用途边界不成立 | 难用小团队形成可验证差异，也难承担误差与现场维护 |

潜在合作方为机器人集成商、扫描/CAD人员和客户仿真团队。收费先围绕明确资产与验收，不假定供应商 SDK 永久可用；长期壁垒来自垂直任务模板、标定方法、对象库、真实错误与版本迁移记录。若基础平台未来自动完成这些步骤，小团队仍需靠现场知识与闭环验证，而非一次格式转换。

## 10. 下一步与完成状态

| 项目 | 状态 | 下一验证 |
|---|---|---|
| 官方资料、schema、格式、公开健康路由核查 | 已完成本轮静态调研 | 后续调用前重新固定 schema 和账户能力 |
| 三条路线、候选/能力/验收 CSV、预算方法 | 方案已完成 | 按 P0–P5 执行一个小样 |
| 本用户 Atlas 权限、完整单任务价格和数据设置 | 待验证 | 登录平台或取得项目功能/费率说明 |
| 自有房间重建、GLB/SPZ 实物文件检查 | 未执行 | 使用已确认可上传的样片和实测尺寸 |
| 门/抽屉导入、碰撞、开合/复位及外观同步 | 未执行 | 完成 mesh 首版，再判断 GS 增量 |
| 真机/训练、客户 ROI 与复购 | 未执行 | 当前不阻塞场景层；另立实验与业务验证 |

**执行建议**：下一步先取同一工作台的固定小样，做“传统/实测主线＋Atlas 资产支路”的功能验收，而不是直接重建整房或训练机器人。API 权限、任务费率或草稿 schema 未清楚时，先准备离线采集、标定和分件，不阻塞已有房间方案。

## 关联连接

- [[_sources/atlas-reconstruction-simulation-source-set-2026-11-12|26 项来源与本地核查]]
- [[news/2026-11-12-corl-atlas-feifei-li-lisa-su|CoRL 文章要点]]
- [[interactive-room-sim-reconstruction-alternatives-2026-11-10|可交互房间重建主线]]
- [[door-drawer-interactive-reconstruction-code-audit-2026-11-10|门与抽屉代码证据]]
- [[so101-workbench-pilot-capture-sop-2026-11-10|手机＋D435i 小样采集 SOP]]
- [[3dgs-ply-to-simready-assets-for-robot-simulation-2026-09-22|3DGS 到 SimReady]]
- [[robotics-embodied-ai/00-index|机器人研究入口]]

## 来源与数据文件

- [能力与缺口矩阵](../../../raw/robotics-embodied-ai/data/atlas-reconstruction-simulation-2026-11-12-capabilities.csv)
- [五种入口与方案比较](../../../raw/robotics-embodied-ai/data/atlas-reconstruction-simulation-2026-11-12-routes.csv)
- [建议验收清单](../../../raw/robotics-embodied-ai/data/atlas-reconstruction-simulation-2026-11-12-acceptance.csv)
- [schema 与健康检查记录](../../../raw/robotics-embodied-ai/documents/SRC-robotics-802-atlas-schema-health-audit.json)

[777]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-777-atlas-developer-api-quickstart.md
[778]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-778-how-to-use-atlas.md
[779]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-779-atlas-cameras-and-posed-images.md
[780]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-780-atlas-build-a-scene-from-images.md
[781]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-781-atlas-using-video-footage.md
[782]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-782-atlas-images-to-posed-rgbd-guide.md
[783]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-783-atlas-generate-views-walkthrough.md
[784]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-784-atlas-posed-images-to-splats-guide.md
[785]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-785-atlas-splat-best-practices.md
[786]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-786-atlas-billing.md
[787]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-787-atlas-rate-limits.md
[788]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-788-atlas-blender-integration.md
[789]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-789-atlas-general-best-practices.md
[790]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-790-atlas-splats2mesh-openapi-schema.md
[791]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-791-atlas-posedimages2splats-openapi-schema.md
[792]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-792-atlas-images2posedrgbd-openapi-schema.md
[793]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-793-atlas-atlasgenerate-openapi-schema.md
[794]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-794-atlaschisel-scene-editing-tutorial.md
[795]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-795-atlas-terms-of-service.md
[796]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-796-atlas-data-processing-addendum.md
[797]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-797-building-worlds-that-train-robots-r2s2r.md
[798]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-798-marble-available-models.md
[799]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-799-marble-world-api-pricing.md
[800]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-800-mujoco-xml-reference-snapshot-2026-11-12.md
[801]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-801-isaac-sim-physics-simulation-fundamentals.md
[802]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-802-atlas-schema-health-audit.md
