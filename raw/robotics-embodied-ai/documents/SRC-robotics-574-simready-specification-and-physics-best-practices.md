---
source_id: "SRC-robotics-574"
title: "SimReady specification and physics best practices"
source_type: "technical_documentation"
publisher: "NVIDIA Omniverse / SimReady Foundation"
source_date: "2026-09-22"
url: "https://docs.omniverse.nvidia.com/simready/latest/overview/simready-spec.html"
evidence_grade: "S"
capture_method: "defuddle"
captured_at: "2026-09-22T02:52:18+00:00"
tags:
  - raw/source
  - source-type/technical-documentation
  - evidence/s
aliases:
  - SRC-robotics-574
---
# SimReady specification and physics best practices

The SimReady Foundation hosts the SimReady Specification. Check out the [SimReady Foundation docs](https://nvidia.github.io/simready-foundation/latest/guides/getting_started.html) and the [SimReady Foundation repo](https://github.com/nvidia/simready-foundation).

![Nighttime downtown intersection with glass office towers, vehicles on wet streets, crosswalk and lane markings, streetlights, and illuminated storefronts and building lobbies.](https://docs.omniverse.nvidia.com/simready/latest/_images/simready_spec.png)

## Goals for the SimReady Specification

While many creators can build 3D assets to photo-real standards, very few understand how to conform their 3D assets so that a machine learning researcher, factory planner or data scientist can take those assets and quickly incorporate them into their work; whether the goal is to create new algorithms for autonomous driving, or to simulate the layout of a new factory design to identify bottlenecks. These consumers are often not 3D creators themselves, and as such, having to manually configure or fix random 3D assets so that they work within their simulation environments is a huge barrier. Mixing and matching licensed 3D assets also forces these users to become responsible for making sure those same 3D assets work within their simulation runtimes, and they do not have that expertise. Simply put, most simulation creators want to license and consume 3D assets that are **purpose-built for simulation.**

Given the rapidly growing need for this sort of content, the SimReady specification provides best practices for the creation and application of additional metadata needed to make 3D assets useful within simulation runtimes. This includes the addition of semantic labeling, non-visual sensor attributes, rigid-body physics and physical mass association, just to name a few.

## What is a SimReady Asset?

SimReady 3D assets are versatile digital models optimized for use across various OpenUSD-compatible simulation platforms. Built on the OpenUSD framework, these assets leverage its powerful composition arcs and inherent flexibility to adapt to a wide range of simulation requirements. This foundation allows SimReady assets to be highly configurable, enabling their seamless integration and functionality within diverse virtual environments.

It’s worth noting that from a high-level, SimReady assets are defined by their **capabilities**. That is to say, that they are defined by their included metadata and semantics over a strict OpenUSD stage hierarchy. There is no single “right way” to create a SimReady asset. What matters is the addition and presence of specific types of metadata and use of core OpenUSD schemas that are available to different simulation runtime environments. While the specification provides suggestions on how a creator should consider building SimReady assets, it doesn’t preclude you from generating assets in other ways. OpenUSD is flexible, and SimReady is equally flexible.

A SimReady asset is also designed to act as a consistent “ground truth” starting point for you when you want to customize or tune your library for a particular machine learning need. Instead of having to rework your entire library of existing assets individually, you can further leverage the flexible nature of OpenUSD to define where new properties and attributes can be applied so that you can augment baseline SimReady files non-destructively.

## Types of SimReady 3D Assets

As this is a brand new specification, it currently covers basic static props (ones that don’t move or articulate). Why? While we would like to provide a SimReady specification for every simulation feature immediately, it’s not practical. Plus, we’ve also made the conscious decision to start small and provide this preliminary set of SimReady capabilities as a **conversation starter**. NVIDIA wants to actively work with external companies to flesh out the SimReady specification together as a community. By providing immediate access to SimReady as it exists now to everyone, our goal is to engage with you collaboratively so that as the specs are being built, you can provide input and be a direct contributor helping shape the future of SimReady so it meets **your** simulation needs.

Defining these standards will take longer and will build upon the knowledge gained by working with various industry stakeholders and understanding their needs and use cases. What this means is that the SimReady specification is designed to evolve over time and grow in lock step with the various simulation industries.
