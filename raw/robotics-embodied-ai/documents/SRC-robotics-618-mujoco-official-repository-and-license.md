---
source_id: "SRC-robotics-618"
title: "MuJoCo official repository and license"
source_type: "repository"
publisher: "Google DeepMind"
source_date: "待验证"
url: "https://github.com/google-deepmind/mujoco"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:35:43+00:00"
tags:
  - raw/source
  - source-type/repository
  - evidence/s
aliases:
  - SRC-robotics-618
---
# MuJoCo official repository and license

[![](https://camo.githubusercontent.com/dab89ab4f758aab5c1e411fb503ac5305c5b0f34f9679266f7458345163738f7/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f676f6f676c652d646565706d696e642f6d756a6f636f2f6275696c642e796d6c3f6272616e63683d6d61696e)](https://github.com/google-deepmind/mujoco/actions/workflows/build.yml?query=branch%3Amain)[![](https://camo.githubusercontent.com/ac45e5d58cda9236d331d60692d947e53a73309bc21a4e74464f957e6bc9154d/68747470733a2f2f72656164746865646f63732e6f72672f70726f6a656374732f6d756a6f636f2f62616467652f3f76657273696f6e3d6c6174657374) ](https://mujoco.readthedocs.io/)[![](https://camo.githubusercontent.com/1e9f460f6b1a26b881029735c43c7d4c3bf871fd4dd75f1fa91fc5627ea11ccf/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f676f6f676c652d646565706d696e642f6d756a6f636f)](https://github.com/google-deepmind/mujoco/blob/main/LICENSE)

**MuJoCo** stands for **Mu** lti- **Jo** int dynamics with **Co** ntact. It is a general purpose physics engine that aims to facilitate research and development in robotics, biomechanics, graphics and animation, machine learning, and other areas which demand fast and accurate simulation of articulated structures interacting with their environment.

This repository is maintained by [Google DeepMind](https://www.deepmind.com/).

MuJoCo has a C API and is intended for researchers and developers. The runtime simulation module is tuned to maximize performance and operates on low-level data structures that are preallocated by the built-in XML compiler. The library includes interactive visualization with a native GUI, rendered in OpenGL. MuJoCo further exposes a large number of utility functions for computing physics-related quantities.

We also provide [Python bindings](https://mujoco.readthedocs.io/en/stable/python.html#python-bindings) and a plug-in for the [Unity](https://unity.com/) game engine.

## Documentation

MuJoCo's documentation can be found at [mujoco.readthedocs.io](https://mujoco.readthedocs.io/). Upcoming features due for the next release can be found in the [changelog](https://mujoco.readthedocs.io/en/latest/changelog.html) in the "latest" branch.

## Getting Started

There are two easy ways to get started with MuJoCo:

1. **Run `simulate` on your machine.** [This video](https://www.youtube.com/watch?v=P83tKA1iz2Y) shows a screen capture of `simulate`, MuJoCo's native interactive viewer. Follow the steps described in the [Getting Started](https://mujoco.readthedocs.io/en/latest/programming#getting-started) section of the documentation to get `simulate` running on your machine.
2. **Explore our online IPython notebooks.** If you are a Python user, you might want to start with our tutorial notebooks running on Google Colab:
- The **introductory** tutorial teaches MuJoCo basics: [![Open In Colab](https://camo.githubusercontent.com/eff96fda6b2e0fff8cdf2978f89d61aa434bb98c00453ae23dd0aab8d1451633/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/python/tutorial.ipynb)
- The **Model Editing** tutorial shows how to create and edit models procedurally: [![Open In Colab](https://camo.githubusercontent.com/eff96fda6b2e0fff8cdf2978f89d61aa434bb98c00453ae23dd0aab8d1451633/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/python/mjspec.ipynb)
- The **rollout** tutorial shows how to use the multithreaded `rollout` module: [![Open In Colab](https://camo.githubusercontent.com/eff96fda6b2e0fff8cdf2978f89d61aa434bb98c00453ae23dd0aab8d1451633/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/python/rollout.ipynb)
- The **LQR** tutorial synthesizes a linear-quadratic controller, balancing a humanoid on one leg: [![Open In Colab](https://camo.githubusercontent.com/eff96fda6b2e0fff8cdf2978f89d61aa434bb98c00453ae23dd0aab8d1451633/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/python/LQR.ipynb)
- The **least-squares** tutorial explains how to use the Python-based nonlinear least-squares solver: [![Open In Colab](https://camo.githubusercontent.com/eff96fda6b2e0fff8cdf2978f89d61aa434bb98c00453ae23dd0aab8d1451633/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/python/least_squares.ipynb)
- The **MJX** tutorial provides usage examples of [MuJoCo XLA](https://mujoco.readthedocs.io/en/stable/mjx.html), a branch of MuJoCo written in JAX: [![Open In Colab](https://camo.githubusercontent.com/eff96fda6b2e0fff8cdf2978f89d61aa434bb98c00453ae23dd0aab8d1451633/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/mjx/tutorial.ipynb)
- The **differentiable physics** tutorial trains locomotion policies with analytical gradients automatically derived from MuJoCo's physics step: [![Open In Colab](https://camo.githubusercontent.com/eff96fda6b2e0fff8cdf2978f89d61aa434bb98c00453ae23dd0aab8d1451633/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/github/google-deepmind/mujoco/blob/main/mjx/training_apg.ipynb)

## Installation

### Prebuilt binaries

Versioned releases are available as precompiled binaries from the GitHub [releases page](https://github.com/google-deepmind/mujoco/releases), built for Linux (x86-64 and AArch64), Windows (x86-64 only), and macOS (universal). This is the recommended way to use the software.

### Building from source

Users who wish to build MuJoCo from source should consult the [build from source](https://mujoco.readthedocs.io/en/latest/programming#building-from-source) section of the documentation. However, note that the commit at the tip of the `main` branch may be unstable.

### Python (>= 3.11)

The native Python bindings, which come pre-packaged with a copy of MuJoCo, can be installed from [PyPI](https://pypi.org/project/mujoco/) via:

```
pip install mujoco
```

Note that Pre-built Linux wheels target `manylinux2014`, see [here](https://github.com/pypa/manylinux) for compatible distributions. For more information such as building the bindings from source, see the [Python bindings](https://mujoco.readthedocs.io/en/stable/python.html#python-bindings) section of the documentation.

## Versioning

We aim to release MuJoCo in the first week of each month. Our versioning standards changed to modified Semantic Versioning in 3.5.0, see [versioning](https://github.com/google-deepmind/mujoco/blob/main/VERSIONING.md) for details.

## Contributing

We welcome community engagement: questions, requests for help, bug reports and feature requests. To read more about bug reports, feature requests and more ambitious contributions, please see our [contributors guide](https://github.com/google-deepmind/mujoco/blob/main/CONTRIBUTING.md) and [style guide](https://github.com/google-deepmind/mujoco/blob/main/STYLEGUIDE.md).

## Asking Questions

Questions and requests for help are welcome as a GitHub ["Asking for Help" Discussion](https://github.com/google-deepmind/mujoco/discussions/categories/asking-for-help) and should focus on a specific problem or question.

## Bug reports and feature requests

GitHub [Issues](https://github.com/google-deepmind/mujoco/issues) are reserved for bug reports, feature requests and other development-related subjects.

## Related software

MuJoCo is the backbone for numerous environment packages. Below we list several bindings and converters.

### Bindings

These packages give users of various languages access to MuJoCo functionality:

#### First-party bindings:

- [Python bindings](https://mujoco.readthedocs.io/en/stable/python.html)
	- [dm\_control](https://github.com/google-deepmind/dm_control), Google DeepMind's related environment stack, includes [PyMJCF](https://github.com/google-deepmind/dm_control/blob/main/dm_control/mjcf/README.md), a module for procedural manipulation of MuJoCo models.
- [JavaScript bindings and WebAssembly support](https://github.com/google-deepmind/mujoco/blob/main/wasm/README.md) (inspired [stillonearth](https://github.com/stillonearth) and [zalo](https://github.com/zalo) 's community projects; [mjswan](https://github.com/ttktjmt/mjswan) extends these with real-time policy control, interactive force application, and more).
- [C# bindings and Unity plug-in](https://mujoco.readthedocs.io/en/stable/unity.html)

#### Third-party bindings:

- **MATLAB Simulink**: [Simulink Blockset for MuJoCo Simulator](https://github.com/mathworks-robotics/mujoco-simulink-blockset) by [Manoj Velmurugan](https://github.com/vmanoj1996).
- **Swift**: [swift-mujoco](https://github.com/liuliu/swift-mujoco)
- **Java**: [mujoco-java](https://github.com/CommonWealthRobotics/mujoco-java)
- **Julia**: [MuJoCo.jl](https://github.com/JamieMair/MuJoCo.jl)
- **Rust**: [MuJoCo-rs](https://github.com/davidhozic/mujoco-rs)

### Converters

- **OpenSim**: [MyoConverter](https://github.com/MyoHub/myoconverter) converts OpenSim models to MJCF.
- **SDFormat**: [gz-mujoco](https://github.com/gazebosim/gz-mujoco/) is a two-way SDFormat <-> MJCF conversion tool.
- **OBJ**: [obj2mjcf](https://github.com/kevinzakka/obj2mjcf) a script for converting composite OBJ files into a loadable MJCF model.
- **onshape**: [Onshape to Robot](https://github.com/rhoban/onshape-to-robot) Converts [onshape](https://www.onshape.com/en/) CAD assemblies to MJCF.

## Citation

If you use MuJoCo for published research, please cite:

```
@inproceedings{todorov2012mujoco,
  title={MuJoCo: A physics engine for model-based control},
  author={Todorov, Emanuel and Erez, Tom and Tassa, Yuval},
  booktitle={2012 IEEE/RSJ International Conference on Intelligent Robots and Systems},
  pages={5026--5033},
  year={2012},
  organization={IEEE},
  doi={10.1109/IROS.2012.6386109}
}
```

## License and Disclaimer

Copyright 2021 DeepMind Technologies Limited.

Box collision code ([`engine_collision_box.c`](https://github.com/google-deepmind/mujoco/blob/main/src/engine/engine_collision_box.c)) is Copyright 2016 Svetoslav Kolev.

ReStructuredText documents, images, and videos in the `doc` directory are made available under the terms of the Creative Commons Attribution 4.0 (CC BY 4.0) license. You may obtain a copy of the License at [https://creativecommons.org/licenses/by/4.0/legalcode](https://creativecommons.org/licenses/by/4.0/legalcode).

Source code is licensed under the Apache License, Version 2.0. You may obtain a copy of the License at [https://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0).

This is not an officially supported Google product.
