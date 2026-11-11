---
title: 可交互房间Sim重建：目标收敛、候选比较与执行路线
type: synthesis
date_created: 2026-11-10
last_updated: 2026-11-10
sources:
  - SRC-robotics-742–757
  - SRC-robotics-727–728
  - SRC-robotics-738–739
tags:
  - real2sim
  - interactive-scene
  - reconstruction
status: active
---

# 可交互房间Sim重建：目标收敛、候选比较与执行路线

> [!summary] 当前任务的正确目标
> **把执行SO-101实验的真实房间重建成可浏览、可编辑、物体可独立运动且具备碰撞／支撑／关节约束的仿真场景。** 本轮不选择ACT／PPO／VLA，不训练策略，不部署真机。SO-101在这里至多是一个场景资产，暂不要求控制它完成任务。

> [!important] 选型结论
> 可控交付主线是**米制房间重建＋对象化mesh＋实测碰撞／关节＋MuJoCo交互**；需要Gaussian外观时优先核验**DISCOVERSE运行时**的现有物理／外观联动。自动化研究重点改为**ϕ-RIE／PhiView与SimFoundry**，但两者都有完整流程依赖缺口，尚不足以替代可控主线。RialTo GUI提供手工分件与关节标注参考；RoboSimStudio适合物理交互编辑，不能自动等同整房摄影测量。

当前完成官方固定提交、许可、源码局部和依赖核查，没有生成用户房间、启动任何候选、运行模型或验证实时效果。用户已确认（2026-11-10）：**首版同时需要门、抽屉开合**，与刚体移动／碰撞／复位并列验收。具体门与抽屉数量及结构待现场清单确认；柔性物体不作为默认交付。

## 1. 分类与研究范围

主分类R05（工具与工作流选型），次分类R04（场景表示、物理重建）、R06（候选比较）。沿用开源与可本地控制的偏好，评价轴改为：输入要求、对象拆分、背景去除、几何／碰撞一致性、交互操作、关节支持、物性来源、许可与可复现性。移除策略训练和真机成功率，不用机器人支持数量给场景重建排序。

截止2026-11-10，来源限官方仓库／项目文档与固定代码；跨全球比较用于本地实验房间选型。重点核查6类候选，另列RoboGSim线索，未穷举所有新论文。自采照片＋D435i继续沿用；不因候选只接视频就丢掉已采深度与实测尺度。政策、投资和市场规模不属于当前技术交付。

## 2. 什么才算“可交互”

| 层级 | 应有能力 | 能证明什么／尚不能证明什么 |
|---|---|---|
| I0 浏览 | 相机漫游、缩放、切视角 | 只是可看；不证明任何物理 |
| I1 编辑 | 选中对象、平移／旋转、改布局、存取场景 | 对象可分离；直接改位置还不算物理接触 |
| I2 刚体物理 | 重力、碰撞、支撑、推移、释放落下、状态复位 | 可做物理互动；不自动说明质量／摩擦真实 |
| I3 关节物体 | 门轴、抽屉滑轨、限位、阻尼、开合 | 必须有分件与joint定义，不能仅依外观猜测 |
| I4 柔性／复杂接触 | 线缆、布料、软垫、液体等 | 独立物理建模与动态实验；普通刚体扫描不覆盖 |

首版交付要求**I0＋I1＋I2＋I3**。I3对清单中的门／抽屉逐个纳入，不能只演示任意一件代替全部；不承诺全屋所有物品都自动具备真实物理。鼠标拖动需分清“编辑模式直接改pose”与“仿真模式施力／约束拖拽”，两者分别验收。

## 3. 候选重新比较

| 候选 | 对可交互重建真正提供的能力 | 关键限制 | 本项目角色 |
|---|---|---|---|
| **分层mesh＋MuJoCo** | 手机／RGB-D恢复房间，Blender分件、材质、关节，MuJoCo提供刚体碰撞与交互 | 资产整理、背景补拍和参数标定需人工；鼠标编辑／保存工具需按缺口补齐 | **主线与验收基准**；组件许可见前轮727／728／738／739 |
| **DISCOVERSE＋Real2Sim** | MJCF物理＋按物体／link组织的Gaussian外观，运行时按MuJoCo状态更新GS；另有mesh→GS等资产工具 | 背景与动态对象仍需拆分、配准；Real2Sim工具链与Gaussian依赖不自动继承运行时MIT | **优先验证的高保真交互运行时** [744][745][754] |
| **ϕ-RIE／PhiView** | 从扫描场景发现／生成对象，米制配准、去除原对象并补背景，连接物理和外观；有移动、投射物、物性编辑界面 | 完整交互构建API依赖单独PhiRoom兼容后端；模型／数据门槛；生成背面与物性不是测量真值 | **最贴题的自动化研究候选，先验证访问与依赖** [742][743][750] |
| **SimFoundry** | 视频→对象分割／mesh／位姿／物性注释→OmniGibson，支持刚体及articulation生成、场景编辑 | 默认Gemini与gated模型；多项非商业／自定义条款；自动背景生成仍列待发布，真实精度需检查 | 自动化对象化与关节生成对照，不作全本地开源默认 [747][757] |
| **RialTo GUI** | 导入扫描mesh、切分对象、标fixed/revolute/prismatic关节、导出USD后运行物理 | 手工操作多；教程用商业采集入口，根许可未见完整声明；Isaac依赖另算 | **门／抽屉分件和关节标注的方法参考** [746][756] |
| **RoboSimStudio** | 交互搭建物理任务，显式调solver／接触／摩擦／刚度，人工或agent迭代 | 不是整房自动扫描器；Alpha、Linux／GPU新栈；照片级房间外观另建 | 对接触／柔性对象需求再评估 [748][755] |
| **Re3Sim** | 场景几何＋GS背景＋独立物体资产，用于高保真仿真 | Isaac依赖、较旧环境；README CC BY-NC 4.0；以数据生成为主，不以房间编辑器为主 | 重建／分层表示参考，不进入首轮部署 [749] |

优先级按当前证据与本任务匹配度，不按论文成功率或宣传“小时级”排序。

## 4. 两个最容易误判的候选

### 4.1 ϕ-RIE：功能非常贴题，但前端公开不等于全流程已通

固定PhiRIE提交`a03543f6472451ffc079502417a48d64c2a6e7f1`已包含PhiView源码，主代码MIT。它把对象身份、生成mesh、碰撞体、原场景Gaussian去除及背景补全放在同一流程里，正面处理“杯子移走后桌上仍留一个杯子”的问题。[742]

但`docs/PHIVIEW.md`明确要求交互编辑／注册API连接兼容PhiRoom后端`26f834ca3468e21c584abd5808082a0b2fdf4c66`，需要访问`RunyiYang/PhiRoom`；替换成当前公开PhiRIE树用于交互构建**尚未验证**。因此可说构建代码和界面源已公开，不能保证匿名下载两个仓库就能完成全流程。[750][756] 本轮未取得该后端，网页cache miss不等于证明仓库一定私有。

`run_video2sim.sh`确有从手机视频构造场景目录、训练GS、对象生成／配准、物性与MJCF导出的入口。[751] 但完整脚本还包含机器人评估suite，本任务应拆出场景阶段，不照抄一键执行全链。独立PhiView仓库也声明doctor检查路径／元信息而非模型推理；import／doctor通过不能当场景成功。[743]

物性注释使用语言模型，示例物体质量和隐藏碰撞几何在文档中标为近似。可以演示改变mass／friction后的响应，不证明自动推得了真实mass／friction。[742][750] 自动化生成的遮挡背面和背景补全必须标来源，不能代替补拍测量。

### 4.2 DISCOVERSE：已存在物理与GS状态桥，仍须自己制作可靠资产

固定`d67f47c084aba0e0cf422a8725235f8b9238655a`的`simulator.py`读取`gs_model_dict`，创建`GSRendererMuJoCo`，渲染时调用`update_gaussians(mj_data)`。这说明已有物体状态驱动GS的实现，不必把它当“只有漂亮视频、没有联动代码”。[754]

但它不从一张场景PLY自动推导每个物体的碰撞／质量／关节。独立Real2Sim工具以mesh或生成模型创建对象，再经Blender与Mesh2GS处理，明确说明所谓重打光是烘焙进GS外观，并非运行时真正PBR。[745] 门、抽屉仍需逐link资产和关节定义，背景对象也要去除。

核心运行时MIT不覆盖全部生成／Gaussian依赖。Real2Sim仓库根未见LICENSE，不能由MIT外推授权；如果复用受研究限制的原始Gaussian组件，就不能把整链叫完整宽松开源。先做依赖核查；遇到受限组件可换为有明确许可的自建mesh／gsplat路径，但替换是开发工作，不是已验证功能。[744][745][756]

## 5. 推荐的重建表示与数据结构

整个房间分成三层，而非一张大网格：

1. **固定结构**：地板、墙、天花板、固定工作台／柜框。视觉可用带贴图mesh或GS，碰撞用清晰分块代理。每层保留真实米制尺度。
2. **可动刚体**：杯子、盒子、椅子、工具。每件有独立坐标、视觉资产、碰撞体和物理参数；从背景中去除对应旧外观。杯壁、开口、把手不许被凸包封死。
3. **关节物体**：门板／门框、抽屉／柜体按link分件，定义轴心、轴向、类型、上下限和阻尼。扫描关门状态不能自动知道内部尺寸和滑轨行程，必须开合采集并实测。

每件对象保留如下清单（拟建，尚未产生实物数据）：

```text
object_id / parent_id / role(static|rigid|articulated)
T_room_object / visual_asset / collision_asset
mass_kg / inertia / friction / restitution
joint_type / axis / origin / limits / damping  # 仅关节对象
geometry_source / parameter_source / uncertainty / capture_version
```

来源须区分`measured`、`multiview_reconstructed`、`generated_completion`、`manual_proxy`和`assumed_default`。对默认／模型推测参数给出可编辑值和待测标记；不可把“物理引擎能跑”标成“高保真物理重建”。

## 6. 场景优先的具体路线

### 阶段A：冻结交互清单并补采

首个小样仍是工作台，但验收改为“工作台固定、杯子／盒子／第三件刚体独立运动”。选择真实存在的对象，不为凑数量购买。采集静态背景时移走这些物体，额外采每件多角度照片、接触底面和可达背面；若无法移走则标遮挡并规划补拍，生成补全单列。

沿用[[so101-workbench-pilot-capture-sop-2026-11-10|手机＋D435i SOP]]的USB／录制／回放、尺度和保留集。门与抽屉必须单独记录关闭、中间、全开状态、运动轴线、限位、柜体内部与门轴坐标，按下一节专项清单补采；仅扫房间一圈不够。

### 门与抽屉专项采集／建模清单（首版必做）

1. **建编号清单**：每扇门、每个抽屉独立object_id。注明门框／柜体固定、门板／抽屉可动；普通合页门按revolute、普通直线抽屉按prismatic建模。折叠门、联动滑轨等多关节结构单列，不能默认简化后仍称完全还原。
2. **先固定状态扫背景**：选一个记录清楚的开合状态完成静态房间采集，固定不动。随后以独立take采关闭、中间、最大正常开启状态，不把运动前后照片直接混入同一静态SfM／GS训练集。
3. **门的外形与轴**：量门板宽／高／厚、门框净口、把手位置、合页轴线上下两个可识别点、离地间隙、关门零位与正常开启上限；拍门板正反面、门框内侧和底部接触区域。不可见部分标未知，不拆合页。
4. **抽屉外形与行程**：量面板／箱体尺寸、内腔、柜口、关闭和最大正常拉出位置的同一基准点；记录滑动方向、总行程、上下左右间隙、底板和可见滑轨。不得拉过真实限位或为扫描拆卸柜体。
5. **运动证据**：相机固定拍一次缓慢打开、暂停、关闭的完整视频；固定标记放在框体和可动件上，记录相机／标记尺寸。视频用于检查轴线、行程和分件，不因有视频就自动声称识别了摩擦／阻尼。
6. **质量与阻力来源**：可安全称量则实测；无法称量的门板／抽屉保持估计并记录方法。缓闭器、门锁、磁吸、弹簧、自闭合、滑轨间隙等单独登记；没有力／动态测量前，不把默认阻尼和摩擦标成真实值。首版对这些附加机构逐项说明是否建模，不能以普通关节冒充其功能。
7. **几何与背景拆分**：门框／柜体与可动件分别保存visual和collision；柜内、门后优先使用开状态补拍的真实数据。去除原背景中的门板／抽屉外观，再让独立link随joint运动，防止开门后原处仍有一扇门。
8. **物理约束**：定义joint origin、axis、range、damping／friction的来源；固定框体，门／抽屉只保留对应自由度。用鼠标施力或约束拖拽开合，不以每帧直接改pose或动画播放代替物理；门框碰撞、限位和薄板代理需一起检查。
9. **验收**：关闭／中间／全开实测参照逐一对比；检查无轴漂移、脱轨、明显穿柜、错误阻挡和原外观残影。每件连续开合／复位10次，保存重载后限位与初始状态一致；数量是初始验收预算，角度／位移误差门槛在测量不确定度明确后冻结。

**候选放行新增硬门槛**：能导入／导出明确的link和revolute／prismatic关节，并在物理运行时让视觉与碰撞同步。只证明可移动刚体、但未验证门／抽屉关节的PhiRIE／GS示例，不算首版方案完成；先用可检查的mesh＋关节基线，再逐link添加高保真外观。

### 阶段B：先做可交互mesh基线

COLMAP恢复手机相机与结构；D435i经独立位姿／配准后融合几何；Blender整理材质、分件与碰撞代理。将米制场景导入独立MuJoCo scene，不改现有机器人工程。实现或复用交互面板：选对象、编辑pose、物理施力／拖拽、暂停／单步／复位、保存／加载布局。无需机器人策略参与。

这条路线最可控且核心组件许可明确，但需要资产制作和少量工具集成，不能称已有自动整房产品。若目前没有桌面实时查看条件，先验证小场景窗口与基本操作，再处理整房资产，避免把图形环境问题误当重建算法失败。

### 阶段C：验证现成的高保真联动

优先取DISCOVERSE的已有可动对象示例，只验证“物理体动→对应GS动→遮挡顺序正确→复位一致”；不装训练模块。通过后只替换一个我们的杯子／盒子，再扩展其余对象。严查`gs_model_dict`对象名／MuJoCo body对应、坐标尺度、静态重影和接触面错位。

同时可做ϕ-RIE的**依赖可得性核查**：公开构建模块是否具备所需权重、兼容PhiRoom后端是否可取得、是否能不用机器人／policy模块打开一个已准备场景。只在这些条件通过后才做“自己的扫描→对象化→PhiView交互”。若后端不可用，保留算法参考，不为它更改主线。

### 阶段D：全房扩展与关节

将工作台小样扩到整房固定结构；每次新增一组可动对象，重新检查视觉／碰撞对齐。门／抽屉列为首版必做，与可动刚体并行追加link／joint模型和多状态照片；先完成一扇门和一个抽屉的代表小样，再按清单推广。首版不处理线缆动力学；线缆外观可保留，但物理代理与真实柔性行为的差别必须注明。

此路线无需选择PPO、ACT或VLA，也不把任何真实机器人部署作为完成条件。物理参数来自测量或受控物体实验，不涉及策略训练。

## 7. 新的交付物与验收

| 交付物／测试 | 怎么检查 | 通过含义 |
|---|---|---|
| 房间几何与坐标 | 独立尺度、桌高、对象位姿检查；沿用总方案分区精度目标 | 米制结构可对齐，不靠“看起来像” |
| 自由视角与布局编辑 | 漫游、选中、移动／旋转、存布局、重载 | I0/I1；编辑直接改pose不算接触物理 |
| 三件刚体 | 分别推、通过约束提起后释放、落桌／地板、互相碰撞 | I2能执行；不自动表示真实摩擦已辨识 |
| 视觉／碰撞一致 | 显示碰撞线框，检查桌边、杯底、物体移动前后 | 无明显穿透／悬浮／旧物体重影 |
| 背景补全 | 移走目标后检查原位置；对照补拍的空背景 | 真实补拍优先；生成区域有标签且不作测量证据 |
| 可重复复位 | 同布局连续复位至少10次，再保存重载 | 实体数量、初始pose和版本一致，无重复对象；数字为拟定小样门槛 |
| 门／抽屉（首版必需） | 按清单逐件检查开合、限位、轴线／行程、碰撞和视觉link跟随；每件连续开合与复位10次为初始测试预算 | I3必过；不能以自由刚体平移／旋转或预录动画代替关节物理 |
| 性能 | 在目标机器测分辨率、帧率、物理步长与显存；先检查能否达到拟定20fps交互目标 | 实测资源报告；尚无硬件／性能保证 |
| 参数真实性 | 几何、质量、摩擦来源逐项填写；可测滑移／落下行为作留出比较 | 区分默认可玩模型与经验证物理副本 |

20fps是初始交互体验目标，不是任何候选的已测性能。房间整体厘米级误差与工作台关键几何毫米级目标不同，不因画质高而省略接触区建模。完整房间是范围清单完整与未观测区域透明，不表示所有封闭柜内均有真实扫描数据。

## 8. 开源、成本与停止条件

当前不存在本轮已验证的“全部必需源码／权重／后端／资产均可匿名获得、无需外部服务”的自动流程。可手工组成核心开源路线；模型许可证、CUDA和驱动等仍单列。SimFoundry代码Apache并不覆盖Gemini与所有模型；RialToGUI教程中的采集／转换服务不是本地主线必须使用的工具。[747][757][746]

暂不报价、不采购。预算按实际阶段测量：背景重建工时、每物体分件／碰撞工时、关节建模工时、GPU渲染与重建时间、每次布局更新成本。先完成小样再估全房，不沿用之前含训练／部署的工期作为当前承诺。

停止／返工条件：对象移走仍留旧影；背景与碰撞错位；凸包封死杯口／抽屉空间；生成补全未标注；必需后台或模型不可得；交互面板只能播放录制而非真实推进物理。若GS整合成本高且无保留视角收益，先交付可交互mesh版本，不让视觉路线阻塞基本物理模型。

## 9. 商业应用可能性

当前直接价值在实验室和机器人团队的场景搭建、互动回归、布局检查与资产维护，使用者为仿真工程师，预算通常由实验室／研发负责人决定。尚处候选研究，无付费／复购证据。优先交付可编辑工作台、可动对象与带误差报告的房间资产；近期1–2年可用小样验证人工节省（判断，置信度中），中期3–5年复制性取决于跨物体、关节和房间更新的成本，待验证。成本需包含扫描、人工分件、模型／服务许可和维护，不能只算一次GPU重建时间。

## 10. 中小型创业者的机会

**可立即验证**：本地场景重建与对象化、碰撞／关节标注、可交互验收报告服务；首个收费物是可运行资产包和参数出处，首批客户为缺资产制作人力的小团队。团队需摄影测量、mesh工具、仿真和基础测量能力，先用现有手机／RGB-D与单工作站，资金量级低至中为条件假设；验证周期以完成一个工作台为单位，不虚构市场报价。

**需要条件成熟**：场景资产编辑器与自动QC、布局版本管理、从扫描到对象化的半自动工具；大平台可能内建功能，服务差异须来自现场数据、许可清楚和可复核质量。复购需以更新和维护收益验证。**不建议进入**：把生成模型补出的物体当精密测量模型、把浏览器漫游包装为物理数字孪生、承诺不测物性即可还原真实接触。下一验证是本小样的交付工时与独立操作者验收。

## 11. 知识冲突与范围修订

### 后续代码与有限运行证据

详见 [[door-drawer-interactive-reconstruction-code-audit-2026-11-10|门／抽屉深查]]：原始MJCF确有hinge／slide，隔离MuJoCo4.0.0编译／短步进和body姿态映射探针通过；尚未验收GPU渲染或自己的房间。当前GaussianRenderer0.2.0实际为MIT＋gsplat，应与Real2Sim中研究用途组件分开；不能笼统称当前renderer受同一限制。ϕ-RIE检查到的对象导出是freejoint，RialTo关节标注与USD导出有实际代码但许可未清。


上轮[[so101-open-source-room-reconstruction-training-alternatives-2026-11-10|开源替代报告]]把训练／部署纳入了主比较，范围超出本轮明确目标。其Playground、ACT等结论保留为后续资料，**不再作为当前候选的优先级依据**。本轮优先对象化重建、交互与物理／外观一致性，且发现PhiView后台依赖，不能以项目页“代码全部发布”推断完整界面流程无门槛。

## 关联连接

- [[so101-workbench-pilot-capture-sop-2026-11-10|继续适用的采集操作手册]]
- [[so101-room-high-fidelity-sim-reconstruction-plan-2026-11-10|分区精度与坐标约定]]
- [[so101-open-source-room-reconstruction-training-alternatives-2026-11-10|前轮广范围比较，训练部分暂缓]]
- [[_sources/interactive-room-reconstruction-source-set-2026-11-10|本轮16项来源与核查边界]]

## 来源

SRC-robotics-742–757含固定README、界面／数据文档、手机入口、运行时同步源码、许可和静态检查包。752 INSTALL.md路径404保留；751／754／755为无.md后缀纯文本fallback，已核阅源码。未运行所有示例，不把源码存在、import或doctor当成功交付。

[742]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-742-insait-institute-phirie-interactive-reconstruction-fixed-readme.md "SRC-robotics-742 insait-institute/PhiRIE interactive reconstruction fixed README"

[743]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-743-runyiyang-physicalview-interactive-reconstruction-fixed-readme.md "SRC-robotics-743 RunyiYang/PhysicalView interactive reconstruction fixed README"

[744]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-744-discoverse-dev-discoverse-interactive-reconstruction-fixed-readme.md "SRC-robotics-744 discoverse-dev/DISCOVERSE interactive reconstruction fixed README"

[745]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-745-discoverse-dev-discoverse-real2sim-interactive-reconstruction-fixed-readme.md "SRC-robotics-745 discoverse-dev/DISCOVERSE-Real2Sim interactive reconstruction fixed README"

[746]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-746-real-to-sim-to-real-rialtogui-interactive-reconstruction-fixed-readme.md "SRC-robotics-746 real-to-sim-to-real/RialToGUI interactive reconstruction fixed README"

[747]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-747-nvlabs-simfoundry-interactive-reconstruction-fixed-readme.md "SRC-robotics-747 NVlabs/SimFoundry interactive reconstruction fixed README"

[748]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-748-robosimstudio-robosimstudio-interactive-reconstruction-fixed-readme.md "SRC-robotics-748 robosimstudio/robosimstudio interactive reconstruction fixed README"

[749]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-749-internrobotics-re3sim-interactive-reconstruction-fixed-readme.md "SRC-robotics-749 InternRobotics/Re3Sim interactive reconstruction fixed README"

[750]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-750-phirie-interactive-viewer-dependencies.md "SRC-robotics-750 PhiRIE interactive viewer dependencies"

[751]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-751-phirie-phone-video-reconstruction-entrypoint.md "SRC-robotics-751 PhiRIE phone video reconstruction entrypoint"

[752]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-752-simfoundry-install-path-failure-note.md "SRC-robotics-752 SimFoundry install and external service boundaries"

[753]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-753-phirie-data-metric-geometry-and-model-inputs.md "SRC-robotics-753 PhiRIE data metric geometry and model inputs"

[754]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-754-discoverse-simulation-and-gaussian-state-synchronization.md "SRC-robotics-754 DISCOVERSE simulation and Gaussian state synchronization"

[755]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-755-robosimstudio-software-dependencies.md "SRC-robotics-755 RoboSimStudio software dependencies"

[756]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-756-interactive-scene-static-review.md "SRC-robotics-756 Interactive scene fixed license and dependency static review"

[757]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-757-simfoundry-fixed-third-party-license-boundaries.md "SRC-robotics-757 SimFoundry fixed third party license boundaries"

[交互路线对照CSV](../../../raw/robotics-embodied-ai/data/interactive-room-reconstruction-comparison-2026-11-10.csv)。
