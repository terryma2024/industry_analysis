---
source_id: "SRC-ic-045"
title: "Mixed-precision memristor and SRAM edge AI processor"
source_type: "nature_paper"
publisher: "Nature / TSMC"
source_date: "2025-03-05"
url: "https://www.nature.com/articles/s41586-025-08639-2"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-09-21T02:06:23+00:00"
tags:
  - raw/source
  - source-type/nature-paper
  - evidence/s
aliases:
  - SRC-ic-045
---
# Mixed-precision memristor and SRAM edge AI processor

## Abstract

Artificial intelligence (AI) edge devices [^1] [^2] [^3] [^4] [^5] [^6] [^7] [^8] [^9] [^10] [^11] [^12] demand high-precision energy-efficient computations, large on-chip model storage, rapid wakeup-to-response time and cost-effective foundry-ready solutions. Floating point (FP) computation provides precision exceeding that of integer (INT) formats at the cost of higher power and storage overhead. Multi-level-cell (MLC) memristor compute-in-memory (CIM) [^13] [^14] [^15] provides compact non-volatile storage and energy-efficient computation but is prone to accuracy loss owing to process variation. Digital static random-access memory (SRAM)-CIM [^16] [^17] [^18] [^19] [^20] [^21] [^22] enables lossless computation; however, storage is low as a result of large bit-cell area and model loading is required during inference. Thus, conventional approaches using homogeneous CIM architectures and computation formats impose a trade-off between efficiency, storage, wakeup latency and inference accuracy. Here we present a mixed-precision heterogeneous CIM AI edge processor, which supports the layer-granular/kernel-granular partitioning of network layers among on-chip CIM architectures (that is, memristor-CIM, SRAM-CIM and tiny-digital units) and computation number formats (INT and FP) based on sensitivity to error. This layer-granular/kernel-granular flexibility allows simultaneous optimization within the two-dimensional design space at the hardware level. The proposed hardware achieved high energy efficiency (40.91 TFLOPS W <sup>−1</sup> for ResNet-20 with CIFAR-100 and 28.63 TFLOPS W <sup>−1</sup> for MobileNet-v2 with ImageNet), low accuracy degradation (<0.45% for ResNet-20 with CIFAR-100 and for MobilNet-v2 with ImageNet) and rapid wakeup-to-response time (373.52 μs).

This is a preview of subscription content, [access via your institution](https://wayf.springernature.com/?redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41586-025-08639-2)

## Access options

[Access through your institution](https://wayf.springernature.com/?redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41586-025-08639-2)

Buy this article

- Purchase on SpringerLink
- Instant access to the full article PDF.

￥ 4,980

Prices may be subject to local taxes which are calculated during checkout

![](https://media.springernature.com/m312/springer-static/image/art%3A10.1038%2Fs41586-025-08639-2/MediaObjects/41586_2025_8639_Fig1_HTML.png?as=webp)

Fig. 1: Overview of proposed heterogeneous INT–FP hybrid-mode and memristor-SRAM-digital mix-CIM AI edge processor.

![](https://media.springernature.com/m312/springer-static/image/art%3A10.1038%2Fs41586-025-08639-2/MediaObjects/41586_2025_8639_Fig2_HTML.png?as=webp)

Fig. 2: Overview of the proposed layer-based INT–FP hybrid-mode controller and hybrid-mode implementation.

![](https://media.springernature.com/m312/springer-static/image/art%3A10.1038%2Fs41586-025-08639-2/MediaObjects/41586_2025_8639_Fig3_HTML.png?as=webp)

Fig. 3: Overview of the proposed memristor-SRAM-digital mix-CIM structure.

![](https://media.springernature.com/m312/springer-static/image/art%3A10.1038%2Fs41586-025-08639-2/MediaObjects/41586_2025_8639_Fig4_HTML.png?as=webp)

Fig. 4: Measurement results and demonstration of the proposed AI edge device.

## Data availability

The datasets that we used for benchmarking are publicly available in refs. [^51] [^52] [^53] [^55] [^56] [^57]. Other data that support the findings of this study can be made available by the corresponding author on request after TSMC management approval.

## Code availability

The codes that support the findings of this study are not available but exceptions for non-commercial use might be made on request after TSMC management approval.

## References

## Acknowledgements

We acknowledge support from National Tsing Hua University (NTHU), TSMC Corporate Research (TSMC-CR), TSMC Design Technology Platform (TSMC-DTP), TSMC More-than-Moore Technologies (TSMC-MtM), TSMC-NTHU Joint Developed Project (JDP) and the National Science and Technology Council (NSTC) of Taiwan. We also acknowledge contributions from TSMC colleagues H.-S. P. Wong, H. Chuang, W. T. Chu and K. C. Huang.

## Ethics declarations

### Competing interests

The authors declare no competing interests.

## Peer review

### Peer review information

*Nature* thanks Yiyu Shi and the other, anonymous, reviewer(s) for their contribution to the peer review of this work.

## Additional information

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Extended data figures and tables

### Extended Data Fig. 1 Experiment platform and timing-extraction circuit.

**a**, Experiment platform used to assess the proposed memristor-SRAM CIM-fusion processor, including data generator, logic analyser, oscilloscope, power supply and analogue voltage supply. **b**, On-chip timing-extraction circuit and experiment methods used to measure wakeup-to-response latency. **c**, Illustration of the signal involving measurement of the wakeup-to-response latency. **d**, Measured waveform indicating wakeup-to-response latency using a ResNet-20 model trained for the FLAME dataset.

### Extended Data Fig. 2 Trade-off between accuracy and energy efficiency under various input and weight formats.

**a**, Measured energy efficiency under various input and weight formats using a ResNet-20 model trained for CIFAR-100. **b**, Inference accuracy using a ResNet-20 model trained for CIFAR-100 versus software baseline under FP16. **c**, FoM performance as a function of input and weight formats. FoM = energy efficiency/inference accuracy degradation.

### Extended Data Fig. 3 Trade-off between accuracy and energy efficiency under various mix-CIM configurations.

**a**, Breakdown of CIM architectures (memristor-CIM, SRAM-CIM and tiny-digital unit). **b**, Measured energy efficiency and inference accuracy degradation of various computing architectures using a ResNet-20 model trained for CIFAR-100. **c**, Normalized deviation in the output value of each layer in a ResNet-20 model trained for the CIFAR-100 dataset. **d**, FoM as a function of mix-CIM configuration. FoM = energy efficiency/inference accuracy degradation.

### Extended Data Fig. 4 Implementation of memristor-CIM and SRAM-CIM.

**a**, The memristor-CIM performs partial dot-product operations in the cell array by inducing cell current in the memristor device and accumulating cell current on the BL. The 5-bit-resolution ADC converts BL current from the analogue domain to the digital domain and the accumulator combines the results from the weight MSB column to the LSB column across input cycles to generate DPVs. **b**, Implementation of SRAM-CIM using a mux-based compute unit for dot-product operations with no accuracy loss.

### Extended Data Fig. 5 Illustration of the proposed 2D-PVA-DA scheme.

**a**, Conventional memristor-CIM using a consistent number of accumulations (the number of WLs that are turned on in a single cycle) across various input place values and weight place values. **b**, The proposed 2D-PVA-DA adjusts the number of accumulations according to the place value of inputs and weights to increase the overall number of accumulations. **c**, This scheme reduced the operation cycle counts by 42% in memristor-CIM.

### Extended Data Fig. 6 Layer-wise configurations for various applications and measurement results demonstrating the efficacy of the proposed AI edge processor when applied to keyword spotting and visual wake word detection.

**a**, Layer-wise configuration of the ResNet-20 model trained for CIFAR-100 using hybrid mode and mix-CIM. **b**, Layer-wise configuration of the MobileNet-v2 model trained for ImageNet using hybrid mode and mix-CIM. **c**, Breakdown of computation types (INT and FP) on the left axis and CIM architectures (memristor-CIM, SRAM-CIM and tiny-digital unit) on the right axis. **d**, Inference accuracy and energy efficiency across use scenarios.

### Extended Data Fig. 7 Comparison of proposed 2DQA scheme versus previous works.

**a**, Processing of the pretrained model by the proposed 2DQA scheme. **b**, Error injection was used to obtain concise guidelines by which to determine the sensitivity of each layer for use in deriving a usable configuration without having to assess all possible combinations iteratively. **c**, 2DQA scheme outperformed all previous mixed-precision architectures in terms of inference accuracy when applied to the complex ImageNet dataset. Data from refs. [^11] [^47] [^60] [^61].

### Extended Data Fig. 8 Illustration of pre-alignment process for FP inputs and weights and comparison of alignment methods for FP operations.

**a**, During the pre-alignment process, the FP format is converted to the fixed-point format to facilitate subsequent processing. **b**, Comparison of different alignment methods: product alignment, input alignment, input-wise and layer-wise weight separate alignment and the proposed input-wise and kernel-wise weight separate alignment. **c**, Simulated energy consumption by memristor-CIM macro under various alignment methods. **d**, Inference accuracy as a function of bit width under various alignment methods.

### Extended Data Fig. 9 Characteristics and specifications of the proposed memristor device.

The characteristics of the proposed memristor, including the underlying technology, memristor cell size, set/reset voltages, read voltage, normalized resistance state of weights, normalized conductance state of weights and dimensions of memristor banks.

**Extended Data Table 1 Comparison of NVM-based processors and macros**

## Rights and permissions

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

[^1]: Prabhu, K. et al. CHIMERA: a 0.92-TOPS, 2.2-TOPS/W edge AI accelerator with 2-Mbyte on-chip foundry resistive RAM for efficient training and inference. *IEEE J. Solid-State Circuits* **57**, 1013–1026 (2022).

[Article](https://doi.org/10.1109%2FJSSC.2022.3140753) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2022IJSSC..57.1013P) [MATH](http://www.emis.de/MATH-item?1524.60239) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=CHIMERA%3A%20a%200.92-TOPS%2C%202.2-TOPS%2FW%20edge%20AI%20accelerator%20with%202-Mbyte%20on-chip%20foundry%20resistive%20RAM%20for%20efficient%20training%20and%20inference&journal=IEEE%20J.%20Solid-State%20Circuits&doi=10.1109%2FJSSC.2022.3140753&volume=57&pages=1013-1026&publication_year=2022&author=Prabhu%2CK)

[^2]: Jain, V. et al. TinyVers: A 0.8-17 TOPS/W, 1.7 μW-20 mW, tiny versatile system-on-chip with state-retentive eMRAM for machine learning inference at the extreme edge. In *Proc. 2022 IEEE Symposium on VLSI Technology and Circuits* 20–21 (IEEE, 2022).

[^3]: Rossi, D. et al. 4.4 A 1.3TOPS/W @ 32GOPS fully integrated 10-core SoC for IoT end-nodes with 1.7μW cognitive wake-up from MRAM-based state-retentive sleep mode. In *Proc. 2021 IEEE International Solid-State Circuits Conference (ISSCC)* 60–62 (IEEE, 2021).

[^4]: Ueyoshi, K. et al. DIANA: an end-to-end energy-efficient digital and analog hybrid neural network SoC. In *Proc. 2022 IEEE International Solid-State Circuits Conference (ISSCC)* 1–3 (IEEE, 2022).

[^5]: Yue, J. et al. A 28nm 16.9-300TOPS/W computing-in-memory processor supporting floating-point NN inference/training with intensive-CIM sparse-digital architecture. In *Proc. 2023 IEEE International Solid-State Circuits Conference (ISSCC)* 1–3 (IEEE, 2023).

[^6]: Yue, J. et al. 15.2 A 2.75-to-75.9TOPS/W computing-in-memory NN processor supporting set-associate block-wise zero skipping and ping-pong CIM with simultaneous computation and weight updating. In *Proc. 2021 IEEE International Solid-State Circuits Conference (ISSCC)* 238–240 (IEEE, 2021).

[^7]: Liu, S. et al. 16.2 A 28nm 53.8TOPS/W 8b sparse transformer accelerator with in-memory butterfly zero skipper for unstructured-pruned NN and CIM-based local-attention-reusable engine. In *Proc. 2023 IEEE International Solid-State Circuits Conference (ISSCC)* 250–252 (IEEE, 2023).

[^8]: Tu, F. et al. 16.1 MuITCIM: a 28nm 2.24μJ/token attention-token-bit hybrid sparse digital CIM-based accelerator for multimodal transformers. In *Proc. 2023 IEEE International Solid-State Circuits Conference (ISSCC)* 248–250 (IEEE, 2023).

[^9]: Huang, W.-H. et al. A nonvolatile Al-edge processor with 4MB SLC-MLC hybrid-mode ReRAM compute-in-memory macro and 51.4-251 TOPS/W. In *Proc. 2023 IEEE International Solid-State Circuits Conference (ISSCC)* 15–17 (IEEE, 2023).

[^10]: Wen, T.-H. et al. A 28nm nonvolatile AI edge processor using 4Mb analog-based near-memory-compute ReRAM with 27.2 TOPS/W for tiny AI edge devices. In *Proc. 2023 IEEE Symposium on VLSI Technology and Circuits* 1–2 (IEEE, 2023).

[^11]: Wen, T.-H. et al. Fusion of memristor and digital compute-in-memory processing for energy-efficient edge computing. *Science* **384**, 325–332 (2024).

[Article](https://doi.org/10.1126%2Fscience.adf5538) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2024Sci...384..325W) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BB2cXovVCnt7s%3D) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=38669568) [MATH](http://www.emis.de/MATH-item?07910186) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Fusion%20of%20memristor%20and%20digital%20compute-in-memory%20processing%20for%20energy-efficient%20edge%20computing&journal=Science&doi=10.1126%2Fscience.adf5538&volume=384&pages=325-332&publication_year=2024&author=Wen%2CT-H)

[^12]: Lele, A. S. et al. A heterogeneous RRAM in-memory and SRAM near-memory SoC for fused frame and event-based target identification and tracking. *IEEE J. Solid-State Circuits* **59**, 52–64 (2024).

[Article](https://doi.org/10.1109%2FJSSC.2023.3297411) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2024IJSSC..59...52L) [MATH](http://www.emis.de/MATH-item?1532.05107) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20heterogeneous%20RRAM%20in-memory%20and%20SRAM%20near-memory%20SoC%20for%20fused%20frame%20and%20event-based%20target%20identification%20and%20tracking&journal=IEEE%20J.%20Solid-State%20Circuits&doi=10.1109%2FJSSC.2023.3297411&volume=59&pages=52-64&publication_year=2024&author=Lele%2CAS)

[^13]: Ambrogio, S. et al. Equivalent-accuracy accelerated neural-network training using analogue memory. *Nature* **558**, 60–67 (2018).

[Article](https://doi.org/10.1038%2Fs41586-018-0180-5) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2018Natur.558...60A) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC1cXhtV2lsr3O) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=29875487) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Equivalent-accuracy%20accelerated%20neural-network%20training%20using%20analogue%20memory&journal=Nature&doi=10.1038%2Fs41586-018-0180-5&volume=558&pages=60-67&publication_year=2018&author=Ambrogio%2CS)

[^14]: Khwa, W.-S. et al. A 40-nm, 2M-cell, 8b-precision, hybrid SLC-MLC PCM computing-in-memory macro with 20.5-65.0TOPS/W for tiny-Al edge devices. In *Proc. 2022 IEEE International Solid-State Circuits Conference (ISSCC)* 1–3 (IEEE, 2022).

[^15]: Yao, P. et al. Fully hardware-implemented memristor convolutional neural network. *Nature* **577**, 641–646 (2020).

[Article](https://doi.org/10.1038%2Fs41586-020-1942-4) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2020Natur.577..641Y) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BB3cXktFegt74%3D) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=31996818) [MATH](http://www.emis.de/MATH-item?1517.93082) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Fully%20hardware-implemented%20memristor%20convolutional%20neural%20network&journal=Nature&doi=10.1038%2Fs41586-020-1942-4&volume=577&pages=641-646&publication_year=2020&author=Yao%2CP)

[^16]: Wu, P.-C. et al. A 22nm 832Kb hybrid-domain floating-point SRAM in-memory-compute macro with 16.2-70.2TFLOPS/W for high-accuracy AI-edge devices. In *Proc. 2023 IEEE International Solid-State Circuits Conference (ISSCC)* 126–128 (IEEE, 2023).

[^17]: Guo, A. et al. A 28-nm 64-kb 31.6-TFLOPS/W digital-domain floating-point-computing-unit and double-bit 6T-SRAM computing-in-memory macro for floating-point CNNs. *IEEE J. Solid-State Circuits* **59**, 3032–3044 (2024).

[Article](https://doi.org/10.1109%2FJSSC.2024.3375359) [MATH](http://www.emis.de/MATH-item?07909892) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%2028-nm%2064-kb%2031.6-TFLOPS%2FW%20digital-domain%20floating-point-computing-unit%20and%20double-bit%206T-SRAM%20computing-in-memory%20macro%20for%20floating-point%20CNNs&journal=IEEE%20J.%20Solid-State%20Circuits&doi=10.1109%2FJSSC.2024.3375359&volume=59&pages=3032-3044&publication_year=2024&author=Guo%2CA)

[^18]: Sinangil, M. E. et al. A 7-nm compute-in-memory SRAM macro supporting multi-bit input, weight and output and achieving 351 TOPS/W and 372.4 GOPS. *IEEE J. Solid-State Circuits* **56**, 188–198 (2021).

[Article](https://doi.org/10.1109%2FJSSC.2020.3031290) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2021IJSSC..56..188S) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%207-nm%20compute-in-memory%20SRAM%20macro%20supporting%20multi-bit%20input%2C%20weight%20and%20output%20and%20achieving%20351%20TOPS%2FW%20and%20372.4%20GOPS&journal=IEEE%20J.%20Solid-State%20Circuits&doi=10.1109%2FJSSC.2020.3031290&volume=56&pages=188-198&publication_year=2021&author=Sinangil%2CME)

[^19]: Mori, H. et al. A 4nm 6163-TOPS/W/b 4790−TOPS/mm <sup>2</sup> /b SRAM based digital-computing-in-memory macro supporting bit-width flexibility and simultaneous MAC and weight update. In *Proc. 2023 IEEE International Solid-State Circuits Conference (ISSCC)* 132–134 (IEEE, 2023).

[^20]: Chih, Y.-D. et al. 16.4 An 89TOPS/W and 16.3TOPS/mm <sup>2</sup> all-digital SRAM-based full-precision compute-in memory macro in 22nm for machine-learning edge applications. In *Proc. 2021 IEEE International Solid-State Circuits Conference (ISSCC)* 252–254 (IEEE, 2021).

[^21]: Fujiwara, H. et al. A 5-nm 254-TOPS/W 221-TOPS/mm <sup>2</sup> fully-digital computing-in-memory macro supporting wide-range dynamic-voltage-frequency scaling and simultaneous MAC and write operations. In *Proc. 2022 IEEE International Solid-State Circuits Conference (ISSCC)* 1–3 (IEEE, 2022).

[^22]: Lee, C.-F. et al. A 12nm 121-TOPS/W 41.6-TOPS/mm <sup>2</sup> all digital full precision SRAM-based compute-in-memory with configurable bit-width for AI edge applications. In *Proc. 2022 IEEE Symposium on VLSI Technology and Circuits* 24–25 (IEEE, 2022).

[^23]: Chiu, Y. C. et al. A CMOS-integrated spintronic compute-in-memory macro for secure AI edge devices. *Nat. Electron.* **6**, 534–543 (2023).

[Article](https://doi.org/10.1038%2Fs41928-023-00994-0) [MATH](http://www.emis.de/MATH-item?0701.76071) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20CMOS-integrated%20spintronic%20compute-in-memory%20macro%20for%20secure%20AI%20edge%20devices&journal=Nat.%20Electron.&doi=10.1038%2Fs41928-023-00994-0&volume=6&pages=534-543&publication_year=2023&author=Chiu%2CYC)

[^24]: Jung, S. et al. A crossbar array of magnetoresistive memory devices for in-memory computing. *Nature* **601**, 211–216 (2022).

[Article](https://doi.org/10.1038%2Fs41586-021-04196-6) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2022Natur.601..211J) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BB38XhtVOlu7s%3D) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=35022590) [MATH](http://www.emis.de/MATH-item?0841.47023) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20crossbar%20array%20of%20magnetoresistive%20memory%20devices%20for%20in-memory%20computing&journal=Nature&doi=10.1038%2Fs41586-021-04196-6&volume=601&pages=211-216&publication_year=2022&author=Jung%2CS)

[^25]: Wen, T.-H. et al. 34.8 A 22nm 16Mb floating-point ReRAM compute-in-memory macro with 31.2TFLOPS/W for AI edge devices. In *Proc. 2024 IEEE International Solid-State Circuits Conference (ISSCC)* 580–582 (IEEE, 2024).

[^26]: Chang, M. et al. A 40nm 60.64TOPS/W ECC-capable compute-in-memory/digital 2.25MB/768KB RRAM/SRAM system with embedded cortex M3 microprocessor for edge recommendation systems. In *Proc. 2022 IEEE International Solid-State Circuits Conference (ISSCC)* 1–3 (IEEE, 2022).

[^27]: Wan, W. et al. A compute-in-memory chip based on resistive random-access memory. *Nature* **608**, 504–512 (2022).

[Article](https://doi.org/10.1038%2Fs41586-022-04992-8) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2022Natur.608..504W) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BB38XitFGls77N) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=35978128) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC9385482) [MATH](http://www.emis.de/MATH-item?1404.35333) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20compute-in-memory%20chip%20based%20on%20resistive%20random-access%20memory&journal=Nature&doi=10.1038%2Fs41586-022-04992-8&volume=608&pages=504-512&publication_year=2022&author=Wan%2CW)

[^28]: Hung, J. M. et al. A four-megabit compute-in-memory macro with eight-bit precision based on CMOS and resistive random-access memory for AI edge devices. *Nat. Electron.* **4**, 921–930 (2021).

[Article](https://doi.org/10.1038%2Fs41928-021-00676-9) [MATH](http://www.emis.de/MATH-item?0315.02007) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20four-megabit%20compute-in-memory%20macro%20with%20eight-bit%20precision%20based%20on%20CMOS%20and%20resistive%20random-access%20memory%20for%20AI%20edge%20devices&journal=Nat.%20Electron.&doi=10.1038%2Fs41928-021-00676-9&volume=4&pages=921-930&publication_year=2021&author=Hung%2CJM)

[^29]: Hung, J.-M. 8-b precision 8-Mb ReRAM compute-in-memory macro using direct-current-free time-domain readout scheme for AI edge devices. *IEEE J. Solid-State Circuits* **58**, 303–315 (2022).

[Article](https://doi.org/10.1109%2FJSSC.2022.3200515) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2023IJSSC..58..303H) [MATH](http://www.emis.de/MATH-item?1005.94517) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=8-b%20precision%208-Mb%20ReRAM%20compute-in-memory%20macro%20using%20direct-current-free%20time-domain%20readout%20scheme%20for%20AI%20edge%20devices&journal=IEEE%20J.%20Solid-State%20Circuits&doi=10.1109%2FJSSC.2022.3200515&volume=58&pages=303-315&publication_year=2022&author=Hung%2CJ-M)

[^30]: Chiu, Y.-C. et al. A 22nm 4Mb STT-MRAM data-encrypted near-memory computation macro with a 192GB/s read-and-decryption bandwidth and 25.1-55.1TOPS/W 8b MAC for AI operations. In *Proc. 2022 IEEE International Solid-State Circuits Conference (ISSCC)* 178–180 (IEEE, 2022).

[^31]: Spetalnick, S. D. et al. A 40nm 64kb 26.56TOPS/W 2.37Mb/mm <sup>2</sup> RRAM binary/compute-in-memory macro with 4.23x improvement in density and >75% use of sensing dynamic range. In *Proc. 2022 IEEE International Solid-State Circuits Conference (ISSCC)* 1–3 (IEEE, 2022).

[^32]: Yoon, J.-H. et al. A 40nm 100Kb 118.44TOPS/W ternary-weight compute-in-memory RRAM macro with voltage-sensing read and write verification for reliable multi-bit RRAM operation. In *Proc. 2021 IEEE Custom Integrated Circuits Conference (CICC)* 1–2 (IEEE, 2022).

[^33]: Khwa, W. S. et al. MLC PCM techniques to improve nerual network inference retention time by 105X and reduce accuracy degradation by 10.8X. In *Proc. 2021 Symposium on VLSI Technology* 1–2 (IEEE, 2021).

[^34]: Xue, C.-X. et al. 15.4 A 22nm 2Mb ReRAM compute-in-memory macro with 121-28TOPS/W for multibit MAC computing for tiny AI edge devices. In *Proc. 2020 IEEE International Solid-State Circuits Conference (ISSCC)* 244–246 (IEEE, 2020).

[^35]: Xue, C.-X. et al. 24.1 A 1Mb multibit ReRAM computing-in-memory macro with 14.6ns parallel MAC computing time for CNN based AI edge processors. In *Proc. 2019 IEEE International Solid-State Circuits Conference (ISSCC)* 388–390 (IEEE, 2019).

[^36]: Xue, C.-X. et al. A CMOS-integrated compute-in-memory macro based on resistive random-access memory for AI edge devices. *Nat. Electron.* **4**, 81–90 (2020).

[Article](https://doi.org/10.1038%2Fs41928-020-00505-5) [MATH](http://www.emis.de/MATH-item?1326.91013) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20CMOS-integrated%20compute-in-memory%20macro%20based%20on%20resistive%20random-access%20memory%20for%20AI%20edge%20devices&journal=Nat.%20Electron.&doi=10.1038%2Fs41928-020-00505-5&volume=4&pages=81-90&publication_year=2020&author=Xue%2CC-X)

[^37]: Chen, W.-H. et al. A 65nm 1Mb nonvolatile computing-in-memory ReRAM macro with sub-16ns multiply-and-accumulate for binary DNN AI edge processors. In *Proc. 2018 IEEE International Solid-State Circuits Conference (ISSCC)* 494–496 (IEEE, 2018).

[^38]: Chen, W. H. et al. CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors. *Nat. Electron.* **2**, 420–428 (2019).

[Article](https://doi.org/10.1038%2Fs41928-019-0288-0) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC1MXhs1Gisr3K) [MATH](http://www.emis.de/MATH-item?1418.62109) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=CMOS-integrated%20memristive%20non-volatile%20computing-in-memory%20for%20AI%20edge%20processors&journal=Nat.%20Electron.&doi=10.1038%2Fs41928-019-0288-0&volume=2&pages=420-428&publication_year=2019&author=Chen%2CWH)

[^39]: Mochida, R. et al. A 4M synapses integrated analog ReRAM based 66.5 TOPS/W neural-network processor with cell current controlled writing and flexible network architecture. In *Proc. 2018 IEEE Symposium on VLSI Technology* 175–176 (IEEE, 2018).

[^40]: Wan, W. et al. 33.1 A 74 TMACS/W CMOS-RRAM neurosynaptic core with dynamically reconfigurable dataflow and in-situ transposable weights for probabilistic graphical models. In *Proc. 2020 IEEE International Solid-State Circuits Conference (ISSCC)* 498–500 (IEEE, 2020).

[^41]: Liu, Q. et al. 33.2 A fully integrated analog ReRAM based 78.4TOPS/W compute-in-memory chip with fully parallel MAC computing. In *Proc. 2020 IEEE International Solid-State Circuits Conference (ISSCC)* 500–502 (IEEE, 2020).

[^42]: Cai, F. et al. A fully integrated reprogrammable memristor–CMOS system for efficient multiply–accumulate operations. *Nat. Electron.* **2**, 290–299 (2019).

[Article](https://doi.org/10.1038%2Fs41928-019-0270-x) [CAS](https://www.nature.com/articles/cas-redirect/1:CAS:528:DC%2BC1MXhtlOlsLjP) [MATH](http://www.emis.de/MATH-item?1423.93341) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20fully%20integrated%20reprogrammable%20memristor%E2%80%93CMOS%20system%20for%20efficient%20multiply%E2%80%93accumulate%20operations&journal=Nat.%20Electron.&doi=10.1038%2Fs41928-019-0270-x&volume=2&pages=290-299&publication_year=2019&author=Cai%2CF)

[^43]: Li, C. et al. Analogue signal and image processing with large memristor crossbars. *Nat. Electron.* **1**, 52–59 (2018).

[Article](https://doi.org/10.1038%2Fs41928-017-0002-z) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2018btnd.book.....L) [MATH](http://www.emis.de/MATH-item?1424.05093) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Analogue%20signal%20and%20image%20processing%20with%20large%20memristor%20crossbars&journal=Nat.%20Electron.&doi=10.1038%2Fs41928-017-0002-z&volume=1&pages=52-59&publication_year=2018&author=Li%2CC)

[^44]: Ielmini, D. & Wong, H. S. P. In-memory computing with resistive switching devices. *Nat. Electron.* **1**, 333–343 (2018).

[Article](https://doi.org/10.1038%2Fs41928-018-0092-2) [MATH](http://www.emis.de/MATH-item?1105.60060) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=In-memory%20computing%20with%20resistive%20switching%20devices&journal=Nat.%20Electron.&doi=10.1038%2Fs41928-018-0092-2&volume=1&pages=333-343&publication_year=2018&author=Ielmini%2CD&author=Wong%2CHSP)

[^45]: Chou, C.-C. et al. A 22nm 96KX144 RRAM macro with a self-tracking reference and a low ripple charge pump to achieve a configurable read window and a wide operating voltage range. In *Proc. 2020 IEEE Symposium on VLSI Circuits* 1–2 (IEEE, 2020).

[^46]: Boybat, I. et al. Neuromorphic computing with multi-memristive synapses. *Nat. Commun.* **9**, 2514 (2018).

[Article](https://doi.org/10.1038%2Fs41467-018-04933-y) [ADS](http://adsabs.harvard.edu/cgi-bin/nph-data_query?link_type=ABSTRACT&bibcode=2018NatCo...9.2514B) [PubMed](http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&db=PubMed&dopt=Abstract&list_uids=29955057) [PubMed Central](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC6023896) [MATH](http://www.emis.de/MATH-item?1442.49037) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Neuromorphic%20computing%20with%20multi-memristive%20synapses&journal=Nat.%20Commun.&doi=10.1038%2Fs41467-018-04933-y&volume=9&publication_year=2018&author=Boybat%2CI)

[^47]: Le Gallo, M. et al. Mixed-precision in-memory computing. *Nat. Electron.* **1**, 246–253 (2018).

[Article](https://doi.org/10.1038%2Fs41928-018-0054-8) [MATH](http://www.emis.de/MATH-item?07947383) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Mixed-precision%20in-memory%20computing&journal=Nat.%20Electron.&doi=10.1038%2Fs41928-018-0054-8&volume=1&pages=246-253&publication_year=2018&author=Gallo%2CM)

[^48]: Qu, Z., Zhou, Z., Cheng, Y. & Thiele, L. Adaptive loss-aware quantization for multi-bit networks. In *Proc. 2020 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)* 7985–7994 (Computer Vision Foundation, 2020).

[^49]: Mishra, A. & Marr, D. Apprentice: using knowledge distillation techniques to improve low-precision network accuracy. In *Proc. Sixth International Conference on Learning Representations* (ICLR, 2018).

[^50]: Chu, T. et al. Mixed-precision quantized neural networks with progressively decreasing bitwidth. *Pattern Recognit.* **111**, 107647 (2021).

[Article](https://doi.org/10.1016%2Fj.patcog.2020.107647) [MATH](http://www.emis.de/MATH-item?1543.62216) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Mixed-precision%20quantized%20neural%20networks%20with%20progressively%20decreasing%20bitwidth&journal=Pattern%20Recognit.&doi=10.1016%2Fj.patcog.2020.107647&volume=111&publication_year=2021&author=Chu%2CT)

[^51]: Lecun, Y. et al. Gradient-based learning applied to document recognition. *Proc. IEEE* **86**, 2278–2324 (1998).

[Article](https://doi.org/10.1109%2F5.726791) [MATH](http://www.emis.de/MATH-item?0936.92008) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Gradient-based%20learning%20applied%20to%20document%20recognition&journal=Proc.%20IEEE&doi=10.1109%2F5.726791&volume=86&pages=2278-2324&publication_year=1998&author=Lecun%2CY)

[^52]: Krizhevsky, A. *Learning Multiple Layers of Features from Tiny Images*. Master’s thesis, Univ. Toronto (2009).

[^53]: Deng, J. et al. ImageNet: a large-scale hierarchical image database. In *Proc. 2009 IEEE Conference on Computer Vision and Pattern Recognition* 248–255 (IEEE, 2009).

[^54]: Houshmand, P. et al. Opportunities and limitations of emerging analog in-memory compute DNN architectures. In *Proc. 2020 IEEE International Electron Devices Meeting (IEDM)* 29.1.1–29.1.4 (IEEE, 2020).

[^55]: Shamsoshoara, A. et al. The FLAME dataset: Aerial Imagery Pile burn detection using drones (UAVs). IEEE DataPort (2020).

[^56]: Warden, P. Speech commands: a dataset for limited-vocabulary speech recognition. Preprint at [https://arxiv.org/abs/1804.03209](https://arxiv.org/abs/1804.03209) (2018).

[^57]: Chowdhery, A. et al. Visual wake words dataset. Preprint at [https://arxiv.org/abs/1906.05721](https://arxiv.org/abs/1906.05721) (2019).

[^58]: Markus, N. et al. A white paper on neural network quantization. Preprint at [https://arxiv.org/abs/2106.08295](https://arxiv.org/abs/2106.08295) (2021).

[^59]: Jacob, B. et al. Quantization and training of neural networks for efficient integer-arithmetic-only inference. In *Proc. Conference on Computer Vision and Pattern Recognition (CVPR)* 2704–2713 (Computer Vision Foundation, 2018).

[^60]: Sun, S., Bai, J., Shi, Z., Zhao, W. & Kang, W. CIM <sup>2</sup> PQ: an arraywise and hardware-friendly mixed precision quantization method for analog computing-in-memory. *IEEE Trans. Comput.-Aided Des. Integr. Circuits Syst.* **43**, 2084–2097 (2024).

[Article](https://doi.org/10.1109%2FTCAD.2024.3358609) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=CIM2PQ%3A%20an%20arraywise%20and%20hardware-friendly%20mixed%20precision%20quantization%20method%20for%20analog%20computing-in-memory&journal=IEEE%20Trans.%20Comput.-Aided%20Des.%20Integr.%20Circuits%20Syst.&doi=10.1109%2FTCAD.2024.3358609&volume=43&pages=2084-2097&publication_year=2024&author=Sun%2CS&author=Bai%2CJ&author=Shi%2CZ&author=Zhao%2CW&author=Kang%2CW)

[^61]: Chen, Y.-W. et al. SUN: dynamic hybrid-precision SRAM-based CIM accelerator with high macro utilization using structured pruning mixed-precision networks. *IEEE Trans. Comput.-Aided Des. Integr. Circuits Syst.* **43**, 2163–2176 (2024).

[Article](https://doi.org/10.1109%2FTCAD.2024.3358583) [MATH](http://www.emis.de/MATH-item?1537.76142) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=SUN%3A%20dynamic%20hybrid-precision%20SRAM-based%20CIM%20accelerator%20with%20high%20macro%20utilization%20using%20structured%20pruning%20mixed-precision%20networks&journal=IEEE%20Trans.%20Comput.-Aided%20Des.%20Integr.%20Circuits%20Syst.&doi=10.1109%2FTCAD.2024.3358583&volume=43&pages=2163-2176&publication_year=2024&author=Chen%2CY-W)

[^62]: Agrawal, A. et al. A 7nm 4-core AI chip with 25.6TFLOPS hybrid FP8 training, 102.4TOPS INT4 inference and workload-aware throttling. In *Proc. 2021 IEEE International Solid-State Circuits Conference (ISSCC)* 144–145 (IEEE, 2021).

[^63]: Wang, J. et al. A compute SRAM with bit-serial integer/floating-point operations for programmable in-memory vector acceleration. In *Proc. 2019 IEEE International Solid-State Circuits Conference (ISSCC)* 224–225 (IEEE, 2019).
