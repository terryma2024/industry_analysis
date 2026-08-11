---
source_id: "SRC-robotics-523"
title: "onshape-to-robot processors documentation"
source_type: "technical_documentation"
publisher: "Rhoban"
source_date: "2026-08-10"
url: "https://onshape-to-robot.readthedocs.io/en/latest/processors.html"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-08-10T15:46:26+00:00"
tags:
  - raw/source
  - source-type/technical-documentation
  - evidence/s
aliases:
  - SRC-robotics-523
---
# onshape-to-robot processors documentation

## Processors

## Introduction

Here is an overview of `onshape-to-robot` pipeline:

![_images/architecture.png](https://onshape-to-robot.readthedocs.io/en/latest/_images/architecture.png)
- **(1)**: The assembly is retrieved from Onshape, to produce an intermediate representation of the robot. See the [robot.py](https://github.com/Rhoban/onshape-to-robot/blob/master/onshape_to_robot/robot.py) from the source code.
- **(2)**: Some operations can be applied on this representation, those are the **processors**, some of them are listed below.
- **(3)**: The robot is exported to the desired format (URDF, MuJoCo, etc.) using an **exporter**.

> [!note] Note
> If you want to tweak your robot in the process, do not hesitate to have a look at the [export.py](https://github.com/Rhoban/onshape-to-robot/blob/master/onshape_to_robot/export.py) script, which is the entry point of the `onshape-to-robot` command, and summarize the above-listed steps.

## Retrieve and Convert Modes

It is possible to only execute the retrieval step **(1)**, by passing the `--retrieve` argument to the `onshape-to-robot` command. This will save the intermediate representation of the robot to a file named `robot.pkl` in the output directory.

Similarly, steps **(2)** and **(3)** can be executed by passing the `--convert` argument, which will load the robot from the `robot.pkl` file. Processors will then be executed and the exported will produce the final output. This can be convenient to avoid sending API requests to Onshape while tweaking processors or exporters.

You can also use the `--save-pickle` argument to save the robot data after retrieval while still proceeding to conversion.

## Processors list

Processors:

- [Ball to Euler](https://onshape-to-robot.readthedocs.io/en/latest/processor_ball_to_euler.html)
	- [Introduction](https://onshape-to-robot.readthedocs.io/en/latest/processor_ball_to_euler.html#introduction)
		- [`config.json` entries](https://onshape-to-robot.readthedocs.io/en/latest/processor_ball_to_euler.html#config-json-entries)
- [Merge STLs](https://onshape-to-robot.readthedocs.io/en/latest/processor_merge_parts.html)
	- [Introduction](https://onshape-to-robot.readthedocs.io/en/latest/processor_merge_parts.html#introduction)
		- [`config.json` entries](https://onshape-to-robot.readthedocs.io/en/latest/processor_merge_parts.html#config-json-entries)
- [Simplify STLs](https://onshape-to-robot.readthedocs.io/en/latest/processor_simplify_stls.html)
	- [Introduction](https://onshape-to-robot.readthedocs.io/en/latest/processor_simplify_stls.html#introduction)
		- [Requirements](https://onshape-to-robot.readthedocs.io/en/latest/processor_simplify_stls.html#requirements)
		- [`config.json` entries](https://onshape-to-robot.readthedocs.io/en/latest/processor_simplify_stls.html#config-json-entries)
- [OpenSCAD pure shapes approximation](https://onshape-to-robot.readthedocs.io/en/latest/processor_scad.html)
- [Adding dummy base link](https://onshape-to-robot.readthedocs.io/en/latest/processor_dummy_base_link.html)
	- [Introduction](https://onshape-to-robot.readthedocs.io/en/latest/processor_dummy_base_link.html#introduction)
		- [`config.json` entries](https://onshape-to-robot.readthedocs.io/en/latest/processor_dummy_base_link.html#config-json-entries)
- [Removing collision meshes](https://onshape-to-robot.readthedocs.io/en/latest/processor_no_collision_meshes.html)
	- [Introduction](https://onshape-to-robot.readthedocs.io/en/latest/processor_no_collision_meshes.html#introduction)
		- [`config.json` entries](https://onshape-to-robot.readthedocs.io/en/latest/processor_no_collision_meshes.html#config-json-entries)
- [Use collisions as visual](https://onshape-to-robot.readthedocs.io/en/latest/processor_collision_as_visual.html)
	- [Introduction](https://onshape-to-robot.readthedocs.io/en/latest/processor_collision_as_visual.html#introduction)
		- [`config.json` entries](https://onshape-to-robot.readthedocs.io/en/latest/processor_collision_as_visual.html#config-json-entries)
- [Convex decomposition (CoACD)](https://onshape-to-robot.readthedocs.io/en/latest/processor_convex_decomposition.html)
	- [Introduction](https://onshape-to-robot.readthedocs.io/en/latest/processor_convex_decomposition.html#introduction)
		- [`config.json` entries](https://onshape-to-robot.readthedocs.io/en/latest/processor_convex_decomposition.html#config-json-entries)
- [Using fixed links](https://onshape-to-robot.readthedocs.io/en/latest/processor_fixed_links.html)
	- [Introduction](https://onshape-to-robot.readthedocs.io/en/latest/processor_fixed_links.html#introduction)
		- [`config.json` entries](https://onshape-to-robot.readthedocs.io/en/latest/processor_fixed_links.html#config-json-entries)
- [Writing & registering custom Processor](https://onshape-to-robot.readthedocs.io/en/latest/custom_processors.html)
