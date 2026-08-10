---
source_id: "SRC-robotics-508"
title: "EtherCAT Implementation Guide"
source_type: "implementation_guide"
publisher: "EtherCAT Technology Group"
source_date: "2026-05-04"
url: "https://www.ethercat.org/download/documents/ETG2200_V3i2i3_G_R_EtherCATImplementationGuide.pdf"
evidence_grade: "S"
capture_method: "pdf-key-info-draft"
captured_at: "2026-08-09T10:36:40+00:00"
source_markdown: "SRC-robotics-508-ethercat-implementation-guide.md"
tags:
  - raw/source
  - raw/pdf
  - source-type/implementation-guide
  - evidence/s
aliases:
  - SRC-robotics-508
---
# EtherCAT Implementation Guide - Key Information Draft

> [!warning]
> This is an extraction draft for analyst review. Verify claims against the raw PDF/Markdown before using them in knowledge notes.

## Source Trace

- Source ID: `SRC-robotics-508`
- Raw Markdown: [SRC-robotics-508-ethercat-implementation-guide.md](SRC-robotics-508-ethercat-implementation-guide.md)
- Evidence grade: `S`

## Page-Level Leads

- [unpaginated] ## **EtherCAT Implementation Guide** ## **Document: ETG.2200 G D V3.2.3** **SECTION I – EtherCAT SubDevice introduction and implementation procedure SECTION II – ESC overview and EtherCAT development products SECTION III – EtherCAT P introduction and implementation** **SECTION IV – Safety over EtherCAT introduction and implementation** Created by: 
- [unpaginated] Other designations used in this publication may be trademarks whose use by third parties for their own purposes could violate the rights of the owners.

## Extracted Tables

### Table 1 (unpaginated)

|**Abbreviations**|**Description**|
|---|---|
|µC / MCU|A**m**icro**c**ontroller (MCU for microcontroller unit) is a small computer on a single integrated circuit. A<br>microcontroller contains one or more CPUs (processor cores) along with memory and programmable<br>input/output peripherals. Program memory in the form of ferroelectric RAM, NOR flash or OTP ROM is<br>also often included on chip, as well as a small amount of RAM. Microcontrollers are designed for<br>embedded applications, in contrast to the microprocessors used in personal computers or other<br>general purpose applications consisting of various discrete chips. (www.wikipedia.org)|
|ADS|The**A**utomation**D**evice**S**pecification describes a device- and fieldbus-independent interface. This<br>interface got designed by Beckhoff, and is – including the protocol – documented in detail. The ADS<br>components are installed together with TwinCAT 3. For integration into own applications and tools<br>there are ADS components (C/C++, .NET) available from Beckhoff. (Beckhoff Information System)|
|AL|The**A**pplication**L**ayer describes the highest layer of the EtherCAT SubDevice stack which includes<br>the EtherCAT State Machine, error handling, mailbox protocol handling, SubDevice application|
|AoE|**A**DS**o**ver**E**therCAT (AoE) is a standard, client-server mailbox application protocol defined by the<br>EtherCAT specification.|
|API|In computer programming, an**A**plication**P**rogramming**I**nterface is a set of subroutine definitions,<br>communication protocols, and tools for building software. In general terms, it is a set of clearly defined<br>methods of communication among various components. (www.wikipedia.org)|
|ASIC|An**A**pplication-**S**pecific**I**ntegrated**C**ircuit is an integrated circuit (IC) customized for a particular use,<br>rather than intended for general-purpose use. (www.wikipedia.org)|
|CAN|A**C**ontroller**A**rea**N**etwork (CAN bus) is a robust vehicle bus standard designed to allow<br>microcontrollers and devices to communicate with each other in applications without a host computer.<br>It is a message-based protocol, designed originally for multiplex electrical wiring within automobiles to<br>save on copper, but is also be used in many other contexts. (www.wikipedia.org)|
|CiA|**C**AN**i**n**A**utomation is the international users' and manufacturers' organization that develops and<br>supports CAN-based higher-layer protocols. (www.wikipedia.org)|
|CoE|With the**C**AN® application protocol**o**ver**E**therCAT protocol, EtherCAT provides the same<br>communication mechanisms as in CANopen®-Standard EN 50325-4: Object Dictionary, PDO Mapping<br>(Process Data Objects) and SDO (Service Data Objects) – even the network management is similar.<br>This makes it possible to implement EtherCAT with minimal effort in devices that were previously<br>outfitted with CANopen, and large portions of the CANopen Firmware are even reusable.<br>(www.ethercat.org)|
|CPU|A**C**entral**P**rocessing**U**nit, also called a central processor or main processor, is the electronic<br>circuitry within a computer that carries out the instructions of a computer program by performing the<br>basic arithmetic, logic, controlling, and input/output (I/O) operations specified by the instructions.<br>(www.wikipedia.org)|
|DC|Distributed Clocks|
|DLL|The**D**ata**L**ink**L**ayer is the second layer of the seven-layer OSI model of computer networking. This<br>layer is the protocol layer that transfers data between adjacent network nodes in a wide area network<br>(WAN) or between nodes on the same local area network (LAN) segment. The data link layer provides<br>the functional and procedural means to transfer data between network entities and might provide the<br>means to detect and possibly correct errors that may occur in the physical layer. (www.wikipedia.org)|
|DPRAM|Dual Ported Random Access Memory|
|DuT|A**D**evice**u**nder**T**est is a manufactured product undergoing testing, either at first manufacture or later<br>during its life cycle as part of ongoing functional testing and calibration checks. This can include a test<br>after repair to establish that the product is performing in accordance with the original product<br>specification.|
|EEPROM|An**E**lectrically**E**rasable**P**rogrammable**R**ead-Only**M**emory is a type of non-volatile memory used in<br>computers, integrated in microcontrollers for smart cards and remote keyless systems, and other<br>electronic devices to store relatively small amounts of data but allowing individual bytes to be erased<br>and reprogrammed. (www.wikipedia.de)|
|ENI|The**E**therCAT**N**etwork**I**nformation represents the standardized, XML-based description of an<br>EtherCAT network. It provides a manufacturer-independent way for configuration tools to generate and<br>provide the network configuration to MainDevices. (www.ethercat.org)|
|EoE|**E**thernet**o**ver**E**therCAT allows one to use a Standard Ethernet device like a printer, camera or PC<br>within an EtherCAT network. There is no restriction on the type of Ethernet device that can be<br>connected. The frames are tunneled by the EtherCAT MainDevice via the EtherCAT protocol. The<br>EtherCAT networks is fully transparent for the Ethernet device, and the real-time characteristics are<br>not impaired. (www.ethercat.org)|

### Table 2 (unpaginated)

|**Abbreviations**|**Description**|
|---|---|
|EPU|The**E**therCAT**P**rocessing**U**nit is the logical core of an EtherCAT SubDevice Controller. It contains<br>registers, memories and data processing elements. A frame always comes from port A before passing<br>through the EtherCAT Processing Unit. It receives, analyzes and processes the EtherCAT data<br>stream. (Beckhoff Infosys)|
|ESC|The**E**therCAT**S**ubDevice**C**ontroller processes the EtherCAT frames on the fly in hardware. It’s<br>implementation can be as an ASIC device, as IP Core for FPGAs, as system on a chip (SoC) or<br>integrated as native EtherCAT interface on an microcontroller or CPU. There is a long list of ESCs of<br>different types and vendors. (Knowledge Base)|
|ESI|The**E**therCAT**S**ubDevice**I**nformation file is a XML based file that comes with an EtherCAT<br>SubDevice and contains the complete description of its network accessible properties, such as<br>manufacturer and product information, Process Data, their mapping options, supported Mailbox<br>application protocols including optional features, as well as the supported modes of Synchronization.<br>(www.ethercat.org)|
|ESM|The state of the EtherCAT SubDevice is controlled via the**E**therCAT**S**tate**M**achine. Depending upon<br>the state, different functions are accessible or executable in the EtherCAT SubDevice. Specific<br>commands must be sent by the EtherCAT MainDevice to the device in each state, particularly during<br>the bootup of the SubDevice. A distinction is made between the following states: init, pre-operational,<br>safe-operational and operational, boot. The regular state of each EtherCAT SubDevice after bootup is<br>the operational state (Beckhoff Infosys/Anpassung: CH)|
|ETC|The official**E**therCAT**T**est**C**enter in Eurodpe, Asia and North America are accredited by the ETG<br>and perform the official EtherCAT Conformance Test. (ETG Brochure 11/2018)|
|ETG|The**E**therCAT**T**echnology**G**roup is a global organization in which OEM, End Users and Technology<br>Providers join forces to support and promote the further technology development. (www.ethercat.org)|
|EtherCAT|The**Ether**net for**C**ontrol**A**utomation**T**echnology is an Ethernet-based fieldbus system, invented by<br>Beckhoff Automation. The protocol is standardized in IEC 61158 and is suitable for both hard and soft<br>real-time computing requirements in automation technology. (www.wikipedia.org)|
|EtherCAT Device|Device using EtherCAT communication|
|FCS|A**F**rame**C**heck**S**equence refers to an error-detecting code added to a frame in a communications<br>protocol. (www.wikipedia.org)|
|FMMU|The**F**ieldbus**M**emory**M**anagement**U**nit belongs to the DLL and can be found in each I/O terminal.<br>FMMUs are used to map logical addresses bitwise or bytewise to physical addresses of the EtherCAT<br>**S**ubDevice Controller. (Beckhoff Infosys)|
|FoE|**F**ile**A**ccess over**E**therCAT is a mailbox application protocol generally intended to transfer file data on<br>an EtherCAT network in both directions, and as such it can be used in any state where the mailbox<br>communication is active (PREOP, SAFEOP, OP). (www.ethercat.org)|
|FPGA|A**F**eld-**P**rogrammable**G**ate**A**rray is an integrated circuit designed to be configured by a customer or<br>a designer after manufacturing. (www.wikipedia.org)|
|FSoE|EtherCAT utilizes the protocol Safety over EtherCAT (**F**ail**S**afe**o**ver**E**therCAT) to transfer safety-<br>critical control data through the same medium as the control data themselves. (www.ethercat.org)|
|FSoE Device|Device using EtherCAT communication with FSoE feature|
|GPIO|A**G**eneral-**P**urpose**I**nput/**O**utput is an uncommitted digital signal pin on an integrated circuit or<br>electronic circuit board whose behavior—including whether it acts as input or output—is controllable by<br>the user at run time. (www.wikipedia.org)|
|HAL|A**H**ardware**A**bstraction**L**ayer is an abstraction layer, implemented in software, between the physical<br>hardware of a computer and the software that runs on that computer. Its function is to hide differences<br>in hardware from most of the operating system kernel, so that most of the kernel-mode code does not<br>need to be changed to run on systems with different hardware. (www.wikipedia.org) r|
|I2C|**I**nter-**I**ntegrated**C**ircuit is a synchronous, multi-master, multi-slave, packet switched, single-ended,<br>serial computer bus invented in 1982 by Philips Semiconductor (now NXP Semiconductors). It is<br>widely used for attaching lower-speed peripheral ICs to processors and microcontrollers in short-<br>distance, intra-board communication. (www.wikipedia.org)|
|IEC|The**I**nterglobal**E**lectrotechnical**C**ommission is a Swiss association that acts as an interglobal<br>standards organization that prepares and publishes interglobal standards for all electrical, electronic<br>and related technologies – collectively known as "electrotechnology". (www.wikipedia.org)|
|ISO|The**I**nternational**O**rganization for**S**tandardization is an international standard-setting body composed<br>of representatives from various national standards organizations. (www.wikipedia.org)|
|LED|A**L**ight-**E**mitting**D**iode is a semiconductor light source that emits light when current flows through it.<br>(www.wikipedia.org)|

### Table 3 (unpaginated)

|**Abbreviations**|**Description**|
|---|---|
|LVDS|**L**ow-**V**oltage**D**ifferential**S**ignaling, also known as TIA/EIA-644, is a technical standard that specifies<br>electrical characteristics of a differential, serial communication protocol. LVDS operates at low power<br>and can run at very high speeds using inexpensive twisted-pair copper cables. LVDS is a physical<br>layer specification only; many data communication standards and applications use it and add a data<br>link layer as defined in the OSI model on top of it. (www.wikipedia.org)|
|MCI|Micro Controller Interface|
|MDP|The**M**odular**D**evice**P**rofile defines a modeling of structures within a device. Mainly the object<br>dictionary structure and corresponding behavior of the entries is defined by the MDP. The intention is<br>to provide an easy way for MainDevice and configuration tools to handle the devices. (Knowledge<br>Base)|
|MII|The**M**edia-**I**ndependent**I**nterface was originally defined as a standard interface to connect a Fast<br>Ethernet (i.e., 100 Mbit/s) media access control (MAC) block to a PHY chip. The MII is standardized by<br>IEEE 802.3u and connects different types of PHYs to MACs. Being media independent means that<br>different types of PHY devices for connecting to different media (i.e. twisted pair, fiber optic, etc.) can<br>be used without redesigning or replacing the MAC hardware. Thus any MAC may be used with any<br>PHY, independent of the network signal transmission media. (www.wikipedia.org)|
|NIC|A**N**etwork**I**nterface**c**ard (also known as a network interface controller, network adapter, LAN adapter<br>or physical network interface) is a computer hardware component that connects a computer to a<br>computer network. (www.wikipedia.org)|
|NW|NetWork|
|OEM|An**O**riginal**E**quipment**M**anufacturer is a company that produces parts and equipment that may be<br>marketed by another manufacturer. (www.wikipedia.org)|
|PD|Power Device|
|PDI|The**P**hysical**D**evice**I**nterface is an interface that allows access to the ESC from the process side.<br>(Beckhoff Infosys)|
|PDO|The**P**rocess**D**ata**O**bject protocol is used to process real time data among various nodes.<br>(www.wikipedia.de)|
|PELV|IEC 61140 defines a**P**rotective**E**xtra-**L**ow**V**oltage system as "an electrical system in which the<br>voltage cannot exceed ELV under normal conditions, and under single-fault conditions, except earth<br>faults in other circuits". (www.wikipedia.org)|
|PhL|**Ph**ysical**L**ayer|
|PIC|Programmable Integrated Circuit|
|PLC|A**P**rogrammable**L**ogic**C**ontroller or programmable controller is an industrial digital computer which<br>has been ruggedized and adapted for the control of manufacturing processes, such as assembly lines,<br>or robotic devices, or any activity that requires high reliability control and ease of programming and<br>process fault diagnosis. (www.wikipedia.org)|
|PSD|**P**ower**S**ourcing**D**evice, s. PSE|
|PSE|**P**ower**S**ourcing**E**quipment are devices that provide (source) power on the Ethernet cable. This<br>device may be a network switch, commonly called an endspan (IEEE 802.3af refers to it as endpoint),<br>or an intermediary device between a non-PoE-capable switch and a PoE device, an external PoE<br>injector, called a midspan device. (www.wikipedia.org)|
|RMII|**R**educed**M**edia-**I**ndependent**I**nterface is a standard which was developed to reduce the number of<br>signals required to connect a PHY to a MAC. Reducing pin count reduces cost and complexity for<br>network hardware especially in the context of microcontrollers with built-in MAC, FPGAs, multiport<br>switches or repeaters, and PC motherboard chipsets. Four things were changed compared to the MII<br>standard to achieve this. These changes mean that RMII uses about half the number of signals<br>compared to MII.<br>- The two clocks TXCLK and RXCLK are replaced by a single clock. This clock is an input to the PHY<br>rather than an output, which allows the clock signal to be shared among all PHYs in a multiport device,<br>such as a switch.<br>- The clock frequency is doubled from 25 MHz to 50 MHz, while the data paths are narrowed from 4<br>bits to 2 bits.<br>- RXDV and CRS signals are multiplexed into one signal.<br>- The COL signal is removed. (www.wikipedia.org)|
|SDO|**S**ervice**D**ata**O**bjects is a technology that allows heterogeneous data to be accessed in a uniform<br>way. The SDO specification was originally developed in 2004 as a joint collaboration between Oracle<br>(BEA) and IBM and approved by the Java Community Process in JSR 235. Version 2.0 of the<br>specification was introduced in November 2005 as a key part of the Service Component Architecture.<br>(www.wikipedia.org)|

### Table 4 (unpaginated)

|**Abbreviations**|**Description**|
|---|---|
|SELV|IEC defines a Separated (or**S**afety)**E**xtra-**L**ow**V**oltage system as "an electrical system in which the<br>voltage cannot exceed ELV under normal conditions, and under single-fault conditions, including earth<br>faults in other circuits". It is generally accepted that the acronym: SELV stands for separated extra-low<br>voltage (separated from earth) as defined in installation standards (e.g., BS 7671), though BS EN<br>60335 refers to it as safety extra-low voltage. (www.wikipedia.de)|
|SII|The**S**ubDevice**I**nformation**I**nterface represents the EEPROM wherein the ESC configuration data is<br>stored.|
|SIL|**S**afety**I**ntegrity**I**evel is defined as a relative level of risk-reduction provided by a safety function, or to<br>specify a target level of risk reduction. (www.wikipedia.de)|
|SM|The**S**ync**M**anager provides a mechanism in an ESC to protect DPRAM from simultaneous access by<br>the MainDevice and SubDevice application to guarantee data consistency.|
|SoE|**S**ervo drive profile**o**ver**E**therCAT according to IEC 61800 7 204|
|SPI|The**S**erial**P**eripheral**I**nterface is a synchronous serial communication interface specification used for<br>short-distance communication, primarily in embedded systems. The interface was developed by<br>Motorola in the mid-1980s and has become a de facto standard. (www.wikipedia.de)|
|SSC|The EtherCAT**S**ubDevice**S**tack**C**ode is an example source code in ANSI C supporting both the µC<br>and the SPI interface. The code serves as a development base for implementation of EtherCAT in<br>devices with own processor. (www.ethercat.org)|
|TC|**T**echnical**C**ommittee of the EtherCAT Technology Group|
|TCP/IP|The Internet protocol suite is the conceptual model and set of communications protocols used in the<br>Internet and similar computer networks. It is commonly known as TCP/IP because the foundational<br>protocols in the suite are the**T**ransmission**C**ontrol**P**rotocol (TCP) and the**I**nternet**P**rotocol (IP).<br>(www.wikipedia.org)|
|USB|**U**niversal**S**erial**B**us is an industry standard that establishes specifications for cables and connectors<br>and protocols for connection, communication and power supply between computers, peripheral<br>devices and other computers. (www.wikipedia.org)|
|XML|E**x**tensible**M**arkup**L**anguage is a markup language that defines a set of rules for encoding<br>documents in a format that is both human-readable and machine-readable. (www.wikipedia.org)|

### Table 5 (unpaginated)

|1|Introduction .................................................................................................................................... I-6|Introduction .................................................................................................................................... I-6|
|---|---|---|
||1.1|Documents for detailed Information and further reading ..................................................... I-6|
|2|EtherCAT system architecture ....................................................................................................... I-8||
||2.1|Configuration tool................................................................................................................. I-8|
||2.2|MainDevice .......................................................................................................................... I-8|
||2.3|SubDevice ........................................................................................................................... I-8|
|3|EtherCAT technology overview ................................................................................................... I-12||
||3.1|General .............................................................................................................................. I-12|
||3.2|Frame processing order .................................................................................................... I-12|
||3.3|SubDevice Information Interface (SII) ............................................................................... I-13|
||3.4|Fieldbus Memory Management Unit (FMMU) ................................................................... I-14|
||3.5|SyncManager (SM) ............................................................................................................ I-15|
||3.6|Distributed Clocks (DC) ..................................................................................................... I-16|
||3.7|Data structure and communication protocols .................................................................... I-16|
||3.8|EtherCAT State Machine ................................................................................................... I-17|
|4|EtherCAT SubDevices implementation aspects .......................................................................... I-20||
||4.1|General procedure – step by step ..................................................................................... I-20|
||4.2|General procedure – step by step ..................................................................................... I-20|
||4.3|Administrative organization ............................................................................................... I-21|
|||4.3.1<br>Development time ................................................................................................. I-21|
|||4.3.2<br>ETG membership and Vendor ID ......................................................................... I-21|
|||4.3.3<br>EtherCAT Conformance Test Tool license ........................................................... I-21|
||4.4|EtherCAT SubDevice design ............................................................................................. I-22|
|||4.4.1<br>Bus interface to EtherCAT network ...................................................................... I-22|
|||4.4.2<br>EtherCAT SubDevice Controller (ESC) and PDI .................................................. I-22|
|||4.4.3<br>SII .......................................................................................................................... I-24|
|||4.4.4<br>Application controller (host controller, µC)............................................................ I-24|
|||4.4.5<br>Application Layer communication protocols ......................................................... I-24|
|||4.4.6<br>Device profiles ...................................................................................................... I-27|
|||4.4.7<br>Synchronization among SubDevices and the MainDevice ................................... I-29|
|||4.4.8<br>Firmware update ................................................................................................... I-30|
||4.5|Tools for EtherCAT SubDevice development .................................................................... I-30|
|||4.5.1<br>XML editor for generating ESI files ....................................................................... I-31|
|||4.5.2<br>EtherCAT network configurator and MainDevice software ................................... I-32|
|||4.5.3<br>Monitoring communication and network diagnosis using Wireshark .................... I-33|
|||4.5.4<br>EtherCAT Conformance Test Tool ....................................................................... I-34|
||4.6|EtherCAT product labels and LEDs................................................................................... I-35|
|5|EtherCAT Conformance Testing .................................................................................................. I-37||
||5.1|EtherCAT Conformance Test Tool .................................................................................... I-37|
||5.2|Official EtherCAT Conformance Test at an EtherCAT Test Center (ETC)........................ I-37|
|6|EtherCAT Development Support ................................................................................................. I-38||
||6.1|EtherCAT training and workshop ....................................................................................... I-38|
||6.2|EtherCAT development support tips.................................................................................. I-39|
|7|EtherCAT Technology Group – events and support .................................................................... I-40||
||7.1|Basic information about the ETG ....................................................................................... I-40|
||7.2|EtherCAT Plug Fests ......................................................................................................... I-41|
||7.3|Official EtherCAT Conformance Test certificate ................................................................ I-41|

### Table 6 (unpaginated)

|7.4|ETG|Technical Committee ................................................................................................ I-42|
|---|---|---|
|7.5|Information and support ..................................................................................................... I-42||
||7.5.1|EtherCAT Compendium ........................................................................................ I-42|
||7.5.2|Download area on the web site ............................................................................ I-42|
||7.5.3|Knowledge Base ................................................................................................... I-43|
||7.5.4|Developers Forum ................................................................................................ I-43|
||7.5.5|Search the EtherCAT web site ............................................................................. I-43|
||7.5.6|Technical support ................................................................................................. I-44|

### Table 7 (unpaginated)

||**Subject**|**Documents, description and access**|
|---|---|---|
|**Introduction**|Brochures and<br>presentations|EtherCAT is introduced in several brochures, published in different languages:<br>→English |Japanese |Chinese | German |Korean| Italian | Spanish<br>This description of EtherCAT technology basics is an introduction in<br>→English |Japanese |Chinese | German |French|Italian |Portuguese<br>An introduction to Safety over EtherCAT is available in<br>→English |German|
||Articles|EtherCAT has been introduced in several articles. A selection of them is given here.<br>→Elektronik 23/03 (German)<br>→AUTlook 2-3/05 (German)|
||Videos (YouTube)|https://www.youtube.com/user/EtherCATGroup<br>→EtherCAT Technology Group<br>→EtherCAT in 20 Minutes<br>→EtherCAT Functional Principle<br>→Safety over EtherCAT<br>→EtherCAT Communication Profiles|
|**Detailed Reading**|EtherCAT Compendium|This is**the**EtherCAT read - from getting started to understanding the functionalities<br>themselves, their purpose, and the models behind. It describes the protocol as a<br>whole and puts it into context in a very comprehensive and easy-to-read style. Those<br>are the big add-ons compared to the very precise specification.<br>→http://www.ethercat.org/compendium1|
||Knowledge Base|An online information system containing FAQs and EtherCAT feature descriptions.<br>→www.ethercat.org/kb1|
||Technology description|Section I of the Beckhoff EtherCAT SubDevice Controller Datasheet ET1100 contains<br>a comprehensive description of EtherCAT functionality. Sections II (ESC register<br>description) and section III (hardware specification) provide more detailed information.<br>→beckhoff.com>Products>I/O>EtherCAT development products|

### Table 8 (unpaginated)

||**Subject**|**Documents, description and access**|
|---|---|---|
||Proceedings of ETG<br>events|Minutes of the Technical Committee meetings hold actual technology development<br>topics:<br>→www.ethercat.org>Downloads>Select Filter: Proceedings and Papers><br>Technical Committee Meeting|
|**Development**|EtherCAT<br>Communications|The communication slides provide a broad description of EtherCAT mechanisms for<br>developers.<br>→English1|Japanese1|
||PHY Selection Guide|The PHY Selection Guide contains information for physical level connection<br>components of several vendors that are available for EtherCAT communication.<br>→PHY Selection Guide (Beckhoff)|
||Individual topics of ITW|The ITW world series - a week of webinars has become a standing event in ETG's<br>event calendar. Webinar slides can be downloaded:<br>→www.ethercat.org/downloads → Test Filter = itw|
||Focus topics Technical<br>Committee meeting|The focus topic presented during the Technical Committee meetings provide answers<br>to many typical topics of interest. They are included in the meeting proceedings.<br>→www.ethercat.org/downloads → Test Filter = tc|
|**Specifications**|Communication<br>specification|EtherCAT is specified by the EtherCAT communication specificationETG.1000 parts<br>2 to 6.<br>→www.ethercat.org/etg10001<br>NoteETG.1000 represents the IEC 61158 - Type 12 (EtherCAT).|
||EtherCAT SubDevice<br>Information (ESI)|TheETG.2000 specification defines the EtherCAT SubDevice Information (ESI) for<br>the EtherCAT device description in XML format. Device description example files can<br>also be found here. The ETG.2001 ESI Annotation specification includes sample files<br>for ESI file development.<br>→www.ethercat.org/etg20001|
||Safety over EtherCAT|Safety over EtherCAT specifies a protocol layer for safe data exchange.ETG.5100<br>contains the safety protocol andETG.6100 specifies a safety drive profile.<br>→www.ethercat.org/etg51001<br>→www.ethercat.org/etg61001<br>NoteETG.5100 represents the IEC 61784 international standard.|
||Drives|The implementation directive for the CiA402 Drive Profile is specified in the ETG.6010<br>specification.<br>→www.ethercat.org/etg60101<br>NoteETG.6010 is based on the IEC 61800-7-201 (CiA402 drive profile).|
||Conformance|Conformance test rules are defined in the EtherCAT Conformance Test Policy<br>ETG.9000.The conformance guide describes how developers can obtain<br>conformance (ETG.7000). Additionally, a test record and the test request form are<br>available here.<br>→www.ethercat.org/etg70001|
||Firmware update|ETG.5003.0002 Firmware Update specification<br>This specification is mandatory only for devices supporting the profile number 5003<br>(Semi Device Profile), however, it is a good guideline for a firmware update<br>implementation on any EtherCAT SubDevice<br>→www.ethercat.org/etg5003|
||Trademark, logo and<br>labelling rules|Marking rules, trademark, logo and labelling usage for products and documentations<br>applying EtherCAT technology or referring to it are defined in theETG.1300 and the<br>ETG.9001 specifications:<br>→www.ethercat.org/etg13001<br>→www.ethercat.org/etg90011|

### Table 9 (unpaginated)

|**ESM state**|**Available functionalities**|
|---|---|
|Init (INIT)|Init state. No communication on the application layer is available.<br>The MainDevice has access only to the DL-information registers.|
|Pre-Operational (PREOP)|Pre-Operational state. Mailbox communication on the application layer available, but no<br>process data communication available.|
|Safe-Operational<br>(SAFEOP)|Safe-Operational state. Mailbox communication on the application layer, process (input) data<br>communication available. In Safe-Operational only inputs are evaluated; outputs are kept in<br>‘safe’ state.|
|Operational (OP)|Operational state. Process data inputs and outputs are valid.|
|Bootstrap (BOOT)|Bootstrap state. Optional but recommended if firmware updates necessary<br>No process data communication. Communication only via mailbox on Application Layer<br>available. Special mailbox configuration is possible, e.g., larger mailbox size.<br>In this state usually the FoE protocol is used for firmware download.|

### Table 10 (unpaginated)

|**Table 3: EtherCAT State Machine transitions for network initialization**<br>**1**|**Table 3: EtherCAT State Machine transitions for network initialization**<br>**1**|
|---|---|
|**Transition**|**MainDevice to SubDevice settings description**|
|Init to Pre-Operational|MainDevice reads VendorID, ProductCode and RevisionNumber from EEPROM, and<br>configures DL control registers (register 0x0100:0x0103)<br>SyncManager registers (registers 0x800+) for mailbox communication,<br>initialization for DC clock synchronization (if supported).<br>MainDevice requests Pre-Operational state by writing the AL Control register (register 0x120)<br>and waits for status confirmation via the AL Status register (register 0x130).|
|Pre-Operational to Safe-<br>Operational|MainDevice configures parameters using mailbox communication, i.e.:<br>Process data mapping if flexible,<br>registers for process data SyncManagers,<br>FMMU registers (0x600 and following).<br>MainDevice requests Safe-Operational state (AL Control register 0x0120 = 0x04) and waits<br>for confirmation via AL Status register.|
|Safe-Operational to<br>Operational|MainDevice sends valid outputs and requests Operational state (AL Control register<br>0x0120 = 0x08, confirmation in AL Status register)|
|Error to Init<br>Error to Pre-Operational<br>Error to Safe-Operational|Incorrect ESC register configuration (DC, FMMU, SM, etc.).<br>The AL Status Code register (register 0x134) indicates error reasons.|

### Table 11 (unpaginated)

||**Category**|**Simple device (no application controller,**<br>**dig. I/O)**|**Complex device (with application**<br>**controller)**|
|---|---|---|---|
|**Hardware**|Application<br>controller|--|microcontroller<br>Programmable Memory<br>(RUN/ERR LEDs)|
||ESC|ESC (ASIC/IP Core)<br>EEPROM||
||Port connection|MII:<br>Plug, Magnetics, PHY, R/C<br>Link/Activity LEDs||
||Device casing|Coverage design, or additional individual hardware etc.||
|**Software**|Host application|--|Local application/Firmware (FW)<br>EtherCAT communication|
||Device description|ESI file<br>EEPPROM configuration||
||Documentation|EtherCAT SubDevice documentation||

### Table 12 (unpaginated)

|||**Buffer Count**|**Length [Byte]**|**Total length [Byte]**|
|---|---|---|---|---|
|**SM0**|Output Mailbox|1|L_MbxOut|1*L_MbxOut|
|**SM1**|Input Mailbox|1|L_MbxIn|+<br>1*L_MbxIn|
|**SM2**|Outputs|3|L_Out (TxPDO)|+<br>3*L_Out|
|**SM3**|Inputs|3|L_In (RxPDO)|+<br>3*L_In|
|||||∑<br>DPRAM size|

### Table 13 (unpaginated)

|**FMMU**|**Assigned SyncManager**|**Name**|**Length [Byte]**|
|---|---|---|---|
|1|SM2|Outputs|L_Out (TxPDO)|
|2|SM3|Inputs|L_In (RxPDO)|
|3|SM0 & SM1|Mbx-SM Status flags|Mbx In/Out Length|

### Table 14 (unpaginated)

|**Object index range**|**Reserved for**|**Reserved for**|**Comment**|
|---|---|---|---|
|0x0000 – 0x0FFF|Data type area||Protected registers for ESC configuration|
|0x1000 – 0x1FFF|Communication area||Communication parameters, settings, etc.|
|0x2000 – 0x5FFF|Manufacturer-specific area|||
|0x6000 – 0x6FFF|Profile-Specific area|Input area|Process data input objects (mapped to TxPDOs)|
|0x7000 – 0x7FFF||Output area|Process data output objects (mapped to RxPDOs)|
|0x8000 – 0x8FFF||Configuration area|Process data configuration and settings objects|
|0x9000 – 0x9FFF||Information area|Scanned information from modules|
|0xA000 – 0xAFFF||Diagnosis area|Diagnostic, status, statistic or other information|
|0xB000 – 0xBFFF||Service Transfer<br>area|Service objects|
|0xC000 – 0xEFFF||Reserved area||
|0xF000 – 0xFFFF||Device area|Parameters belonging to the device|

### Table 15 (unpaginated)

||**Tool**|**Description and access**|
|---|---|---|
|**Network configuration**|EtherCAT configurator|Configurator for loading XML device descriptions (ESI) and for generating XML network<br>configuration descriptions (ENI).<br>Several EtherCAT MainDevices already include an EtherCAT configuration tool.<br>Visit the officialEtherCAT Product Section of the ETG website for the variety of<br>configuration tools.<br>Main Interest:<br>Development Systems, Tools<br>Subject:<br>Configuration Tools<br>For development purposes, an EtherCAT configuration tool with MainDevice (e.g.,<br>TwinCAT can be downloaded as free 7-day trail version from the beckhoff website)|
|**Development**<br>|XML editor|Used to edit or view EtherCAT SubDevice Information (ESI) files.<br>Any browser or text editor can be used, as well as the CTT.<br>Further tools:<br>Altova XML Spy (extensive xml editor, license fee required)<br>XML Notepad (freeware)|
||Hex file editor|Used to convert bitmap images (vendor or device logos) to a hex value which is needed<br>in the ESI. Any hex editor is fine, here are two examples:<br>HxD (freeware)<br>Mirkes TinyHexer (freeware)|
|**Diagnosis**|Network Monitor|Wireshark (former Ethereal) can be used to monitor frame communication of EtherCAT<br>networks. Wireshark is freeware and has already included a parser for comfortable<br>EtherCAT frame analysis.|

### Table 16 (unpaginated)

|**Tool**|||**Description and access**|
|---|---|---|---|
||||~~Available for Linux and Windows~~|
|EtherCAT|||The CTT is used to check EtherCAT protocol|
|Conformance Test Tool|||compliance in-house.|
|(CTT)|||The test tool is provided by Beckhoff Automation GmbH & Co. KG.|
||||Contactctt@beckhoff.com|
|Further Tools|||Also consult the officialEtherCAT Product Sectionof the ETG website for a continuative|
||||list of tools.|

### Table 17 (unpaginated)

|**RUN LED**|**EtherCAT state**|**ERR LED**|**EtherCAT state**|
|---|---|---|---|
|Off|Init|Off|No Error|
|Blinking|Pre-Operational|Blinking|Invalid configuration|
|Single Flash|Safe-Operational|Single Flash|Unsolicited state change|
|||Double Flash|Application watchdog timeout|
|Flashes|none (Initialisation) or Bootstrap|Flickering|Booting error|
|On|Operational|On|PDI watchdog timeout|

### Table 18 (unpaginated)

|**Label type**|**Requirements**|
|---|---|
|IN port label|Must be placed near the port. The label should be clearly<br>allocated to the subject port. The characters on the label<br>should be one of the following "IN" or "ECAT IN" (Capitals<br>and small characters both permitted).|
|OUT port label|Must be placed near the port. The label should be clearly<br>allocated to the subject port. The characters on the label<br>should be one of the following "OUT" or "ECAT Out"<br>(Capitals and small characters both permitted).|
|L/A LED label|Preferably the print characters should be placed directly next<br>to the network interface but is not compulsory. The mark can<br>be placed on other location or can be omitted. The print<br>characters, if not omitted, should show one of the following<br>phrases. " ", "Link/Act" or "Link/Activity" (Capitals and small<br>characters both permitted). Label is required on removable<br>connectors.|

### Table 19 (unpaginated)

|**Training/ Workshop**|**Description**|**Reference**|
|---|---|---|
|EtherCAT Technology<br>Basics|This is the training to get started with EtherCAT, developer of a<br>SubDevice, MainDevice, or configuration tool logic, but also as<br>advanced EtherCAT machine application developer or service<br>engineer.<br>During this training the EtherCAT protocol is explained in detail, starting<br>at a system point of view, and then explaining topology, Ethernet<br>hardware incl. PHYS, all functionality processed by an ESC (EtherCAT<br>SubDevice Controller) on the Data Link Layer and the Application<br>Layer protocol and services incl. the EtherCAT State Machine, mailbox<br>application protocols such as CoE, FoE, EoE and synchronization<br>modes based on Distributed Clocks (DC). Conformance testing, where<br>to find references and support and more is explained.<br>This training is about one day in total, either in-person or online as two<br>half days.|www.ethercat.org →<br>Events<br>(Beckhoff, TR8110)|
|FSoE Technology Basics|The Safety over EtherCAT Seminar gives you a comprehensive<br>overview about today's requirements for safety machine architectures<br>with the focus on safety communication with the Safety over EtherCAT<br>(FSoE; Fail-Safe over EtherCAT) protocol. The FSoE highlights and<br>technical features are shown and implementation aspects are provided.<br>Decision makers, product manager as well as R&D engineers from<br>ETG members who are involved in their companies safety product<br>strategy are invited to this seminar.<br>This training is about half a day.|www.ethercat.org →<br>Events|
|EtherCAT Configuration<br>and MainDevice Basics|Content:<br>•<br>Reference to ETG.1500 "EtherCAT Master Classes"<br>•<br>Requirements and interfaces to MainDevices and configuration<br>tools<br>•<br>Offline/online network configuration: ESI, ENI and SII<br>•<br>Topology detection and monitoring<br>•<br>Distributed Clocks: configuration and monitoring<br>•<br>Handling and monitoring of the EtherCAT State Machine (ESM)<br>•<br>Network initialization: Init Commands and CoE start-up<br>commands<br>•<br>Sending and receiving cyclic data: process image, logical<br>addressing<br>•<br>Process Data configuration: CoE objects, start-up commands,<br>ESI flags<br>•<br>Mailbox communication: protocols and monitoring mechanisms<br>•<br>Dependencies between Object Dictionary, ESI and SII<br>•<br>Diagnostic functionalities and their implementation<br>•<br>One day, as two half day sessions.|www.ethercat.org →<br>Events<br>(Beckhoff, TR8210)|
|Workshop: EtherCAT<br>Evaluation Kit and<br>SubDevice Stack Code<br>(SSC)|The online training is aimed at developers of EtherCAT SubDevices<br>using the EtherCAT SubDevice Evaluation Kit (EL98xx) and SubDevice<br>Stack Code (SSC) from Beckhoff Automation. In addition to theoretical<br>content, they also include practical exercises. Basic EtherCAT<br>knowledge is assumed. The workshop is led by developers and held in<br>manageable groups so that individual interests can be addressed.|www.ethercat.org →<br>Events<br>(Beckhoff, TR8100)|
|Workshop: EtherCAT<br>MainDevice Sample<br>Code|This training addresses developers and EtherCAT users alike. A deep<br>understanding of the EtherCAT configuration and network operation is<br>provided. Basic EtherCAT knowledge is assumed. The workshop is led<br>by developers and held in manageable groups so that individual<br>interests can be addressed.<br>Offered on request|(Beckhoff, TR8200)|

### Table 20 (unpaginated)

||CONTENTS|
|---|---|
|1|Introduction ................................................................................................................................... II-5|
|2|Product references........................................................................................................................ II-6|
|3|EtherCAT product guide ............................................................................................................... II-8|

### Table 21 (unpaginated)

|**Category**|**Description**|**references**|
|---|---|---|
|ESC|There is great variety of ESC vendors and types,<br>including ASICs, IP Cores, SoCs|ESC overview<br>EtherCAT Product Guide ><br>Development Systems, Tools ><br>EtherCAT SubDevice Controller (ESC)|
|Evaluation/ development kits|ESC vendors may offer development kits|EtherCAT Product Guide ><br>Development Systems, Tools ><br>SubDevice Evaluation Kits|
|Communication modules|Those solutions provide the EtherCAT<br>SubDevice interface including ESC, PHYs,<br>Magnetics, RJ45 jacks and maybe even<br>including an EtherCAT SubDevice stack with<br>dedicated programming interface for the<br>SubDevice application|EtherCAT Product Guide ><br>Development Systems, Tools ><br>Communication Modules|
|SubDevice stacks|EtherCAT SubDevices stack|EtherCAT Product Guide ><br>Development Systems, Tools ><br>SubDevice Stacks|

### Table 22 (unpaginated)

|||CONTENTS|
|---|---|---|
|1|EtherCAT P introduction .............................................................................................................. III-5||
|2|EtherCAT P technology ............................................................................................................... III-6||
||2.1|EtherCAT P connectors and cables .................................................................................. III-6|
||2.2|PHY selection .................................................................................................................... III-7|
||2.3|EtherCAT P use cases ...................................................................................................... III-8|
||2.4|EtherCAT P device structure ............................................................................................. III-8|
|||2.4.1<br>EtherCAT P in the ESI file .................................................................................. III-10|
|||2.4.2<br>EtherCAT P device types .................................................................................... III-11|
|||2.4.3<br>EtherCAT P device categories ........................................................................... III-11|
|3|EtherCAT P specification and documents ................................................................................. III-13||
|4|EtherCAT P conformance testing .............................................................................................. III-15||
||4.1|General ............................................................................................................................ III-15|
||4.2|Evaluate your current EtherCAT SubDevice for EtherCAT P ......................................... III-15|
||4.3|Contact for EtherCAT P conformance testing ................................................................. III-15|
|5|EtherCAT P licensing ................................................................................................................. III-16||
||5.1|General ............................................................................................................................ III-16|
||5.2|License agreement .......................................................................................................... III-16|
|6|EtherCAT P implementation aspects ......................................................................................... III-17||
||6.1|EtherCAT P and EtherCAT configuration tool ................................................................. III-17|
|7|EtherCAT P development support ............................................................................................. III-19||
||7.1|EtherCAT and EtherCAT P training ................................................................................. III-19|
||7.2|Technical support ............................................................................................................ III-19|

### Table 23 (unpaginated)

|**(typical) wire color**|**Yellow**|**Orange**|**White**|**Blue**|
|---|---|---|---|---|
|EtherCAT|TX+|TX-|RX+|RX-|
|Power|GNDS|US|GNDP|UP|

### Table 24 (unpaginated)

|**#**|**Type**|**Category**|**Description**|
|---|---|---|---|
|1|PD|device|“Standard” EtherCAT P device with an EtherCAT P IN port and at least one<br>EtherCAT P OUT port. Other OUT ports may also be EtherCAT.|
|2|PD|end device|Only an EtherCAT P IN port. Suits ideally for very small EtherCAT P devices (e.g.,<br>proximity sensors)|
|3|PD|decoupler|Decouples power and EtherCAT on the EtherCAT P IN port and has EtherCAT<br>OUT ports. This device has an ESC inside.|
|4|PSD|feed in|Builds the start of the EtherCAT P segment on the OUT port, while it combines the<br>EtherCAT signal from the IN port and US/UP(taken from external power supply)|
|5|PSD|renewing device|EtherCAT P device using external power supply to refresh USand UPon the OUT<br>ports. The power supplied on the EtherCAT P IN port is not used any more.|
|6|Passive|passive decoupler|A decoupler just without ESC (this is the only EtherCAT P device without ESC)|

### Table 25 (unpaginated)

||**Subject**|**Documents, Description and Access**|
|---|---|---|
|**Introduction**|EtherCAT Compendium|Section II: Technology Details, chapter 3 Data link layer (DLL) describes the basic<br>concept of EtherCAT P, and how it relates to 100BASE-TX<br>→http://www.ethercat.org/compendium|
||Articles|EtherCAT P has been introduced in several articles. A selection of them is given here.<br>→ PC Control (English):01/2016| (German):01/2016(stronger technical footprint)<br>→ PC Control (English):01/2016| (German):01/2016(system view)|
||Proceedings of ETG<br>events|Minutes of the Technical Committee Meetings give additional background information.<br>EtherCAT P was introduced on the spring meeting 2016. Meeting minutes from then<br>on are of specific EtherCAT P interest.<br>→www.ethercat.org → Downloads → Select Filter: Proceedings and Papers →<br>Technical Committee Meeting|
|**Specifications**|Communication slides|The communication slides provide a broad description of EtherCAT mechanisms for<br>developers. It also describes some basics on the physical layer, which, naturally,<br>include some EtherCAT P basics, too.<br>→English|
||Application note<br>TOP READING|While the EtherCAT specifications describe the EtherCAT P technology in a more<br>formal context, the application note aims to give very practical guidance on a doing-<br>level. It includes details for both, PSD and PD. This includes EtherCAT P schematic<br>details, electronic components, layout recommendations for grounding/ EMI/ EMC/<br>layout and examples.<br>→ Application Note: EtherCAT P Implementation Guide<br>www.ethercat.org/ethercatp|
|**Specifications**|EtherCAT P specification|The main EtherCAT P specification document. It describes:<br>Voltages, system architecture, device types, powered devices, power sourcing<br>devices, passive components, device categories, physical layer extension, cables,<br>connectors.<br>It refers to related specifications<br>→ETG.1030 www.ethercat.org/ethercatp|
||EtherCAT P connector|Specification of M8 P-coded connector. Any cable manufacturer can produce and sell<br>such a connector. The M8 P-coded connector has also been submitted for IEC<br>standardization.<br>→ETG.1030.1 www.ethercat.org/ethercatp|
||EtherCAT P physical layer<br>extension|EtherCAT P physical layer specifics.<br>→ETG.1000.2 P www.ethercat.org/ethercatp|
||EtherCAT SubDevice<br>Information (ESI)|Description of EtherCAT P-specific details in the ESI file, such as EtherCAT P device<br>type (PD, PSE), min/max voltages and load types. →ETG.2000 (EtherCAT P):<br>www.ethercat.org/ethercatp<br>The related schema file is also available for download<br>→ EtherCATInfo.xsd (and related xsd files): www.ethercat.org/ethercatp|

### Table 26 (unpaginated)

||**Subject**|**Documents, Description and Access**|
|---|---|---|
||ETG.9001 Marking Rules|As with EtherCAT and Safety over EtherCAT, for EtherCAT P logo and trademark are<br>defined. This and their usage are specified in ETG.9001.<br>→ETG.9001 (EtherCAT P): www.ethercat.org/ethercatp|

### Table 27 (unpaginated)

||CONTENTS|CONTENTS|
|---|---|---|
|1|Introduction ................................................................................................................................ IV-24||
|2|Safety over EtherCAT technology ............................................................................................. IV-25||
||2.1|Overview .......................................................................................................................... IV-25|
||2.2|Documents for detailed information and further reading ................................................. IV-26|
|3|Technology users....................................................................................................................... IV-28||
|||3.1.1<br>Machine builders ................................................................................................. IV-28|
|||3.1.2<br>Standard EtherCAT MainDevice manufacturer .................................................. IV-28|
|||3.1.3<br>FSoE device manufacturer ................................................................................. IV-29|
|4|Safety over EtherCAT implementation aspects ......................................................................... IV-30||
||4.1|FSoE device structure ..................................................................................................... IV-30|
||4.2|Hardware architecture ..................................................................................................... IV-30|
||4.3|Software architecture ....................................................................................................... IV-30|
||4.4|Safety manual .................................................................................................................. IV-31|
|5|Safety over EtherCAT Licensing ................................................................................................ IV-32||
||5.1|General ............................................................................................................................ IV-32|
||5.2|License Agreement .......................................................................................................... IV-32|
|6|Safety over EtherCAT conformance testing .............................................................................. IV-33||
||6.1|FSoE Test Cases............................................................................................................. IV-33|
||6.2|FSoE Conformance Test Tool for FSoE devices ............................................................ IV-33|
||6.3|FSoE Conformance Test ................................................................................................. IV-34|
|||6.3.1<br>FSoE SubInstance Conformance Test ............................................................... IV-34|
|||6.3.2<br>FSoE MainInstance Conformance Test .............................................................. IV-35|
|7|Safety over EtherCAT development support ............................................................................. IV-37||
||7.1|EtherCAT and Safety over EtherCAT training ................................................................. IV-37|
||7.2|Technical support ............................................................................................................ IV-37|
||7.3|Step by step implementation for an FSoE device manufacturer ..................................... IV-37|
|8|Frequently asked questions ....................................................................................................... IV-38||

### Table 28 (unpaginated)

|**Document**|**Description**|**Reference**|
|---|---|---|
|ETG.5100|**Safety over EtherCAT Specification**<br>FSoE protocol specification approved by TÜV.|Available per email<br>send request to ETG<br>(info@ethercat.org)|
|IEC 61784-3|**IEC specification of FSoE protocol**<br>IEC 61784-3: Industrial communication networks - Profiles – Part 3:<br>Functional safety fieldbuses,<br>defines general requirements for functional safety fieldbuses.<br>Functional Safety Communication Protocol FSCP 12/1 defines the<br>Safety over EtherCAT technology.<br>This part has the same content as ETG.5100.|www.iec.ch|
|ETG.5120|**Safety over EtherCAT Specification Enhancements**<br>This specification contains enhancements of the Safety over<br>EtherCAT protocol. These enhancements are part of the Safety over<br>EtherCAT specification and shall be considered for device<br>implementation.|www.ethercat.org/etg5120|
|FSoE license|**Safety over EtherCAT license**<br>Safety over EtherCAT is a registered trademark and patented<br>technology licensed by Beckhoff Automation GmbH & Co. KG.<br>Beckhoff has assured that it is willing to negotiate licenses under<br>reasonable and non-discriminatory terms and conditions with<br>applicants throughout the world.<br>**The license is available free of charge**. Beckhoff offers a license<br>agreement.|Send request to Beckhoff<br>(licensing@beckhoff.com)|
|**Safety over EtherCAT Conformance Test**|||
|ETG.9100|**Safety over EtherCAT Policy**<br>Rules and requirements for using and implementing Safety over<br>EtherCAT technology. The objective of this specification is to maintain<br>the integrity of both EtherCAT and Safety over EtherCAT (FSoE).<br>All requirements defined in theETG.9100 that are applicable for a<br>device shall be fully met.|www.ethercat.org/etg9100|
|ETG.7100 series|**Safety over EtherCAT Conformance Test Specification**<br>TheETG.7100series consists of following parts:|www.ethercat.org/etg7100|
|ETG.7100.1|**ETG.7100.1: General Requirements**<br>defines the FSoE test in which the conformance of the FSoE device<br>under test with the FSoE specification is tested|www.ethercat.org/etg7100|
|ETG.7100.2-2|**ETG.7100.2-2: SubInstance Test Record**<br>A set of test instructions for the performance of the FSoE<br>SubInstance Conformance Test and documentation of it at the same<br>time. The document includes an informative test execution guide.|www.ethercat.org/etg7100|
|ETG.7100.2-3|**ETG.7100.2-2: MainInstance Test Record**<br>A set of test instructions for the performance of the FSoE<br>MainInstance Conformance Test and documentation of it at the same<br>time. An informative execution guide is available in a separate<br>document.|www.ethercat.org/etg7100|
|ETG.7100.3|**ETG.7100.3: FSoE test cases specification**<br>Comprehensive test list for FSoE MainInstance and FSoE<br>SubInstances (Excel sheet)<br>Approved by TÜV|Comes with FSoE<br>Conformance Test Tool<br>(ET9402, ET9403)|
|ET9402|**Safety over EtherCAT SubInstance Conformance Test Tool**<br>•<br>Automatic test tool for FSoE SubInstance devices<br>•<br>Mandatory for approval of FSoE SubInstances.<br>(The tool is offered by Beckhoff. Test cases are defined in ETG TWG<br>Safety)|Send request to Beckhoff<br>(your local representative)|
|ET9403|**Safety over EtherCAT MainInstance Conformance Test Tool**<br>•<br>Automatic test tool for FSoE MainInstance devices<br>•<br>Mandatory for approval of FSoE MainInstances.<br>(The tool is offered by Beckhoff. Test cases are defined in ETG TWG<br>Safety)|Send request to Beckhoff<br>(your local representative)|

### Table 29 (unpaginated)

|**Document**|**Description**|**Reference**|
|---|---|---|
|**Safety over EtherCAT profile specifications**|||
|ETG.5001.4|**Modular Device Specification – Part 4: MDP Safety Module**<br>**Specification**<br>Standardized module profiles for FSoE digital I/O devices, FSoE<br>drives and FSoE MainInstance devices|www.ethercat.org/etg5001|
|ETG.6100|**Safety over EtherCAT Drive Profile**<br>Profile for adjustable speed electrical Power Drive Systems (PDS)<br>that are suitable for use in Safety-Related (SR) application with<br>Safety over EtherCAT protocol|www.ethercat.org/etg6100|
|**Safety over EtherCAT training**|||
|FSoE_Seminar.pdf|**Safety over EtherCAT seminar presentation**<br>•<br>Basic of safety networks and international standards<br>•<br>Safety over EtherCAT technology<br>•<br>Technical implementation aspects<br>•<br>Safety drive profile<br>•<br>Benefits for the user|http://www.ethercat.org/do<br>wnload/safety_seminar/def<br>ault.asp|
|**Important standard EtherCAT specifications**, further standards: www.ethercat.org →Downloads|||
|ETG.1000|**EtherCAT Specification**<br>EtherCAT Data link layer and application layer specification|www.ethercat.org/etg1000|
|ETG.2000|**EtherCAT SubDevice Information (ESI) Schema and**<br>**Specification**<br>Describes the structure of the EtherCAT SubDevice description in<br>XML format. FSoE related Parts are included.|www.ethercat.org/etg2000|
|ETG.2100|**EtherCAT Network Information (ENI) Schema and Specification**<br>Describes the structure of the EtherCAT network information<br>description in XML format. Parts for Copy Information (SubDevice-to-<br>SubDevice communication) are included|www.ethercat.org/etg2100|
|ETG.2200|**EtherCAT Implementation Guide (this document)**<br>Describes from a very practical point of view which topics have to be<br>kept in mind for a successful EtherCAT implementation|www.ethercat.org/etg2200|

### Table 30 (unpaginated)

||**FSoE MainInstance**|**FSoE SubInstance**|
|---|---|---|
|**EtherCAT MainDevice**|FSoE CTT for FSoE MainInstances<br>using an EtherCAT bridge device|ETG.7100.3<br>SubDevice tests incorporated in<br>vendors’ test environment|
|**EtherCAT SubDevice**|FSoE CTT for FSoE MainInstances|FSoE CTT for FSoE SubInstances|
|**Non-EtherCAT device**|ETG.7100.3<br>MainInstance tests incorporated in<br>vendors’ test environment|ETG.7100.3<br>SubDevice tests incorporated in<br>vendors’ test environment|

### Table 31 (unpaginated)

|**No**|**SafeInput***<br>**[Byte]**|**SafeOutput***<br>**[Byte]**|**Safe Application**<br>**Parameter [Byte]**|**Rationale**|
|---|---|---|---|---|
|**1**|2|1|0|Code coverage|
|**2**|2|4|0|Code coverage|
|**3**|1<br>(minimum)|1<br>(minimum)|0|Minimum length Safe-In/Out|
|**4**|252<br>(maximum<br>supported)|252<br>(maximum<br>supported)|0|Maximum length Safe-In/Out|
|**5**|2|4|9<br>(not word aligned)|Check content of FSoE connection parameter<br>set|
|**6**|1|1|256<br>(maximum supported)|Maximum length of FSoE connection<br>parameter set|
|**7**|1|1|SRA CRC<br>SRA Parameter|Check SRA CRC calculation of FSoE<br>MainInstance configuration tool|

### Table 32 (unpaginated)

||DOCUMENT HISTORY|
|---|---|
|**Version**|**Comment**|
|1.0.0|Official release|
|1.1.0|Document revised<br>Editorial changes<br>ESC variants updated<br>More implementation products added<br>New documentation links|
|1.1.1|Editorial changes|
|1.1.2|Use of marking rules (ETG.9001)and indicator specification(ETG.1300) added|
|1.1.3|Editorial changes|
|1.1.4|Editorial changes|
|1.1.5|Editorial changes<br>ETG.9003Conformance Test Policy added<br>ETG.9002Vendor ID Policy added<br>Minor changes in step by step implementation|
|1.1.6|Editorial changes|
|2.0.0|Document revised<br>New document structure<br>Enhanced general procedure - step by step<br>Major content enhancements|
|2.0.1|Editorial changes<br>Policies added<br>Download links updated/fixed<br>Minor content enhancements|
|2.0.3|Editorial changes|
|2.1.0|Contact email address isconformance@ethercat.org|
|2.1.1|Development products updated|
|2.1.2|Development products (Renesas, TESSERA) updated|
|2.1.4|Correction of trade mark term acc. ToETG.9001|
|2.1.5|Editorial changes|
|2.1.6|Added reference toETG.5003.2|
|2.1.7|Editorial Changes, updates of hyperlinks and ESC overview<br>Add and update chapters on Knowledge Base/Search/Download, support|
|3.0.0|Add EtherCAT P section|
|3.0.1|Development products (Profichip) updated|
|3.0.2|Add description on CTT license|
|3.0.3|Update of EtherCAT P specifications status (available as release)|
|3.0.4|Update of contact graphics<br>Update of colors of some graphics|
|3.1.0|Add “Evaluate your current EtherCAT SubDevice for EtherCAT P”<br>Add products<br>Update abbreviations, links, references, layout|
|3.1.1|Update links, references<br>Major content enhancements<br>Add Section IV Safety over EtherCAT introduction and implementation<br>Add section information in footer|
|3.2.0|Update EtherCAT terms to consider inclusive language<br>New Abbreviations table<br>Update section IV Safety over EtherCAT introduction and implementation and add FSoE MainInstance<br>Conformance Test|
|3.2.1|Update file and document name<br>Formatting, formatting of pdf navigation pane|
|3.2.2|Updates ETC-J address|
|3.2.3|Update Section II – replace products overview with links to product guide and ESC overview to reflect<br>dynamics in new ESCs and development kits.<br>Updated EtherCAT P testing equipment figure|


## Analyst Checklist

- Facts: extract numeric claims, dates, policy names, technical claims, and company disclosures.
- Estimates: mark market-size forecasts, CAGR, shipment forecasts, and assumptions.
- Judgments: separate source judgments from your own investment/career analysis.
- Traceability: cite page numbers or table numbers before moving claims into `knowledge/` notes.
