---
title: "机械臂一碰就穿模？北大英伟达 PhysisForcing 纠正视频生成物理盲区"
type: source
date_created: 2026-07-03
last_updated: 2026-07-03
source_urls:
  - https://www.bilibili.com/video/BV12pTq6qECg
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-03-bilibili-bv12ptq6qecg-physisforcing.json
tags:
  - bilibili
  - video
  - ai-research
  - ai
status: draft
---

# 机械臂一碰就穿模？北大英伟达 PhysisForcing 纠正视频生成物理盲区

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV12pTq6qECg |
| BV / video id | `BV12pTq6qECg` |
| Author | Agent创世纪 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-03-bilibili-bv12ptq6qecg-physisforcing.json` |

## Transcript Excerpt

Agent 创世纪为您讲解物理强化世界模拟。这项研究由北京大学与英伟达共同提出，它旨在解决视频模型接触操作的物理失效。现有模型虽画面逼真，但常出现物体穿模或脱手。研究者提出在训练阶段注入物理约束的方法，具体是在潜空间中强化运动轨迹与交互关系。这样模型能学会遵守真实物理规律与因果逻辑。该方法不增加任何推理时的计算开销，它为具身智能构建更可靠的世界模拟器提供蓝图。视频生成模型视觉保真度飞跃。例如 Sora One 二点二与 Cosmos，它们被视为可扩展世界模拟器，为物理 AI 提供视觉未来。但具身模拟不仅需逼真像素，更需动态符合物理规律。真正的问题在于生成动态是否符合物理规律。数接触操作中，模型出现红色闪电与像素化为影。这些视觉幻象说明算法缺乏接触式物理理解，视觉保真度与物理一致性之间存在本质鸿沟。因此必须突破像素级生成，构建物理一致世界模拟。视频生成模型看似逼真，但在物理交互中频频失效。异常形变让物体在接触瞬间像流体一样扭曲，交互不一致则表现为夹爪闭合后物体纹丝不动。轨迹断裂更为隐蔽，机械臂在两帧之间发生瞬移。这些缺陷暴露了模型缺乏对接触动力学的理解，它们生成的画面只是视觉拼贴。而非物理连贯的世界。如果不解决这些根本问题，世界模拟器就只是空谈。因此，必须从像素层到语义层彻底重塑物理一致性。该矩阵将物理失效划分为两个独立维度。纵轴时间动态衡量运动是否连续，横轴空间尺度从局部像素延伸至全局区域。全局关系错误位于右上象限，涉及语义因果性，其症状包括物体漂浮、脱手等反重力现象。局部动态错误位于左下象限。涉及运动连续性，其症状表现为点轨迹断裂与物体穿模。结论，现有模型无法同时解决这两类问题。目前五个技术流派在四个维度上各有明显短板。通用视频模型如 Sora 和 One 在局部与全局一致性上均失败。机器人导向模型 Cosmos 局部一致性不确定且全局关系失败。几何驱动模型能保证局部运动连续，但丢失了全局语义因果偏好。反馈模型作为事后修正，信号稀疏且不区分核心交互区。几何约束只捕捉局部结构，偏好反馈又不够聚焦。而 Faces Forcing 则四项指标全部成功，包括核心区域聚焦。这证明需要一种训练期分层结构且聚焦关键区域的新范式。物理真实性同时存在于微观与宏观两个维度。微观上，轨迹与接触置换必须连续而不产生断裂。宏观上，对象关系需符合因果逻辑，如推对应远离。第二个原则针对监督的空间分布提出聚焦策略。物理线索高度集中在机械臂与操作物体界面，在全图施加均匀损失会稀释关键的物理信号。因此必须锁定核心交互区实施约束，避免稀释。这两项设计共同为物理强化奠定双重保障基础。输入序列经 VAE 编码器。进入前空间，编码特征进入代替块。这是强化核心区。在代替内部，物理强化分叉为两条并行路径，像素级约束微观运动。语义级约束宏观因果，二者聚焦于物理区域掩码，排除背景干扰。最后经 VAE 解码器输出校正后视频。所有物理知识注入全部在训练阶段闭环完成，推理时不增加计算负担，保持原模型速度。物理信息区域提取是拒绝背景稀释的第一步。全图均匀施加损失会模糊关键动作特征，ExAnything R 则基于深度感知排除背景噪声，两者的输出结合生成二值化的物理掩码 M v C y。掩码仅高亮机械臂和操作物体区域，后续所有物理对齐只在这个发光区域内发生，这确保了监督信号集中在核心交互区。物理对齐分为像素级和语义级两大支柱。像素级对齐以 CoTracker 3提取的点轨迹为目标，它防止物体穿模和轨迹断裂等局部错误。其监督仅作用于单点坐标，不影响背景语义及对齐。以 VJEPA 的时空 token 关系为目标，它防止物体脱手与反重力悬空等宏观问题。两者互补，分别解决微观连续与宏观因果。这种双支柱结构构成了完整的物理对齐框架。像素级物理对齐的核心目标是锁定运动轨迹。他从目标视频中抽取真实轨迹作为物理基准，同时从代替中间层提取特征，用相似度匹配得出预测点，两者之间施加均方误差损失。并由物理区域掩码约束。这相当于在前空间特征中打入无形的物理钢钉，它强制要求底层特征在时间维度保持平滑几何转移。从而从根本上消除局部偏移与穿孔位移。像素级对齐解决了微观运动连续性问题，语义级物理对齐注入因果关系结构。他利用冻结的 VJEA 解码器从真实视频交互区域提取 token 这些 token 之间的关系矩阵天然包含物体...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-07-03-bilibili-bv12ptq6qecg-physisforcing.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[ai/00-index|AI]]
