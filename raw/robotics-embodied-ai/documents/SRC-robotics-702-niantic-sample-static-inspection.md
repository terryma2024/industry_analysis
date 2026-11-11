---
source_id: SRC-robotics-702
title: Niantic sample asset static inspection
source_type: evidence_packet
publisher: original source with analyst inspection
source_date: 2026-11-10
url: https://huggingface.co/datasets/NianticSpatial/real2sim-sample-usdz-scenes/tree/f7ca59406bf15cdaf28e9c95bb99a317ebd7c83c
evidence_grade: S
capture_method: bounded-http-range-and-openusd
captured_at: 2026-11-10
tags: [raw/source, real2sim]
---

# Niantic sample asset static inspection

Fixed HF revision `f7ca59406bf15cdaf28e9c95bb99a317ebd7c83c`. [Inspection JSON](../data/niantic-sample-asset-inspection-2026-11-10.json); [asset inventory](../data/niantic-sample-assets-inventory-2026-11-10.csv).

Sample: `Nurec Volume Schema/pondicherry_nurec.usdz`, 281508778 bytes. Only final ZIP central directory and three selected stored members fetched via HTTP Range. Selected member CRC32 verified and individual SHA256 recorded; full archive LFS SHA256 was not independently verified. Full archive and 276917543-byte sim.nurec were NOT downloaded. This directory is not a complete renderable scene.

- [default.usda](SRC-robotics-702-selected-usdz-members/default.usda): root metersPerUnit=1, Z-up, defaultPrim World, reference to gauss.usda.
- [gauss.usda](SRC-robotics-702-selected-usdz-members/gauss.usda): NuRec Volume references sim.nurec and mesh.usd, local transform authored for mesh.
- [mesh.usd](SRC-robotics-702-selected-usdz-members/mesh.usd): parsed with OpenUSD 0.26.11; 259296 points and 499999 faces, PhysicsCollisionAPI and PhysicsMeshCollisionAPI; collisionEnabled True, approximation none, visibility invisible.
- GetStageMetersPerUnit on isolated mesh returns fallback0.01 and up-axis Y; BOTH metadata fields unauthored. Do not infer an authored 100x unit error or rescale from these fallbacks. Preserve root composition and transforms; composed rendering/collision alignment not tested.
- No physics material prim appeared in this mesh-only traversal; do not infer global material absence in all scenes or runtime defaults.
- OpenUSD emitted an ARCH_CACHE_LINE_SIZE assumption warning, but source parsing completed. No simulator/render/policy/hardware tests run.

