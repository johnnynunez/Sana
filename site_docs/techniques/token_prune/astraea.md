# Astraea

Astraea searches token budgets for video DiTs under a performance target. It treats token reduction as a budget allocation problem rather than a fixed pruning rule.

## Role in Sol-Engine

Astraea is part of the token-pruning method family cited by the paper. It is useful when the target deployment needs an explicit speed budget and can search pruning ratios across layers or timesteps.

## Search knobs

- token budget.
- layer schedule.
- timestep schedule.
- quality constraint.

## Validation

Use a fixed validation set and inspect representative videos before composing the candidate with sparse attention or cache.
