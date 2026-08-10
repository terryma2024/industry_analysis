---
source_id: "SRC-robotics-510"
title: "EtherCAT and TSN"
source_type: "technical_documentation"
publisher: "EtherCAT Technology Group"
source_date: "2026-08-09"
url: "https://www.ethercat.org/en/ethercat_and_tsn.htm"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-08-09T09:47:36+00:00"
tags:
  - raw/source
  - source-type/technical-documentation
  - evidence/s
aliases:
  - SRC-robotics-510
---
# EtherCAT and TSN

![](https://www.ethercat.org/images/teaser_top/ETG_TSN_584.jpg)

## EtherCAT and TSN

EtherCAT is the dominant technology in the fieldbus domain, and Ethernet is the standard for wired office applications using switching technology. TSN (Time-Sensitive Networking) is the enabler for real-time communication in a heterogeneous environment. In some cases, a combination of these two technologies is required. A better understanding of TSN and the streaming concept is a precondition for a successful implementation at the factory floor. The adoption of EtherCAT in this environment can be done very efficiently, with an upgrade at the MainDevice side and no changes to the Subordinate Devices, and a moderate extension in the bridges connecting EtherCAT segments.

## What is TSN?

Time-Sensitive Networking is a set of standards to improve the real-time features of today’s commercial (IEEE 802.1) networks through advanced synchronization, availability, guaranteed resources and rapid response. These standards can be supported by switches and end stations. The TSN task group is part of the IEEE 802.1 working group, which is responsible for bridged (switched) networks.

Communication with improved real-time characteristics runs parallel to classic communication methods according to the best effort principle, in which the data exchange works as quickly as possible, depending on the network traffic situation.

TSN can be used in heterogeneous networks and offers different functions such as

- time synchronization
- scheduled traffic with time slices reserved for real time traffic
- frame preemption (interruption of low priority frames with continuation after interrupting traffic is completed)
- stream reservation

All functions are based on a streaming concept with a talker sending not more as a specified amount of data to one or more listeners. EtherCAT can use streams for the transport of data between MainDevice and EtherCAT segments. No changes are required to support the TSN adaptation. The MainDevice can use TSN to run several applications and control multiple EtherCAT segments which allows a higher flexibility on a standard platform.

[![](https://www.ethercat.org/images/technology/EtherCAT_and_TSN_Network_Example.jpg)](https://www.ethercat.org/images/technology/EtherCAT_and_TSN_Network_Example_Full.jpg)  
**TSN enables isolation of EtherCAT communication in a network**

![](https://www.ethercat.org/images/teaser_right/ETG_TSN_right.jpg)
