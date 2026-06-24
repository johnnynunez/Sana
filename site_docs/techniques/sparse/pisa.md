# PISA

PISA is the sparse attention method selected for LTX-2.3. It uses piecewise sparse attention: important blocks are computed exactly, while less important blocks can be approximated or skipped depending on configuration.

## Sol-Engine placement

Sol-Engine uses PISA in selected LTX-2.3 stage-2 video self-attention blocks
together with cache, token pruning, NVFP4, and kernel fusion.

## Tunable knobs

- sparsity.
- block size.
- route mode.
- dense fallback layers.
- approximate-remainder policy.
- stage and layer placement.

## Validation

Validate temporal coherence and fine detail. Sparse attention errors can be subtle in single frames but visible over motion.
