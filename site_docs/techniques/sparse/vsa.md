# VSA

VSA is a video sparse attention operator family cited by the paper. It targets redundant attention interactions in video token sequences.

## Role in Sol-Engine

VSA is part of the sparse-attention candidate set. It may be useful when the target model exposes stable video-specific sparse attention patterns.

## Practical knobs

- operator backend.
- sparsity pattern.
- stage placement.
- dense fallback layers.

## Validation

Use side-by-side videos and report both denoise time and end-to-end time. Attention savings can be hidden by decode or offload overhead.
