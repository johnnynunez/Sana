# Technique audit status

This page records the 2026-06-24 implementation and test pass for the Techniques section. The detailed machine-readable inventory is in `technique/manifest.json`; the full report is in `technique/status_report.md`.

## End-to-end checks

| Model | Covered methods | Status |
|---|---|---|
| SANA-Video | EasyCache, SANA fusion toggles, compile path | Passed |
| Cosmos3-Super | TeaCache | Passed |
| LTX-2.3 | Fixed-step cache, feature-norm pruning, PISA, LTX fusion stack | Passed |

## Blocked dependencies

| Method | Missing dependency | Result |
|---|---|---|
| SpargeAttention | `spas_sage_attn` | Build failed in the shared CUDA 13/aarch64 environment |
| VSA | `vsa`, `st_attn` | Build failed in the shared CUDA 13/aarch64 environment |
| NVFP4 | `transformer_engine` | True TE NVFP4 E2E not completed; BF16 fallback paths ran |
