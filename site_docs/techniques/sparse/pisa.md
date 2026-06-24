# PISA

PISA is the sparse attention method selected for LTX-2.3. It uses piecewise sparse attention: important blocks are computed exactly, while less important blocks can be approximated or skipped depending on configuration.

## Sol-Engine placement

| Pipeline | Scope | Configuration role |
|---|---|---|
| LTX-2.3 | selected stage-2 video self-attention | combines with cache, token pruning, NVFP4, and KWL fusion |

## Tunable knobs

- sparsity.
- block size.
- route mode.
- dense fallback layers.
- approximate-remainder policy.
- stage and layer placement.

## Validation

Validate temporal coherence and fine detail. Sparse attention errors can be subtle in single frames but visible over motion.
