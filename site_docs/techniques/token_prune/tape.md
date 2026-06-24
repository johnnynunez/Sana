# TAPE

TAPE smooths token importance across frames to reduce temporal jitter in video diffusion token reduction.

## Role in Sol-Engine

TAPE is part of the token-pruning design space for long videos, where per-frame independent pruning decisions can create flicker.

## Search knobs

- importance smoothing window.
- keep ratio.
- layer placement.
- timestep placement.

## Validation

Focus on temporal flicker, subject consistency, and motion smoothness. A method can look acceptable frame-by-frame but fail over time.
