"""Model registry and decoding protocols (configs/*.json)."""

from __future__ import annotations

import json
from functools import lru_cache

from cseprompts.data import REPO_ROOT

CONFIG_DIR = REPO_ROOT / "configs"


@lru_cache
def models() -> dict[str, dict]:
    return json.loads((CONFIG_DIR / "models.json").read_text())["models"]


@lru_cache
def protocols() -> dict[str, dict]:
    return json.loads((CONFIG_DIR / "protocols.json").read_text())["protocols"]


def model(key: str) -> dict:
    try:
        return models()[key]
    except KeyError:
        raise SystemExit(f"unknown model key {key!r}; known: {', '.join(models())}") from None


def protocol(name: str) -> dict:
    try:
        return protocols()[name]
    except KeyError:
        raise SystemExit(f"unknown protocol {name!r}; known: {', '.join(protocols())}") from None
