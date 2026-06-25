"""Shared utilities for technique adapters."""

from __future__ import annotations

from importlib.util import find_spec


def module_available(module_name: str) -> bool:
    """Return whether a Python module can be resolved without importing it."""

    try:
        return find_spec(module_name) is not None
    except Exception:
        return False


def dependency_status(*module_names: str) -> dict[str, bool]:
    return {name: module_available(name) for name in module_names}
