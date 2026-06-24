# GEMM epilogues

GEMM epilogue fusion executes memory-bound follow-up work while intermediate GEMM results remain close to the compute kernel. The paper discusses CUTLASS epilogues, ByteTransformer-style fused bias / GELU paths, and CODA-style transformer block rewriting as representative kernel-fusion families.

## Typical fused sequences

- GEMM + bias.
- GEMM + GELU.
- FFN projection plus activation.
- GEMM + residual update.
- GEMM + normalization-related epilogue work.

## Role in Sol-Engine

These fusions are candidates after profiling shows that fragmented memory-bound operators dominate the partially optimized stack.

## Validation

Epilogue fusion must preserve numerics within the expected precision envelope and should be benchmarked at the actual deployment shape.
