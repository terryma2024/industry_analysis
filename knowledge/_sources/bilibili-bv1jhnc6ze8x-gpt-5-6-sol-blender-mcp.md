---
title: "GPT 5.6 Sol 操控 Blender 有多强？社区案例、MCP 安装与真实实测"
type: source
date_created: 2026-07-18
last_updated: 2026-07-18
source_urls:
  - https://www.bilibili.com/video/BV1JhNC6zE8X
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-07-18-bilibili-bv1jhnc6ze8x-gpt-5-6-sol-blender-mcp.json
tags:
  - bilibili
  - video
  - ai-research
  - ai
status: active
---

# GPT 5.6 Sol 操控 Blender 有多强？社区案例、MCP 安装与真实实测

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1JhNC6zE8X |
| BV / video id | `BV1JhNC6zE8X` |
| Author | kate人不错 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.seedasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-07-18-bilibili-bv1jhnc6ze8x-gpt-5-6-sol-blender-mcp.json` |

## Transcript Excerpt

大家好，我是凯特。GPT 5.6发布之后呢，社区里已经有非常多 GPT 5.6 Soar 和 Blender 在一起做的Blender 的精彩案例。今天我将介绍一下社区用户怎么去使用它，并且展示我通过 Blender 来做的一些页面，包括我们现在看到的，这是清明上河图的页面。其实让 AI 做 Blender 呢，在去年的时候我就有介绍过，当时用的是 Blender MCP。作者的这个仓库呢，现在已经有23 KS 大了。非常非常受欢迎。Sora 加 Blender 非常火，那背后呢是有两条技术，一是刚刚我们提到的 Blender MCP，第二就是现在的 Sora 模型。它的长城 Agent 还有Ultra 模式都是比较适合使用 Blender 的。主流工作法呢，一是用 MCP 直接来控制 Blender 第二呢是用无头的 Blender 也就是你可以不安装 MCP。提示 CodeX 说你的电脑里面已经安装了 Blender 让它通过无头模式帮你去构建什么。我这两种方式都比较过，发现呢 MCP 的话来构建它的速度会更快。质量会更好。有用户分享，他在纸上呢画了一个机器人的草图，然后用 AI 增强了它，让 GPT 5.6搜，生成所有用于3D打印的零件。然后用强化学习验证设计。有位用户呢，他是花了3小时来做出这样场景非常丰富的建筑场景。场景呢是您外部素材，从几何到材质都是由SOLO 模型来自己构建的，非常非常厉害。我们可以看到它这里用到的是5.6 SOLO ULTRA。这个是比较耗 token 的。作者公开的关键做法是明确写明时间不限，不计积分，然后要世界级的质量。还有博主呢，他用一句提示词。就生成了一个写实的蝙蝠。我们可以看到先是骨架，然后有更多细节，最终生成是这样的效果。同样呢，作者在这里用到的是5.6 so ultra 模式。还有博主对比了用 Three JS 来生成场景。和用无头的 Blender 来生成同样的场景。我们可以看到无头 Blender 生成的场景，它的细节明显是要好于。Threejs 来生成的。还有博主呢用 Sora 模型来生成一个3D的猫，我们看出这个毛茸茸的质感还是非常非常好的。社区反复验证过呢。如果说你给他的提示词太短，就很容易得到方块、球体和无聊贴片的质量一般的资产。而一些高赞的案例呢？基本上都是在提示词里面塞了质量标准、研究步骤、拆分策略，还有时间预算。我们看这样一个例子。他这里呢就先动工前先让他去检索，然后禁止他一次性的去糊弄完成什么。在之后呢，统一色调。再接着是拉起子代理进行分工，并且提示他时间和积分不是约束条件，而是以质量为优先。第六条，每完成一批资产就渲染检查，不通过就返工。这一点也是非常重要的。我在这里完成的清明上河图其实是算模型在很快就完成的。后来才看到这位博主分享的这样的思路。也就是说，我在这个案例里呢，一开始有很多提示都是做的不到位的。要是改成像这样的一个提示，效果应该会好很多。先来看一下如何把 MCP 安装到 CodeX APP 里。我呢是直接问了 GPT 它告诉我先要安装 UV。然后呢在 Blender 里面安装插件，需要先下载仓库中的一个 Python 脚本，然后再把这个插件呢添加到页面里。安装好之后呢，我们再通过 A 键。来进行啊，把这个Blender MCP 展示出来。对应呢，在 Blender 页面，我们会看到有一个 Blender MCP。 这是它的插件。目前呢它是运行着，默认呢它是不开启的，所以我们需要点击一下，让它开启一下。之后呢我们就需要在 Codecademy APP 里面添加 MCP。 比较可靠的方式呢是直接编辑文件。比如说 Mac OS 是这样添加，然后 Windows 是这样添加。我呢在这里也是比较偷懒，直接在 CodeDesk 里面呢。把刚刚我和 GPT 的对话添加到当前任务里，提示 CodeX 是让它帮我添加一下 MCP。当然这个插件也是可以用在别的 AI 里的。比如说 Cloud Code 或者Grok CUI 或者是 Cursor 什么的都是可以的。如果大家在安装方面有一些问题的话。可以看一下我之前的视频。现在就给大家看一下我的实测。一开始我将这样一张图发给他，然后我选择的模型模式呢是 So Media。这也是为了节约 token 我发现在这个模式下，它生成的速...

## Research Handoff

- 已完成单视频深研：[[../_syntheses/bilibili-codex-blender-mcp-toolchain-deep-dive-2026-07-18|Codex 与 Blender MCP 工具链视频深度调研]]（R05 主分类，R07 次分类）。
- BlenderMCP 架构已用 `SRC-ai-082` 项目 README 核验；视频 ASR 中的模型名称、模式、耗时、质量和案例仍为待验证线索。

## Related Links

- [[ai/00-index|AI]]
