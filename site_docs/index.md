# Sol-Engine

Sol-Engine is an efficiency-oriented inference framework for high-resolution video diffusion. It wraps Cosmos3-Super, LTX-2.3, and SANA-Video with one explicit acceleration line per model.

## Models and speedups

| Model | Params | Acceleration line | Speedup |
|---|:---:|---|:---:|
| [Cosmos3-Super (4xB200)](pipelines/cosmos3.md) | 64B | TeaCache + NVFP4 | ~2.26x |
| [LTX-2.3 (1xB200)](pipelines/ltx.md) | 22B | cache + PISA + NVFP4 + token-prune .. | 2.40x |
| [SANA-Video (1xB200)](pipelines/sana.md) | 2B | EasyCache + fusion + compile | 2.77x |

## The five acceleration methods

Video diffusion inference exposes redundancy at three complementary levels: **Algorithm level**: adjacent denoising steps run structurally similar computation over slowly changing latents. **Model level**: long spatiotemporal sequences contain redundant tokens and attention interactions. **Kernel level**: DiT blocks repeatedly launch memory-bound work around GEMMs, layout movement, normalization, activation, and precision conversion.

<table class="sol-methods-table">
  <thead>
    <tr>
      <th>Method</th>
      <th>Implemented entries</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="techniques/cache/">Cache</a></td>
      <td>TeaCache, EasyCache, fixed-step cache</td>
    </tr>
    <tr>
      <td><a href="techniques/quant/">Quantization</a></td>
      <td>NVFP4</td>
    </tr>
    <tr>
      <td><a href="techniques/kernel/">Kernel fusion</a></td>
      <td>KWL fusion, QKV merge, compile</td>
    </tr>
    <tr>
      <td><a href="techniques/sparse/">Sparse attention</a></td>
      <td>PISA, SpargeAttention, Sparse VideoGen, ...</td>
    </tr>
    <tr>
      <td><a href="techniques/token_prune/">Token pruning</a></td>
      <td>Feature-norm pruning, ToMe-SD, Astraea, ...</td>
    </tr>
  </tbody>
</table>

## Quick start

In Claude Code or Codex, run:

```text
/goal Execute the inference code for the three models using both baseline and full-opt
settings with the following requirements. Refer to AGENTS.md for the environment creation,
model download, and inference guides. For the environment, you need to create a new
environment. For model weights, you are allowed to reuse existing weights if they are
locally available; otherwise, you need to download them. Regarding adaptability, be aware
that the provided guides for environment creation, download scripts, and inference may
contain system incompatibilities, so you are expected to troubleshoot and adapt them to
your specific machine.
```

## Start here

- [Installation](installation.md): environment creation, CUDA JIT fixups, and model downloads.
- [Pipelines](pipelines/cosmos3.md): optimized launch paths for Cosmos3-Super, LTX-2.3, and SANA-Video.
- [Techniques](techniques/cache.md): the five acceleration methods and where they apply.

## Citation

```bibtex
@misc{li2026solvideoinferenceengine,
  title         = {Sol Video Inference Engine: Agent-Native Full-Stack Acceleration Framework for Efficient Video Generation},
  author        = {Yitong Li and Junsong Chen and Haopeng Li and Haozhe Liu and Jincheng Yu and Ligeng Zhu and Ping Luo and Song Han and Enze Xie},
  year          = {2026},
  eprint        = {2606.23743},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CV},
  doi           = {10.48550/arXiv.2606.23743},
  url           = {https://arxiv.org/abs/2606.23743},
}
```
