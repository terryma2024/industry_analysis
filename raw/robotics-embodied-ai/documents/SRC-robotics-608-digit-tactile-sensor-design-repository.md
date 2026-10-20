---
source_id: "SRC-robotics-608"
title: "DIGIT tactile sensor design repository"
source_type: "code_repository"
publisher: "Meta FAIR"
source_date: "待验证"
url: "https://github.com/facebookresearch/digit-design"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-20T05:41:11+00:00"
tags:
  - raw/source
  - source-type/code-repository
  - evidence/s
aliases:
  - SRC-robotics-608
---
# DIGIT tactile sensor design repository

## DIGIT-DESIGN

[![License: CC BY-NC 4.0](https://camo.githubusercontent.com/a668adc80787365ae6ec3fa12856aa51bbca4c79e4efca0acce45f2fa21161bc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d434325323042592d2d4e43253230342e302d6c69676874677265792e737667)](https://github.com/facebookresearch/digit-design/blob/main/LICENSE)

[![DIGIT-render](https://github.com/facebookresearch/digit-design/raw/main/DIGIT/docs/digit-render.png)](https://github.com/facebookresearch/digit-design/blob/main/DIGIT/docs/digit-render.png)

Manufacturing design files for the [DIGIT tactile sensor](https://digit.ml/).

**For updates and discussions please join the #DIGIT channel at the [www.touch-sensing.org](https://www.touch-sensing.org/) community.**

## Content

[This repository](https://github.com/facebookresearch/digit-design/blob/main/DIGIT) contains the documentation and manufacturing files for the plastics enclosure, elastomer, electronics and the firmware binary.

## Design Notes

Due to some parts being out of stock due to shortages, we recommend the following part substituions:

- Digit Main PCB, Camera, OVM7692-RAAA with OVM7692-RYAA
- Digit Main PCB, MCU, FT900-R with FT900Q-C-T
- Digit Flex PCB, LEDs, ARGB1313HS-TR with 19-337C/RSBHGHC-A88/4T
	- Note: this change is only compatible with Digit Flex rev. 2021-2

## Quick Start

Manufacturing and assembly documentation is found in the [Quick Start Guide](https://github.com/facebookresearch/digit-design/blob/main/DIGIT/DIGIT_Quick_Start_Guide.pdf)

The manufacturing files are released in [releases](https://github.com/facebookresearch/digit-design/blob/main/DIGIT/releases) for PCBA fabrication.

## Questions and Contributing

If you have questions or need help with the content of this repo please open a ticket. We welcome useful contributions to the repo -- if you want to contribute please read [how to contribute](https://github.com/facebookresearch/digit-design/blob/main/CONTRIBUTING.md).

## License

These design files are licensed under CC-by-NC, as found in the [LICENSE](https://github.com/facebookresearch/digit-design/blob/main/LICENSE) file.

## Citing

If you use this project in your research, please cite this [paper](https://arxiv.org/abs/2005.14679):

```
@Article{Lambeta2020DIGIT,
    = {Lambeta, Mike and Chou, Po-Wei and Tian, Stephen and Yang, Brian and Maloon, Benjamin and Victoria Rose Most and Stroud, Dave and Santos, Raymond and Byagowi, Ahmad and Kammerer, Gregg and Jayaraman, Dinesh and Calandra, Roberto},
  title   = {{DIGIT}: A Novel Design for a Low-Cost Compact High-Resolution Tactile Sensor with Application to In-Hand Manipulation},
  journal = {IEEE Robotics and Automation Letters (RA-L)},
  year    = {2020},
  volume  = {5},
  number  = {3},
  pages   = {3838--3845},
  doi     = {10.1109/LRA.2020.2977257},
}
```

## DIGIT-PINKI-DESIGN

[![License: CC BY-NC 4.0](https://camo.githubusercontent.com/a668adc80787365ae6ec3fa12856aa51bbca4c79e4efca0acce45f2fa21161bc/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d434325323042592d2d4e43253230342e302d6c69676874677265792e737667)](https://github.com/facebookresearch/digit-design/blob/main/LICENSE)

## Content

[This repository](https://github.com/facebookresearch/digit-design/blob/main/DIGIT_Pinki) contains the documentation and manufacturing files for the plastics enclosure, elastomer, and assembly.

## Quick Start

Manufacturing and assembly documentation is found in the [Quick Start Guide](https://github.com/facebookresearch/digit-design/blob/main/DIGIT_Pinki/DIGIT_Pinki_Quick_Start_Guide.pdf)

## Questions and Contributing

If you have questions or need help with the content of this repo please open a ticket. We welcome useful contributions to the repo -- if you want to contribute please read [how to contribute](https://github.com/facebookresearch/digit-design/blob/main/CONTRIBUTING.md).

## License

These design files are licensed under CC-by-NC, as found in the [LICENSE](https://github.com/facebookresearch/digit-design/blob/main/LICENSE) file.

## Citing

If you use this project in your research, please cite this [paper](https://arxiv.org/abs/2403.05500).
