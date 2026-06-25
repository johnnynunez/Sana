# Technique Inventory

This directory is the normalized implementation layer for methods listed in
`site_docs/techniques`. The categories follow the processing order requested for
the inventory:

1. `cache`
2. `token_pruning`
3. `sparse_attention`
4. `quantization`

Each open-source method has an adapter directory under the corresponding
category. Local implementations re-export or point to the existing SGLang
runtime code; external methods expose dependency checks and the expected package
entry point. Methods marked `not-open-source` remain documented but intentionally
do not have implementation directories.

The current audit outcome is recorded in `status_report.md` and
`manifest.json`.

Use the shared repository environment described in `AGENTS.md`:

```bash
source scripts/use_code_storage_env.sh
conda activate "$PWD/.conda/ltx23"
```

Then run the lightweight adapter check:

```bash
PYTHONPATH="$PWD:$PWD/python" python technique/check_status.py
```

The checker runs each adapter in an isolated subprocess by default. Use
`--timeout N` to tune the per-adapter timeout for slow CUDA package imports.
