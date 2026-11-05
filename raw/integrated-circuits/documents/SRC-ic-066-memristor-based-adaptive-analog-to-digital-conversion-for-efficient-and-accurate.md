---
source_id: "SRC-ic-066"
title: "Memristor-based adaptive analog-to-digital conversion for efficient and accurate compute-in-memory"
source_type: "research_paper"
publisher: "Nature Communications"
source_date: "2025-11-06"
url: "https://www.nature.com/articles/s41467-025-65233-w"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-09-22T02:35:06+00:00"
tags:
  - raw/source
  - source-type/research-paper
  - evidence/s
aliases:
  - SRC-ic-066
---
# Memristor-based adaptive analog-to-digital conversion for efficient and accurate compute-in-memory

## Abstract

Compute-in-memory technology offers promising solutions for neural network acceleration but its potential is severely limited by inflexible and resource-intensive analog-to-digital converters. Here, we present a memristor-based analog-to-digital converter featuring adaptive quantization for diverse output distributions. Our design employs analog content-addressable memory cells with programmable overlapped boundaries to establish optimized quantization thresholds, demonstrating excellent integral and differential non-linearities. Extensive experiments validate the robustness of our approach by achieving 89.55% accuracy on CIFAR-10 (VGG8) at 5-bit adaptive quantized precision and maintaining competitive performance on ImageNet (ResNet18) through a proposed super-resolution strategy under experimental memristor variations. Compared to state-of-the-art designs, our converter achieves a 15.1× improvement in energy efficiency and a 12.9× reduction in area. Furthermore, integrating our converter into CIM systems reduces the energy and area overhead by up to 57.2% and 30.7%, respectively. This work establishes a paradigm for efficient and accurate signal quantization in practical compute-in-memory systems.

## Introduction

As artificial intelligence (AI) advances rapidly, the increasing complexity of deep neural networks exposes critical limitations in traditional von Neumann architectures [^1] [^2]. These architectures, with their separate computation and memory units [^3], suffer from massive data movement overheads in modern neural network operations [^4] [^5], resulting in high energy consumption and latency [^6] [^7] [^8]. Compute-in-memory (CIM) with emerging memory devices, particularly memristors, offers a promising solution by integrating computation directly within memory crossbar arrays [^9] [^10] [^11] [^12] [^13] [^14] [^15] [^16] [^17] [^18] [^19] (Fig. [1a](https://www.nature.com/articles/s41467-025-65233-w#Fig1)). This integration overcomes the von Neumann bottleneck and enables efficient vector-matrix multiplications (VMMs) for deep learning operations [^15] [^20] [^21] [^22] [^23]. A typical mixed-signal CIM system (Fig. [1b](https://www.nature.com/articles/s41467-025-65233-w#Fig1)) consists of digital-to-analog converters (DACs), analog crossbar arrays, analog-to-digital converters (ADCs), and digital activation circuit implementing linear operations, quantization, and nonlinear activation functions in neural network layers, respectively.

![Fig. 1: Challenges in CIM systems for neural network computation.](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-025-65233-w/MediaObjects/41467_2025_65233_Fig1_HTML.png?as=webp)

Fig. 1: Challenges in CIM systems for neural network computation.

Despite these advantages, analog-to-digital signal conversion emerges as a critical bottleneck in CIM systems [^10] [^24] [^25] [^26] [^27]. Current ADCs, as fundamental components for signal conversion, consume excessive energy and circuit area, fundamentally constraining the scalability of CIM systems as neural network complexity grows. For example, in a state-of-the-art implementation [^28], ADCs occupy up to 87.8% of total energy and 75.2% of chip area (Fig. [1c](https://www.nature.com/articles/s41467-025-65233-w#Fig1)). Moreover, existing quantization methods struggle to handle diverse output distributions in CIM architectures [^29] [^30] in an energy-efficient manner. In CIM implementations, different neural network layers and even channels are mapped to separate crossbar arrays, each carrying distinct weight patterns. This mapping, combined with varying input patterns during inference, leads to significantly different output distributions across arrays (Fig. [1a](https://www.nature.com/articles/s41467-025-65233-w#Fig1)), demanding quantization schemes that are both adaptive and efficient. Current solutions present a clear trade-off: at low ADC precision (≤6 bits), uniform quantization generally offers hardware-friendly implementation with low energy and area overhead but suffers from significant precision loss [^2], while adaptive approaches based on cumulative distribution function [^31] and Lloyd-Max algorithm [^32] [^33] [^34] achieve higher accuracy through dynamic boundary adjustment but lack practical hardware implementations. At higher ADC precision, uniform quantization provides sufficient accuracy, making adaptive quantization less advantageous. However, the significant energy and area overhead of high-precision ADCs substantially diminishes the efficiency benefits of CIM systems, making low-bit implementations crucial for maintaining CIM’s advantages in hardware efficiency.

To address these fundamental challenges, we introduce a memristor-based ADC that leverages the intrinsic programmability of memristors to enable adaptive quantization directly in hardware. It uses analog content-addressable memory (CAM) cells to implement this approach in CIM systems, significantly reducing quantization errors compared to uniform approaches. By establishing quantization thresholds with overlapped CAM boundaries, our design demonstrates excellent quantization performance with integral non-linearity (INL) and differential non-linearity (DNL) of 0.319 and 0.419 least significant bit (LSB) for a 5-bit configuration. In neural network applications, our ADC exhibits robust performance across different architectures under practical memristor variations. The 5-bit ADC achieves 89.55% accuracy on CIFAR-10 using VGG8. For more complex networks like ResNet18 on ImageNet, our super-resolution strategy effectively mitigates hardware variations, achieving near-ideal accuracies of 34.76% (4-bit), 61.81% (5-bit), and 65.50% (6-bit), respectively. Moreover, the ADC exhibits high hardware efficiency, delivering a 15.1× lower energy consumption while reducing the chip area by 12.9× compared to state-of-the-art solutions. Furthermore, compared to memristor ramp-based ADC implementation [^35], our one-step conversion ADC achieves 48.5× lower latency and 26.6× lower energy consumption while maintaining comparable area efficiency. When integrated into CIM systems and compared to conventional successive approximation register (SAR) ADC, our design significantly reduces ADC overhead, decreasing energy and area contribution by 57.2% and 30.7% respectively for VGG8, and by 56.9% and 25.1% for ResNet18.

## Results

### Design of the memristor-based ADC

Our ADC design leverages analog CAM [^36] [^37] [^38] as the core to create a programmable voltage quantizer, termed a quantization cell (Q-cell) (Fig. [2a](https://www.nature.com/articles/s41467-025-65233-w#Fig2)). The Q-cell consists of two memristors (M <sub>1</sub>, M <sub>2</sub>), five transistors (T <sub>1</sub> to T <sub>5</sub>), and two inverters (INV <sub>1</sub>, INV <sub>2</sub>). V <sub>H</sub> and V <sub>L</sub> are applied across voltage dividers formed by M <sub>1</sub> -T <sub>1</sub> and M <sub>2</sub> -T <sub>3</sub> pairs, while restricted to avoid mis-programming the device conductance. By tuning the memristor conductance, quantization boundaries can be defined through these dividers. Specifically, the M <sub>1</sub> -T <sub>1</sub> divider controls the lower boundary via discharge transistor T <sub>2</sub>, while the M <sub>2</sub> -T <sub>3</sub> divider, coupled with INV <sub>1</sub>, determines the upper boundary through discharge transistor T <sub>4</sub>. This dual-boundary configuration enables voltage quantization based on programmed thresholds, as verified through circuit simulations using the UMC 180 nm technology library. The voltage responses at nodes A and B were obtained with a sampling time of 2 μs, with V <sub>H</sub> and V <sub>L</sub> set to 0.8 V and 0.3 V, respectively, across the M <sub>1</sub> -T <sub>1</sub> and M <sub>2</sub> -T <sub>3</sub> pairs. The input voltage was swept from 0.75 V to 1.30 V to characterize the Q-cell’s response at nodes A and B (Fig. [2b](https://www.nature.com/articles/s41467-025-65233-w#Fig2)). A PMOS transistor (T <sub>5</sub>) initializes the circuit by charging the match line. The match line voltage, after passing through INV <sub>2</sub>, generates a binary output: ‘0’ when the input voltage falls within the programmed boundaries, and ‘1’ otherwise.

![Fig. 2: Memristor-based ADC design.](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-025-65233-w/MediaObjects/41467_2025_65233_Fig2_HTML.png?as=webp)

Fig. 2: Memristor-based ADC design.

To illustrate the fundamental operation of our ADC architecture, we first present its implementation with uniform quantization, which allows us to validate the basic functionality and reliability of our design through well-established ADC metrics. This uniform configuration serves as a foundation for understanding the device’s capabilities before exploring its adaptive quantization features.

The ADC precision determines the required number of Q-cells, with an n-bit ADC requiring 2 <sup>n-1</sup> Q-cells to cover the input range (see Supplementary Note [1](https://www.nature.com/articles/s41467-025-65233-w#MOESM1) for details). Figure [2c, d](https://www.nature.com/articles/s41467-025-65233-w#Fig2) shows a 3-bit ADC implementation using four Q-cells, where seven quantization boundaries divide the normalized input range into eight uniformly distributed segments. Each Q-cell employs a progressive boundary distribution pattern based on LSB, with unique lower and upper boundary pairs. To maximize conductance range utilization, we implement a dual-bias strategy: the left input (T <sub>1</sub>) receives a bias voltage matching the minimum input range of the ADC, while the right input receives a smaller bias (half of the input range). This approach ensures balanced conductance utilization across both sides, enabling the same conductance range to define both lower and upper quantization boundaries. In our 3-bit implementation, the Q-cells are programmed with voltage ranges of (0, 0.5), (0.125, 0.625), (0.25, 0.75), and (0.375, 0.875). This overlapping configuration generates unique digital codes through distinct Q-cell activation patterns. For example, an input of 0.8 V activates only the last Q-cell (falling within 0.75–0.875), producing an output code of ‘1110’, which is then decoded to the final binary output ‘110’ (see Supplementary Note [2](https://www.nature.com/articles/s41467-025-65233-w#MOESM1) and Supplementary Table [1](https://www.nature.com/articles/s41467-025-65233-w#MOESM1) for details).

Although the illustrative example shows uniform quantization, the quantization boundary in our design is reconfigurable to achieve adaptive quantization. The key advantage of our design lies in its hardware efficiency and adaptability, where memristor programmability enables dynamic boundary reconfiguration to accommodate varying system requirements [^39].

### Experimental benchmarking of uniform quantization ADC

The experimental characterization of our memristor-based ADC architecture necessitates a rigorous evaluation framework that encompasses both conventional ADC performance metrics and adaptive quantization capabilities. Given that the fundamental operation of our design relies on precise analog-to-digital conversion, we first evaluated its baseline performance using metrics such as INL and DNL under uniform quantization conditions. These metrics provide quantitative validation of the device’s intrinsic conversion accuracy and linearity, which underpin both conventional and adaptive quantization functionalities.

To experimentally demonstrate our ADC design, we fabricated and characterized an 8×8 memristor array comprising 64 devices (Fig. [3a](https://www.nature.com/articles/s41467-025-65233-w#Fig3)). The devices exhibit stable, multi-level conductance states controlled by programming compliance current (Fig. [3b](https://www.nature.com/articles/s41467-025-65233-w#Fig3)), which is fundamental for establishing quantization boundaries. Statistical analysis of the array revealed device-to-device variation with a standard deviation of 2.73 µS for programmed states in the range of 100–400 µS, corresponding to <1% relative variation (Fig. [3c](https://www.nature.com/articles/s41467-025-65233-w#Fig3)). Excellent read stability was demonstrated with only 0.14 µS (0.047%) conductance variation over 1000 consecutive cycles (Fig. [3d](https://www.nature.com/articles/s41467-025-65233-w#Fig3)). These experimental characterizations (including Supplementary Figs. [1](https://www.nature.com/articles/s41467-025-65233-w#MOESM1) – [3](https://www.nature.com/articles/s41467-025-65233-w#MOESM1)) validate the variation parameters to be used in our following simulation evaluations. Furthermore, endurance testing confirmed robust switching over 3 × 10 <sup>7</sup> cycles within the required conductance window (Supplementary Fig. [4](https://www.nature.com/articles/s41467-025-65233-w#MOESM1)). For ADC applications where write operations are infrequent, this endurance projects to a device lifetime of ~87 years under a conservative estimate of 1000 daily updates, ensuring excellent long-term reliability.

![Fig. 3: Experimental characterization of the fabricated memristor device and array.](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-025-65233-w/MediaObjects/41467_2025_65233_Fig3_HTML.png?as=webp)

Fig. 3: Experimental characterization of the fabricated memristor device and array.

Further analysis of device variability under programming conditions [^40] extended our static characterization to encompass both INL and DNL [^41] across the full operating range (see Methods for details). INL quantifies deviation from ideal linear response, while DNL measures uniformity between successive codes. In CIM systems, INL affects feature map computations, where high values lead to reduced inference accuracy, while DNL determines precision in distinguishing activation levels. The impact of these variations is amplified in CIM architectures, as ADC quantization across array lines can cascade through network layers, causing significant accuracy loss in deep learning tasks.

For our 4-bit ADC implementation, maximum INL and DNL were limited to 0.215 LSB and 0.322 LSB, respectively (Fig. [4a, b](https://www.nature.com/articles/s41467-025-65233-w#Fig4)), validating design robustness under experimental variation. Scalability analysis across 2-6 bit resolutions (Fig. [4c, d](https://www.nature.com/articles/s41467-025-65233-w#Fig4)) using root mean square (RMS) analysis of maximum INL and DNL revealed consistent performance (see Methods for details). As detailed in Supplementary Table [2](https://www.nature.com/articles/s41467-025-65233-w#MOESM1), all bit precisions maintained sub-1-LSB linearity metrics under experimental variation. Specifically, at 5-bit precision, our architecture achieved RMS values of 0.319 LSB and 0.419 LSB for maximum INL and DNL, respectively. Beyond device conductance variations, the ADC also demonstrates strong resilience to dynamic power supply noise and offers an in-situ recalibration mechanism to counteract static DC drifts, as detailed in Supplementary Note [3](https://www.nature.com/articles/s41467-025-65233-w#MOESM1) and Supplementary Fig. [5](https://www.nature.com/articles/s41467-025-65233-w#MOESM1). These measurements, conducted under uniform quantization, establish the fundamental precision and stability of our ADC architecture, providing critical attributes that enable subsequent implementation of adaptive quantization schemes across diverse CIM applications.

![Fig. 4: Simulated performance metrics of the memristor-based ADC.](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-025-65233-w/MediaObjects/41467_2025_65233_Fig4_HTML.png?as=webp)

Fig. 4: Simulated performance metrics of the memristor-based ADC.

### Adaptive quantization ADC for efficient neural networks

Although our ADC design has demonstrated competitive benchmark performance, its full potential has yet to be exploited. What makes it special is that the quantization boundaries can be programmed arbitrarily using the memristors in the Q-cell, opening up the possibility for adaptive quantization in neural networks and achieving non-degraded performance even with low-bit quantization. Our adaptive quantization implementation integrates hardware-based boundary adjustment with software optimization. This process encompasses both offline analysis and dynamic operation during inference. Initially, we collect output statistics from each convolution layer by running inference on a representative training dataset, capturing the distinct characteristics of various network layers. Utilizing these statistics, we apply a modified Lloyd-Max algorithm [^32] to determine optimal quantization boundaries (Supplementary Fig. [6](https://www.nature.com/articles/s41467-025-65233-w#MOESM1)), iteratively adjusting them to minimize mean squared error (MSE) while adhering to hardware constraints. Subsequently, we program these optimized boundaries into the memristor devices through precise conductance modulation, employing either compliance current control or programming pulses with program-and-verify calibration. This approach accounts for the non-linear relationship between conductance and voltage thresholds in our Q-cell design. During inference, each Q-cell operates with these optimized boundaries, enabling adaptive quantization that closely aligns with the actual distribution of CIM array outputs.

This software-hardware co-optimization methodology ensures the effective realization of adaptive quantization’s theoretical benefits in physical implementation. The hardware component exploits memristors’ programmable conductance states for dynamic quantization boundary setting, while the software optimization process fine-tunes these boundaries based on actual data distributions and hardware constraints, resulting in a highly efficient and adaptable CIM system.

To validate our approach, we evaluated our strategy using the VGG8 network [^42] on the CIFAR-10 dataset [^43]. The experimental results demonstrated the effectiveness of our adaptive quantization method. Specifically, the reconfigurable ADC achieved improved boundary alignment with data distribution compared to uniform quantization (Fig. [5a](https://www.nature.com/articles/s41467-025-65233-w#Fig5)), reducing MSE from 14.99 to 3.10 (Fig. [5b](https://www.nature.com/articles/s41467-025-65233-w#Fig5)).

![Fig. 5: Simulation analysis of adaptive quantization and network performance with our ADC.](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-025-65233-w/MediaObjects/41467_2025_65233_Fig5_HTML.png?as=webp)

Fig. 5: Simulation analysis of adaptive quantization and network performance with our ADC.

Across different ADC precisions (Fig. [5c](https://www.nature.com/articles/s41467-025-65233-w#Fig5)), our adaptive approach achieved 68.1%, 88.9%, and 90.2% accuracy at 3-bit, 4-bit, and 5-bit, respectively, significantly outperforming uniform quantization (13.0%, 52.3%, 89.9%). Under experimental variations (Fig. [5d](https://www.nature.com/articles/s41467-025-65233-w#Fig5)), the network maintained robust performance with 66.30%, 88.39%, and 89.55% accuracy at respective bit levels.

For the more complex ResNet18 network [^44] on ImageNet [^45], we conducted a comprehensive evaluation across different quantization scenarios. First, we established baseline performance using ideal adaptive quantization, achieving 30.7%, 61.4%, and 67.5% accuracy at 4-bit, 5-bit, and 6-bit precisions, respectively. These results exhibit the theoretical benefits of adaptive quantization at different bit precisions (Fig. [5e](https://www.nature.com/articles/s41467-025-65233-w#Fig5)). However, when implementing the ADC with real memristor devices under experimental variations (1% conductance variation), the accuracies dropped to 24.1%, 51.3%, and 59.0%. This accuracy degradation (average 6.6% drop) reveals the impact of device variations on quantization precision.

To address this challenge, we developed a super-resolution strategy that leverages the inherent variation between paired ADCs. When two ADCs with nominally identical boundaries produce different outputs due to device variations, it suggests that the input lies within the boundary region affected by these variations. We identify such boundary-proximate states, assign appropriate boundary values, and thereby utilize device variations for super-resolution (see Methods for implementation details). This approach effectively improved accuracies to 34.8%, 61.8%, and 65.5% for 4-bit, 5-bit, and 6-bit configurations respectively (Fig. [5f](https://www.nature.com/articles/s41467-025-65233-w#Fig5)). Notably, these results not only recover the accuracy loss from device variations but, in some cases (e.g., 4-bit: +4.06% improvement), also surpass the theoretical adaptive quantization baseline. This improvement shows how our super-resolution strategy transforms device variations from a limitation into an advantage, thereby enhancing quantization precision.

The above results also reveal that the performance advantage of our adaptive quantization scales with network complexity. For simpler networks like VGG8, benefits are most pronounced at very low bitwidths (+55.1% at 3-bit), while the accuracy gap narrows at 5-bit as uniform quantization becomes adequate. Conversely, complex networks like ResNet18 on ImageNet generate more diverse output distributions, extending the value of adaptivity to higher bitwidths. Rather than exhibiting diminishing returns, our approach delivers a substantial +17.3% absolute accuracy improvement at 6-bit (65.5% with SR vs. 48.2% for uniform), demonstrating effectiveness well beyond the “ultra-low bit” regime.

### Hardware efficiency evaluation of memristor-based ADC

To evaluate the hardware benefits of our approach, we conducted a comprehensive analysis comparing our ADC design with state-of-the-art SAR, Flash, and other ADCs from a public survey [^46] of designs presented at the ISSCC and VLSI symposia between 1997 and 2024. Given the emerging nature of low-bit ADCs at advanced technology nodes, direct comparisons at 16 nm node with 5–6 bit precision are challenging due to the limited number of published works in this specific domain. To provide a comprehensive evaluation of our design’s capabilities, we extended our comparison across different technology nodes and precision levels, enabling a broader assessment of the advantages offered by our memristor-based approach.

As illustrated in Fig. [6a](https://www.nature.com/articles/s41467-025-65233-w#Fig6), our memristor-based ADC demonstrates significant improvements in both energy efficiency and area utilization at 5-bit ADC precision across this comprehensive comparison space. A detailed breakdown of both energy consumption and area utilization (Fig. [6b](https://www.nature.com/articles/s41467-025-65233-w#Fig6)) reveals the relative contributions of the ADC core components and the decoder, demonstrating the efficient resource allocation in our design. The design achieves an energy efficiency of 12.58 fJ per conversion (see Methods for details), representing a 15.1× improvement over conventional designs [^47]. In terms of area, our ADC occupies only 24.29 μm², which is 12.9× smaller than the most compact conventional ADCs [^48]. We also designed a full custom layout of the proposed ADC design (Supplementary Fig. [7](https://www.nature.com/articles/s41467-025-65233-w#MOESM1)). Besides, we conducted a comprehensive analysis comparing our ADC with a detailed comparison against CIM-specific designs provided in Supplementary Table [3](https://www.nature.com/articles/s41467-025-65233-w#MOESM1).

![Fig. 6: Estimated energy and area comparison of memristor-based ADC.](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-025-65233-w/MediaObjects/41467_2025_65233_Fig6_HTML.png?as=webp)

Fig. 6: Estimated energy and area comparison of memristor-based ADC.

Compared to existing memristor ramp-based ADC implementations [^35], our one-step conversion mechanism demonstrates advantages in both speed and energy efficiency (Supplementary Table [4](https://www.nature.com/articles/s41467-025-65233-w#MOESM1)). Ramp-based ADCs achieve complete parallelism by allocating a dedicated comparator to each column, enabling simultaneous quantization of all column outputs. This architecture is exceptionally well-suited for CIM systems that require high readout bandwidth. Consequently, these systems become optimal for data-intensive and high-throughput applications where the simultaneous processing of large information volumes is critical. In scenarios requiring lower latency, the architecture may be less optimal due to its operational principle, which requires sequential comparisons as the ramp signal progresses through each quantization. The prolonged comparator activation during this comparison period leads to elevated energy dissipation. For example, this principle results in a reported latency of 32 ns and energy consumption of 42.82 pJ at 5-bit precision. In contrast, our design achieves quantization in a single step, with all thresholds evaluated simultaneously. Our implementation demonstrates a latency of 0.66 ns and energy consumption of 1.61 pJ per VMM computation in a configuration of 32 ADCs per macro, while maintaining area efficiency (777.28 μm²). These improvements represent a 48.5× reduction in conversion latency and a 26.6× reduction in energy consumption.

While our single-stage adaptive memristor-based ADC excels in latency and energy for low-to-mid bitwidths, its flash-like architecture faces a scalability challenge for achieving very high resolutions due to the exponential growth of Q-cells. For such applications, a promising direction is to employ a multi-stage pipeline architecture, where our ADC can serve as an efficient sub-converter in each stage. This approach resolves the scalability issue by ensuring hardware cost grows linearly, rather than exponentially, with the target resolution. A conceptual illustration and detailed explanation of this scalable pipeline architecture are provided in the Supplementary Fig. [8](https://www.nature.com/articles/s41467-025-65233-w#MOESM1).

The benefits of our design extend beyond component-level comparisons to system-level improvements. Integration into CIM systems exhibits a significant reduction in analog-to-digital conversion overhead. Compared to energy- and area-efficient SAR ADC [^49] in CIM systems, our design achieves substantial improvements: for VGG8 implementations, as illustrated in Fig. [7](https://www.nature.com/articles/s41467-025-65233-w#Fig7), the energy contribution of ADC components decreases from 79.8% to 22.5% of total system energy (a 57.2% reduction), while the area overhead drops from 47.6% to 16.9% of total chip area (a 30.7% reduction). Similar improvements are observed in ResNet18 implementations, where ADC energy overhead is reduced from 71.5% to 14.6% (a 56.9% reduction), and area contribution decreases from 36.6% to 11.5% (a 25.1% reduction), as illustrated in Supplementary Fig. [9](https://www.nature.com/articles/s41467-025-65233-w#MOESM1) and Supplementary Tables [5](https://www.nature.com/articles/s41467-025-65233-w#MOESM1), [6](https://www.nature.com/articles/s41467-025-65233-w#MOESM1).

![Fig. 7: Simulated system-level energy and area analysis of VGG8 implementation.](https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs41467-025-65233-w/MediaObjects/41467_2025_65233_Fig7_HTML.png?as=webp)

Fig. 7: Simulated system-level energy and area analysis of VGG8 implementation.

These comprehensive improvements across different metrics and comparison scenarios show the advantages of our architecture, enabling substantially higher system operating frequencies and better energy efficiency for CIM applications. The dramatic reductions in both energy and area overhead effectively address the conversion bottleneck in CIM systems, highlighting the transformative potential of our memristor-based ADC for efficient and accurate neural network inference acceleration.

## Discussion

This work presents a memristor-based ADC architecture for neural network acceleration. Our ADC employs analog content-addressable memory cells with overlapped boundaries to establish optimized quantization thresholds, implements a super-resolution strategy to maintain competitive accuracy under practical memristor variations, and achieves a 15.1× improvement in energy efficiency and a 12.9× reduction in area compared to state-of-the-art designs. When integrated into CIM systems, it dramatically reduces ADC overhead, with energy and area reductions of 57.2% and 30.7% for VGG8, and 56.9% and 25.1% for ResNet18, respectively.

It is important to note that our ADC architecture is designed as a modular component within a larger CIM system. While this work focuses on optimizing the quantization stage, our ADC can operate synergistically with advanced techniques that address circuit-level non-idealities, such as signal margin limitations [^50] and IR drop [^51], as well as crossbar device-to-device variations [^17] [^52] [^53]. A detailed discussion on the orthogonality and complementary nature of our approach with state-of-the-art compensation schemes is provided in Supplementary Note [4](https://www.nature.com/articles/s41467-025-65233-w#MOESM1).

Building on these design principles, our ADC supports adaptive quantization while maintaining robust performance, making it particularly suitable for edge computing applications. Beyond immediate applications in inference acceleration, this design opens further possibilities for adaptive hardware-algorithm co-design in next-generation AI systems, bridging the gap between algorithmic requirements and hardware constraints.

## Methods

### Device characterization

The memristor devices were fabricated on a silicon wafer with a 300 nm thick SiO <sub>2</sub> layer. The device structure consists of a Pt/TaO <sub>x</sub> /Ta stack, where TaO <sub>x</sub> serves as the resistive switching layer with a thickness of ~5 nm. The devices are fabricated using equipment available in the clean room at The University of Hong Kong. All patterns are created through a standard lift-off process following photolithography. The bottom electrode (BE) and top electrode (TE) are composed of Cr/Pt metals deposited via an e-beam evaporator. The TaO <sub>x</sub> switching layer is formed in an ion-beam etcher operating in an oxygen-reactive sputter mode from a Ta target.

The electrical characterization of the memristor device is conducted at room temperature using a semiconductor parameter analyzer (Keysight B1500A) with the chip mounted on a probe station. To precisely control the device’s conductance, we employed a customized program-and-verify scheme based on quasi-static DC sweeps. For program cycle-to-cycle variation measurement (Supplementary Fig. [1](https://www.nature.com/articles/s41467-025-65233-w#MOESM1)), this scheme incrementally increases the compliance current based on the difference between the measured and target conductance. The step size is determined by multiplying this difference (in µS) by an empirical scaling factor, which is set to 0.5 for the initial 10 iterations and reduced to 0.25 thereafter to enhance convergence. The process terminates after a maximum of 20 iterations. If the measured conductance overshoots the target tolerance (±5 µS), a reset sweep (starting from −1.2 V) is applied before restarting the programming process.

To gather programming statistics, target conductance values ranging from 100 µS to 400 µS were selected in 50 µS steps, with each target programmed 100 times after a reset. This procedure showed high reliability, with 91.6% of attempts converging to the target within 10 iterations and an average of 5.57 iterations required per successful programming event. For read cycle-to-cycle variation characterization (Fig. [3d](https://www.nature.com/articles/s41467-025-65233-w#Fig3)), the device conductance was first set to the target values using the same program-and-verify method. Once a state was successfully programmed, its conductance was read 1000 consecutive times to assess its stability. All single-device measurements were performed on the same device to ensure consistency.

To evaluate device uniformity and statistical properties critical for practical ADC applications, we extended the analysis from a single device to an integrated 8 × 8 memristor crossbar array (64 devices) fabricated using the same process. The microscopy image in Fig. [3a](https://www.nature.com/articles/s41467-025-65233-w#Fig3) shows the array test structure. All 64 devices were characterized using the identical program-and-verify scheme to assess statistical variations in programmed conductance states. Furthermore, the array was used to demonstrate analog conductance switching capabilities. The detailed results of the array-level characterization, including representative multi-device *I* - *V* curves and pattern mapping demonstrations, are provided in the Supplementary Figs. [2](https://www.nature.com/articles/s41467-025-65233-w#MOESM1), [3](https://www.nature.com/articles/s41467-025-65233-w#MOESM1).

### Adaptive ADC design

The reconfigurable ADC design was implemented using Spice and Cadence Virtuoso tools. The quantization cell with memristor devices was modeled and simulated. The performance metrics of the memristor-based ADC were evaluated based on the simulation results, including INL, DNL, RMS of maximum INL, and RMS of maximum DNL.

The INL, which represents the maximum deviation of the actual conversion characteristic from the ideal straight line, was calculated using:

$${{{\\rm{IN}}}}{{{{\\rm{L}}}}}\_{k}=\\frac{V\\left(k\\right)-{V}\_{{{{\\rm{best}}}}-{{{\\rm{fit}}}}}\\left(k\\right)}{{{{\\rm{LSB}}}}}$$

(1)

where \\(V(k)\\) is the actual voltage corresponding to output code \\(k\\), \\({V}\_{{{{\\rm{best}}}}-{{{\\rm{fit}}}}}(k)\\) is the voltage on the best-fit line. The best-fit line is determined through linear regression:

$${V}\_{{{{\\rm{best}}}}-{{{\\rm{fit}}}}}\\left(k\\right)={ak}+b$$

(2)

where \\(a\\) and \\(b\\) are coefficients calculated using the least squares method.

The DNL, which measures the difference between the actual and ideal code step widths, was determined using:

$${{{\\rm{DN}}}}{{{{\\rm{L}}}}}\_{k}=\\frac{V\\left(k+1\\right)-V\\left(k\\right)}{{{{\\rm{LSB}}}}}-1$$

(3)

To assess the overall nonlinearity errors, we calculated the RMS INL and RMS DNL:

$${{{\\rm{IN}}}}{{{{\\rm{L}}}}}\_{{{{\\rm{RMS}}}}}=\\sqrt{\\frac{1}{N}{\\sum }\_{k=0}^{N-1}{{{\\rm{IN}}}}{{{{\\rm{L}}}}}\_{k}^{2}}$$

(4)

$${{{\\rm{DN}}}}{{{{\\rm{L}}}}}\_{{{{\\rm{RMS}}}}}=\\sqrt{\\frac{1}{N-1}{\\sum }\_{k=0}^{N-2}{{{\\rm{DN}}}}{{{{\\rm{L}}}}}\_{k}^{2}}$$

(5)

where \\(N\\) is the total number of ADC codes.

The design was optimized by precisely controlling the programming compliance current or pulse to adjust memristor conductance. To measure INL and DNL, a range of input voltages was applied, and the ADC’s output was compared to the ideal linear response. The impact of device variation was analyzed by introducing controlled conductance variations in the memristors and observing the resulting changes in INL and DNL.

### Neural network evaluation

We evaluated our ADC strategy using two neural network architectures: VGG8 for CIFAR-10 classification and ResNet18 for ImageNet classification. The networks were implemented using a modified NeuroSim framework [^49], which we enhanced with detailed ADC behavioral models to accurately capture the impact of quantization and device variations. Our simulation framework incorporates precise modeling of ADC characteristics, providing realistic performance estimates for practical CIM implementations. The networks were implemented with different ADC configurations and quantization strategies.

### Super resolution strategy

To address device variations in practical implementations, we developed the super-resolution strategy, which utilizes two ADCs with nominally identical quantization boundaries. Under memristor variations, these boundaries exhibit slight misalignments. When an input voltage falls near a quantization boundary, the two ADCs may produce different quantization results. We leverage this disagreement to identify and precisely quantize these boundary-proximate values. Specifically, when the two ADCs produce different outputs for the same input, we assign the input to the corresponding boundary value, effectively achieving super-resolution at quantization boundaries. This approach not only improves quantization accuracy but also takes advantage of inherent device variations to enhance precision.

### Implementation details for 5-bit ADC design

Our design consists of the ADC core and a decoder circuit, with their respective contributions to energy and area detailed in Fig. [6b](https://www.nature.com/articles/s41467-025-65233-w#Fig6). The estimations are based on our previous analog CAM in 16 nm technology [^36]. To calculate the energy consumption, we began with the baseline analog CAM design, which consumes 0.47 fJ per operation (excluding its DAC portion). To enhance the linearity of our ADC, we expanded the memristor conductance range to 100–400 μS. This primarily affected the source driver within each Q-cell, increasing its energy consumption from 0.29 fJ to 0.58 fJ. Consequently, the total energy for the ADC core is estimated at 12.58 fJ per operation.

For the area estimation, a single Q-cell occupies an area of ~0.72 μm × 0.72 μm, or 0.52 μm <sup>2</sup>, as shown in the 16-nm physical layout [^36]. Therefore, the 5-bit ADC core, comprising 16 Q-cells, has an area of 8.29 μm <sup>2</sup>. The decoder circuit, synthesized using a 28 nm technology library, adds an area of 16.00 μm <sup>2</sup>, resulting in a total estimated ADC area of 24.29 μm <sup>2</sup>. This area estimation for ADC-specific components excludes memristor write drivers since they are treated as shared system-level resources. To further validate this estimation methodology, we designed a full custom layout of a comparable 5-bit ADC in a UMC 28 nm process, which supports our scaled estimations (see Supplementary Fig. [7](https://www.nature.com/articles/s41467-025-65233-w#MOESM1) for details).

The total conversion latency is estimated as 0.165 ns, which combines the core’s 45 ps latency from the CAM reference and the decoder’s 0.12 ns latency from synthesis. This total latency serves as the basis for our system-level timing analysis. While our estimation uses a mixed-technology approach, it represents a conservative projection. A full 16 nm implementation would likely yield further improvements in energy and area. By extrapolating these validated figures, we calculated the total energy and area metrics for various ADC configurations.

### CIM system evaluation

To comprehensively evaluate the system-level benefits of our proposed memristor-based ADC design, we conducted a detailed performance analysis using a modified NeuroSim framework [^49]. The CIM architecture was implemented with memristor crossbar arrays, each configured as a 128 × 128 matrix. To optimize the balance between performance and hardware overhead, we adopted a resource-sharing strategy where every four columns share one ADC, resulting in 32 ADCs per array. All ADCs were configured with 5-bit precision (32 quantization levels) to maintain consistent comparison across different network architectures.

The complete system architecture incorporates several key components, including the core crossbar array, ADC, adder, and other peripheral circuits. The adder units include adder trees and shift register pairs for accumulating partial products. Other circuits comprise essential peripheral components such as word line decoders and their corresponding drivers, multiplexer circuits with associated decoders, and word line switch matrices. The entire system, including the conventional SAR ADC model, was evaluated under a 14 nm technology node to ensure fair comparison with state-of-the-art implementations. The detailed energy consumption and area utilization of each component were analyzed for both VGG8 and ResNet18 implementations, as presented in Fig. [7](https://www.nature.com/articles/s41467-025-65233-w#Fig7) and Supplementary Fig. [9](https://www.nature.com/articles/s41467-025-65233-w#MOESM1), respectively. The comprehensive breakdown of system-level metrics is provided in Supplementary Tables [5](https://www.nature.com/articles/s41467-025-65233-w#MOESM1), [6](https://www.nature.com/articles/s41467-025-65233-w#MOESM1), demonstrating the significant reduction in ADC overhead achieved by our design across different network architectures.

### Robustness to voltage variations and in-situ recalibration

To assess the robustness of our ADC in practical chip environments, we conducted comprehensive simulation-based analysis of its resilience to reference voltage variations. Our evaluation systematically investigated the impact of both high-frequency dynamic power supply noise and quasi-static DC voltage drift on ADC linearity (INL/DNL). The results show that the ADC is highly resilient to dynamic noise, as demonstrated by the 5-bit ADC which maintains INL well below 0.5 LSB even under 20 mV peak-to-peak noise.

While the analysis indicates higher sensitivity to static DC drift, this highlights a core strength of our architecture. Unlike conventional designs that require dedicated compensation circuits, our ADC can directly counteract such drifts through in-situ recalibration. Since memristor conductances define the quantization boundaries, any quasi-static voltage drift can be completely nullified by reprogramming the memristors to new conductance values corresponding to the desired thresholds under the drifted condition. This ability to directly reconfigure quantization boundaries eliminates the need for additional hardware, thus demonstrating significant advantages in efficiency and design simplicity (detailed methodology and results in Supplementary Note [3](https://www.nature.com/articles/s41467-025-65233-w#MOESM1) and Supplementary Fig. [5](https://www.nature.com/articles/s41467-025-65233-w#MOESM1)).

## Data availability

The data that support the findings of this study are available in the public repository at [https://github.com/MIKEHHQ/ReADC](https://github.com/MIKEHHQ/ReADC) [^54] or from the corresponding authors upon request. [Source data](https://www.nature.com/articles/s41467-025-65233-w#Sec17) are provided with this paper.

## Code availability

The codes used for the simulations in this study are available in the public repository at [https://github.com/MIKEHHQ/ReADC](https://github.com/MIKEHHQ/ReADC) [^54] or from the corresponding authors upon request.

## References

## Acknowledgements

This work was supported in part by the Theme-based Research Scheme (TRS) project T45-701/22-R (N.W., C.L. & W.Z.), the National Natural Science Foundation of China (62404187 (Z.L.), 62122005 (C.L.)), Croucher Foundation (C.L.), and the General Research Fund (GRF) Project (17200925 (Z.L.), 17203224 (N.W.), 17207925 (C.L.)) of the Research Grants Council (RGC), Hong Kong SAR.

## Ethics declarations

### Competing interests

The authors declare no competing interests.

## Peer review

### Peer review information

*Nature Communications* thanks Mario Lanza, Yiyu Shi, Abhairaj Singh and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. A peer review file is available.

## Additional information

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Supplementary information

## Rights and permissions

**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/).

[^1]: Li, C. et al. Analogue signal and image processing with large memristor crossbars. *Nat. Electron* **1**, 52–59 (2018).

[Article](https://doi.org/10.1038%2Fs41928-017-0002-z) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2018btnd.book.....L) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Analogue%20signal%20and%20image%20processing%20with%20large%20memristor%20crossbars&journal=Nat.%20Electron&doi=10.1038%2Fs41928-017-0002-z&volume=1&pages=52-59&publication_year=2018&author=Li%2CC)

[^2]: Aguirre, F. et al. Hardware implementation of memristor-based artificial neural networks. *Nat. Commun.* **15**, 1974 (2024).

[Article](https://doi.org/10.1038%2Fs41467-024-45670-9) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2024NatCo..15.1974A) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BB2cXlsVKlt7w%3D) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=38438350) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC10912231) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Hardware%20implementation%20of%20memristor-based%20artificial%20neural%20networks&journal=Nat.%20Commun.&doi=10.1038%2Fs41467-024-45670-9&volume=15&publication_year=2024&author=Aguirre%2CF)

[^3]: Von Neumann, J. First draft of a report on the EDVAC. *IEEE Ann. Hist. Comput.* **15**, 27–75 (1993).

[Article](https://doi.org/10.1109%2F85.238389) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=1241101) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=First%20draft%20of%20a%20report%20on%20the%20EDVAC&journal=IEEE%20Ann.%20Hist.%20Comput.&doi=10.1109%2F85.238389&volume=15&pages=27-75&publication_year=1993&author=Neumann%2CJ)

[^4]: LeCun, Y., Bengio, Y. & Hinton, G. Deep learning. *Nature* **521**, 436–444 (2015).

[Article](https://doi.org/10.1038%2Fnature14539) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2015Natur.521..436L) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC2MXht1WlurzP) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=26017442) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Deep%20learning&journal=Nature&doi=10.1038%2Fnature14539&volume=521&pages=436-444&publication_year=2015&author=LeCun%2CY&author=Bengio%2CY&author=Hinton%2CG)

[^5]: Bassey, J., Qian, L. & Li, X. A survey of complex-valued neural networks. Preprint at [http://arxiv.org/abs/2101.12249](http://arxiv.org/abs/2101.12249) (2021).

[^6]: Chen, Y.-H., Emer, J. & Sze, V. Eyeriss: a spatial architecture for energy-efficient dataflow for convolutional neural networks. In *2016 ACM/IEEE 43rd Annual International Symposium on Computer Architecture (ISCA)* 367–379. [https://doi.org/10.1109/ISCA.2016.40](https://doi.org/10.1109/ISCA.2016.40) (2016).

[^7]: Chen, Y.-H., Yang, T.-J., Emer, J. & Sze, V. Eyeriss v2: a flexible accelerator for emerging deep neural networks on mobile devices. *IEEE J. Emerg. Sel. Top. Circuits Syst.* **9**, 292–308 (2019).

[Article](https://doi.org/10.1109%2FJETCAS.2019.2910232) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2019IJEST...9..292C) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Eyeriss%20v2%3A%20a%20flexible%20accelerator%20for%20emerging%20deep%20neural%20networks%20on%20mobile%20devices&journal=IEEE%20J.%20Emerg.%20Sel.%20Top.%20Circuits%20Syst.&doi=10.1109%2FJETCAS.2019.2910232&volume=9&pages=292-308&publication_year=2019&author=Chen%2CY-H&author=Yang%2CT-J&author=Emer%2CJ&author=Sze%2CV)

[^8]: Ganguly, A., Muralidhar, R. & Singh, V. Towards energy efficient non-von neumann architectures for deep learning. In *20th International Symposium on Quality Electronic Design (ISQED)* 335–342, [https://doi.org/10.1109/ISQED.2019.8697354](https://doi.org/10.1109/ISQED.2019.8697354) (2019).

[^9]: Prezioso, M. et al. Training and operation of an integrated neuromorphic network based on metal-oxide memristors. *Nature* **521**, 61–64 (2015).

[Article](https://doi.org/10.1038%2Fnature14441) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2015Natur.521...61P) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC2MXnvFWjtb4%3D) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=25951284) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Training%20and%20operation%20of%20an%20integrated%20neuromorphic%20network%20based%20on%20metal-oxide%20memristors&journal=Nature&doi=10.1038%2Fnature14441&volume=521&pages=61-64&publication_year=2015&author=Prezioso%2CM)

[^10]: Shafiee, A. et al. ISAAC: a convolutional neural network accelerator with in-situ analog arithmetic in crossbars. In *2016 ACM/IEEE 43rd Annual International Symposium on Computer Architecture (ISCA)* 14–26 [https://doi.org/10.1109/ISCA.2016.12](https://doi.org/10.1109/ISCA.2016.12) (2016).

[^11]: Ielmini, D. & Wong, H.-S. P. In-memory computing with resistive switching devices. *Nat. Electron* **1**, 333–343 (2018).

[Article](https://doi.org/10.1038%2Fs41928-018-0092-2) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=In-memory%20computing%20with%20resistive%20switching%20devices&journal=Nat.%20Electron&doi=10.1038%2Fs41928-018-0092-2&volume=1&pages=333-343&publication_year=2018&author=Ielmini%2CD&author=Wong%2CH-SP)

[^12]: Ni, K. et al. In-Memory Computing Primitive for Sensor Data Fusion in 28 nm HKMG FeFET Technology. In *2018 IEEE International Electron Devices Meeting (IEDM)* 16.1.1-16.1.4, [https://doi.org/10.1109/IEDM.2018.8614527](https://doi.org/10.1109/IEDM.2018.8614527) (2018).

[^13]: Xue, C.-X. et al. 24.1 A 1Mb multibit ReRAM computing-in-memory macro with 14.6ns parallel MAC computing time for CNN based AI edge processors. In *2019 IEEE International Solid- State Circuits Conference - (ISSCC)* 388–390, [https://doi.org/10.1109/ISSCC.2019.8662395](https://doi.org/10.1109/ISSCC.2019.8662395) (2019).

[^14]: Deng, B. L., Li, G., Han, S., Shi, L. & Xie, Y. Model compression and hardware acceleration for neural networks: a comprehensive survey. *Proc. IEEE* **108**, 485–532 (2020).

[Article](https://doi.org/10.1109%2FJPROC.2020.2976475) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2020IEEEP.108..485D) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Model%20compression%20and%20hardware%20acceleration%20for%20neural%20networks%3A%20a%20comprehensive%20survey&journal=Proc.%20IEEE&doi=10.1109%2FJPROC.2020.2976475&volume=108&pages=485-532&publication_year=2020&author=Deng%2CBL&author=Li%2CG&author=Han%2CS&author=Shi%2CL&author=Xie%2CY)

[^15]: Yu, S., Jiang, H., Huang, S., Peng, X. & Lu, A. Compute-in-memory chips for deep learning: recent trends and prospects. *IEEE Circuits Syst. Mag.* **21**, 31–56 (2021).

[Article](https://doi.org/10.1109%2FMCAS.2021.3092533) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Compute-in-memory%20chips%20for%20deep%20learning%3A%20recent%20trends%20and%20prospects&journal=IEEE%20Circuits%20Syst.%20Mag.&doi=10.1109%2FMCAS.2021.3092533&volume=21&pages=31-56&publication_year=2021&author=Yu%2CS&author=Jiang%2CH&author=Huang%2CS&author=Peng%2CX&author=Lu%2CA)

[^16]: Mao, R. et al. Experimentally validated memristive memory augmented neural network with efficient hashing and similarity search. *Nat. Commun.* **13**, 6284 (2022).

[Article](https://doi.org/10.1038%2Fs41467-022-33629-7) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2022NatCo..13.6284M) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BB38XislWiurfL) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=36271072) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC9587027) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Experimentally%20validated%20memristive%20memory%20augmented%20neural%20network%20with%20efficient%20hashing%20and%20similarity%20search&journal=Nat.%20Commun.&doi=10.1038%2Fs41467-022-33629-7&volume=13&publication_year=2022&author=Mao%2CR)

[^17]: Le Gallo, M. et al. A 64-core mixed-signal in-memory compute chip based on phase-change memory for deep neural network inference. *Nat Electron* 1–14, [https://doi.org/10.1038/s41928-023-01010-1](https://doi.org/10.1038/s41928-023-01010-1) (2023).

[^18]: Jiang, M., Shan, K., He, C. & Li, C. Efficient combinatorial optimization by quantum-inspired parallel annealing in analogue memristor crossbar. *Nat. Commun.* **14**, 5927 (2023).

[Article](https://doi.org/10.1038%2Fs41467-023-41647-2) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2023NatCo..14.5927J) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BB3sXitVSrsbnK) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=37739944) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC10516914) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Efficient%20combinatorial%20optimization%20by%20quantum-inspired%20parallel%20annealing%20in%20analogue%20memristor%20crossbar&journal=Nat.%20Commun.&doi=10.1038%2Fs41467-023-41647-2&volume=14&publication_year=2023&author=Jiang%2CM&author=Shan%2CK&author=He%2CC&author=Li%2CC)

[^19]: Wang, Z. et al. A dual-domain compute-in-memory system for general neural network inference. *Nat Electron* 1–12, [https://doi.org/10.1038/s41928-024-01315-9](https://doi.org/10.1038/s41928-024-01315-9) (2025).

[^20]: Yu, S. Neuro-inspired computing with emerging nonvolatile memory. *Proc. IEEE* **106**, 260–285 (2018).

[Article](https://doi.org/10.1109%2FJPROC.2018.2790840) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2018IEEEP.106..260Y) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC1MXjt1GrtL8%3D) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Neuro-inspired%20computing%20with%20emerging%20nonvolatile%20memory&journal=Proc.%20IEEE&doi=10.1109%2FJPROC.2018.2790840&volume=106&pages=260-285&publication_year=2018&author=Yu%2CS)

[^21]: Hu, M. et al. Dot-product engine for neuromorphic computing: programming 1T1M crossbar to accelerate matrix-vector multiplication. In *Proceedings of the 53rd Annual Design Automation Conference* 1–6, [https://doi.org/10.1145/2897937.2898010](https://doi.org/10.1145/2897937.2898010) (2016).

[^22]: Gallo, M. L. et al. Mixed-precision in-memory computing. *Nat. Electron* **1**, 246–253 (2018).

[Article](https://doi.org/10.1038%2Fs41928-018-0054-8) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Mixed-precision%20in-memory%20computing&journal=Nat.%20Electron&doi=10.1038%2Fs41928-018-0054-8&volume=1&pages=246-253&publication_year=2018&author=Gallo%2CML)

[^23]: Wang, Z. et al. In situ training of feed-forward and recurrent convolutional memristor networks. *Nat. Mach. Intell.* **1**, 434–442 (2019).

[Article](https://doi.org/10.1038%2Fs42256-019-0089-1) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=In%20situ%20training%20of%20feed-forward%20and%20recurrent%20convolutional%20memristor%20networks&journal=Nat.%20Mach.%20Intell.&doi=10.1038%2Fs42256-019-0089-1&volume=1&pages=434-442&publication_year=2019&author=Wang%2CZ)

[^24]: Chi, P. et al. Prime: a novel processing-in-memory architecture for neural network computation in reram-based main memory. *ACM SIGARCH Comput. Architecture N.* **44**, 27–39 (2016).

[Article](https://doi.org/10.1145%2F3007787.3001140) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Prime%3A%20a%20novel%20processing-in-memory%20architecture%20for%20neural%20network%20computation%20in%20reram-based%20main%20memory&journal=ACM%20SIGARCH%20Comput.%20Architecture%20N.&doi=10.1145%2F3007787.3001140&volume=44&pages=27-39&publication_year=2016&author=Chi%2CP)

[^25]: Zhu, Z. et al. A configurable multi-precision CNN computing framework based on single bit RRAM. In *Proceedings of the 56th Annual Design Automation Conference 2019*, 1–6, [https://doi.org/10.1145/3316781.3317739](https://doi.org/10.1145/3316781.3317739) (2019).

[^26]: Jiang, H. et al. Analog-to-digital converter design exploration for compute-in-memory accelerators. *IEEE Des. Test.* **39**, 48–55 (2022).

[Article](https://doi.org/10.1109%2FMDAT.2021.3050715) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Analog-to-digital%20converter%20design%20exploration%20for%20compute-in-memory%20accelerators&journal=IEEE%20Des.%20Test.&doi=10.1109%2FMDAT.2021.3050715&volume=39&pages=48-55&publication_year=2022&author=Jiang%2CH)

[^27]: Wan, W. et al. A compute-in-memory chip based on resistive random-access memory. *Nature* **608**, 504–512 (2022).

[Article](https://doi.org/10.1038%2Fs41586-022-04992-8) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2022Natur.608..504W) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BB38XitFGls77N) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=35978128) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC9385482) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20compute-in-memory%20chip%20based%20on%20resistive%20random-access%20memory&journal=Nature&doi=10.1038%2Fs41586-022-04992-8&volume=608&pages=504-512&publication_year=2022&author=Wan%2CW)

[^28]: Yao, P. et al. Fully hardware-implemented memristor convolutional neural network. *Nature* **577**, 641–646 (2020).

[Article](https://doi.org/10.1038%2Fs41586-020-1942-4) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2020Natur.577..641Y) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BB3cXktFegt74%3D) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=31996818) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Fully%20hardware-implemented%20memristor%20convolutional%20neural%20network&journal=Nature&doi=10.1038%2Fs41586-020-1942-4&volume=577&pages=641-646&publication_year=2020&author=Yao%2CP)

[^29]: He, Y. et al. InfoX: an energy-efficient ReRAM accelerator design with information-lossless low-bit ADCs. In *Proceedings of the 59th ACM/IEEE Design Automation Conference* 97–102, [https://doi.org/10.1145/3489517.3530396](https://doi.org/10.1145/3489517.3530396) (2022).

[^30]: Yue, J. et al. 15.2 A 2.75-to-75.9TOPS/W computing-in-memory NN processor supporting set-associate block-wise zero skipping and ping-pong CIM with simultaneous computation and weight updating. In *2021 IEEE International Solid- State Circuits Conference (ISSCC)* 238–240, [https://doi.org/10.1109/ISSCC42613.2021.9365958](https://doi.org/10.1109/ISSCC42613.2021.9365958) (2021).

[^31]: Sun, H. et al. An energy-efficient quantized and regularized training framework for processing-in-memory accelerators. In *2020 25th Asia and South Pacific Design Automation Conference (ASP-DAC)* 325–330, [https://doi.org/10.1109/ASP-DAC47756.2020.9045192](https://doi.org/10.1109/ASP-DAC47756.2020.9045192) (2020).

[^32]: Lloyd, S. Least squares quantization in PCM. *IEEE Trans. Inf. Theory* **28**, 129–137 (1982).

[Article](https://doi.org/10.1109%2FTIT.1982.1056489) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=1982ITIT...28..129L) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=651807) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Least%20squares%20quantization%20in%20PCM&journal=IEEE%20Trans.%20Inf.%20Theory&doi=10.1109%2FTIT.1982.1056489&volume=28&pages=129-137&publication_year=1982&author=Lloyd%2CS)

[^33]: Sun, X. et al. XNOR-RRAM: A scalable and parallel resistive synaptic architecture for binary neural networks. In *2018 Design, Automation & Test in Europe Conference & Exhibition (DATE)* 1423–1428, [https://doi.org/10.23919/DATE.2018.8342235](https://doi.org/10.23919/DATE.2018.8342235) (2018).

[^34]: Cai, Y. et al. Low bit-width convolutional neural network on RRAM. *IEEE Trans. Comput. Aided Des. Integr. Circuits Syst.* **39**, 1414–1427 (2020).

[Article](https://doi.org/10.1109%2FTCAD.2019.2917852) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2020ITCAD..39.1414C) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Low%20bit-width%20convolutional%20neural%20network%20on%20RRAM&journal=IEEE%20Trans.%20Comput.%20Aided%20Des.%20Integr.%20Circuits%20Syst.&doi=10.1109%2FTCAD.2019.2917852&volume=39&pages=1414-1427&publication_year=2020&author=Cai%2CY)

[^35]: Yang, J. et al. Efficient nonlinear function approximation in analog resistive crossbars for recurrent neural networks. *Nat. Commun.* **16**, 1136 (2025).

[Article](https://doi.org/10.1038%2Fs41467-025-56254-6) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2025NatCo..16.1136Y) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BB2MXis1Crsbc%3D) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=39881186) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC11779922) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Efficient%20nonlinear%20function%20approximation%20in%20analog%20resistive%20crossbars%20for%20recurrent%20neural%20networks&journal=Nat.%20Commun.&doi=10.1038%2Fs41467-025-56254-6&volume=16&publication_year=2025&author=Yang%2CJ)

[^36]: Li, C. et al. Analog content-addressable memories with memristors. *Nat. Commun.* **11**, 1638 (2020).

[Article](https://doi.org/10.1038%2Fs41467-020-15254-4) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2020NatCo..11.1638L) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=32242006) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC7118145) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Analog%20content-addressable%20memories%20with%20memristors&journal=Nat.%20Commun.&doi=10.1038%2Fs41467-020-15254-4&volume=11&publication_year=2020&author=Li%2CC)

[^37]: Pedretti, G. et al. Tree-based machine learning performed in-memory with memristive analog CAM. *Nat. Commun.* **12**, 5806 (2021).

[Article](https://doi.org/10.1038%2Fs41467-021-25873-0) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2021NatCo..12.5806P) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BB3MXitFKqt7jN) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=34608133) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC8490381) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Tree-based%20machine%20learning%20performed%20in-memory%20with%20memristive%20analog%20CAM&journal=Nat.%20Commun.&doi=10.1038%2Fs41467-021-25873-0&volume=12&publication_year=2021&author=Pedretti%2CG)

[^38]: Pedretti, G. et al. Differentiable content addressable memory with memristors. *Adv. Elect. Mater.* **8**, 2101198 (2022).

[Article](https://doi.org/10.1002%2Faelm.202101198) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BB38XlvVeitrc%3D) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Differentiable%20content%20addressable%20memory%20with%20memristors&journal=Adv.%20Elect.%20Mater.&doi=10.1002%2Faelm.202101198&volume=8&publication_year=2022&author=Pedretti%2CG)

[^39]: Huang, S., Jiang, H. & Yu, S. Hardware-aware quantization/mapping strategies for compute-in-memory accelerators. *ACM Trans. Des. Autom. Electron. Syst.* **28**, 1–23 (2023).

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=Hardware-aware%20quantization%2Fmapping%20strategies%20for%20compute-in-memory%20accelerators&journal=ACM%20Trans.%20Des.%20Autom.%20Electron.%20Syst.&volume=28&pages=1-23&publication_year=2023&author=Huang%2CS&author=Jiang%2CH&author=Yu%2CS)

[^40]: Feinberg, B., Wang, S. & Ipek, E. Making memristive neural network accelerators reliable. In *2018 IEEE International Symposium on High Performance Computer Architecture (HPCA)* 52–65, [https://doi.org/10.1109/HPCA.2018.00015](https://doi.org/10.1109/HPCA.2018.00015) (2018).

[^41]: Jespers, P. G. *Integrated Converters: D to A and A to D Architectures, Analysis and Simulation* (Oxford University Press, 2001).

[^42]: Simonyan, K. & Zisserman, A. Very deep convolutional networks for large-scale image recognition. In Proc. *Int. Conf. Learn. Represent. (ICLR)* (2015).

[^43]: Krizhevsky, A., Nair, V. & Hinton, G. Learning Multiple Layers of Features from Tiny Images. Technical report, University of Toronto (2009).

[^44]: He, K., Zhang, X., Ren, S. & Sun, J. Deep residual learning for image recognition. In *2016 IEEE Conference on Computer Vision and Pattern Recognition* 770–778, [https://doi.org/10.1109/CVPR.2016.90](https://doi.org/10.1109/CVPR.2016.90) (2016).

[^45]: Deng, J. et al. ImageNet: a large-scale hierarchical image database. In *2009 IEEE Conference on Computer Vision and Pattern Recognition* 248–255, [https://doi.org/10.1109/CVPR.2009.5206848](https://doi.org/10.1109/CVPR.2009.5206848) (2009).

[^46]: Boris, M. ADC Performance Survey 1997-2024. *GitHub*, [https://github.com/bmurmann/ADC-survey](https://github.com/bmurmann/ADC-survey)

[^47]: Bindra, H. S., Annema, A.-J., Louwsma, S. M. & Nauta, B. A 0.2 - 8 MS/s 10b flexible SAR ADC achieving 0.35 - 2.5 fJ/conv-step and using self-quenched dynamic bias comparator. In *2019 Symposium on VLSI Circuits* C74–C75, [https://doi.org/10.23919/VLSIC.2019.8778093](https://doi.org/10.23919/VLSIC.2019.8778093) (2019).

[^48]: Yonar, A. S. et al. An 8b 1.0-to-1.25GS/s 0.7-to-0.8V single-stage time-based gated-ring-oscillator ADC with 2\\times interpolating sense-amplifier-latches. In *2023 IEEE International Solid-State Circuits Conference (ISSCC)* 1–3, [https://doi.org/10.1109/ISSCC42615.2023.10067745](https://doi.org/10.1109/ISSCC42615.2023.10067745) (2023).

[^49]: Peng, X., Huang, S., Luo, Y., Sun, X. & Yu, S. DNN+NeuroSim: an end-to-end benchmarking framework for compute-in-memory accelerators with versatile device technologies. In *2019 IEEE International Electron Devices Meeting (IEDM)* 32.5.1-32.5.4 [https://doi.org/10.1109/IEDM19573.2019.8993491](https://doi.org/10.1109/IEDM19573.2019.8993491) (2019).

[^50]: Hsu, H.-H. et al. A nonvolatile AI-edge processor with SLC–MLC hybrid ReRAM compute-in-memory macro using current–voltage-hybrid readout scheme. *IEEE J. Solid State Circuits* **59**, 116–127 (2024).

[Article](https://doi.org/10.1109%2FJSSC.2023.3314433) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2024IJSSC..59..116H) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20nonvolatile%20AI-edge%20processor%20with%20SLC%E2%80%93MLC%20hybrid%20ReRAM%20compute-in-memory%20macro%20using%20current%E2%80%93voltage-hybrid%20readout%20scheme&journal=IEEE%20J.%20Solid%20State%20Circuits&doi=10.1109%2FJSSC.2023.3314433&volume=59&pages=116-127&publication_year=2024&author=Hsu%2CH-H)

[^51]: Roy, S. K. et al. Compute SNDR-boosted 22-nm MRAM-based in-memory computing macro using statistical error compensation. *IEEE J. Solid State Circuits* **60**, 1092–1102 (2025).

[Article](https://doi.org/10.1109%2FJSSC.2024.3442013) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2025IJSSC..60.1092R) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Compute%20SNDR-boosted%2022-nm%20MRAM-based%20in-memory%20computing%20macro%20using%20statistical%20error%20compensation&journal=IEEE%20J.%20Solid%20State%20Circuits&doi=10.1109%2FJSSC.2024.3442013&volume=60&pages=1092-1102&publication_year=2025&author=Roy%2CSK)

[^52]: Hung, J.-M., Jhang, C.-J., Wu, P.-C., Chiu, Y.-C. & Chang, M.-F. Challenges and trends of nonvolatile in-memory-computation circuits for AI edge devices. *IEEE Open J. Solid-State Circuits Soc.* **1**, 171–183 (2021).

[Article](https://doi.org/10.1109%2FOJSSCS.2021.3123287) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Challenges%20and%20trends%20of%20nonvolatile%20in-memory-computation%20circuits%20for%20AI%20edge%20devices&journal=IEEE%20Open%20J.%20Solid-State%20Circuits%20Soc.&doi=10.1109%2FOJSSCS.2021.3123287&volume=1&pages=171-183&publication_year=2021&author=Hung%2CJ-M&author=Jhang%2CC-J&author=Wu%2CP-C&author=Chiu%2CY-C&author=Chang%2CM-F)

[^53]: Khaddam-Aljameh, R. et al. HERMES-core—a 1.59-TOPS/mm <sup>2</sup> PCM on 14-nm CMOS in-memory compute core using 300-ps/LSB linearized CCO-based ADCs. *IEEE J. Solid State Circuits* **57**, 1027–1038 (2022).

[Article](https://doi.org/10.1109%2FJSSC.2022.3140414) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2022IJSSC..57.1027K) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=HERMES-core%E2%80%94a%201.59-TOPS%2Fmm2%20PCM%20on%2014-nm%20CMOS%20in-memory%20compute%20core%20using%20300-ps%2FLSB%20linearized%20CCO-based%20ADCs&journal=IEEE%20J.%20Solid%20State%20Circuits&doi=10.1109%2FJSSC.2022.3140414&volume=57&pages=1027-1038&publication_year=2022&author=Khaddam-Aljameh%2CR)

[^54]: Hong, H. Memristor-based adaptive analog-to-digital conversion for efficient and accurate compute-in-memory. *GitHub*, [https://github.com/MIKEHHQ/ReADC](https://github.com/MIKEHHQ/ReADC) (2025).
