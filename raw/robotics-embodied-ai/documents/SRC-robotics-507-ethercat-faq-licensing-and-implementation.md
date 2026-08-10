---
source_id: "SRC-robotics-507"
title: "EtherCAT FAQ licensing and implementation"
source_type: "technical_faq"
publisher: "EtherCAT Technology Group"
source_date: "2026-08-09"
url: "https://www.ethercat.org/en/faq.html"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-08-09T09:47:34+00:00"
tags:
  - raw/source
  - source-type/technical-faq
  - evidence/s
aliases:
  - SRC-robotics-507
---
# EtherCAT FAQ licensing and implementation

![](https://www.ethercat.org/images/teaser_top/ETG_FAQs_584.jpg)

## EtherCAT FAQs

## 1\. EtherCAT Technology

## 2\. EtherCAT Technology Group

- [2.1 Do I have to be an ETG member to use EtherCAT?](#776)
- [2.2 Do I have to be an ETG member to implement EtherCAT?](#779)
- [2.3 How can I become a member of the EtherCAT Technology Group?](#781)
- [2.4 What are the membership benefits?](#782)
- [2.5 ETG Membership is free of charge - why?](#784)
- [2.6 And will this be changed?](#783)
- [2.7 How do ETG members have an impact on the technology?](#785)
- [2.8 What is the legal status of the EtherCAT Technology Group?](#7546)

## 3\. EtherCAT: Open Technology

- [3.1 EtherCAT is an open technology. What does this mean?](#787)
- [3.2 Are there any patents?](#788)
- [3.3 How about licences?](#789)
- [3.4 How about Open Source?](#790)
- [3.5 Are there multiple sources for the EtherCAT SubDevice Controller?](#791)

## 4\. Implementation Aspects

- [4.1 We want to implement an EtherCAT SubDevice. What do we need?](#795)
- [4.2 We want to implement an EtherCAT MainDevice. What do we need?](#796)
- [4.3 How about the license for EtherCAT SubDevice Controller chips?](#2592)
- [4.4 How about the license for FPGAs?](#793)
- [4.5 Do we have to submit our EtherCAT device to a Conformance Test Center?](#797)

## 5\. EtherCAT Vendor ID

- [5.1 What is the EtherCAT Vendor ID?](#2972)
- [5.2 Our sister/affiliated company has an EtherCAT Vendor ID. May we use this ID for our devices?](#2973)
- [5.3 We are using an interface board from a technology provider to add EtherCAT connectivity to our device. May we use the Vendor ID of that technology provider for our device, too?](#2975)
- [5.4 What is a secondary Vendor ID?](#2976)
- [5.5 We have a CANopen® Vendor ID. Can we use that for our EtherCAT device?](#2977)
- [5.6 How do we apply for our Vendor ID?](#2978)

## 6\. Safety over EtherCAT

- [6.1 Do I need a redundant EtherCAT Interface within my Safety over EtherCAT device?](#3363)
- [6.2 Do I need redundant controller architecture for my Safety over EtherCAT device?](#3364)
- [6.3 Can I use Safety over EtherCAT via other communication systems than EtherCAT?](#3365)
- [6.4 Is there a certified Safety over EtherCAT stack available?](#3368)
- [6.5 Is a Safety over EtherCAT Conformance Test available?](#3369)
- [6.6 Do I need an approval by a notified body (e.g. TUV, BGIA) for my Safety over EtherCAT device?](#3366)
- [6.7 Do I need to perform an official test at an FSoE Test Center for my device approval?](#6310)
- [6.8 Why do I need a licence to use the Safety over EtherCAT protocol within my device?](#3370)
- [6.9 How can I get and use the Safety over EtherCAT logo?](#3371)
- [6.10 I'm an EtherCAT MainDevice vendor. How can I support Safety over EtherCAT SubInstances?](#3373)
- [6.11 I'm a machine builder. Do I need a license to use Safety over EtherCAT devices?](#3374)
- ## 1\. EtherCAT Technology
- **1.1 EtherCAT is faster than my application requirements. Why should I use it?**
	Superior fieldbus performance never harms. Even with slow controls, it improves reaction times and reduces configuration effort, since default settings will do the job. Furthermore, shorter reaction times improve the performance of your application, since the transition waiting times are reduced (e.g. waiting for an input signal before the next process step is initiated). If you do not care so much about performance though, use EtherCAT for its other benefits: e.g. lower costs, more flexible topology or simply ease of use. Or, why use a slower system just before it is more expensive?
- **1.2 Why does EtherCAT provide cost advantages?**
	For several reasons: Inexpensive SubDevice controllers lead to lower SubDevice costs. No special MainDevice card required, the on-board Ethernet controller is sufficient. No switches or hubs required, therefore lower infrastructure costs. Use of standard cabling. Simple to implement, therefore lower implementation costs. Auto-configuration is supported, no manual address setting required, no network tuning required, therefore lower configuration costs.
- **1.3 Is EtherCAT limited to MainDevice/SubDevice Applications?**
	No. Like with every real time Industrial Ethernet system, one device (the MainDevice) has to be in charge of the network management and organize the Medium Access Control. With EtherCAT, SubDevice to SubDevice communication is supported in two ways: topology dependent within one communication cycle ("upstream" device talks to "downstream" device), topology independent within two cycles. Since EtherCAT is so much faster than competing systems, SubDevice-to-SubDevice communication using two cycles is faster, too.
- **1.4 How is the interoperability of EtherCAT devices maintained?**
	Conformance and interoperability are very important factors for the success of a communication technology. Therefore the EtherCAT Technology Group is taking these topics very seriously. Conformance of the technology implementation with the specifications is the pre-requisite of interoperability, which means that devices of different manufacturers co-operate within the same networked application. To ensure this approach, the use of the Conformance Test Tool (CTT) is mandatory. Furthermore there are EtherCAT Conformance Test Centers (ETC) troughout the world. For devices that pass theEtherCAT Conformance Test at an official ETC, a conformance certificate is issued.  
	More information about conformance and certification of devices can be found within the conformance section here:  
	[Conformance & Interoperability](https://www.ethercat.org/en/conformance.html)
- **1.5 EtherCAT uses the Master/Slave Medium Access Control (MAC) method. How about inclusive language?**
	The EtherCAT medium access control method follows the master/slave principle: only the main device sends frames, the subordinate devices process them. While it is considered ethically acceptable for one electronic device to impose communication behavior on another electronic device, there are people and institutions that have concerns about the use of these terms in technical descriptions and specifications. Since ETG does not intend to offend, we will use the terms MainDevice (abbreviated MDevice) and SubordinateDevice (abbreviated SubDevice). In our (new) documents we will thus replace 'Master' by 'MainDevice' or 'MDevice', and 'Slave' by 'SubDevice', and will show the terms MainDevice and SubordinateDevice in the list of abbreviations.  
	FSoE Terminology: The Safety over EtherCAT technology uses a master/slave relationship between the FSoE Master Instance and an FSoE Slave Instance: State transitions are initiated by the FSoE Master and acknowledged by the FSoE Slave. The term ‘FSoE MainInstance’ (abbreviated FSoE MInstance) will replace ‘FSoE Master’ and ‘FSoE SubordinateInstance’ (abbreviated FSoE SubInstance) will replace ‘FSoE Slave’.
- ## 2\. EtherCAT Technology Group
- **2.1 Do I have to be an ETG member to use EtherCAT?**
	No. However, you may want to consider joining the ETG in order to indicate your interest in and support for this technology to your suppliers and customers. As a member of the group, you are invited to attend the ETG meetings, you get access to technology information, specifications, presentations and can influence the direction in which the technology moves.
- **2.2 Do I have to be an ETG member to implement EtherCAT?**
	If you implement EtherCAT in your machine or machine line by using EtherCAT devices, you are considered an end user and do not have to join ETG, even though we would recommend it (see 2.1/2.4). Manufacturers of EtherCAT devices have to join ETG and need a valid EtherCAT Vendor ID. For details see EtherCAT Vendor ID Policy within the download section here (you have use your member login):  
	[EtherCAT Vendor ID Policy](https://www.ethercat.org/en/downloads/downloads_92BF652860154453B4D16C903CB9E722.htm) Please keep in mind that membership is free of charge (see 2.5/2.6).
- **2.3 How can I become a member of the EtherCAT Technology Group?**
	To apply for a membership please contact the ETG Headquarters by sending an email to [info@ethercat.org](mailto:info@ethercat.org). All necessary information, e.g. requirements and the membership application form will be provided.  
	Please inform yourself about the by-laws before becoming a member of the group here:  
	[ETG Membership By-Laws](https://www.ethercat.org/en/downloads/downloads_6820D9C60B074CF9B9167468468C9B36.htm)
- **2.4 What are the membership benefits?**
	ETG members enjoy preferred support, get access to EtherCAT specifications, guidelines, a free SubDevice stack code (SSC) and other supportive tools and information which is available for ETG members only.  
	They are invited to the ETG meetings like the Technical Committee (TC) or one of the Technical Working Groups (TWG), e.g. where the specs are reviewed and discussed. ETG members are eligible to participate in dedicated EtherCAT training classes and development workshops. Furthermore, ETG members may promote their products on the EtherCAT website, participate as partners in our global seminar series and on the joint ETG booths at major worldwide trade shows. [ETG Membership Benefits](https://www.ethercat.org/en/membership_benefits.html)
- **2.5 ETG Membership is free of charge - why?**
	Access to an open technology should not be a question of annual membership fees or other significant costs. Therefore not only the ETG membership is free of charge, but for ETG members protocol stacks, sample code, evaluation kits, implementation support and other services are either free or available for a nominal fee.
- **2.6 And will this be changed?**
	There are no plans to charge for the ETG membership. If there is a need for membership fees in the future (e.g. to support additional services provided by the ETG), the membership assembly will have to take this decision.
- **2.7 How do ETG members have an impact on the technology?**
	At the ETG technical committee meetings the EtherCAT technology is presented and discussed in detail. Members are encouraged to join the technical working groups and task forces and provide comments as well as propose enhancements. A list of all working groups is available within the member area here (you need to login to see details):  
	[ETG Technical Working Groups](https://www.ethercat.org/memberarea/en/technical_working_groups.htm) This feedback and the requirements of users, OEMs, system integrators and device manufacturers are both valuable and welcome and considered for implementation. The ETG history showed that this approach works very efficiently. Direct and personal contact between technology users and developers allow for in-depth exchange of know-how and technical information. Please find detailed information on how every member get involved in ETG here:  
	[ETG Organisation Structure](https://www.ethercat.org/en/tech_group.html)
- **2.8 What is the legal status of the EtherCAT Technology Group?**
	ETG is – similar to most unions or political parties in Germany – a non-registered association or „nicht eingetragener Verein“, which is a legal entity by German law. According to the By-laws, and because ETG does not sell any products, ETG is a non-commercial association. Members are only liable for up to their share of assets in the association – and since ETG has no assets, the liability is factually nil.
- ## 3\. EtherCAT: Open Technology
- **3.1 EtherCAT is an open technology. What does this mean?**
	This means that everybody may use, implement and benefit from this technology. This also means that EtherCAT implementations have to be compatible, and nobody may change the technology in a way that prevents others to use it. EtherCAT is standarized in several international standards (IEC61158, IEC 61784, IEC 61800, ISO 15745) and is also a SEMI standard (E54.20).
- **3.2 Are there any patents?**
	Yes, there are patents on the EtherCAT technology just like there are patents on every other fieldbus technology that is worth it. Technologies that provide unique features need patents and licenses to protect them from being copied or falsified.
- **3.3 How about licences?**
	There is a licence for implementing an EtherCAT MainDevice which is free of charge - the agreement demands compatibility, ensures that the licence remains free of charge and provides legal certainty. For SubDevices EtherCAT has adopted the CAN license model (CAN is an excellent example for a standardized open technology that is protected by patents): The small license fee is "embedded" in the EtherCAT SubDevice Controller (ESC) chip, so ESC vendors need a license, but device manufacturers, end users, system integrators, tool manufacturers etc. do not have to pay a license.
- **3.4 How about Open Source?**
	EtherCAT technology itself is not Open Source. Backed by the standardization of EtherCAT by IEC, ISO and SEMI, access to EtherCAT technology is available to everyone to non-discriminatory terms. Additionally, MainDevice Licenses are free of royalties. Maintenance and all further development of the technology is available to all users by membership within the ETG, the user group for EtherCAT technology. If you have questions regarding implementing or using EtherCAT in conjunction with shared source or open source systems please contact ETG headquarters or Beckhoff, the EtherCAT technology licensor.
- **3.5 Are there multiple sources for the EtherCAT SubDevice Controller?**
	Yes. EtherCAT SubDevice Controller (ESC) implementations are available from Artichip, ASIX Electronics, Beckhoff, Codefair, GigaDevice, Hilscher, HMS Industrial Networks, HPMicro Semiconductor, Infineon Technologies, Microchip, Nations Technologies, NSING Technologies, NXP Semiconductors, Renesas Electronics, Texas Instruments, Triductor Technology, Yaswaka, as well as IP cores for FPGAs from Altera (Intel), AMD, Microship, and Lattice. Further implementations are following.  
	An ESC overview can be found within the download section here:  
	[EtherCAT SubDevice Controller](https://www.ethercat.org/en/downloads/downloads_70CA98412F1440E695C5AA1D2BC2418F.htm)
- ## 4\. Implementation Aspects
- **4.1 We want to implement an EtherCAT SubDevice. What do we need?**
	A good starting point is the SubDevice Implementation Guide, available for download here:  
	[EtherCAT SubDevice Implementation Guide](https://www.ethercat.org/en/downloads/downloads_7BA2567EB9F443219AD0014448F674F2.htm)  
	This document contains first steps when starting a SubDevice implementation including information about development hardware, software, workshops and trainings, conformance and a step-by-step instruction. EtherCAT SubDevice stacks are available from several suppliers. Beckhoff provides its Slave Stack Code (SSC) free of charge to all ETG members – in source code. EtherCAT SubDevice implementation kits are also available from several suppliers. Please find more evaluation kits within the official EtherCAT Product Guide:  
	[EtherCAT Product Guide](https://www.ethercat.org/en/products.html) > Development Systems, Tools > SubDevice Evaluation Kits
- **4.2 We want to implement an EtherCAT MainDevice. What do we need?**
	For a MainDevice, you do not need a special hardware. Any Ethernet MAC will do. Since EtherCAT is very easy on resources, you do not need a dedicated communication processor, either. MainDevice code is available from several suppliers, ranging from several free of charge open source projects via a sample code package to products that include the RTOS. Implementation services are also available from several suppliers.  
	Please check out the EtherCAT product section to find a suitable MainDevice code here:  
	[EtherCAT Product Guide](https://www.ethercat.org/en/products.html) > Development Systems, Tools > MainDevice Stacks
- **4.3 How about the license for EtherCAT SubDevice Controller chips?**
	When you purchase an EtherCAT SubDevice Controller (ESC) chip from one of the ESC suppliers, the EtherCAT license is embedded in the chip. For EtherCAT SubDevice vendors there is no additional EtherCAT license fee, since it is the duty of the ESC supplier to obtain this license.
- **4.4 How about the license for FPGAs?**
	When you purchase your FPGA from your preferred semiconductor distributor, the EtherCAT code is not already loaded. EtherCAT IP Core licences are available both for Altera (Intel), AMD, Microchip and Lattice FPGAs. There are licences available that entitle you to manufacture as many EtherCAT SubDevices as you want with just one licence payment. Alternatively, there are quantity based licences available, too.  
	The IP Cores provide freely configurable EtherCAT functionality, so that you can adapt the core-size to your requirements. You can also add application specific functions to the same FPGA, including soft-core processors. This further lowers the hardware costs for the EtherCAT SubDevice.
- **4.5 Do we have to submit our EtherCAT device to a Conformance Test Center?**
	No. Performing the conformance test at an official EtherCAT Test Center is optional - however, your customer may require a conformance certificate, which is only issued after passing the test at such a lab. You have to ensure conformance by applying the official Conformance Test Tool (CTT) at your R&D facilities, though. The CTT is licensed as a subscription in order to ensure the long term maintenance and further development of the tool with a yearly contribution.  
	More details about conformance can be found here: [Conformance & Interoperability](https://www.ethercat.org/en/conformance.html)
- ## 5\. EtherCAT Vendor ID
- **5.1 What is the EtherCAT Vendor ID?**
	The EtherCAT Vendor ID is a unique vendor identification number uniquely assigned by the EtherCAT Technology Group. Together with the product code it is contained in the Identity Object of the EtherCAT device.  
	An overview about the topic Vendor ID can be also found here:  
	[EtherCAT Vendor ID](https://www.ethercat.org/en/vendor_id.html)
- **5.2 Our sister/affiliated company has an EtherCAT Vendor ID. May we use this ID for our devices?**
	In case of an affilated company this can be granted upon request, please contact ETG Headquarters. However, we recommend that each vendor of an EtherCAT device uses its own Vendor ID.
- **5.3 We are using an interface board from a technology provider to add EtherCAT connectivity to our device. May we use the Vendor ID of that technology provider for our device, too?**
	No. The technology provider is supposed to ship his communication device with a secondary Vendor ID. You are supposed to replace it by your own unique Vendor ID, so that the device can be recognized in the network as yours.
- **5.4 What is a secondary Vendor ID?**
	This is a Vendor ID derived from the orginal Vendor ID that allows one to identify the original vendor of a communication interface device but which is invalid in the context of conformance testing.
- **5.5 We have a CANopen® Vendor ID. Can we use that for our EtherCAT device?**
	For your EtherCAT device you need an EtherCAT Vendor ID. However, in your EtherCAT Vendor ID application you may ask to get the same number; if it is still available ETG will assign it for your EtherCAT Vendor ID, too.  
	Please find a list of assigned and valid EtherCAT Vendor IDs here:  
	[EtherCAT Vendor ID List](https://www.ethercat.org/en/vendor_id_list.html)
- **5.6 How do we apply for our Vendor ID?**
	Simply go to the member section of the EtherCAT website:  
	[EtherCAT Vendor ID Assignment Form](http://www.ethercat.org/memberarea/vendorid/)
- ## 6\. Safety over EtherCAT
- **6.1 Do I need a redundant EtherCAT Interface within my Safety over EtherCAT device?**
	No. The Safety over EtherCAT protocol is implemented using a black channel approach; there is no safety related dependency to the standard communication interface. The communication interface such as controllers, ASICs, links, couplers, etc. remains unmodified.
- **6.2 Do I need redundant controller architecture for my Safety over EtherCAT device?**
	Using two microcontrollers is a common approach for implementing a safety device for SIL 3. But this is not demanded by the Safety over EtherCAT specification. A protocol implementation must fulfill following requirements:  
	\- complete fulfilment of IEC 61508 and IEC 61784-3  
	\- complete fulfilment of the FSoE protocol specification  
	\- complete fulfillment of the claimed Safety Integrity Level (SIL) and corresponding product specific requirements
- **6.3 Can I use Safety over EtherCAT via other communication systems than EtherCAT?**
	Yes. Since the beginning in 2005 Safety over EtherCAT was open and independent of the underlying bus system. The communication path is arbitrary; it can be EtherCAT, a fieldbus system, Ethernet or similar paths; fibre optics, copper wires or even wireless transmission. There are no restrictions or requirements on bus coupler or other devices in the communication path.
- **6.4 Is there a certified Safety over EtherCAT stack available?**
	Yes, within the ETG there are service providers available offering pre-certified FSoE protocol stacks and safety development services. The Safety over EtherCAT specification is quite lean and the protocol state machine is well defined. Experience therefore shows that an implementation can be done in short time – with or without using a pre-certified stack.
- **6.5 Is a Safety over EtherCAT Conformance Test available?**
	Yes. For Safety over EtherCAT devices a Safety over EtherCAT test case specification exists and is approved by TÜV SÜD Rail. For FSoE SubInstances those test cases are available for the EtherCAT Conformance Test Tool (CTT) so that an automated test can be performed. In general the automated test of a FSoE MainInstance stack is much more complex due to the flexible MainDevice configuration. Therefore the available test case specification can be used for the FSoE MainInstance approval.  
	The [ETG.9100 Safety over EtherCAT Policy](https://www.ethercat.org/en/downloads/downloads_1FD3308AA0404893936C8B0F6275719D.htm) includes the overall test procedure for a device approval.
- **6.6 Do I need an approval by a notified body (e.g. TUV, BGIA) for my Safety over EtherCAT device?**
	Yes. The development of a device using the Safety over EtherCAT technology shall be assessed. The device approval includes a passed EMC report, the Safety over EtherCAT conformance approval and the overall safety lifecycle process approval according to IEC 61508 or appropriate product standards. The assessment shall be done by a notified body.
- **6.7 Do I need to perform an official test at an FSoE Test Center for my device approval?**
	Yes, the FSoE Test Policy demands passing the test at an official FSoE Test Center. Precondition for the FSoE Conformance Test is a valid Certificate for the EtherCAT protocol implementation. All tests performed by the FSoE Test Center are available for preparation in-house.
- **6.8 Why do I need a licence to use the Safety over EtherCAT protocol within my device?**
	Safety over EtherCAT is a technology that is used by many device manufacturers. For such a technology compatibility is an important feature which ensures interoperability in the field. With the licence the device manufacturer gets the right to implement the technology – but he has to do this compatible to the specification. The licence is granted free of charge.  
	Machine builders and control system providers who use off-the-shelf FSoE devices do not need a licence.
- **6.9 How can I get and use the Safety over EtherCAT logo?**
	The Safety over EtherCAT logo can be obtained by the ETG Headquarters. The Safety over EtherCAT logo shall only be used in accordance with the ETG.9001 EtherCAT Marking Rules as published by the ETG.
- **6.10 I'm an EtherCAT MainDevice vendor. How can I support Safety over EtherCAT SubInstances?**
	If you just want to support off-the-shelf Safety over EtherCAT devices in the EtherCAT segment you do not need any safety-related implementation in the MainDevice. FSoE MainInstances with an EtherCAT SubDevice interface are available and can be used as safety logic devices.  
	Only SubDevice-to-SubDevice communication must be supported by the EtherCAT MainDevice to route the safety datagrams from the FSoE MainInstance to the FSoE SubInstances and vice versa.
- **6.11 I'm a machine builder. Do I need a license to use Safety over EtherCAT devices?**
	No. You can use off-the-shelf Safety-over-EtherCAT devices in the machine without a license.  
	You have to take care of the resulting Safety Integrity Level (SIL) or Performance Level (PL). Relevant standards (IEC 62061, ISO 13849) or product standards as well as compliance to other relevant standards, like national and international legal requirements (e.g. Directive of machinery, OSHA, UL etc.) must be fulfilled.

![](https://www.ethercat.org/images/teaser_right/ETG_FAQs_Right.jpg)  

## Technical FAQs

[For further technical FAQs please see EtherCAT Knowledge Base](https://www.ethercat.org/memberarea/en/knowledge_base.htm)
