# Technique Status Report

Audit date: 2026-06-24

Shared environment: `.conda/ltx23`, created and tested through `scripts/use_code_storage_env.sh`. GPU tests used Slurm 4-GPU allocations because the login node exposes an older CUDA driver than the CUDA 13 runtime needs.

## End-to-End Model Tests

| Model | Covered methods | Status | Evidence |
|---|---|---|---|
| SANA-Video 2B | EasyCache, SANA kernel-fusion toggles, compile path | Passed | `outputs/technique_audit_sana_baseline.mp4`, `outputs/technique_audit_sana_fullopt.mp4`, logs in `outputs/technique_audit_sana/` |
| Cosmos3-Super 64B | TeaCache | Passed | `outputs/technique_audit_cosmos/64b/prompt_0/teacache_c115_s1_m3/out.mp4`, `perf.json`, TeaCache hit stats in `outputs/technique_audit_cosmos/logs/64b_prompt0_teacache_c115_s1_m3.log` |
| LTX-2.3 | Fixed-step cache, feature-norm pruning, PISA sparse attention, LTX fusion stack, NVFP4-requested path | Passed with caveat | `outputs/technique_audit_ltx23/fullopt/out.mp4`, `perf.json`; the run completed, but true TE NVFP4 is blocked by missing `transformer_engine` |

Test scales were sanity settings where possible, not paper benchmark settings:

- SANA: 480x832, 9 frames, 4 steps.
- Cosmos3-Super: 480x832, 9 frames, 4 steps, 4 GPUs.
- LTX-2.3: repository HQ script settings, 1 GPU, reused local LTX-2.3 weights.

## Open-Source Methods

| Category | Method | Implementation | Test status |
|---|---|---|---|
| Cache | TeaCache | `technique/cache/teacache`, local Cosmos runtime | Passed E2E on Cosmos3-Super |
| Cache | EasyCache | `technique/cache/easycache`, local SANA runtime | Passed E2E on SANA-Video |
| Cache | TaylorSeer | `technique/cache/taylorseer`, cache-dit adapter | Dependency check passed; no dedicated video E2E selected |
| Cache | Fixed-step cache | `technique/cache/fixed_step_cache`, local LTX runtime | Passed E2E on LTX-2.3 |
| Cache | Cache-DiT / DBCache | `technique/cache/cache_dit_dbcache`, cache-dit adapter | Dependency check passed; no dedicated video E2E selected |
| Token pruning | Feature-norm pruning | `technique/token_pruning/feature_norm_pruning`, local LTX runtime | Passed E2E on LTX-2.3 |
| Token pruning | ToMe-SD | `technique/token_pruning/tome_sd`, external `tomesd` adapter | Dependency check passed; no Sol-Engine video E2E selected |
| Sparse attention | PISA | `technique/sparse_attention/pisa`, local LTX runtime | Passed E2E on LTX-2.3 |
| Sparse attention | SpargeAttention | `technique/sparse_attention/spargeattention`, external adapter | Blocked: `spas_sage_attn` build failed in the shared CUDA 13/aarch64 env |
| Sparse attention | Sparse VideoGen | `technique/sparse_attention/sparse_videogen`, external `svg` adapter | Dependency check passed; no Sol-Engine SVG1 E2E selected |
| Sparse attention | Sparse VideoGen2 | `technique/sparse_attention/sparse_videogen2`, local backend plus `svg` | Dependency check passed; no supported pipeline/backend E2E selected |
| Sparse attention | VSA | `technique/sparse_attention/vsa`, local backend adapter | Blocked: `vsa` / `st_attn` build failed in the shared CUDA 13/aarch64 env |
| Quantization | NVFP4 | `technique/quantization/nvfp4`, ModelOpt/TE path | Blocked: `transformer_engine` failed to install/import; BF16 fallback paths ran |
| Quantization | Diffusion PTQ | `technique/quantization/diffusion_ptq`, reference adapter | Dependency check passed; no calibrated video checkpoint selected |
| Quantization | SVDQuant / Nunchaku | `technique/quantization/svdquant_nunchaku`, local Nunchaku path | Dependency check passed; no compatible quantized video checkpoint selected |
| Quantization | SageAttention | `technique/quantization/sageattention`, local backend | Dependency check passed; no compatible video backend E2E selected |
| Quantization | ModelOpt / FP8 | `technique/quantization/modelopt_fp8`, local ModelOpt path | Dependency check passed; no FP8-exported video checkpoint selected |

## Dependency Notes

- `cache-dit`, `tomesd`, `svg`, `sageattention`, `nunchaku`, and `modelopt` are present in the shared environment.
- `spas_sage_attn`, `vsa`, `st_attn`, and `transformer_engine` are not usable in the shared environment from this pass.
- `scripts/postinstall_cuda_jit.sh` now pins `nvidia-cuda-cccl==13.2.75` to match the CUDA 13.2 compiler wheel series used by the JIT toolchain.
