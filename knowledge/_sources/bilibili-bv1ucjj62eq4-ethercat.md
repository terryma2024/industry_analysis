---
title: "EtherCAT通讯原理讲解"
type: source
date_created: 2026-08-13
last_updated: 2026-08-13
source_urls:
  - https://www.bilibili.com/video/BV1uCJj62EQ4
evidence_grade: B
sources:
  - raw/_inbox/transcripts/2026-08-13-bilibili-bv1ucjj62eq4-ethercat.json
tags:
  - bilibili
  - video
  - ai-research
  - ai
status: active
---

# EtherCAT通讯原理讲解

> [!summary]
> Bilibili video source packet; its claims are separated and cross-checked in the linked deep research.

## Source Metadata

| Field | Value |
|---|---|
| Platform | Bilibili |
| URL | https://www.bilibili.com/video/BV1uCJj62EQ4 |
| BV / video id | `BV1uCJj62EQ4` |
| Author | 只是芝士知识之事 |
| Published | unknown |
| Favorited | unknown |
| Category | unknown |
| Tags | unknown |
| Extraction method | volcengine-external-command:volc.bigasr.auc |
| Raw artifact | `raw/_inbox/transcripts/2026-08-13-bilibili-bv1ucjj62eq4-ethercat.json` |

## Transcript Excerpt

我是在成都的那个 Michael 吕。今天主要是跟大家分享一下 EtherCAT 这个技术的一些基本介绍，还有它的一些通信原理方面的。还有一些小的一些虚拟的演示。另外就是咱们这个 Microchip 9252的这个一个介绍。那我们就开始。这个是今天的一个课程的一个安排。第一个是对 Ethernet 进行一个总体的介绍。那下面的话呢，就是 Ethernet 一个网络的一个原理，啊，包括它的一个通讯的一个原理。这个讲完以后呢，我们会有一个虚拟的一个演示，就是给大家演示一下，EtherCAT 这个 DC 时钟的一个演示。这个完了以后呢，我们就是9252的这个咱们这个 LAN9252这个芯片的一个介绍。这个在下面呢就是我们最新出的一个 EVP，就是 STM D51跟这个 LAN9252的一个Harmony 的一个。Driver 的一个介绍。啊，最后就是一些总结跟问题啊。稍等一下啊。OK，那我们下面就开始这个 iscat 的这个介绍。EtherCAT 这个技术呢，是一个一一种工业以太网的一个技术。那我们可以看一下，就是这张图上面。工业以太网呢，有很多种技术，有若干种。那基本上市面上目前比较主流的呢，有这个 Profinet 还有这个 Ethernet/IP 还有包括这个 Powerlink 然后还有就是咱们这个 EtherCAT。其他的一些技术呢，也不是不主流，它也有它的一个市场份额，跟它一些应用场合。就说这个工业现场以太网总线呢，是现在一个很热门的一个领域。我们可以看到左边的这个这个图上，左边是一些这个这个现场技术的名字，右边呢就是他们相应的一个组织。比如说咱们这个 Itcast。 那它就是由这个 ETG 就是这个 Ethernet 的这个 Technology Group 在进行一个技术的一个发布，跟它的一个后续一些软件啊，SDK 的维护。所以的话呢，我们每一个技术都有相应的一个组织在后面去进，对它进行一个支持。这个是对他一个进进行一个简单的介绍。那为什么我们要使用一个 cat 呢？就说这个不管是咱们自己的一个学习方面，还是说到客户那边去进行一个分享介绍的时候呢，可能会有这个疑问。对吧？我们有这么多现场总线。那实际上呢，EtherCAT 技术是发展最快的一个工业以太网协议。那右边的话是我们的一个第三方一个市场调调研机构的一个调查的一个数据。Itchat 的这个增长是非常的快。第二个第二点呢，就是说 Itchat 技术呢，可以通过优化每个以太网帧的消息呢来传送，达到网络性能的一个新的高度。这个呢等一下我们会跟大家仔细去介绍。它通过一系列的这个技术的一个优化，基本上可以认为是目前这个性能最好的一个现场总线。然后呢，第三点是它是一个硬件驱动型的价格，对软件的协议站性能依赖性是比较小，也就是说它的这个一致性是比较好的。最后一点呢，其实也是蛮重要的，大家可以看到它有，目前啊，这个其实应该是应该应该是一两年前的数据了，有超过4100个 Excel 的协会的一个会员在全球。那这个呢，首先跟大家再澄清一下，就是说 Ethernet 的会员呢，是完全免费的。就说不管是芯片公司也好，或者是任何一个做想做 Ethernet 的公司，那么你只需要到这个 ETG 就刚才我们看过这个 Ethernet 这个协会的一个网站上。去注册一下，那注册呢基本上只需要填一些简单的信息，还有就是公司的一个营业执照，就可以免费成为他的会员。那成为他的会员之后呢，一个是后续也没有每年的年费。第二个的话呢，它可以，就是说你可以永久地下载它后续不断更新的这个核心的协议站，所以它是完全免费的。啊，而且它的源代码也是开放的，所以呢，这个也是它发展非常快的一个一个原因啊。那我们下面把 EtherCAT 再进行一个简单的一个介绍。EtherCAT 呢代表的就是这个 Ethernet for Control Automation Technology 也就是说它呢是基于 Ethernet 的，这点是很重要的。第二点呢是 EtherCAT 是一种直达 IO级的实时以太网，那它呢最初是由德国的这个 Beckhoff 公司开发的。也就是说它呢通过这个主站，我们可以直接到达每一个从站的一个 IO级别的一个控制。那这个呢是通过它内部的一些帧。的一些特殊结构来实现的，所以它的这个效率非常高。因为我们都知道，在工...

## Research Handoff

- Extract facts, estimates, judgments, and hypotheses from the full transcript in `raw/_inbox/transcripts/2026-08-13-bilibili-bv1ucjj62eq4-ethercat.json`.
- Check whether this should update AI, robotics/embodied AI, integrated circuits, or another industry page.
- Preserve source traceability using the Bilibili URL and BV / video id.
- Do not treat this source as primary evidence for company financials, policy facts, or market size without cross-checking primary sources.

## Related Links

- [[ai/00-index|AI]]
- [[_syntheses/bilibili-ethercat-robotics-control-network-deep-dive-2026-08-14|EtherCAT 控制网络视频深研]]
