---
source_id: "SRC-robotics-509"
title: "EtherCAT G technology overview"
source_type: "technical_documentation"
publisher: "EtherCAT Technology Group"
source_date: "2026-08-09"
url: "https://www.ethercat.org/en/ethercat-g.html"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-08-09T09:47:35+00:00"
tags:
  - raw/source
  - source-type/technical-documentation
  - evidence/s
aliases:
  - SRC-robotics-509
---
# EtherCAT G technology overview

![](https://www.ethercat.org/images/teaser_top/ETG_EtherCAT-G_584x151.jpg)

## Enhanced EtherCAT functionality at gigabit levels

EtherCAT G lifts EtherCAT technology up to gigabit levels – and thus delivers in applications that must transport particularly high process data per device, e.g. in the field of machine vision, high-end measurement technology or in complex motion applications. As an addition to the core EtherCAT technology, EtherCAT G is fully compatible. Existing devices based on 100 Mb/s can be integrated seamlessly because EtherCAT G devices act like traditional EtherCAT devices in a 100 Mb/s EtherCAT system. The well-known benefits of EtherCAT, including data transmission on the fly, comprehensive diagnostics, easy configuration and integrated synchronization, are of course fully retained when EtherCAT G is used and are carried into the connected segments transparently.

![](https://www.ethercat.org/images/technology/EtherCAT_G_G10_Network_Overview.jpg)

## How does it work?

A central element of EtherCAT G is the branch concept. It is realized with the EtherCAT Branch Controllers (EBC), which essentially fulfil two main functions:

- They act as a kind of node for the integration of independent segments with 100 Mb/s devices.
- They enable parallel processing to the connected EtherCAT segments.

As a result the propagation delay is significantly reduced, which increases system performance many times over previous levels.

With the branch concept even big plants can be managed from one central control unit. The configuration of the network participants is conducted EtherCAT-typically by the MainDevice without the need for additional configuration tools.

## Put simply, it’s EtherCAT

EtherCAT G is fully compatible to the IEEE 802.3 Ethernet standard. With EtherCAT G, topology flexibility is fully retained, too: lines, drop lines, daisy chains or tree structures can all be realized. And with the EtherCAT Branch Controllers you now have the possibility to optimally combine Gb/s segments with 100 Mb/s segments in one single network.

![](https://www.ethercat.org/images/teaser_right/ETG_EtherCAT-G_200x151.jpg)
