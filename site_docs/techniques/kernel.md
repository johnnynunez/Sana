# Kernel fusion

Kernel fusion reduces memory-bound overhead inside DiT blocks. The target is the repeated glue around GEMMs: layout movement, normalization, activation, gate application, QK normalization, RoPE, and precision conversion.

The paper frames kernel fusion as a late-stage local-tuning problem: after other methods shift the bottlenecks, the fusion agent profiles fragmented operators and chooses custom kernels, compiler fusion, or GEMM epilogues for the current tensor shapes and precision formats.

## In Sol-Engine

| Pipeline | Fusion path | Role |
|---|---|---|
| LTX-2.3 | KWL fusion | Operator-level optimization before other methods |
| SANA-Video | Linear attention BF16, QKV merge, compile | Part of the 2.77x path |

## Methods

| Method | Role in the design space |
|---|---|
| [KWL fusion](kernel/kwl.md) | Sol-Engine DiT glue fusion around AdaLN, gates, FFN, and attention paths |
| [GEMM epilogues](kernel/gemm_epilogues.md) | GEMM + GELU / bias / residual style fusion described by CUTLASS and ByteTransformer-style paths |
| [QK-norm + RoPE fusion](kernel/qknorm_rope.md) | fused normalization and rotary-position work on attention Q/K paths |
| [QKV merge](kernel/qkv_merge.md) | merged projection path used in the SANA-Video optimization stack |
| [torch.compile](kernel/torch_compile.md) | compiler-driven graph fusion for stable operator sequences |

## Scope

Fusion should not change scheduler settings, prompts, seeds, or the number of denoising steps. It is an implementation-level optimization that reduces launch and memory traffic overhead.
