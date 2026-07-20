---
source_id: "SRC-robotics-314"
title: "MuJoCo Unreal Engine Plugin upstream repository"
source_type: "code_repository"
publisher: "oneclicklabs"
source_date: "2025-03-15"
url: "https://github.com/oneclicklabs/MuJoCo-Unreal-Engine-Plugin"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-07-20T08:57:22+00:00"
tags:
  - raw/source
  - source-type/code-repository
  - evidence/s
aliases:
  - SRC-robotics-314
---
# MuJoCo Unreal Engine Plugin upstream repository

## MuJoCo Unreal Engine Plugin

This plugin integrates MuJoCo physics engine with Unreal Engine, allowing you to load MuJoCo XML files directly into Unreal Engine and run advanced physics simulations.

## Features

- Load MuJoCo XML files into Unreal Engine
- Run MuJoCo simulations and display results in real-time
- Support for procedural mesh generation for non-primitive MuJoCo shapes
- Import object colors from MuJoCo models
- Multiple simultaneous simulation instances support

## Demo

[![Simulation Demo](https://camo.githubusercontent.com/72495dd128479d3171026d58e1ae9033fed5bb1bf268ba4d14c8b1dc09a9b2ed/68747470733a2f2f63646e2e6c6f6f6d2e636f6d2f73657373696f6e732f7468756d626e61696c732f65633236633839326235303134613033616662376430313662326434623464352d383862613266636530303134306534642d66756c6c2d706c61792e676966)](https://camo.githubusercontent.com/72495dd128479d3171026d58e1ae9033fed5bb1bf268ba4d14c8b1dc09a9b2ed/68747470733a2f2f63646e2e6c6f6f6d2e636f6d2f73657373696f6e732f7468756d626e61696c732f65633236633839326235303134613033616662376430313662326434623464352d383862613266636530303134306534642d66756c6c2d706c61792e676966)

[![Simulation Demo 2](https://camo.githubusercontent.com/1ba06f3b3164e4e229d0f0bfa2449018273b6d69867f4accb6911f39091dc38e/68747470733a2f2f63646e2e6c6f6f6d2e636f6d2f73657373696f6e732f7468756d626e61696c732f63373530666335343366333534383230386164383864313462303434373235312d626562353033326430633163646632372d66756c6c2d706c61792e676966)](https://camo.githubusercontent.com/1ba06f3b3164e4e229d0f0bfa2449018273b6d69867f4accb6911f39091dc38e/68747470733a2f2f63646e2e6c6f6f6d2e636f6d2f73657373696f6e732f7468756d626e61696c732f63373530666335343366333534383230386164383864313462303434373235312d626562353033326430633163646632372d66756c6c2d706c61792e676966)

[![Simulation Demo 3](https://camo.githubusercontent.com/d6139d415f3cdd59f32f451f77eb30d199b8b97ee2afe64867ac41d39c21a8ae/68747470733a2f2f63646e2e6c6f6f6d2e636f6d2f73657373696f6e732f7468756d626e61696c732f38316438346339613835363534363531393961616532326434643565363237632d343764396561323866333236363032322d66756c6c2d706c61792e676966)](https://camo.githubusercontent.com/d6139d415f3cdd59f32f451f77eb30d199b8b97ee2afe64867ac41d39c21a8ae/68747470733a2f2f63646e2e6c6f6f6d2e636f6d2f73657373696f6e732f7468756d626e61696c732f38316438346339613835363534363531393961616532326434643565363237632d343764396561323866333236363032322d66756c6c2d706c61792e676966)

## Installation

1. Clone this repository to your Unreal Engine project's `Plugins` folder
2. Rebuild your project
3. Enable the MuJoCo plugin in your project settings

## Usage

### Basic Setup

1. Place a `MuJoCoSimulation` actor in your level
2. Set the XML file path in the actor's properties
3. Start play mode to see the simulation

### Controls

- **Z key**: Hold to run simulation, release to pause
- **R key**: Reset simulation to initial state
- **C key**: Test MuJoCo actuators control (sets Actuator 0 to a small value, useful for testing models like car.xml)

## Current Limitations

- Texture support is not yet implemented (only colors are imported)
- It is still rough and not optimized for performance
