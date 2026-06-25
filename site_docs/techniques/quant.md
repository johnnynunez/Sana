# Quantization

Quantization targets kernel-level redundancy and bandwidth pressure by lowering precision where the model tolerates it.

The paper treats quantization as selective local tuning rather than uniform low-bit conversion. The quantization agent profiles layer sensitivity, tensor shapes, layer-wise precision choices, activation and weight bitwidths, and timestep-dependent scaling.

## In Sol-Engine

| Pipeline | Quantization path | Notes |
|---|---|---|
| Cosmos3-Super | NVFP4 | First and last denoising steps stay dense |
| LTX-2.3 | NVFP4 video FFN | Used inside the full optimization stack |

NVFP4 requires Blackwell GPUs and TransformerEngine. On older GPUs, the code falls back to BF16 with a warning.

## Methods

| Method | Open-source status | Implementation status | Test status | Role in the design space |
|---|---|---|---|---|
| [NVFP4](quant/nvfp4.md) | open-source | implemented locally | blocked: missing `transformer_engine` | production low-precision path used by Cosmos3-Super and LTX-2.3 |
| [Diffusion PTQ](quant/diffusion_ptq.md) | open-source family | reference adapter | dependency check passed | PTQ4DiT / Q-DiT / ViDiT-Q style diffusion-aware calibration family |
| [SVDQuant / Nunchaku](quant/svdquant.md) | open-source | implemented locally | dependency check passed | outlier absorption with low-rank components for 4-bit diffusion inference |
| [SageAttention](quant/sageattention.md) | open-source | implemented locally | dependency check passed | attention-specific 8-bit to 4-bit acceleration family |
| [ModelOpt / FP8](quant/modelopt_fp8.md) | open-source | implemented locally | dependency check passed | practical transformer checkpoint and runtime quantization family in the codebase |

## Why boundary steps stay dense

Early and late denoising steps are more sensitive to numerical error. Sol-Engine keeps those steps dense and applies NVFP4 where the speed/quality tradeoff is better.
