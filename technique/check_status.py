"""Check normalized technique adapter availability.

This is intentionally lightweight: it imports adapter modules and asks each
adapter to resolve dependencies without downloading models or launching GPU work.
End-to-end video tests are tracked separately in ``manifest.json``.
"""

from __future__ import annotations

import argparse
import importlib
import json
import subprocess
import sys
from pathlib import Path


def _check_adapter_in_process(adapter: str) -> dict:
    module = importlib.import_module(adapter)
    return {
        "adapter_import": True,
        "dependencies": module.dependency_status(),
    }


def _check_adapter(adapter: str, timeout_s: float, in_process: bool) -> dict:
    if in_process:
        try:
            return _check_adapter_in_process(adapter)
        except Exception as exc:  # pragma: no cover - diagnostic path
            return {
                "adapter_import": False,
                "dependencies": {"error": repr(exc)},
            }

    code = """
import importlib, json, sys
adapter = sys.argv[1]
try:
    module = importlib.import_module(adapter)
    out = {"adapter_import": True, "dependencies": module.dependency_status()}
except Exception as exc:
    out = {"adapter_import": False, "dependencies": {"error": repr(exc)}}
print(json.dumps(out, sort_keys=True))
"""
    try:
        proc = subprocess.run(
            [sys.executable, "-c", code, adapter],
            check=False,
            capture_output=True,
            text=True,
            timeout=timeout_s,
        )
    except subprocess.TimeoutExpired:
        return {
            "adapter_import": False,
            "dependencies": {"error": f"timeout after {timeout_s:g}s"},
        }
    if proc.returncode != 0:
        return {
            "adapter_import": False,
            "dependencies": {
                "error": f"subprocess exit {proc.returncode}",
                "stderr": proc.stderr.strip()[-1000:],
            },
        }
    try:
        return json.loads(proc.stdout.strip().splitlines()[-1])
    except Exception as exc:
        return {
            "adapter_import": False,
            "dependencies": {
                "error": f"invalid subprocess output: {exc!r}",
                "stdout": proc.stdout.strip()[-1000:],
                "stderr": proc.stderr.strip()[-1000:],
            },
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--timeout",
        type=float,
        default=60.0,
        help="per-adapter subprocess timeout in seconds",
    )
    parser.add_argument(
        "--in-process",
        action="store_true",
        help="check adapters in one process instead of isolated subprocesses",
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / "manifest.json").read_text())
    rows = []
    for category in manifest["categories"]:
        for method in category["methods"]:
            adapter = method.get("adapter")
            if not adapter:
                rows.append(
                    {
                        "id": method["id"],
                        "name": method["name"],
                        "implementation_status": method["implementation_status"],
                        "adapter_import": None,
                        "dependencies": {},
                    }
                )
                continue
            result = _check_adapter(adapter, args.timeout, args.in_process)
            rows.append(
                {
                    "id": method["id"],
                    "name": method["name"],
                    "implementation_status": method["implementation_status"],
                    "adapter_import": result["adapter_import"],
                    "dependencies": result["dependencies"],
                }
            )
    print(json.dumps(rows, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
