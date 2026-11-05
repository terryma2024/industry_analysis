---
source_id: "SRC-ic-061"
title: "A 64-core mixed-signal in-memory compute chip based on phase-change memory"
source_type: "research_paper"
publisher: "Nature Electronics / IBM"
source_date: "2023-08-10"
url: "https://www.nature.com/articles/s41928-023-01010-1"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-09-22T02:35:06+00:00"
tags:
  - raw/source
  - source-type/research-paper
  - evidence/s
aliases:
  - SRC-ic-061
---
# A 64-core mixed-signal in-memory compute chip based on phase-change memory

## Abstract

Analogue in-memory computing (AIMC) with resistive memory devices could reduce the latency and energy consumption of deep neural network inference tasks by directly performing computations within memory. However, to achieve end-to-end improvements in latency and energy consumption, AIMC must be combined with on-chip digital operations and on-chip communication. Here we report a multicore AIMC chip designed and fabricated in 14 nm complementary metal–oxide–semiconductor technology with backend-integrated phase-change memory. The fully integrated chip features 64 AIMC cores interconnected via an on-chip communication network. It also implements the digital activation functions and additional processing involved in individual convolutional layers and long short-term memory units. With this approach, we demonstrate near-software-equivalent inference accuracy with ResNet and long short-term memory networks, while implementing all the computations associated with the weight layers and the activation functions on the chip. For 8-bit input/output matrix–vector multiplications, in the four-phase (high-precision) or one-phase (low-precision) operational read mode, the chip can achieve a maximum throughput of 16.1 or 63.1 tera-operations per second at an energy efficiency of 2.48 or 9.76 tera-operations per second per watt, respectively.

This is a preview of subscription content, [access via your institution](https://wayf.springernature.com/?redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41928-023-01010-1)

## Access options

[Access through your institution](https://wayf.springernature.com/?redirect_uri=https%3A%2F%2Fwww.nature.com%2Farticles%2Fs41928-023-01010-1)

Buy this article

- Purchase on SpringerLink
- Instant access to the full article PDF.

39,95 €

Prices may be subject to local taxes which are calculated during checkout

![](https://media.springernature.com/m312/springer-static/image/art%3A10.1038%2Fs41928-023-01010-1/MediaObjects/41928_2023_1010_Fig1_HTML.png?as=webp)

Fig. 1: IBM HERMES project chip overview.

![](https://media.springernature.com/m312/springer-static/image/art%3A10.1038%2Fs41928-023-01010-1/MediaObjects/41928_2023_1010_Fig2_HTML.png?as=webp)

Fig. 2: MVM characterization.

![](https://media.springernature.com/m312/springer-static/image/art%3A10.1038%2Fs41928-023-01010-1/MediaObjects/41928_2023_1010_Fig3_HTML.png?as=webp)

Fig. 3: ResNet-9 on CIFAR-10 measurement results.

![](https://media.springernature.com/m312/springer-static/image/art%3A10.1038%2Fs41928-023-01010-1/MediaObjects/41928_2023_1010_Fig4_HTML.png?as=webp)

Fig. 4: LSTM for character prediction measurement results.

![](https://media.springernature.com/m312/springer-static/image/art%3A10.1038%2Fs41928-023-01010-1/MediaObjects/41928_2023_1010_Fig5_HTML.png?as=webp)

Fig. 5: LSTM for image caption generation measurement results.

## Data availability

The data that support the plots within this paper and other findings of this study are available from the corresponding authors upon reasonable request.

## References

## Acknowledgements

We thank G. W. Burr, M. Bühler, T. Maurer, A. Müller, Y. Kohda, K. Hosakawa, S. Ambrogio, F. L. Lie, F. Liu, T. Levin and T. Gordon for assistance with the chip design; A. Okazaki, H. Mori and M. Bergendahl for assistance with the chip packaging; J. F. Mas, G. Cristiano and J. Paret for chip testing and simulation; F. Odermatt, I. Boybat, S. R. Nandakumar, C. Piveteau, C. Lammie and H. Benmeziane for help with the network deployment on the chip; and A. Pantazi, R. Haas, A. Curioni, S. Tsai, W. Haensch, J. Burns, R. Divakaruni and M. Khare for managerial support. We would also like to thank L. Benini and B. Rajendran for their support with supervising the students. This work was supported by the IBM Research AI Hardware Center. A. Sebastian acknowledges partial funding from the European Research Council (ERC) under the European Union’s Horizon 2020 research and innovation programme (grant agreement nos. 682675 and 966764).

## Ethics declarations

### Competing interests

The authors declare no competing interests.

## Peer review

### Peer review information

*Nature Electronics* thanks the anonymous reviewers for their contribution to the peer review of this work.

## Additional information

**Publisher’s note** Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Extended data

### Extended Data Fig. 1 Digital communication fabric.

**a**, Schematic of link controller. The dotted line refers to the core boundary. The transmitter-side link controller prepends a preamble to the payload being sent on the links. The preamble contains information to uniquely identify a routing path for a particular type of payload. If the receiving core is enabled to receive data from the transmitting core in the routing table, the link controller samples the incoming data. Furthermore, the link controller in the transmitting and receiving cores can select a portion of the payload according to another set of routing registers. **b**, Possible link connections for Core(3,5) and Core(4,5), where the notation Core(*r*,*c*) refers to the core located at row *r* and column *c* in Fig. [1b](https://www.nature.com/articles/s41928-023-01010-1#Fig1). **c**, Link connections for the entire chip (available connections are denoted in green color). The RX and TX connections for Core(3,5) and Core(4,5) shown in **b** are indicated. **d**, Link characterization results on one chip for communicating data from the LDPU of a core to the LDPU of another core. A payload of 255 bytes is sent by the transmitter core and an error is triggered if at least one byte of the payload received in the LDPU of the receiver core does not match with the original payload. All links with a Manhattan distance of 1 or 2 cores show no errors when run at 100 MHz, and 98% of them at 400 MHz. Links with longer Manhattan distances show more errors potentially due to attenuation from longer-distance routing metal wires due to parasitics. The issue can be mitigated in a future design by placement of buffers at reasonable distances along the wires, or by employing a core connectivity matrix that does not rely on long distance links. All the links used in the experimental demonstrations shown in this work have a Manhattan distance of 1 core and are fully working at 400 MHz.

### Extended Data Fig. 2 PCM crossbar array.

**a**, Schematic of 8T4R unit-cell. The top electrodes of the conductance pairs of each polarity connect to separate bit lines \\(B{L}\_{m}^{+}\\), \\(B{L}\_{m}^{-}\\) and the sources of their lower access-transistors connect to separate source lines \\(S{L}\_{n}^{+}\\), \\(S{L}\_{n}^{-}\\). Thus, the devices in a conductance pair are weighted with equal significance and the total conductance per unit-cell becomes: \\(\\left({g}\_{1}^{+}+{g}\_{2}^{+}\\right)-\\left({g}\_{1}^{-}+{g}\_{2}^{-}\\right)\\). **b**, Schematic of PCM crossbar array. To program the PCM devices, the dedicated per-core programming FSM instructs the diagonal selection decoder to enable one diagonal of cells that contains the devices that are to be programmed. The diagonal selection decoder controls the \\({SEL}\_{m,n}^{1}\\) and \\({SEL}\_{m,n}^{2}\\) signals in the unit-cell, which are routed diagonally throughout the array. The selected devices are programmed by the current-steering DAC-based programming units located on top of the PCM array. To perform an MVM, the 256 inputs to the crossbar array (*I* *N* <sub>0</sub>  −  *I* *N* <sub>255</sub>) are applied via the red source lines (SLs) to the 8T4R cells. The resulting bit line (BL) currents are summed up on the blue wires and read by the ADCs that flank the crossbar array on the left and right. **c**, Layout of one ADC. The block diagram that is shown below the layout illustrates the various components of the ADC, namely, the read voltage regulator, the current-to-frequency converter, and the 2 × 12-bit ripple counter.

### Extended Data Fig. 3 PCM device.

**a**, A typical programming curve indicating the programmed device conductance as a function of the programming current. The device conductance is determined by the phase configuration within the PCM device and in particular, the size of the amorphous region. Data are presented as mean values + / − one standard deviation over 10 repeated measurements on a single device. **b**, Low-angle annular darkfield (LAADF) scanning transmission electron microscope (STEM) image of a fully RESET PCM device showing a substantially large amorphous region that fully blocks the bottom electrode. LAADF enables the imaging of the amorphous region with high resolution. **c**, LAADF of a partially RESET PCM device showing a much smaller amorphous region. The synaptic weights are stored in an analog manner in terms of these phase configurations and the resulting conductance values.

### Extended Data Fig. 4 Input modulation modes for MVM.

**a**, Full array read procedure for MVMs showing the connection between ADC, unit-cells, and input modulator switches. Signals PP and PN connect the positive source lines \\(S{L}\_{1:N}^{+}\\) to the positive potential *V* <sup>+</sup> and negative potential *V* <sup>−</sup>, respectively. For NP and NN it is vice versa. **b**, 1-phase modulation mode. Inputs of positive and negative polarity are applied to weights of positive and negative polarity in one modulation cycle *T* <sub>PWM</sub>. **c**, 4-phase modulation mode. Inputs of positive and negative polarity are applied individually to weights of positive and negative polarity in four modulation cycles.

### Extended Data Fig. 5 Weight programming procedure.

**a**, Crossbar array during programming. **b**, Proposed TDP algorithm to program a target conductance value *G* on a unit-cell. **c**, Weight error comparison between TDP of this work and previous approaches. TDP - Max-fill refers to programming the two devices with iterative programming up to the ODP \\({G}\_{\\max }\\), as proposed in Ref. [^31]. Due to the wide SET distribution shown in Fig. [2a](https://www.nature.com/articles/s41928-023-01010-1#Fig2), some devices in the core either cannot achieve \\({G}\_{\\max }\\), or conversely could be programmed to much higher conductance values than \\({G}\_{\\max }\\). Therefore, the latter approach leads to programming inaccuracies resulting from either under-utilizing the conductance range of individual devices or from devices that cannot reach \\({G}\_{\\max }\\). The proposed TDP algorithm solves this issue by using the readout SET conductance of the devices of the unit-cell to map the weight.

### Extended Data Fig. 6 Area and power splits.

**a**, Area breakdown of the main chip components. **b**, Static power consumed by the different components of the chip measured for the operation of the LSTM unit of the image caption generation task (4 core rows and GDPU active).

**Extended Data Table 1 Summary of IBM HERMES Project Chip specifications**

**Extended Data Table 2 Comparison of IBM HERMES Project Chip with other multi-core AIMC chips demonstrating neural network inference**

## Supplementary information

### Supplementary Video 1 (download MP4 )

Live demonstration of image captioning using the IBM HERMES project chip.

## Rights and permissions

Springer Nature or its licensor (e.g. a society or other partner) holds exclusive rights to this article under a publishing agreement with the author(s) or other rightsholder(s); author self-archiving of the accepted manuscript version of this article is solely governed by the terms of such publishing agreement and applicable law.

[^1]: Murmann, B. Mixed-signal computing for deep neural network inference. *IEEE Trans. Very Large Scale Integr. (VLSI) Syst.* **29**, 3–13 (2021).

[Article](https://doi.org/10.1109%2FTVLSI.2020.3020286) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Mixed-signal%20computing%20for%20deep%20neural%20network%20inference&journal=IEEE%20Trans.%20Very%20Large%20Scale%20Integr.%20%28VLSI%29%20Syst.&doi=10.1109%2FTVLSI.2020.3020286&volume=29&pages=3-13&publication_year=2021&author=Murmann%2CB)

[^2]: Shafiee, A. et al. ISAAC: a convolutional neural network accelerator with in-situ analog arithmetic in crossbars. in *2016 ACM/IEEE 43rd Annual International Symposium on Computer Architecture (ISCA)* 14–26 (IEEE Press, 2016).

[^3]: Sebastian, A., Le Gallo, M., Khaddam-Aljameh, R. & Eleftheriou, E. Memory devices and applications for in-memory computing. *Nat. Nanotechnol.* **15**, 529–544 (2020).

[Article](https://doi.org/10.1038%2Fs41565-020-0655-z) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Memory%20devices%20and%20applications%20for%20in-memory%20computing&journal=Nat.%20Nanotechnol.&doi=10.1038%2Fs41565-020-0655-z&volume=15&pages=529-544&publication_year=2020&author=Sebastian%2CA&author=Gallo%2CM&author=Khaddam-Aljameh%2CR&author=Eleftheriou%2CE)

[^4]: Yu, S., Jiang, H., Huang, S., Peng, X. & Lu, A. Compute-in-memory chips for deep learning: recent trends and prospects. *IEEE Circuits Syst. Magazine* **21**, 31–56 (2021).

[Article](https://doi.org/10.1109%2FMCAS.2021.3092533) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Compute-in-memory%20chips%20for%20deep%20learning%3A%20recent%20trends%20and%20prospects&journal=IEEE%20Circuits%20Syst.%20Magazine&doi=10.1109%2FMCAS.2021.3092533&volume=21&pages=31-56&publication_year=2021&author=Yu%2CS&author=Jiang%2CH&author=Huang%2CS&author=Peng%2CX&author=Lu%2CA)

[^5]: Lanza, M. et al. Memristive technologies for data storage, computation, encryption, and radio-frequency communication. *Science* **376**, eabj9979 (2022).

[Article](https://doi.org/10.1126%2Fscience.abj9979) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Memristive%20technologies%20for%20data%20storage%2C%20computation%2C%20encryption%2C%20and%20radio-frequency%20communication&journal=Science&doi=10.1126%2Fscience.abj9979&volume=376&publication_year=2022&author=Lanza%2CM)

[^6]: Wang, Z. et al. Resistive switching materials for information processing. *Nat. Rev. Mater.* **5**, 173–195 (2020).

[Article](https://doi.org/10.1038%2Fs41578-019-0159-3) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Resistive%20switching%20materials%20for%20information%20processing&journal=Nat.%20Rev.%20Mater.&doi=10.1038%2Fs41578-019-0159-3&volume=5&pages=173-195&publication_year=2020&author=Wang%2CZ)

[^7]: Xiao, T. P., Bennett, C. H., Feinberg, B., Agarwal, S. & Marinella, M. J. Analog architectures for neural network acceleration based on non-volatile memory. *Appl. Phys. Rev.* **7**, 031301 (2020).

[Article](https://doi.org/10.1063%2F1.5143815) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Analog%20architectures%20for%20neural%20network%20acceleration%20based%20on%20non-volatile%20memory&journal=Appl.%20Phys.%20Rev.&doi=10.1063%2F1.5143815&volume=7&publication_year=2020&author=Xiao%2CTP&author=Bennett%2CCH&author=Feinberg%2CB&author=Agarwal%2CS&author=Marinella%2CMJ)

[^8]: Yu, S. et al. Binary neural network with 16 Mb RRAM macro chip for classification and online training. in *2016 IEEE International Electron Devices Meeting (IEDM)* 16.2.1–16.2.4 (IEEE, 2016).

[^9]: Hu, M. et al. Memristor-based analog computation and neural network classification with a dot product engine. *Adv. Mater.* **30**, 1705914 (2018).

[Article](https://doi.org/10.1002%2Fadma.201705914) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Memristor-based%20analog%20computation%20and%20neural%20network%20classification%20with%20a%20dot%20product%20engine&journal=Adv.%20Mater.&doi=10.1002%2Fadma.201705914&volume=30&publication_year=2018&author=Hu%2CM)

[^10]: Tsai, H. et al. Inference of long-short term memory networks at software-equivalent accuracy using 2.5m analog phase change memory devices. in *2019 Symposium on VLSI Technology* T82–T83 (IEEE, 2019).

[^11]: Yao, P. et al. Fully hardware-implemented memristor convolutional neural network. *Nature* **577**, 641–646 (2020).

[Article](https://doi.org/10.1038%2Fs41586-020-1942-4) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Fully%20hardware-implemented%20memristor%20convolutional%20neural%20network&journal=Nature&doi=10.1038%2Fs41586-020-1942-4&volume=577&pages=641-646&publication_year=2020&author=Yao%2CP)

[^12]: Joshi, V. et al. Accurate deep neural network inference using computational phase-change memory. *Nat. Commun.* **11**, 2473 (2020).

[Article](https://doi.org/10.1038%2Fs41467-020-16108-9) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Accurate%20deep%20neural%20network%20inference%20using%20computational%20phase-change%20memory&journal=Nat.%20Commun.&doi=10.1038%2Fs41467-020-16108-9&volume=11&publication_year=2020&author=Joshi%2CV)

[^13]: Biswas, A. & Chandrakasan, A. P. CONV-SRAM: an energy-efficient SRAM with in-memory dot-product computation for low-power convolutional neural networks. *IEEE J. Solid-State Circuits* **54**, 217–230 (2019).

[Article](https://doi.org/10.1109%2FJSSC.2018.2880918) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=CONV-SRAM%3A%20an%20energy-efficient%20SRAM%20with%20in-memory%20dot-product%20computation%20for%20low-power%20convolutional%20neural%20networks&journal=IEEE%20J.%20Solid-State%20Circuits&doi=10.1109%2FJSSC.2018.2880918&volume=54&pages=217-230&publication_year=2019&author=Biswas%2CA&author=Chandrakasan%2CAP)

[^14]: Merrikh-Bayat, F. et al. High-performance mixed-signal neurocomputing with nanoscale floating-gate memory cell arrays. *IEEE Trans. Neural Netw. Learn. Syst.* **29**, 4782–4790 (2018).

[Article](https://doi.org/10.1109%2FTNNLS.2017.2778940) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=High-performance%20mixed-signal%20neurocomputing%20with%20nanoscale%20floating-gate%20memory%20cell%20arrays&journal=IEEE%20Trans.%20Neural%20Netw.%20Learn.%20Syst.&doi=10.1109%2FTNNLS.2017.2778940&volume=29&pages=4782-4790&publication_year=2018&author=Merrikh-Bayat%2CF)

[^15]: Cai, F. et al. A fully integrated reprogrammable memristor–CMOS system for efficient multiply–accumulate operations. *Nat. Electron.* **2**, 290–299 (2019).

[Article](https://doi.org/10.1038%2Fs41928-019-0270-x) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20fully%20integrated%20reprogrammable%20memristor%E2%80%93CMOS%20system%20for%20efficient%20multiply%E2%80%93accumulate%20operations&journal=Nat.%20Electron.&doi=10.1038%2Fs41928-019-0270-x&volume=2&pages=290-299&publication_year=2019&author=Cai%2CF)

[^16]: Chen, W.-H. et al. CMOS-integrated memristive non-volatile computing-in-memory for AI edge processors. *Nat. Electron.* **2**, 420–428 (2019).

[Article](https://doi.org/10.1038%2Fs41928-019-0288-0) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=CMOS-integrated%20memristive%20non-volatile%20computing-in-memory%20for%20AI%20edge%20processors&journal=Nat.%20Electron.&doi=10.1038%2Fs41928-019-0288-0&volume=2&pages=420-428&publication_year=2019&author=Chen%2CW-H)

[^17]: Yin, S., Sun, X., Yu, S. & Seo, J.-S. High-throughput in-memory computing for binary deep neural networks with monolithically integrated RRAM and 90-nm CMOS. *IEEE Trans. Electron Devices* **67**, 4185–4192 (2020).

[Article](https://doi.org/10.1109%2FTED.2020.3015178) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=High-throughput%20in-memory%20computing%20for%20binary%20deep%20neural%20networks%20with%20monolithically%20integrated%20RRAM%20and%2090-nm%20CMOS&journal=IEEE%20Trans.%20Electron%20Devices&doi=10.1109%2FTED.2020.3015178&volume=67&pages=4185-4192&publication_year=2020&author=Yin%2CS&author=Sun%2CX&author=Yu%2CS&author=Seo%2CJ-S)

[^18]: Khaddam-Aljameh, R. et al. HERMES-Core—a 1.59-TOPS/mm <sup>2</sup> PCM on 14-nm CMOS in-memory compute core using 300-ps/LSB linearized CCO-based ADCs. *IEEE J. Solid-State Circuits* **57**, 1027–1038 (2022).

[Article](https://doi.org/10.1109%2FJSSC.2022.3140414) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=HERMES-Core%E2%80%94a%201.59-TOPS%2Fmm2%20PCM%20on%2014-nm%20CMOS%20in-memory%20compute%20core%20using%20300-ps%2FLSB%20linearized%20CCO-based%20ADCs&journal=IEEE%20J.%20Solid-State%20Circuits&doi=10.1109%2FJSSC.2022.3140414&volume=57&pages=1027-1038&publication_year=2022&author=Khaddam-Aljameh%2CR)

[^19]: Deaville, P., Zhang, B. & Verma, N. A 22nm 128-kb MRAM row/column-parallel in-memory computing macro with memory-resistance boosting and multi-column ADC readout. in *2022 IEEE Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits)* 268–269 (IEEE, 2022).

[^20]: Khwa, W.-S. et al. A 40-nm, 2M-cell, 8b-precision, hybrid SLC-MLC PCM computing-in-memory macro with 20.5–65.0TOPS/W for tiny-Al edge devices. in *2022 IEEE International Solid-State Circuits Conference (ISSCC)* **65**, 1–3 (IEEE, 2022).

[^21]: Wan, W. et al. A compute-in-memory chip based on resistive random-access memory. *Nature* **608**, 504–512 (2022).

[Article](https://doi.org/10.1038%2Fs41586-022-04992-8) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20compute-in-memory%20chip%20based%20on%20resistive%20random-access%20memory&journal=Nature&doi=10.1038%2Fs41586-022-04992-8&volume=608&pages=504-512&publication_year=2022&author=Wan%2CW)

[^22]: Hung, J.-M. et al. A four-megabit compute-in-memory macro with eight-bit precision based on CMOS and resistive random-access memory for AI edge devices. *Nat. Electron.* **4**, 921–930 (2021).

[Article](https://doi.org/10.1038%2Fs41928-021-00676-9) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20four-megabit%20compute-in-memory%20macro%20with%20eight-bit%20precision%20based%20on%20CMOS%20and%20resistive%20random-access%20memory%20for%20AI%20edge%20devices&journal=Nat.%20Electron.&doi=10.1038%2Fs41928-021-00676-9&volume=4&pages=921-930&publication_year=2021&author=Hung%2CJ-M)

[^23]: Fick, L., Skrzyniarz, S., Parikh, M., Henry, M. B. & Fick, D. Analog matrix processor for edge AI real-time video analytics. in *2022 IEEE International Solid-State Circuits Conference (ISSCC)* **65**, 260–262 (IEEE, 2022).

[^24]: Jia, H. et al. Scalable and programmable neural network inference accelerator based on in-memory computing. *IEEE J. Solid-State Circuits* **57**, 198–211 (2022).

[Article](https://doi.org/10.1109%2FJSSC.2021.3119018) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Scalable%20and%20programmable%20neural%20network%20inference%20accelerator%20based%20on%20in-memory%20computing&journal=IEEE%20J.%20Solid-State%20Circuits&doi=10.1109%2FJSSC.2021.3119018&volume=57&pages=198-211&publication_year=2022&author=Jia%2CH)

[^25]: Narayanan, P. et al. Fully on-chip MAC at 14 nm enabled by accurate row-wise programming of PCM-based weights and parallel vector-transport in duration-format. *IEEE Trans. Electron Devices* **68**, 6629–6636 (2021).

[Article](https://doi.org/10.1109%2FTED.2021.3115993) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Fully%20on-chip%20MAC%20at%2014%E2%80%89nm%20enabled%20by%20accurate%20row-wise%20programming%20of%20PCM-based%20weights%20and%20parallel%20vector-transport%20in%20duration-format&journal=IEEE%20Trans.%20Electron%20Devices&doi=10.1109%2FTED.2021.3115993&volume=68&pages=6629-6636&publication_year=2021&author=Narayanan%2CP)

[^26]: Dazzi, M. et al. Efficient pipelined execution of CNNs based on in-memory computing and graph homomorphism verification. *IEEE Trans. Comput.* **70**, 922–935 (2021).

[Article](https://doi.org/10.1109%2FTC.2021.3073255) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=4267906) [MATH](http://www.emis.de/MATH-item?07497348) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Efficient%20pipelined%20execution%20of%20CNNs%20based%20on%20in-memory%20computing%20and%20graph%20homomorphism%20verification&journal=IEEE%20Trans.%20Comput.&doi=10.1109%2FTC.2021.3073255&volume=70&pages=922-935&publication_year=2021&author=Dazzi%2CM)

[^27]: Boybat, I. et al. Neuromorphic computing with multi-memristive synapses. *Nat. Commun.* **9**, 2514 (2018).

[Article](https://doi.org/10.1038%2Fs41467-018-04933-y) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Neuromorphic%20computing%20with%20multi-memristive%20synapses&journal=Nat.%20Commun.&doi=10.1038%2Fs41467-018-04933-y&volume=9&publication_year=2018&author=Boybat%2CI)

[^28]: Khaddam-Aljameh, R. et al. A multi-memristive unit-cell array with diagonal interconnects for in-memory computing. *IEEE Trans. Circuits Syst. II, Exp. Briefs* **68**, 3522–3526 (2021).

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20multi-memristive%20unit-cell%20array%20with%20diagonal%20interconnects%20for%20in-memory%20computing&journal=IEEE%20Trans.%20Circuits%20Syst.%20II%2C%20Exp.%20Briefs&volume=68&pages=3522-3526&publication_year=2021&author=Khaddam-Aljameh%2CR)

[^29]: Sarwat, S. G. et al. Mechanism and impact of bipolar current voltage asymmetry in computational phase-change memory. *Adv. Mater.* 2201238 (2022).

[^30]: Papandreou, N. et al. Programming algorithms for multilevel phase-change memory. in *IEEE International Symposium on Circuits and Systems (ISCAS)* 329–332 (IEEE, 2011).

[^31]: Le Gallo, M. et al. Precision of bit slicing with in-memory computing based on analog phase-change memory crossbars. *Neuromorp. Comput. Eng.* **2**, 014009 (2022).

[Article](https://doi.org/10.1088%2F2634-4386%2Fac4fb7) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Precision%20of%20bit%20slicing%20with%20in-memory%20computing%20based%20on%20analog%20phase-change%20memory%20crossbars&journal=Neuromorp.%20Comput.%20Eng.&doi=10.1088%2F2634-4386%2Fac4fb7&volume=2&publication_year=2022&author=Gallo%2CM)

[^32]: Ielmini, D., Sharma, D., Lavizzari, S. & Lacaita, A. Reliability impact of chalcogenide-structure relaxation in phase-change memory (PCM) cells, part I: experimental study. *IEEE Trans. Electron Devices* **56**, 1070–1077 (2009).

[Article](https://doi.org/10.1109%2FTED.2009.2016397) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Reliability%20impact%20of%20chalcogenide-structure%20relaxation%20in%20phase-change%20memory%20%28PCM%29%20cells%2C%20part%20I%3A%20experimental%20study&journal=IEEE%20Trans.%20Electron%20Devices&doi=10.1109%2FTED.2009.2016397&volume=56&pages=1070-1077&publication_year=2009&author=Ielmini%2CD&author=Sharma%2CD&author=Lavizzari%2CS&author=Lacaita%2CA)

[^33]: Le Gallo, M., Krebs, D., Zipoli, F., Salinga, M. & Sebastian, A. Collective structural relaxation in phase-change memory devices. *Adv. Electron. Mater.* **4**, 1700627 (2018).

[Article](https://doi.org/10.1002%2Faelm.201700627) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Collective%20structural%20relaxation%20in%20phase-change%20memory%20devices&journal=Adv.%20Electron.%20Mater.&doi=10.1002%2Faelm.201700627&volume=4&publication_year=2018&author=Gallo%2CM&author=Krebs%2CD&author=Zipoli%2CF&author=Salinga%2CM&author=Sebastian%2CA)

[^34]: Le Gallo, M., Sebastian, A., Cherubini, G., Giefers, H. & Eleftheriou, E. Compressed sensing with approximate message passing using in-memory computing. *IEEE Trans. Electron Devices* **65**, 4304–4312 (2018).

[Article](https://doi.org/10.1109%2FTED.2018.2865352) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Compressed%20sensing%20with%20approximate%20message%20passing%20using%20in-memory%20computing&journal=IEEE%20Trans.%20Electron%20Devices&doi=10.1109%2FTED.2018.2865352&volume=65&pages=4304-4312&publication_year=2018&author=Gallo%2CM&author=Sebastian%2CA&author=Cherubini%2CG&author=Giefers%2CH&author=Eleftheriou%2CE)

[^35]: Krizhevsky, A. *Learning Multiple Layers of Features from Tiny Images*. Tech. Rep. (2009).

[^36]: Marcus, M. P., Santorini, B. & Marcinkiewicz, M. A. Building a large annotated corpus of English: the Penn Treebank. *Comput. Linguist.* **19**, 313–330 (1993).

[Google Scholar](http://scholar.google.com/scholar_lookup?&title=Building%20a%20large%20annotated%20corpus%20of%20English%3A%20the%20Penn%20Treebank&journal=Comput.%20Linguist.&volume=19&pages=313-330&publication_year=1993&author=Marcus%2CMP&author=Santorini%2CB&author=Marcinkiewicz%2CMA)

[^37]: Rashtchian, C., Young, P., Hodosh, M. & Hockenmaier, J. Collecting image annotations using Amazon’s mechanical turk. in *Proc. NAACL HLT 2010 Workshop on Creating Speech and Language Data with Amazon’s Mechanical Turk* *CSLDAMT ’10* 139–147 (Association for Computational Linguistics, 2010).

[^38]: Rasch, M. J. et al. Hardware-aware training for large-scale and diverse deep learning inference workloads using in-memory computing-based accelerators. Preprint at *arXiv* [https://doi.org/10.48550/arXiv.2302.08469](https://doi.org/10.48550/arXiv.2302.08469) (2023).

[^39]: Rasch, M. J. et al. A flexible and fast pytorch toolkit for simulating training and inference on analog crossbar arrays. in *2021 IEEE 3rd International Conference on Artificial Intelligence Circuits and Systems (AICAS)* 1–4 (IEEE, 2021).

[^40]: Mujika, A., Meier, F. & Steger, A. Fast-slow recurrent neural networks. in *Advances in Neural Information Processing Systems* Vol. 30 (eds Guyon, I. et al.) (Curran Associates, 2017).

[^41]: Papineni, K., Roukos, S., Ward, T. & Zhu, W.-J. Bleu: a method for automatic evaluation of machine translation. in *Proc. 40th Annual Meeting on Association for Computational Linguistics, ACL ’02* 311–318 (Association for Computational Linguistics, 2002).

[^42]: Jain, S. et al. A heterogeneous and programmable compute-in-memory accelerator architecture for analog-AI using dense 2-D mesh. *IEEE Trans. Very Large Scale Integr. (VLSI) Syst.* **31**, 114–127 (2022).

[Article](https://doi.org/10.1109%2FTVLSI.2022.3221390) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20heterogeneous%20and%20programmable%20compute-in-memory%20accelerator%20architecture%20for%20analog-AI%20using%20dense%202-D%20mesh&journal=IEEE%20Trans.%20Very%20Large%20Scale%20Integr.%20%28VLSI%29%20Syst.&doi=10.1109%2FTVLSI.2022.3221390&volume=31&pages=114-127&publication_year=2022&author=Jain%2CS)

[^43]: Dazzi, M., Sebastian, A., Benini, L. & Eleftheriou, E. Accelerating inference of convolutional neural networks using in-memory computing. *Front. Comput. Neurosci.* **15**, 674154 (2021).

[Article](https://doi.org/10.3389%2Ffncom.2021.674154) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Accelerating%20inference%20of%20convolutional%20neural%20networks%20using%20in-memory%20computing&journal=Front.%20Comput.%20Neurosci.&doi=10.3389%2Ffncom.2021.674154&volume=15&publication_year=2021&author=Dazzi%2CM&author=Sebastian%2CA&author=Benini%2CL&author=Eleftheriou%2CE)

[^44]: Lin, P. et al. Three-dimensional memristor circuits as complex neural networks. *Nat. Electron.* **3**, 225–232 (2020).

[Article](https://doi.org/10.1038%2Fs41928-020-0397-9) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Three-dimensional%20memristor%20circuits%20as%20complex%20neural%20networks&journal=Nat.%20Electron.&doi=10.1038%2Fs41928-020-0397-9&volume=3&pages=225-232&publication_year=2020&author=Lin%2CP)

[^45]: Huo, Q. et al. A computing-in-memory macro based on three-dimensional resistive random-access memory. *Nat. Electron.* **5**, 469–477 (2022).

[Article](https://doi.org/10.1038%2Fs41928-022-00795-x) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20computing-in-memory%20macro%20based%20on%20three-dimensional%20resistive%20random-access%20memory&journal=Nat.%20Electron.&doi=10.1038%2Fs41928-022-00795-x&volume=5&pages=469-477&publication_year=2022&author=Huo%2CQ)

[^46]: He, K., Zhang, X., Ren, S. & Sun, J. Deep residual learning for image recognition. in *2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)* 770–778 (IEEE Computer Society, 2016).

[^47]: Devries, T. & Taylor, G. W. Improved regularization of convolutional neural networks with cutout. Preprint at *arXiv* [https://doi.org/10.48550/arXiv.1708.04552](https://doi.org/10.48550/arXiv.1708.04552) (2017).

[^48]: Nandakumar, S. R. et al. Phase-change memory models for deep learning training and inference. in *2019 26th IEEE International Conference on Electronics, Circuits and Systems (ICECS)* 727–730 (IEEE, 2019).

[^49]: Hochreiter, S. & Schmidhuber, J. Long short-term memory. *Neural Comput.* **9**, 1735–1780 (1997).

[Article](https://doi.org/10.1162%2Fneco.1997.9.8.1735) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Long%20short-term%20memory&journal=Neural%20Comput.&doi=10.1162%2Fneco.1997.9.8.1735&volume=9&pages=1735-1780&publication_year=1997&author=Hochreiter%2CS&author=Schmidhuber%2CJ)

[^50]: Srivastava, N., Hinton, G., Krizhevsky, A., Sutskever, I. & Salakhutdinov, R. Dropout: a simple way to prevent neural networks from overfitting. *J. Mach. Learn. Res.* **15**, 1929–1958 (2014).

[MathSciNet](http://www.ams.org/mathscinet-getitem?mr=3231592) [MATH](http://www.emis.de/MATH-item?1318.68153) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Dropout%3A%20a%20simple%20way%20to%20prevent%20neural%20networks%20from%20overfitting&journal=J.%20Mach.%20Learn.%20Res.&volume=15&pages=1929-1958&publication_year=2014&author=Srivastava%2CN&author=Hinton%2CG&author=Krizhevsky%2CA&author=Sutskever%2CI&author=Salakhutdinov%2CR)

[^51]: Kingma, D. P. & Ba, J. Adam: a method for stochastic optimization. in *3rd International Conference on Learning Representations, ICLR 2015* (2015).

[^52]: Vinyals, O., Toshev, A., Bengio, S. & Erhan, D. Show and tell: a neural image caption generator. in *2015 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)* 3156–3164 (IEEE, 2015).

[^53]: Szegedy, C., Vanhoucke, V., Ioffe, S., Shlens, J. & Wojna, Z. Rethinking the inception architecture for computer vision. in *2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR)* 2818–2826 (IEEE, 2016).

[^54]: Russakovsky, O. et al. Imagenet large scale visual recognition challenge. *Int. J. Comput. Vision* **115**, 211–252 (2015).

[Article](https://link.springer.com/doi/10.1007/s11263-015-0816-y) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=3422482) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Imagenet%20large%20scale%20visual%20recognition%20challenge&journal=Int.%20J.%20Comput.%20Vision&doi=10.1007%2Fs11263-015-0816-y&volume=115&pages=211-252&publication_year=2015&author=Russakovsky%2CO)

[^55]: Ioffe, S. & Szegedy, C. Batch normalization: accelerating deep network training by reducing internal covariate shift. in *Proc. 32nd International Conference on International Conference on Machine Learning—Volume 37, ICML’15* 448–456 (PMLR, 2015).
