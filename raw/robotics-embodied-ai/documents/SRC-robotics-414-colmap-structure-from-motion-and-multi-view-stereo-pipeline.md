---
source_id: "SRC-robotics-414"
title: "COLMAP structure-from-motion and multi-view-stereo pipeline"
source_type: "technical_documentation"
publisher: "COLMAP contributors"
source_date: "2026-08-06"
url: "https://colmap.github.io/index.html"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-08-06T03:34:18+00:00"
tags:
  - raw/source
  - source-type/technical-documentation
  - evidence/s
aliases:
  - SRC-robotics-414
---
# COLMAP structure-from-motion and multi-view-stereo pipeline

## COLMAP

## Install COLMAP

Select your platform below to get the recommended install command or download.

For all installation options and build-from-source instructions, see the [installation guide](https://colmap.github.io/install.html#installation).

## Features

Structure-from-Motion

[Tutorial](https://colmap.github.io/tutorial.html)

Multi-View Stereo

[Tutorial](https://colmap.github.io/tutorial.html)

Graphical & Command-Line

[Graphical User Interface](https://colmap.github.io/gui.html)

PyCOLMAP

[PyCOLMAP](https://colmap.github.io/pycolmap/index.html)

Camera Models & Rigs

[Camera Models](https://colmap.github.io/cameras.html)

Datasets & Formats

[Datasets](https://colmap.github.io/datasets.html)

## Getting Started

1. Install COLMAP using the selector above, download the [pre-built binaries](https://github.com/colmap/colmap/releases), or build from [source](https://colmap.github.io/install.html) (see [Installation](https://colmap.github.io/install.html#installation)).
2. Download one of the provided datasets (see [Datasets](https://colmap.github.io/datasets.html#datasets)) or use your own images.
3. Use the **automatic reconstruction** to easily build models with a single click (see [Quickstart](https://colmap.github.io/tutorial.html#quick-start)).

## Support

Please, use [GitHub Discussions](https://github.com/colmap/colmap/discussions) for questions and the [GitHub issue tracker](https://github.com/colmap/colmap) for bug reports, feature requests/additions, etc.

## Citation

If you use this project for your research, please cite:

```
@inproceedings{schoenberger2016sfm,
    ={Sch\"{o}nberger, Johannes Lutz and Frahm, Jan-Michael},
    title={Structure-from-Motion Revisited},
    booktitle={Conference on Computer Vision and Pattern Recognition (CVPR)},
    year={2016},
}

@inproceedings{schoenberger2016mvs,
    ={Sch\"{o}nberger, Johannes Lutz and Zheng, Enliang and Pollefeys, Marc and Frahm, Jan-Michael},
    title={Pixelwise View Selection for Unstructured Multi-View Stereo},
    booktitle={European Conference on Computer Vision (ECCV)},
    year={2016},
}
```

If you use the global SfM pipeline (GLOMAP), please cite:

```
@inproceedings{pan2024glomap,
    ={Pan, Linfei and Barath, Daniel and Pollefeys, Marc and Sch\"{o}nberger, Johannes Lutz},
    title={{Global Structure-from-Motion Revisited}},
    booktitle={European Conference on Computer Vision (ECCV)},
    year={2024},
}
```

If you use the image retrieval / vocabulary tree engine, please cite:

```
@inproceedings{schoenberger2016vote,
    ={Sch\"{o}nberger, Johannes Lutz and Price, True and Sattler, Torsten and Frahm, Jan-Michael and Pollefeys, Marc},
    title={A Vote-and-Verify Strategy for Fast Spatial Verification in Image Retrieval},
    booktitle={Asian Conference on Computer Vision (ACCV)},
    year={2016},
}
```

## Acknowledgments

COLMAP was originally written by [Johannes Schönberger](https://demuc.de/) with funding provided by his PhD advisors Jan-Michael Frahm and Marc Pollefeys. The team of core project maintainers currently includes [Johannes Schönberger](https://github.com/ahojnnes), [Paul-Edouard Sarlin](https://github.com/sarlinpe), and [Shaohui Liu](https://github.com/B1ueber2y).

The Python bindings in PyCOLMAP were originally added by [Mihai Dusmanu](https://github.com/mihaidusmanu), [Philipp Lindenberger](https://github.com/Phil26AT), and [Paul-Edouard Sarlin](https://github.com/sarlinpe).

The project has also benefitted from countless community contributions, including bug fixes, improvements, new features, third-party tooling, and community support (special credits to [Torsten Sattler](https://tsattler.github.io/)).
