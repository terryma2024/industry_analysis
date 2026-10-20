---
title: 触觉末端执行器方案来源集
type: source
date_created: 2026-10-20
last_updated: 2026-10-20
sources:
  - knowledge/robotics-embodied-ai/sources.csv
tags: [industry/robotics-embodied-ai, sources, tactile-sensing]
status: active
---

# 触觉末端执行器方案来源集

> [!summary]
> 对应20个方案组、25条新增来源（SRC-robotics-593–617）。产品页A只核验厂商声明；技术文档/代码/论文S不代表本次独立复现。重要参数需对照具体SKU与标定报告。

## 捕获质量与局限

22条完成Defuddle抽取；602仅保留HTML回退；605/607自动抓取及HTML下载返回403，失败记录保留在manifest。后3条均另保存网页工具核阅的选摘转述，不能当作全文。603的GitHub抽取保留代码但有行号噪声，不曾执行。

| 来源 | 发布者 / 等级 | 官方页面 | 本地证据 | 捕获状态与边界 |
|---|---|---|---|---|
| SRC-robotics-593 | Daimon Robotics / A | [Daimon DM-Tac G visuotactile gripper](https://www.dmrobot.com/devices/dm-tac-g.html) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-593-daimon-dm-tac-g-visuotactile-gripper.md) | ok；2026-10-20 accessed; Integrated tactile gripper; vendor parameters; delivery unverified |
| SRC-robotics-594 | Daimon Robotics / A | [Daimon DM-Tac X tactile sensor](https://www.dmrobot.com/devices/dm-tac-x.html) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-594-daimon-dm-tac-x-tactile-sensor.md) | ok；2026-10-20 accessed; 120 Hz and life are vendor claims |
| SRC-robotics-595 | Xense Robotics / A | [Xense Aurora Lite tactile gripper](https://www.xenserobotics.com/product/385/detail/11) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-595-xense-aurora-lite-tactile-gripper.md) | ok；2026-10-20 accessed; Integrated edge compute; vendor specifications |
| SRC-robotics-596 | Xense Robotics / S | [Xense tactile sensor SDK](https://github.com/XenseRobotics/xensesdk) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-596-xense-tactile-sensor-sdk.md) | ok；2026-10-20 accessed; Raw images versus inferred force; SDK snapshot |
| SRC-robotics-597 | Xense Robotics / S | [XenseGripper SAFE mode documentation](https://xensesdk-cn.readthedocs.io/en/latest/GripperSDK/user/API/mode.html) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-597-xensegripper-safe-mode-documentation.md) | ok；2026-10-20 accessed; SAFE mode requires tactile sensor; not safety certification |
| SRC-robotics-598 | PaXini / A | [PaXini DexH13 Gen2 tactile dexterous hand](https://www.paxini.com/product/dex/gen2) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-598-paxini-dexh13-gen2-tactile-dexterous-hand.md) | ok；2026-10-20 accessed; 13 active plus 3 passive DOF; lab specifications |
| SRC-robotics-599 | Inspire Robots / A | [Inspire RH56F1 tactile and non-tactile variants](https://en.inspire-robots.com/product/rh56f1/) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-599-inspire-rh56f1-tactile-and-non-tactile-variants.md) | ok；2026-10-20 accessed; T1 has eight sensors; communication rate not tactile stream rate |
| SRC-robotics-600 | Linkerbot / A | [Linker Hand current product specifications](https://linkerhand.com/) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-600-linker-hand-current-product-specifications.md) | ok；2026-10-20 accessed; Model-specific tactile options and active-passive DOFs |
| SRC-robotics-601 | Linkerbot / S | [LinkerHand Python SDK current repository](https://github.com/linker-bot/linkerhand-python-sdk) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-601-linkerhand-python-sdk-current-repository.md) | ok；2026-10-20 accessed; Replaces archived linkerbotai route; model API needs freeze |
| SRC-robotics-602 | Wuji Technology / S | [Wuji Hand optional tactile sensing glove documentation](https://docs.wuji.tech/docs/en/wuji-hand/v1/overview/) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-602-web-reviewed-facts-2026-10-20.md) | fallback_html；2026-10-20 accessed; Robot-worn optional glove with over 400 sensors |
| SRC-robotics-603 | Wuji Technology / S | [Wuji Hand tactile status example](https://github.com/wuji-technology/wuji-sdk/blob/main/examples/python/wuji_hand/3.tactile_status.py) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-603-wuji-hand-tactile-status-example.md) | ok；2026-10-20 accessed; Public tactile example; hardware untested |
| SRC-robotics-604 | HITBOT / A | [HITBOT eHand-6 optional tactile product page](https://en.hitbot.cc/dexterous-hand/e-hand-6.html) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-604-hitbot-ehand-6-optional-tactile-product-page.md) | ok；2026-10-20 accessed; 6 DOF optional 5-channel touch; no dense shear map established |
| SRC-robotics-605 | XELA Robotics / A | [XELA uSkin integration for Allegro Hand V4 flat](https://xelarobotics.com/products/for-allegro-hand-v4-flat/) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-605-web-reviewed-facts-2026-10-20.md) | failed；2026-10-20 accessed; 312 taxels; 1248 measurements includes 3 axes plus temperature |
| SRC-robotics-606 | Robotiq / A | [Robotiq 2FC physical AI gripper and TSF retrofit](https://robotiq.com/physical-ai-grippers) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-606-robotiq-2fc-physical-ai-gripper-and-tsf-retrofit.md) | ok；2026-10-20 accessed; Preorder shipping Q1 2027; TSF retrofit availability separate |
| SRC-robotics-607 | GelSight / A | [GelSight Mini tactile sensor](https://www.gelsight.com/products/gelsightmini/) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-607-web-reviewed-facts-2026-10-20.md) | failed；2026-10-20 accessed; Optical sensor; current China price unverified |
| SRC-robotics-608 | Meta FAIR / S | [DIGIT tactile sensor design repository](https://github.com/facebookresearch/digit-design) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-608-digit-tactile-sensor-design-repository.md) | ok；2026-10-20 accessed; Open design; hardware and software licenses separate |
| SRC-robotics-609 | Meta FAIR / S | [Digit 360 multimodal tactile sensor project](https://digit.ml/digit360.html) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-609-digit-360-multimodal-tactile-sensor-project.md) | ok；2026-10-20 accessed; Research and early access; current China stock unverified |
| SRC-robotics-610 | Bhirangi et al. / S | [AnySkin plug-and-play skin sensing paper](https://arxiv.org/abs/2409.08276) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-610-anyskin-plug-and-play-skin-sensing-paper.md) | ok；2026-10-20 accessed; Replaceable magnetic skin; generalization in author setting |
| SRC-robotics-611 | Raunaq Bhirangi / S | [AnySkin sensor library](https://github.com/raunaqbhirangi/anyskin) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-611-anyskin-sensor-library.md) | ok；2026-10-20 accessed; MIT software; drift and zero reset documented |
| SRC-robotics-612 | GelSlim authors / S | [GelSlim 4 focusing on touch and reproducibility](https://arxiv.org/abs/2409.19770) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-612-gelslim-4-focusing-on-touch-and-reproducibility.md) | ok；2026-10-20 accessed; Research design; not turnkey industrial gripper |
| SRC-robotics-613 | GelSight Fin Ray authors / S | [GelSight Fin Ray compliant tactile gripper paper](https://arxiv.org/abs/2204.07146) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-613-gelsight-fin-ray-compliant-tactile-gripper-paper.md) | ok；2026-10-20 accessed; Compliant optical tactile prototype; no industrial procurement inference |
| SRC-robotics-614 | Xense Robotics / S | [Xense TacCap Gripper SDK](https://github.com/XenseRobotics-AI/TacCap-Gripper) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-614-xense-taccap-gripper-sdk.md) | ok；2026-10-20 accessed; UMI-like leader-follower; separate optical SDK; not Aurora Lite |
| SRC-robotics-615 | Xense Robotics / A | [Xense GS-PS neutron tactile sensor](https://www.xenserobotics.com/product/367/detail/23) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-615-xense-gs-ps-neutron-tactile-sensor.md) | ok；2026-10-20 accessed; UVC; headline 120 Hz vs table 30-150 Hz |
| SRC-robotics-616 | Wonik Robotics / A | [Allegro Hand current tactile product lineup](https://www.allegrohand.com/index.php) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-616-allegro-hand-current-tactile-product-lineup.md) | ok；2026-10-20 accessed; V5 Plus Sense V6 F; V4 retrofit specs not transferable |
| SRC-robotics-617 | PaXini / A | [PaXini PX-6AX Gen3 tactile sensor modules](https://www.paxini.com/news/ax/gen3) | [本地记录](../../raw/robotics-embodied-ai/documents/SRC-robotics-617-paxini-px-6ax-gen3-tactile-sensor-modules.md) | ok；2026-10-20 accessed; Modular fingers and palm; aggregate sample rate not loop rate |

## 来源编译结论

- 夹爪：593/595支持集成式国产候选；606的2FC明确预订与未来交期。
- 手：598/599/602支持不同自由度与触觉形态；600/604必须确认触觉选配；605的312触点不能写成1248触点。
- 改装：594/615/617/607是传感器级方案，不能隐去支架、线缆、标定与推理成本。
- 研究：608设计非商业许可且已归档；609现货不明；610–613研究结果不等同工业资格；614数采夹爪与595不是同一设备。

## 知识冲突

因时力分辨率与触觉精度、千觉帧率范围、帕西尼英文翻译、XELA触点与测量量、DIGIT商业许可与供货边界均已在下游报告中显式保留。网页未标可核发布日期时，sources.csv日期写待验证，访问日单独保留为2026-10-20。

## 关联连接

- [[robotics-embodied-ai/research-notes/tactile-end-effectors-hands-grippers-selection-2026-10-20|触觉末端方案比较与验收]]
- [[robotics-embodied-ai/00-source-capture-index|机器人来源抽取索引]]
- [[robotics-embodied-ai/00-index|机器人研究入口]]
