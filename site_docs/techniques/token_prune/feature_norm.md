# Feature-norm pruning

Feature-norm pruning is the Sol-Engine token-pruning implementation used for LTX-2.3. It scores video tokens by feature norm, keeps the highest-salience tokens, runs the expensive block stack on that subset, and compensates dropped tokens from prior state.

## Sol-Engine placement

| Pipeline | Scope | Default role |
|---|---|---|
| LTX-2.3 | stage-2 midpoint steps | combines with PISA, KWL fusion, cache, and NVFP4 |

## Tunable knobs

- keep ratio.
- pruning steps.
- salience metric.
- compensation rule.
- prunable token seam.

## Validation

Middle-step pruning should preserve temporal coherence and late-step detail. Do not accept it from latency alone.
