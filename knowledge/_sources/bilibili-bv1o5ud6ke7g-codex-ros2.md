---
title: "具身探索-CodeX控制ROS2机器人"
type: source
date_created: 2026-08-12
last_updated: 2026-08-12
source_urls:
  - https://www.bilibili.com/video/BV1o5ud6kE7G
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-08-12-bilibili-bv1o5ud6ke7g-codex-ros2.json
tags:
  - bilibili
  - video
  - ai-research
  - robotics
  - embodied-ai
status: active
---

# 具身探索-CodeX控制ROS2机器人

> [!summary]
> Bilibili video source packet captured by the daily AI / embodied-intelligence pipeline. This page is a traceable source card, not yet a full industry synthesis.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1o5ud6kE7G |
| BV / video id | `BV1o5ud6kE7G` |
| Author | GundaSmart |
| Published | 2026-08-10 |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-08-12-bilibili-bv1o5ud6ke7g-codex-ros2.json` |

## Transcript Excerpt

哈喽，大家好！如今呢，智能正在逐渐走进我们的工作和生活。那么作为机器人开发者，我们该如何跟上这一轮技术发展的步伐呢？那所谓的就是智能，也就是让人工智能呢拥有一个可以与现实世界交互的身体。它呢能够通过机器人或者智能设备感知环境、理解任务并做出判断。最后呢采取实际的行动，那整个过程呢往往会形成一个封闭的闭环。这一视频呢，我们来尝试一种新的 ROS2 机器人开发方式。我们呢，正在 VS Code 中使用 Code X，并结合 ROS MCP Server，让 AI 直接读取第一智能车的热图运行状态，检查配置文件，诊断系统问题，并调用 Navigation Tool 实现。实车的导航。那为了增加点趣味性呢，我们这里要完成两个任务。第一个呢，就是利用 D435呢识别盆栽，并且计算距离之后呢，调用 Navigation two 移动到指定的附近位置。那第二个呢就是搜索环境中的指定物体，比如标定板，然后呢移动到指定物体。那为了做区别呢，这里呢我们不用那个给人图。好，接下来我们看一下整体的技术架构说明。这里呢我们分为简单的两大块，一块呢就是用户的电脑，另一类的话呢就是机器人的板载主机。那在用户的电脑上面呢，我们可以安装 VS Code，ROS，MFC，VS Server 以及 Code X。那由于 VS Code 的跨平台性呢，我们得用户电脑主机的系统呢，也没有明确的要求。它可以支持 Windows Ubuntu 和 Mac 这里呢，我们以常用的 Windows 平台为例进行解释说明。在 Windows 电脑主机中呢，我们会先安装 VS Code，然后呢安装 Code X 的插件，以及 ROS MCP Server 的虚拟机环境。在我们机器人或智能车上面呢，运行 ROS2、 FASTLIO2的重定位系统以及 Navigation 2。同时呢，也会启动 ROS Bridge，对外提供 WebSocket 的接口，用于通讯。那这里呢，很明显可以看出，ROS MCP Server 呢，位于一个通讯枢纽的位置。它呢，可以把查询的节点，获取 topic 以及定义的消息呢。和定的 service 呢，以及 action 呢等，按照操作转换成 CodeX 能够发现、理解并调用的 MCP 工具。那需要说明的是呢，ROS MCP Server 呢并不是直接与 ROS2通讯。而是通过 ROS Bridge 提供的 WebSocket 接口呢访问机器人。好，接下来呢我们介绍一下 MCP。那 MCP 呢，也就是模型上下文协议的意思。我们可以把它理解为一套连接 AI 与外部工具的通用接口规范。那通过 MCP 协议呢，CodeX ChatGPT Cloud 的 AI 模型呢，不再只能进行文字对话。还可以呢按照统一的方式访问文件、数据库和开发工具，以及整个机器人的系统。那从这个角度来看呢， MCP 不仅是 AI 与软件工具之间的接口。在机器人场景中呢，它也可以成为 AI 连接物理世界的一座桥梁。是不是感觉黑客帝国里的某些场景正在一点点变成现实？ROS MCP Server 呢，就是一套专门面向 ROS 机器人开发的 MCP Server 它呢可以将 ROS 中的节点、 Topic Service 等能力，以 MCP 公约的形式呢。暴露给 CodeX。我们不需要修改机器人原有的 ROS 功能，只需要在机器人端呢运行 ROS Bridge，并在电脑端呢配置好 ROS MCP Server，就可以通过网络建立起连接。那简单来说呢，ROS MCP Server 所做的事情就是把原本主要面向程序员的 ROS 接口转换成 AI 可以发现、理解并调用的工具。接下来呢，我们先介绍安装部署，然后呢会演示两个应用。好，我们先看怎么安装部署。这里用到设备呢，一个呢就是我们的电脑主机，这里呢我们以 Windows 平台为例。那第二个呢，我们有现成的智能车。那第一个步骤呢，我们先在机器人端安装并启动 ROS Bridge。那整个 ROS Bridge 的安装过程呢比较简单，这里呢我们就一笔带过。做过多介绍。那第二个步骤呢，就是在电脑端安装 ROS MCP Server 并接入 Code X。那这里呢要分三个步骤。第一个步骤呢，就是先安装 VS Code 以及 Code X 插件。然后呢安装 UV，以及在...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-08-12-bilibili-bv1o5ud6ke7g-codex-ros2.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[robotics-embodied-ai/00-index|机器人与具身智能]]
- [[ai/00-index|AI]]
