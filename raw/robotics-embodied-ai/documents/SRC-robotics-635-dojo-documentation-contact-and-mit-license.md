---
source_id: "SRC-robotics-635"
title: "Dojo documentation contact and MIT license"
source_type: "documentation"
publisher: "Dojo"
source_date: "待验证"
url: "https://dojo-sim.github.io/Dojo.jl/dev/"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-10-26T01:35:43+00:00"
tags:
  - raw/source
  - source-type/documentation
  - evidence/s
aliases:
  - SRC-robotics-635
---
# Dojo documentation contact and MIT license

## Get Started

**[Dojo](https://github.com/dojo-sim/Dojo.jl) is a differentiable simulator for robotics**, prioritizing accurate physics and useful gradients. The simulator is written in pure Julia in order to be both performant and easy to use.

## Features

- **Maximal-Coordinates Representation**: Fast and efficient conversion between [maximal](https://dojo-sim.github.io/Dojo.jl/dev/background_representations/maximal_representation.html) and [minimal](https://dojo-sim.github.io/Dojo.jl/dev/background_representations/minimal_representation.html) representations
- **Smooth Gradients**: Simulation with [hard contact](https://dojo-sim.github.io/Dojo.jl/dev/background_contact/impact.html) and useful [gradients](https://dojo-sim.github.io/Dojo.jl/dev/background_representations/gradients.html) through contact events
- **Open Source**: Code is available on [GitHub](https://github.com/dojo-sim/Dojo.jl) and distributed under the MIT License
- **Python Interface**: [dojopy](https://github.com/dojo-sim/dojopy)

## Installation

Dojo can be installed using the Julia package manager for Julia `v1.6` and higher. Inside the Julia REPL, type `]` to enter the Pkg REPL mode then run

`pkg> add Dojo`

## Related talks

## Credits

The following people are involved in the development of Dojo:

**Primary Development**

- [Simon Le Cleac'h](https://simon-lc.github.io/) (main development, contact modeling, interior-point solver, gradients)
- [Taylor Howell](https://thowell.github.io/) (main development, contact modeling, interior-point solver, gradients)
- [Jan Bruedigam](https://github.com/janbruedigam) (main development, maximal representation and graph-based solver)

**Additional Contributions**

Development by the [Robotic Exploration Lab](https://roboticexplorationlab.org/).

If this project is useful for your work please consider

## Licence

Dojo.jl is licensed under the MIT License. For more details click [here](https://github.com/dojo-sim/Dojo.jl/blob/main/LICENSE.md).
