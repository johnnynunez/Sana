# EasyCache

EasyCache is the cache policy selected for SANA-Video. It is a runtime-adaptive feature reuse method that balances speed and quality online instead of relying on a fixed offline schedule.

## Sol-Engine placement

Sol-Engine uses EasyCache in the SANA-Video denoising transformer path with
`--easycache 0.1` in the full optimization stack.

SANA-Video already uses an efficient linear-attention architecture, so EasyCache becomes the main algorithm-level acceleration component before kernel-level optimization is applied.

## Tunable knobs

- cache threshold: controls reuse aggressiveness.
- warmup: keeps early denoising steps dense when needed.
- subsampling: estimates feature change with reduced overhead.

## Validation

Use the same prompt, seed, scheduler, resolution, and frame count when comparing baseline and full optimization outputs.
