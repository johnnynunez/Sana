# KWL fusion

KWL fusion is Sol-Engine's custom kernel-fusion path for DiT glue operators. It targets memory-bound work around GEMMs and attention paths.

## Sol-Engine placement

| Pipeline | Scope | Role |
|---|---|---|
| LTX-2.3 | DiT block glue operators | operator-level optimization in the full stack |

## Candidate fusions

- AdaLN normalization, scale, shift, and residual gate.
- Q/K normalization and RoPE path.
- FFN projection plus activation.
- attention gate-to-output path.
- residual and modulation glue.

## Trade-off

KWL fusion should preserve the original block math apart from normal BF16 rounding. Keep it shape- and workload-specific; retain only fusions that improve the target deployment.
