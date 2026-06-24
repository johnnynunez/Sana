# CoReDiT

CoReDiT prunes spatially coherent DiT tokens and reconstructs skipped outputs to preserve a dense representation for later layers or stages.

## Role in Sol-Engine

CoReDiT is part of the token-pruning family cited by the paper. It is relevant when spatial coherence matters more than raw token-count reduction.

## Search knobs

- coherent region selection.
- pruning ratio.
- reconstruction rule.
- layer and timestep placement.

## Validation

Inspect object boundaries, small structures, and temporal motion. Reconstruction should not create persistent spatial artifacts.
