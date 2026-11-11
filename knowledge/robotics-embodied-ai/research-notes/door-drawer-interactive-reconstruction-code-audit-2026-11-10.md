---
title: 门与抽屉必须可开合：DISCOVERSE、ϕ-RIE与RialTo代码及许可核查
type: synthesis
date_created: 2026-11-10
last_updated: 2026-11-10
sources:
  - SRC-robotics-758–772
  - SRC-robotics-744–746
  - SRC-robotics-750
  - SRC-robotics-756
tags:
  - interactive-scene
  - articulated-reconstruction
  - code-audit
status: active
---

# 门与抽屉必须可开合：三项目代码、依赖与开源许可核查

> [!summary] 推荐路线
> **选择DISCOVERSE方向作为场景运行骨架：实测＋多状态分件→Blender整理→显式MJCF门轴／滑轨→独立MuJoCo交互场景；先全部mesh验收，再选择性增加逐link Gaussian外观。** 不运行仓库中的机器人任务脚本，不安装策略依赖。它已有门、抽屉的真实关节定义和按MuJoCo body驱动GS的实现，技术路径最短；但仍需制作我们的资产、独立交互界面和锁定兼容版本，不能称扫描后一键完成。

> [!important] 不是三选一都能直接满足
> ϕ-RIE检查到的对象MJCF导出是freejoint，尚未证明自动生成门轴／滑轨；其完整交互编辑还有独立后台访问要求。RialTo GUI确有revolute／prismatic标注与USD物理导出，但浏览器编辑不等于完成物理验收，顶层许可也未明确。两者适合作为方法／工具参照，当前不承担首版必需功能。

## 1. 任务、分类与验证边界

主分类R05，次分类R04／R06。目标只包括真实房间的几何、外观、对象拆分、刚体、门、抽屉与交互保存／复位。**排除策略训练、机器人任务执行、真机部署。** 手机＋D435i继续作为采集组合，设备当前可用性仍待实际检查。

截至2026-11-10，读取四仓库完整GitHub tree（均未截断）、固定源码与许可，追查外置GaussianRenderer。使用GitHub连接器获取主要文件，并用只读API获得递归目录／固定版本；归档原文、行号、hash和两项隔离探针。没有安装完整DISCOVERSE／PhiRIE／RialTo、没有GPU渲染、真实房间数据或现场操作。

与上轮纯静态研究不同，本轮实际在**隔离MuJoCo4.0.0环境**编译并短步进原始柜子资产，验证门／抽屉和body映射；没有修改现有机器人环境，不能据此认定现有工程版本已兼容。

## 2. 判定矩阵

| 必需能力 | DISCOVERSE方向 | ϕ-RIE／PhiView | RialTo GUI |
|---|---|---|---|
| 对象分件 | 消费独立MJCF body／GS模型；本房间仍需分件 | 有发现、生成、配准、背景补全管线 | GUI切mesh、组织父子对象 |
| 门关节 | 原始toy_cabinet为hinge；本轮局部编译／施力探针通过 | 检查到对象导出为freejoint，门关节自动构建未证实 | SceneInit写RevoluteJoint数据，USDZExporter写Physics关节 |
| 抽屉关节 | 原始toy_cabinet为slide；0.1m位移探针通过 | 同上，滑轨／限位重建未证实 | PrismaticJoint、local frame与上下限实际存在 |
| 视觉跟随物理 | 外置renderer按body名→xpos／xquat更新；CPU映射探针通过 | 有物理／GS联动设计，但完整编辑后台有访问前提 | 导出后由外部USD物理引擎执行；本轮未跑Isaac |
| 关节限制／摩擦 | MJCF明示range、frictionloss；不是实测本房间参数 | 对象mass／friction注释不等于关节辨识 | 导出limit、jointFriction等字段；输入仍需测量 |
| 首版全部必需依赖可避开模型服务 | mesh基线可以；GS另需CUDA／Torch／gsplat | 完整自动化需多模型／多环境，后台访问待核 | 依赖React／Three和外部物理验证，许可待澄清 |
| 完整开合与高保真联动已在本机验收 | **未完成**，只有限探针 | 未完成 | 未完成 |
| 当前选择 | **主线候选＋明确补齐清单** | 研究参考，不能代替I3 | 手工关节标注参考，暂不直接复用代码 |

“有源码”与“已验收”分列；未发现门关节自动构建不等于底层MuJoCo不支持关节。训练演示、录制动画或策略成功率不作为本矩阵证据。

## 3. DISCOVERSE：实际到哪一层

### 3.1 门和抽屉不是动画占位

固定提交`d67f47c084aba0e0cf422a8725235f8b9238655a`：

- `models/mjcf/object/toy_cabinet.xml:L3–13`：`cabinet_door` body下的joint轴为`0 0 -1`、range为`0 3.1416`、frictionloss为0.5；省略type时采用MuJoCo默认hinge。[758]
- 同文件`L15–30`：`cabinet_drawer`为`type="slide"`，axis为`-1 0 0`、range为`0 0.22`、frictionloss为0.5；抽屉箱体用多个box组成，保留开口。[758]
- `models/mjcf/tasks_mmk2/cabinet_door_open.xml`用`compiler angle="radian"`并include上述资产，因此原门range应按弧度解释；0.22为该示例抽屉行程，**不可抄作我们的实际尺寸**。[770]

`cabinet_door_open.py`和`drawer_open.py`确实加载对应场景，不过属于机器人任务／数据循环。本任务只复用资产和运行结构，不执行这些脚本。门示例默认`use_gaussian_renderer=False`；抽屉示例默认也关GS，但允许`--use_gs`开启。因此源码证明有物理关节，不证明下载示例就已具备我们需要的门板逐link GS。[759][760]

### 3.2 物理到Gaussian的代码链

DISCOVERSE `simulator.py`渲染分支调用：

```text
MuJoCo step → mj_data
           → gs_renderer.update_gaussians(mj_data)
           → gs_renderer.render(...)
           → 用返回RGB／depth作为GS画面
```

`gaussian_renderer>=0.1.3`是可选gs extra。此次单独固定检查外置GaussianRenderer提交`577efdb50c3891f46db3971dc0b7c4129146dd16`（声明版本0.2.0），不是假定它与DISCOVERSE同提交发布。[764][771]

- `src/gaussian_renderer/gs_renderer_mujoco.py:L55–73`：遍历MuJoCo body名称，与`gaussian_model_names`匹配并记录Gaussian点区间及body id。
- `L75–91`：从`mj_data.xpos`和`xquat`提取位置／wxyz四元数，调用`update_gaussian_properties`。**没有仅允许freejoint的过滤，因此hinge和slide body也能进入映射。**[761]
- `core/gs_renderer.py`：用body pose变换原始Gaussian位置／旋转；使用gsplat，更新函数显式把数组转到CUDA。[772]

这条链已经存在，不必从零发明。但需要满足**每个可动link一个正确命名的外观资产、Gaussian坐标在对应body本地系**。如果把房间世界坐标PLY直接当门板本地模型，会重复叠加平移／旋转；只给柜体一个PLY，则柜门与抽屉无法独立跟随。

### 3.3 两项本轮实际探针

原始include中的body与geom未改，外面加独立`<mujoco><compiler angle="radian"/>...`，不加载机器人／外部mesh：

| 探针 | 结果 | 不能外推的结论 |
|---|---|---|
| MJCF编译／前向变换 | 2个joint，类型分别hinge／slide，limited均为true；抽屉q=0.1时位移`[-0.1,0,0]m`，门q=0.5时朝向改变 | limited标志不等于已测试软限位受力；不是我们的房间尺度验收 |
| 广义力短步进 | 初始q=`[0.3,0.08]`，施力后100步到约`[0.453845,0.094786]`，状态有限且变化 | 没有穷尽极限角度、碰撞、关节稳定性或真实物性 |
| body→渲染pose映射 | 使用原`init_renderer`与`update_gaussians`方法，真实MuJoCo状态，截获更新函数收到的位置／四元数；门／抽屉都匹配且随joint变化 | 截获替身没有运行GPU点变换／rasterization；不称GS渲染通过 |

脚本、准确结果、源文件hash见[探针证据包][771]。隔离环境解析到MuJoCo4.0.0，既非完整DISCOVERSE锁环境，也非当前机器人项目版本。

### 3.4 高保真仍有的缺口

GS分支直接使用GS返回图，**检查路径没有自动把任意未注册的mesh物体与GS背景作深度正确合成**。所以“给背景一个PLY、门仍用mesh”不能未经验证就承诺正常显示／遮挡。第二阶段有两个选择：每个门板／抽屉／柜体都制作并映射GS；或专门开发且验收mesh＋GS深度合成。[754][761][772]

GS携带拍摄时光照。门打开后的新阴影、柜内曝光、反光与背面不是刚体位姿更新就能正确恢复；未知背景要补拍，生成补全须标注。首版物理交互先用完整mesh场景验收，GS不阻塞关节功能。

## 4. ϕ-RIE：对象化不是自动关节化

固定PhiRIE `a03543f6472451ffc079502417a48d64c2a6e7f1`的`robo/sim/export_mjcf.py:L1225–1235`对生成对象写：body、`<freejoint/>`、质量／惯量和碰撞mesh。检查到的导出路径没有为这些对象输出hinge／slide／parent-link树。[765]

它擅长的仍是对象发现、生成、米制注册、源对象Gaussian移除与背景补全；这些可帮助制作可移动杯子，但**门／抽屉I3仍需另外分件、建关节并修改导出／接口**。不能因为接口可拖动瓶子，就推断已经识别柜门合页或抽屉滑轨。

官方`docs/PHIVIEW.md`明确：完整交互编辑／注册API使用另一个PhiRoom兼容后台`26f834ca3468e21c584abd5808082a0b2fdf4c66`，需要访问对应仓库；直接用当前PhiRIE树替代未验证。打包前端源码、doctor路径检查与整流程可用是不同证据。[750][756]

必要重建环境包含SAM、TRELLIS、深度／位姿、背景编辑等模型；不同Torch环境分开。主代码和界面MIT并不覆盖每项模型／数据许可。即使完全跳过机器人policy，重建／交互后台和这些模型前提也不会自动消失。[742][743][753] 本轮不安装它们，也不要求为当前门／抽屉目标先解决全部环境。

**结论**：保留为自动化对象构建研究参考；除非追加真实关节导出与证明后台可得，否则不作为首版完成门／抽屉的主线。

## 5. RialTo：关节标注／导出代码是实的，运行与许可需另算

固定RialToGUI `9f0191453d7884d6eaf301a12e6f1cdb24a0ae28`的调用链：

1. `src/SceneInit.js`提供`preAddJoint`、`postAddPrisJoint`、`postAddRevoJoint`；用户选两个mesh，利用标注框在双方坐标系中的变换计算`localPos0/1`、`localRot0/1`。[766]
2. `postAddPrisJoint:L672–716`写`PrismaticJoint`，上下限来自标注圆柱的长度，轴写Y并配合local rotation。`postAddRevoJoint:L727–780`写`RevoluteJoint`，角度限位来自GUI值；默认界面限位±90并非实际门的量测。[766]
3. `USDZExporter.js:buildJoint:L303–360`输出`PhysicsRevoluteJoint`／`PhysicsPrismaticJoint`、body0/1关系、local frame、axis、lower／upper limit和jointFriction。其它段输出质量、RigidBodyAPI与convexDecomposition等碰撞字段。[767]
4. USD头部声明`metersPerUnit=1`、`upAxis="Y"`；接入我们的Z-up房间坐标时必须真实转换几何／关节帧，不是只改元数据。旋转关节限位和滑轨长度还须按目标USD引擎语义核查。[767]

因此它不是“仅README声称能加关节”。但`package.json`主要为React18／Three0.150等前端依赖，检查界面路径没有完整接触求解器；官方流程要求导出后进Isaac按Play检查物理。**GUI预览、USD字段存在、实际稳定开合分别验收**，本轮只证实前两者的代码路径，未执行浏览器构建或USD／Isaac运行。[768][746]

根目录tree未发现LICENSE，`package.json`也无license字段；`private:true`仅是npm发布控制，不意味着仓库私有，也不提供复用许可。不能从Three.js等依赖许可推导其新增GUI代码许可。现阶段可参考操作／数据设计，不把整份GUI代码直接纳入交付。若后续取得明确授权，才考虑用其标注后导出；它的扫描教程使用Polycam等工具不是我们必须采用的依赖。[771]

## 6. 许可和依赖分层判定

| 部分 | 本轮证据 | 选型含义 |
|---|---|---|
| DISCOVERSE核心 | MIT；core有MuJoCo／NumPy／SciPy／OpenCV等；GS、editor、策略是分开的extras | 首版可只用core／自建独立scene，不装策略包 [764] |
| 当前GaussianRenderer0.2.0 | MIT，依赖gsplat；实现走gsplat backend而非原始diff-gaussian-rasterization | 不能笼统判它为非商业；需固定renderer和gsplat版本，再验CUDA路径 [762][763][772] |
| DISCOVERSE-Real2Sim | 独立仓库，根许可未见；其LitMesh2GS内diff-gaussian-rasterization为研究／非商业条款 | 首版不依赖该生成链；用自采mesh／独立许可清楚的GS训练器替换不是零成本 [769][756] |
| PhiRIE／打包PhiView | 主代码MIT；兼容后台、权重和数据独立 | MIT不解决后台访问与门关节缺口 [742][750] |
| RialTo GUI | 根及package未见明确许可 | 暂作方法参考，不当成许可已清楚的可交付软件 [768][771] |
| 扫描与第三方资产 | 公开示例模型／HF素材各自条款，物体几何可能另有来源 | 优先用户自采资产；不由代码MIT外推资产许可 |
| GPU／桌面 | renderer数组更新显式CUDA；系统图形／驱动独立 | CPU探针成功不证明Mac／工作站的完整高保真链可用 [772] |

这里核查的是公开许可文本与代码依赖边界，不是对所有传递依赖的完整授权审计；未替用户接受新合同或上传房间数据。基础mesh路线不强制访问模型服务，生成模型也不作为还原真实门轴／行程的必要环节。

## 7. 能落地的分阶段场景路线

### 7.1 交付结构：先定义门／抽屉，而不是先训练大场景GS

```text
room_fixed                 # 墙、地面、工作台、门框、柜体
  door_frame_fixed
    door_leaf_hinge        # origin在真实轴上；axis、range实测
  cabinet_fixed
    drawer_box_slide       # axis、range实测；箱体保持开放容积
objects_rigid              # 杯子等可动刚体
```

每link有视觉mesh／贴图、碰撞代理、质量／惯量来源、关节参数和本地坐标。GS如启用，沿用同一link名与本地frame。先用一扇真实门和一个真实抽屉做代表小样，再逐件覆盖交互清单；具体数量与特殊机构待现场登记。

### 7.2 采集与几何

- 沿用手机＋D435i[[so101-workbench-pilot-capture-sop-2026-11-10|采集SOP]]；房间尺度与固定基准独立检查。
- 门／抽屉分关闭、中间、正常全开独立take采集。静态重建不得混入正在开合的对象；在固定框体上设共同标记，把多状态证据配准后分件，不靠无约束合并照片恢复运动物体。
- 门测板宽高厚、轴线上下两点、离地／框间隙、把手与开角；抽屉测柜口、箱体、轴向、行程、内腔与间隙。正常开合范围内补拍门后和柜内；不可达区域标未知。
- COLMAP用于手机位姿／结构；D435i另有自己的轨迹与RGB／depth内外参，经定位／配准后才融合Open3D几何。Blender清理、分件与真实照片贴图，固定结构用清晰碰撞代理；不要求先跑Real2Sim AIGC链。

### 7.3 第一里程碑：纯mesh房间可物理开合

1. 从已核查的DISCOVERSE MJCF关节组织出发，**按实测重写用户资产参数**，不复制示例的180°／0.22m／摩擦值。
2. 固定门框／柜体，门板只设hinge、抽屉只设slide；有多节轨道／折叠门等复杂结构时单独列建模工作，普通joint近似须注明。
3. 实现或复用独立MuJoCo场景窗口：漫游、暂停、施力／约束拖拽、复位与保存／加载。编辑时直接改qpos与物理互动分开；不加载机器人或任何policy。
4. 碰撞代理按薄板和箱体分件，柜内自由空间不能被单一凸包封死。门锁、磁吸、缓闭器／弹簧没有测量就登记未建模，不拿普通阻尼冒充。
5. 每件关节先检查零位、25%／50%／75%和全开位置，再检查受力、碰撞、限位与连续复位。

这是必需的第一交付。原生MuJoCo画面可使用真实贴图，但不宣称照片级；先证明真实几何与交互正确，禁止以GS画质遮盖关节／碰撞问题。

### 7.4 第二里程碑：逐link高保真外观

在独立环境锁定DISCOVERSE core、GaussianRenderer0.2.0和兼容gsplat／Torch／CUDA组合；本轮候选SHA不是完整已测lock。先使用自采单门板、抽屉箱体和固定背景的外观资产，转换到对应link本地系，逐名称注册。

固定同一组关节状态对照mesh／GS画面与碰撞线框，检查门板正反面、抽屉内部、遮挡、近裁面与重影。多link合成必须真实按深度排序。只有背景GS而门板mesh的混合方案，另做深度合成实现和验收，不能假定当前渲染分支自动包含未映射mesh。

若GS在开门光照／柜内遮挡下失真，保留该部件mesh或降低其GS范围；需要不同渲染器来混合时明确新增开发成本，不强行全屋GS。固定状态的照片级外观和动态光照逼真度分别报告。

### 7.5 交付文件

拟建`room.xml`、`door_<id>.xml`、`drawer_<id>.xml`、分link视觉／碰撞资产、`joint_measurements.csv`、`link_frames.json`、布局版本与参数来源表、独立检查视图和互动验收报告。大图／PLY／视频放用户数据盘，Git只存配置、脚本与脱敏报告；具体目录沿用现有房间方案，不在本轮创建空壳“已重建房间”。

## 8. 放行标准、成本与证伪条件

| 检查 | 建议小样标准 | 不通过时 |
|---|---|---|
| 结构与尺度 | 独立距离、桌面／框体基准符合既定分区误差预算 | 修尺度／坐标／几何，再谈材质 |
| joint种类与frame | 门hinge、抽屉slide；轴线／行程来自实测；frame方向可复查 | 不用动画或freejoint替代 |
| 全行程 | 0／25／50／75／100%位置与参考照片对照；间隙与接触合理 | 修局部几何、joint origin／axis和碰撞 |
| 真实物理互动 | 施力／约束拖拽、释放、支撑／碰撞、受力限位均有日志 | 检查求解参数、碰撞、质量；未实测物性不写高保真 |
| 重复与存取 | 每件10次开合／复位，保存重载后对象数／初始状态／限位一致 | 修复状态管理／重复对象；此数为工程提案 |
| GS联动（如用） | 每link body匹配；相同q状态无旧影、错轴、遮挡倒置 | 回退mesh，逐link定位误差 |
| 性能 | 目标机器报告分辨率、FPS、物理步长和显存；暂以20fps为待验证交互目标 | 减资产／分区／降低画质，不声称已达到 |

关节末端角度／位移误差门槛在测量不确定度明确后冻结，不能凭源码给毫米／角度承诺。当前没有全场景性能、长期稳定或物性精度数据。

工作量主要来自每件门／抽屉的测量、分件、局部碰撞、背面和内腔，不能按整屋照片数量推算。先完成一个代表柜子的mesh里程碑，记录人工／计算／返工时间后，再估整房；不沿用之前含训练的工期，不虚构采购／云服务价格。

改变推荐的条件：如果RialTo获得明确代码授权且实际USD物理运行成本更低，可引入其关节标注器；若PhiRIE补齐关节构建并解决后台可得性，可比较自动化工时；若GS无动态视角收益或显存超预算，主线全部mesh仍可交付。当前不为任何候选做端到端保证。

## 商业应用可能性

近期价值是实验室／机器人研发团队的可交互房间资产、门／抽屉场景维护与回归测试，用户是仿真工程师，决策／付款者通常为研发负责人。本案只有局部代码／探针证据，未付费试点。相较托管扫描，价值在几何／关节参数可追溯、私有数据可本地留存，代价是人工分件、物性测量和维护；以每件资产工时、返工次数、更新成本、验收通过率量化。1–2年可小样验证，3–5年规模复制与复购待跨场景数据支持，置信度中低；不从开源星数推导需求或市场空间。

## 中小型创业者的机会

**可立即验证**：有明确交互清单、参数出处和验收日志的“柜子／房间可交互资产包”；MVP是一扇门＋一个抽屉，首批客户为缺仿真资产工程能力的研究团队。需要摄影测量、Blender、MuJoCo与现场测量能力，使用已有设备和单工作站的小额至中等投入为条件假设，无真实报价证据。

**需要条件成熟**：关节标注／碰撞检查工具、扫描资产版本管理和场景维护；可复购价值须证明更新工时确实降低，头部平台也可能内建同类功能。合作应围绕现场交付与可验证质量而非垄断算法。**不建议进入**：将许可不清GUI或研究限定组件打包商用，宣称自动推断真实摩擦／门轴或“GS一键变物理”。下一验证是在代表柜子里程碑后让独立操作者按验收表操作并记录工时，再询问外部客户付费意愿。

## 知识冲突与修订

1. 前轮对DISCOVERSE／Real2Sim的授权提醒必须拆开：**当前检查的GaussianRenderer0.2.0为MIT＋gsplat，不能笼统说它含原始Gaussian非商业限制**；研究用途限制在本轮明确查到的Real2Sim rasterizer组件，资产许可仍另算。
2. 前轮“有GS联动”不等于“门／抽屉GS示例已跑通”。现在补充实际hinge／slide模型、默认关闭GS的示例及body映射探针；完整GPU画面／本项目仍待验收。
3. PhiRIE提供可移动对象不等于I3关节重建；RialTo能导出关节字段不等于界面已进行接触物理。三种证据层次分别保留。

## 关联连接

- [[interactive-room-sim-reconstruction-alternatives-2026-11-10|当前范围与I0–I3验收]]
- [[so101-workbench-pilot-capture-sop-2026-11-10|采集SOP]]
- [[so101-room-high-fidelity-sim-reconstruction-plan-2026-11-10|原房间坐标与分区精度]]
- [[_sources/door-drawer-interactive-code-audit-source-set-2026-11-10|固定来源、许可与探针索引]]

## 来源与方法

15项本轮来源（758–772），复用744–746／750／756等先前官方文档。源码／许可证为一级技术证据，用户数据精度仍无实测。本轮14个网页源中13个无.md后缀触发纯文本fallback，原状态保留；与GitHub连接器副本逐项核对正文，14源均有内容；771为另建本地代码／探针包。每个结论可沿来源编号、固定GitHub行号、hash与探针JSON复核。

[742]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-742-insait-institute-phirie-interactive-reconstruction-fixed-readme.md "SRC-robotics-742 insait-institute/PhiRIE interactive reconstruction fixed README"

[743]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-743-runyiyang-physicalview-interactive-reconstruction-fixed-readme.md "SRC-robotics-743 RunyiYang/PhysicalView interactive reconstruction fixed README"

[746]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-746-real-to-sim-to-real-rialtogui-interactive-reconstruction-fixed-readme.md "SRC-robotics-746 real-to-sim-to-real/RialToGUI interactive reconstruction fixed README"

[750]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-750-phirie-interactive-viewer-dependencies.md "SRC-robotics-750 PhiRIE interactive viewer dependencies"

[753]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-753-phirie-data-metric-geometry-and-model-inputs.md "SRC-robotics-753 PhiRIE data metric geometry and model inputs"

[754]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-754-discoverse-simulation-and-gaussian-state-synchronization.md "SRC-robotics-754 DISCOVERSE simulation and Gaussian state synchronization"

[756]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-756-interactive-scene-static-review.md "SRC-robotics-756 Interactive scene fixed license and dependency static review"

[758]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-758-discoverse-door-drawer-original-mjcf.md "SRC-robotics-758 DISCOVERSE door drawer original MJCF"

[759]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-759-discoverse-cabinet-door-example-source.md "SRC-robotics-759 DISCOVERSE cabinet door example source"

[760]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-760-discoverse-drawer-example-source.md "SRC-robotics-760 DISCOVERSE drawer example source"

[761]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-761-gaussianrenderer-mujoco-body-pose-bridge.md "SRC-robotics-761 GaussianRenderer MuJoCo body pose bridge"

[762]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-762-gaussianrenderer-0-2-dependency-manifest.md "SRC-robotics-762 GaussianRenderer 0.2 dependency manifest"

[763]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-763-gaussianrenderer-mit-license.md "SRC-robotics-763 GaussianRenderer MIT license"

[764]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-764-discoverse-core-optional-dependencies.md "SRC-robotics-764 DISCOVERSE core optional dependencies"

[765]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-765-phirie-mjcf-rigid-object-export-implementation.md "SRC-robotics-765 PhiRIE MJCF rigid object export implementation"

[766]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-766-rialto-gui-joint-authoring-implementation.md "SRC-robotics-766 RialTo GUI joint authoring implementation"

[767]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-767-rialto-usd-physics-joint-exporter.md "SRC-robotics-767 RialTo USD physics joint exporter"

[768]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-768-rialto-gui-package-metadata-license-boundary.md "SRC-robotics-768 RialTo GUI package metadata license boundary"

[769]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-769-discoverse-real2sim-rasterizer-research-license.md "SRC-robotics-769 DISCOVERSE Real2Sim rasterizer research license"

[770]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-770-discoverse-cabinet-parent-scene-compiler-contract.md "SRC-robotics-770 DISCOVERSE cabinet parent scene compiler contract"

[771]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-771-door-drawer-code-audit.md "SRC-robotics-771 Door drawer code audit and isolated probes"

[772]: ../../../raw/robotics-embodied-ai/documents/SRC-robotics-772-gaussianrenderer-gsplat-backend-implementation.md "SRC-robotics-772 GaussianRenderer gsplat backend implementation"

[能力与证据矩阵CSV](../../../raw/robotics-embodied-ai/data/door-drawer-code-capability-matrix-2026-11-10.csv) · [原文hash与探针清单](../../../raw/robotics-embodied-ai/data/door-drawer-code-audit-provenance-2026-11-10.json)。
