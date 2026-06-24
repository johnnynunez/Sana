# Diffusion PTQ

Diffusion post-training quantization methods study how to reduce precision while preserving denoising quality. The paper cites PTQ4DiT, Q-DiT, and ViDiT-Q as representative diffusion-aware calibration families.

## Design point

| Method family | Main idea |
|---|---|
| PTQ4DiT | account for salient channels and timestep-varying activations |
| Q-DiT | allocate quantization granularity automatically for DiTs |
| ViDiT-Q | video diffusion quantization with diffusion-specific calibration |

## Role in Sol-Engine

These methods define the broader quantization search space. The reported Sol-Engine stacks use selective NVFP4 rather than a uniform PTQ conversion, but the same agent framework can evaluate diffusion PTQ candidates per deployment.

## Search knobs

- layer-wise precision.
- activation and weight bitwidth.
- timestep-dependent scaling.
- ignored or fallback layers.
