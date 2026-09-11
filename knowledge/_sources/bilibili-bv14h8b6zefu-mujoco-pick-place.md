---
title: "Mujoco仿真自动采集pick&place数据（附代码）"
type: source
date_created: 2026-09-11
last_updated: 2026-09-11
source_urls:
  - https://www.bilibili.com/video/BV14h8b6zEfu
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-09-11-bilibili-bv14h8b6zefu-mujoco-pick-place.json
tags:
  - bilibili
  - video
  - ai-research
  - ai
status: active
---

# Mujoco仿真自动采集pick&place数据（附代码）

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV14h8b6zEfu |
| BV / video id | `BV14h8b6zEfu` |
| Author | 荔枝澄 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-09-11-bilibili-bv14h8b6zefu-mujoco-pick-place.json` |

## Transcript Excerpt

哈喽，大家好，我是李姐。那今天给大家分享一下这个 mujoco 仿真，那仿的这个 SO 100这个pick up and place 这个。数据采集的一个方式啊，这里的话我是使用了一个规控方式。那好处的话就是不用去用这个鼠标呀，或者说用键盘啊，或者说用手柄去控制它去采集这个数据在仿真里面，那也不用去实际的去用啊真机，然后去采集数据。啊，那我们可以做一些简单的实验来去啊进行一个学习。好。然后呢，那这里面的话就是分为几个内容内容，那一个是一个状态机的一个构建和规控的一个使用，规控的一个就是相当于任务之间的串接。还有就是一个数据数据的一个存储，啊以及啊几个相机视野，像 top side 的和那个 rest 的一个相机视野的一个保存。然后的话这里面我们要首先要去修改的就是那个场scene 下面的一个相机的一个添加。要添加三个相机。啊，那当然你添加两个也可以啊。那就比如说你就只有只有 side 和这个 rest 也可以，你用 top 和 rest 也可以。然后这个像这个 rest 的话，它是这个 fix 在这个joe 这个关节上的，所以说我们要去改的是它这个，SO100这个 XML 里面，那其他两个的话，它是 fix 在一个世界坐标下的。也就是那个 top 和 side 这个两个视野。然后还有的话就是我们要去弄，弄一个这个叫，两个框吧，这个框的话就不要，我就没去找那种，就比如说两个真的框，我就用两个这个薄的这个 box 进行一个，画两个颜色吧。然后让他一个是做 target 的，一个做这个source 一个目标，一个这个一个来，这个圆圆，就是相当于起始位置吧。啊，所以然，我们要首先要去把这个 thing 改造一下。啊，可以看看一下。啊，这个地方的话就是一个是啊，还有一个 cube cube 的话之前也弄过。然后地面标记的话就是一个 sour- sour box marker 和这个 target bo- box mar- box marker。然后的话，相机的话 fix fix 在在这个相机视野，然后相机视野的一个调整的话，我上期分享了一个视频的话，大家也可以去看一下。就是可以可以很方便的可视化去一个调节。调调调整这个视野，然后确定它的一个这个安装的一个位置。然后就我这边的 REST 相机的话就是其实其实装的这个这个 move moving joe 这个位置，然后它的一个相关关系什么样的？那也也可以通过上上期分享的一个工具来进行一个调整，然后把那个具体的 pose 和那个，和位位姿的话就固定在这里。啊，那这样的话你的相机视野这一部分就 ok 了。然后的话，整个这个分享这个脚本里面的话是只写了一个归控的一个任务逻辑。那其他的相关组件的话都放在了这个仓库里面的 SRC 下面像 state machine 啊， contact detector 和和一些这个，texture smoother 还有那个 camera re- re- render 等。等等，打开 episode record record 等等。那整个控制的方式的话，就是障碍机给这个迪卡尔的一个，就是末端的一个位，位置位置。那当然这个位置的姿态的话我们是固定那个，夹爪朝下的，这样的话最后抓取这个任务的话会相对简单点，不涉及到别的姿态的一个一个一些旋转啊等等。然后的话是因为它是一个界位信号嘛，那这时候要通过这个平滑器去给出一个 s 的一个曲线，然后在使用这个之前也弄过那个 Kinematic 的一个匹诺曹的一个优化器方法。通过卡萨迪的一个一个求解。得到一个关节角，然后再进行一个位置控制，去通过 DT 啊等等去递增，增量式的一个运动。然后状态机的话就是进行一个切换，那状态机流程，approach design Grasp left move place descend then release settle 和那个 return 啊那分别的话对应就是移动到那个 cube 的一个上方。然后下降，然后抓取，然后提升，然后再移动到目标位置，然后再下降。然后再松开夹爪，然后再等一会，然后再这个返回到 home 位置。好，然后就是接触的话呢，它需要有一个判断，就什么时候算是抓到了。好那，现在那个强化学习里面，其实也也做过类似的，就是通过判断一个接触力和它的一个位置吧，来判断它是否是否真的夹住了。然后...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-09-11-bilibili-bv14h8b6zefu-mujoco-pick-place.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[ai/00-index|AI]]
