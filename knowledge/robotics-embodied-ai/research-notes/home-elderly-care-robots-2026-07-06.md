---
title: 家庭养老机器人公司与方案调研
type: synthesis
date_created: 2026-07-06
last_updated: 2026-07-06
sources:
  - knowledge/robotics-embodied-ai/03-market-and-policy.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-003-source.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-006-2025.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-082-source.md
  - raw/robotics-embodied-ai/documents/SRC-robotics-083-source.md
  - https://elliq.com/
  - https://elliq.com/pages/caregivers
  - https://labradorsystems.com/products/
  - https://www.1x.tech/neo
  - https://www.figure.ai/figure
  - https://www.fftai.com/products-gr3series
  - https://hyodol.com/
  - https://joyforall.com/
  - https://www.businessinsider.com/weave-robotics-isaac-1-8000-home-robot-chores-2026-7
  - https://www.techradar.com/ai-platforms-assistants/ubtech-just-introduced-its-first-full-size-ultra-bionic-humanoid-robot-but-what-it-really-wants-to-do-is-make-robot-replicas-of-loved-ones-thats-a-hard-no
  - https://arxiv.org/abs/2410.12205
  - https://arxiv.org/abs/2302.12686
tags:
  - industry/robotics-embodied-ai
  - eldercare
  - home-care
  - service-robots
  - embodied-ai
status: draft
---

# 家庭养老机器人公司与方案调研

> [!summary]
> 家庭养老机器人不是一个单一产品市场，而是四条路线的叠加：AI 陪伴与照护提醒、移动巡视与远程看护、取物搬运等轻体力辅助、康复护理与通用家务机器人。2026 年更接近商业化的是“陪伴/提醒/家属 App/传感器/社区服务”组合，而不是全能人形保姆。

## 核心判断

- **当前最可落地的是照护操作系统，而不是机器人本体**：ElliQ、Hyodol 等产品证明，家庭养老的第一层价值是语音陪伴、用药/饮水/运动提醒、家属连接、生活状态摘要和异常提示。硬件可以是桌面机器人、玩偶机器人、屏幕音箱或低速移动底盘。
- **近中期物理辅助的可行切口是移动载物和“找人”**：Labrador Retriever/Caddie 用室内地图、固定站点、语音/App 调度和托盘搬运解决取物、送水、送药、减少弯腰走动的问题，明显比“全屋做家务的人形机器人”更窄也更可信。
- **康复护理和人形家务机器人仍应分层看**：傅利叶等中国公司在康复机构、医疗康养和 Care-bot 方向有技术与渠道基础；1X NEO、Figure 03、Weave Isaac、特斯拉 Optimus 和优必选 UWorld U1 更像“未来家务/陪伴平台”线索，安全、隐私、远程接管、售后和真实复购仍未充分验证。
- **中国机会不宜从“老人买一台昂贵人形机器人”开始**：更现实的方案是面向独居/半失能/认知下降风险老人，做低成本终端 + 家属微信小程序/App + 居家 IoT + 社区养老站/医生/护士服务的闭环，再逐步加入移动巡视、取物送药、康复训练和遥操作能力。

## 需求与政策背景

中国养老压力足够大。[[robotics-embodied-ai/03-market-and-policy|机器人市场与政策]] 已记录：截至 2025 年末，中国 60 岁及以上人口约 3.23 亿，占 23.0%；65 岁及以上人口约 2.24 亿，占 15.9%；养老服务床位约 768 万张。证据见国家统计来源 [`SRC-robotics-006`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-006-2025.md)。

政策上，`机器人+` 应用行动把医疗、养老等场景列为机器人推广方向之一，见 [`SRC-robotics-003`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-003-source.md)。地方层面，北京人形机器人训练与评测中心提到共建商业服务、家庭、养老等典型场景，亦庄也把医疗康养列为标杆应用方向，见 [`SRC-robotics-082`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-082-source.md)。上海具身智能行动方案则明确支持医疗机构、养老机构探索医疗康养服务中的示范应用，见 [`SRC-robotics-083`](../../../raw/robotics-embodied-ai/documents/SRC-robotics-083-source.md)。

但政策牵引不等于家庭端马上爆发。家庭养老场景存在五个硬约束：老人安全、隐私与家属授权、售后维护、支付意愿、责任划分。尤其是带摄像头、麦克风、遥操作和机械臂的设备，家庭接受门槛高于机构试点。

## 方案分层

| 层级 | 代表能力 | 典型公司/产品 | 商业化判断 |
|---|---|---|---|
| 1. 陪伴与提醒 | 对话、情绪陪伴、用药/饮水/运动提醒、家属连接 | ElliQ、Hyodol、Joy for All、LOVOT | 最接近规模化，但更像“AI 照护终端”而非传统机器人。 |
| 2. 远程巡视 | 视频通话、找人、夜间巡房、异常提醒、远程看护 | Amazon Astro、Temi 类远程临场机器人、家庭摄像头+AI 方案 | 价值明确，隐私和误报是核心问题。 |
| 3. 轻体力辅助 | 室内移动载物、送水送药、减少弯腰和走动 | Labrador Retriever/Caddie、未来小型移动底盘 | 比人形机械臂更窄，适合半失能与术后恢复人群。 |
| 4. 康复护理 | 步态/上肢康复、训练计划、机构护理辅助 | 傅利叶 RehabHub/GRx/GR-3、Lio 等 | 先在医院、康复中心、养老机构落地，再下沉到家庭。 |
| 5. 通用家务 | 洗衣、整理、清洁、拿取、做饭等多任务操作 | 1X NEO、Figure 03、Weave Isaac、Tesla Optimus、优必选 UWorld U1 | 2026 年仍是早期高风险路线，需警惕宣传和真实自治能力差距。 |

## 公司与产品横向

| 公司/产品 | 国家/路线 | 已公开功能 | 落地状态 | 研判 |
|---|---|---|---|---|
| Intuition Robotics / [ElliQ](https://elliq.com/) | 美国；桌面 AI 养老陪伴机器人 | 健康/疼痛/情绪追踪、用药与补水提醒、运动建议、视频通话、娱乐陪伴、家属 App 与照护洞察。Caregiver 页面还强调家属可收到痛感/情绪变化、最后活跃时间、照片展示等信息。 | 官方会员制：一次性 lease initiation fee 加月费；官网称产品面向独居老人并有家属端。 | 家庭养老产品定义最清晰的标杆之一。局限是无移动和物理操作，官网也声明不是医疗设备。 |
| [Hyodol](https://hyodol.com/) | 韩国；AIoT 玩偶/陪伴照护平台 | 日常管理、认知/痴呆预防内容、互动、安全管理、生活日志与个性化 coaching。 | 官网称其为韩国 care robot，并积累大量 senior life-log data。 | 对中国社区养老最有参考价值：硬件温和、照护流程强、适合 B2G/B2B2C。 |
| [Joy for All](https://joyforall.com/) | 美国；陪伴宠物与老人游戏 | Companion Pets 会对声音和触摸做出反应；Walker Squawkers 用于提醒老人使用助行器；游戏产品面向老年记忆和互动。 | 成熟消费品形态，价格和使用门槛低。 | 适合作为低成本情绪陪伴和认知活动入口，但缺少连续看护、异常监测和物理辅助。 |
| [LOVOT](https://lovot.life/en/) | 日本；情绪陪伴机器人 | 目标是让用户开心、回应情绪、提供温暖陪伴。 | 消费级陪伴机器人，官网提供购买/订阅计划。 | 证明“被爱/陪伴”是一个需求，但养老刚需和家属照护闭环较弱。 |
| [Labrador Retriever/Caddie](https://labradorsystems.com/products/) | 美国；室内移动载物/取物辅助 | 家庭地图、站点导航、App/语音/蓝牙/计划任务控制；Caddie 载重 25 lb；Retriever 支持自动托盘取回、托盘约 10 lb。 | 面向家庭行动不便场景，产品规格强调单层地面、避障、传感器和自充电。 | “窄任务物理辅助”很适合养老：送水送药、餐食、洗衣篮、减少跌倒风险。 |
| [Fourier GR-3 / RehabHub](https://www.fftai.com/products-gr3series) | 中国；康复机器人 + Care-bot/人形 | GR-3 定位 Caring and Capable Companion，强调 wellness companionship、55 自由度、双热插拔电池、远程操作与模块化；傅利叶康复业务服务全球机构。 | 机构康复基础较强，GR-3 面向护理/陪伴和未来个人空间。 | 国内“医疗康养 + 具身智能”最值得跟踪的公司之一，但家庭端价格、服务与安全仍需验证。 |
| [1X NEO](https://www.1x.tech/neo) | 挪威/美国；家庭人形机器人 | 家务、日程任务、Expert Mode 远程协助、软质外壳、低噪声、腱驱动、自动充电、语音/手机控制。 | 官方称 early access 具备基础自治，并会随使用学习。 | 家庭人形路线的关键样本；养老价值取决于远程接管透明度、隐私策略、故障处理和真实家务成功率。 |
| [Figure 03](https://www.figure.ai/figure) | 美国；通用人形机器人 | 官方宣称可做 laundry、cleaning、dishes 等家庭任务，Helix VLA 支持家庭环境理解和自主任务。 | 从劳动力场景向家庭帮助延展。 | 技术叙事强，但养老场景专用功能、价格、售后和监管责任还不清楚。 |
| Tesla [Optimus](https://www.tesla.com/AI) | 美国；通用双足机器人 | 官方定位为执行 unsafe、repetitive、boring tasks 的通用双足机器人。 | 仍以通用机器人研发和示范为主。 | 需作为长期平台期权跟踪，不应当成当前家庭养老方案。 |
| Weave Robotics / Isaac 1 | 美国；轮式家务机器人 | [Business Insider](https://www.businessinsider.com/weave-robotics-isaac-1-8000-home-robot-chores-2026-7) 报道其主打洗衣、铺床、整理等家务，支持 App 与远程协助，价格约 7999 美元或 449 美元/月。 | 2026 年 7 月媒体报道的新产品，交付节奏和真实能力待验证。 | 轮式家务机器人比双足成本和安全压力小，但目前证据主要来自媒体，需补官网/用户部署验证。 |
| UBTECH UWorld U1 | 中国；陪伴/仿真人形线索 | [TechRadar](https://www.techradar.com/ai-platforms-assistants/ubtech-just-introduced-its-first-full-size-ultra-bionic-humanoid-robot-but-what-it-really-wants-to-do-is-make-robot-replicas-of-loved-ones-thats-a-hard-no) 报道其面向社交孤独和情感陪伴，具有仿真皮肤、表情和大模型交互等能力。 | 2026 年媒体线索，家庭真实部署和伦理细节待验证。 | 中国家庭陪伴机器人可关注优必选，但 3D 人脸/声音复刻等方向需要特别审视隐私与伦理风险。 |

## 可行产品方案

### 方案 A：AI 陪伴 + 家属照护 App

目标用户是独居老人、空巢老人、轻度认知下降老人，以及异地子女。硬件可以先不是移动机器人，而是桌面机器人、屏幕音箱或温和玩偶形态。

核心功能：

- 老人端：自然语言对话、方言适配、日程/用药/饮水/运动提醒、情绪陪伴、小游戏和认知训练。
- 家属端：每日摘要、最后活跃时间、提醒完成情况、异常情绪/疼痛/长时间无响应提示、视频通话。
- 服务端：紧急联系人、社区养老站、家庭医生、上门护理和售后维修工单。
- 数据策略：默认最小化采集，敏感音视频本地处理或明确授权上传，远程人工介入必须可见、可追溯、可关闭。

适合商业模式：硬件低毛利 + 月费订阅 + 社区/保险/养老机构 B2B2C。中国本土化关键在微信生态、社区网格、医保/商业保险/长护险衔接、方言和反诈教育。

### 方案 B：移动巡视 + 找人 + 远程看护

目标用户是跌倒风险、夜间起居风险和子女远程照护压力较大的家庭。产品形态可以是低速移动底盘 + 摄像头/麦克风/扬声器 + 夜灯 + 呼叫按钮。

关键不是让机器人“做家务”，而是把老人是否安全这件事做成闭环：定时巡房、老人呼叫、长时间无响应核查、夜间辅助照明、远程视频确认、必要时通知家属或社区人员。

主要风险：室内导航失败、误报/漏报、摄像头隐私、老人拒绝感、网络断连、电池与充电可靠性。

### 方案 C：移动载物 + 送水送药

目标用户是行动不便、术后恢复、轻中度失能或与照护者同住但需要减少护理负担的人群。Labrador 的窄任务路线说明，养老机器人的物理价值可以先从托盘、篮子、药盒、杯子开始。

中国版可以先不做灵巧手：固定托盘、药盒抽屉、杯架、夜灯、语音调度、固定站点导航、跌倒不跨越策略，服务 80% 高频小任务。等真实家庭数据和售后网络跑通后，再考虑机械臂和抓取。

### 方案 D：机构康复先行，家庭作为二阶段

康复训练、护理搬运和复杂辅助动作更适合先在医院、康复中心、养老机构验证。原因是机构有专业人员、空间可控、付费主体清晰、设备维护集中，能先形成训练数据、疗效评估和安全 SOP。

家庭化路径应从康复设备小型化、租赁、远程医生/治疗师指导开始，而不是直接把高自由度人形机器人卖给家庭。

## 中国公司与机会地图

国内真正以“家庭养老机器人”为核心、且已大规模家庭部署的标杆仍少。更成熟的能力分散在三类主体：

- **康复/医疗机器人公司**：傅利叶等已有机构渠道和康复产品，适合从“医疗康养机构”切入。
- **人形/具身智能公司**：优必选、傅利叶、智元、宇树、逐际动力等值得跟踪，但多数还处于家庭场景展示、开发者平台或非养老通用路线。
- **智能家居和 IoT 服务商**：音箱、摄像头、门磁、毫米波雷达、可穿戴、紧急按钮、家庭网关和 App 已经接近养老所需的传感器层，缺的是照护 workflow、可信 AI 和机器人移动/互动终端。

因此，一个中国创业或投资视角下更稳的切入点是：

1. 先做老人端 AI 终端 + 家属端 App + IoT 传感器。
2. 绑定社区养老站、物业、家庭医生或商业护理服务。
3. 用订阅和服务费覆盖人工介入、设备维护和异常响应。
4. 在真实家庭中积累低风险数据：作息、提醒、呼叫、无响应、照护工单。
5. 再加入低速移动底盘和载物能力，最后才考虑机械臂与人形本体。

## 评价框架

评估家庭养老机器人公司时，不应只看视频里的任务数量，应按以下问题打分：

- **需求刚性**：解决的是孤独、提醒、找人、送药、跌倒风险、康复训练，还是泛泛“陪伴/家务”？
- **老人可控感**：老人能否随时关闭、拒绝、改提醒、知道谁在远程接入？arXiv `2302.12686` 的独立居住老人研究提示，老年人对身体辅助有偏好，同时重视对机器人辅助的控制权。
- **中国适配**：是否支持方言、微信家属群、社区养老站、家庭医生、长护险或地方养老服务平台？
- **隐私与责任**：摄像头、麦克风、遥操作、家庭数据训练是否有清晰授权、日志、最小化采集和退出机制？
- **可靠性与售后**：能否处理断网、找不到充电桩、卡住、误报警、老人误触、家属不在线？
- **支付与渠道**：ToC 单价是否可接受？是否能通过社区、养老机构、保险、政府采购或租赁降低一次性门槛？
- **证据质量**：是真实家庭复购和留存，还是展会演示、媒体试用和预售？

## 投资与职业观察

- 投资上，短期更应关注“养老照护 workflow + 终端 + 服务网络”的公司，而不是只关注高自由度本体。硬件毛利可能不高，持续价值在数据闭环、家属端粘性、社区服务调度和异常响应。
- 对国内机器人公司，医疗康养机构场景比普通家庭更容易形成订单和训练数据。家庭端要等成本、可靠性和隐私治理再降一档。
- 对职业路径，家庭养老机器人需要复合能力：机器人产品经理、老年人 UX、IoT/边缘 AI、语音交互、隐私合规、服务运营、医疗康复/护理流程。纯算法或纯硬件都不够。
- 研究上要警惕“陪伴机器人价值主张错配”。arXiv `2410.12205` 对中国退休群体焦点小组的研究指出，当前 companion robot 价值主张与健康老年人的需求可能存在错配，采用意愿受自我披露、陪伴质量、差异化价值和社区养老服务融合影响。

## 待验证清单

- 中国家庭养老机器人量产产品清单：优必选 UWorld U1、科沃斯/小度/小米/华为生态、养老 IoT 厂商和地方试点项目是否已有家庭真实部署数据。
- 价格带：老人端愿付、子女愿付、社区/政府/保险愿付分别是多少。
- 监管：家庭远程看护视频、遥操作和老人健康数据是否涉及个人信息保护、医疗器械、互联网诊疗或养老服务规范。
- 真实留存：陪伴机器人 30/90/180 天留存、提醒完成率、家属端活跃、异常响应闭环率。
- 安全：移动底盘在中国家庭高门槛、地毯、杂物、宠物、夜间环境下的可靠性。

## 关联连接

- [[robotics-embodied-ai/00-index|机器人（具身智能）]]
- [[robotics-embodied-ai/03-market-and-policy|机器人市场与政策]]
- [[robotics-embodied-ai/04-companies|机器人公司与竞争]]
- [[robotics-embodied-ai/13-robot-company-product-comparison-2026-06-08|机器人公司产品型号全景对比]]
- [[_concepts/embodied-ai|Embodied AI]]
- [[_concepts/robot-training-data|Robot Training Data]]
