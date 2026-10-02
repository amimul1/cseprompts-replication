"""Record what produced a result: code version, environment, hardware, Slurm job.

Written into every run_meta.json, so any number in a report can be traced back
to the exact commit, packages and machine that produced it.
"""

from __future__ import annotations

import importlib.metadata
import os
import platform
import subprocess
import sys
import time

from cseprompts.data import REPO_ROOT


def _git(*args: str) -> str | None:
    try:
        return subprocess.run(["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, timeout=10).stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return None


def _version(pkg: str) -> str | None:
    try:
        return importlib.metadata.version(pkg)
    except importlib.metadata.PackageNotFoundError:
        return None


def _gpu() -> dict:
    info: dict = {}
    try:
        out = subprocess.run(
            ["nvidia-smi", "--query-gpu=name,memory.total,driver_version", "--format=csv,noheader"],
            capture_output=True, text=True, timeout=20,
        ).stdout.strip()
        info["nvidia_smi"] = out.splitlines()
    except (OSError, subprocess.SubprocessError):
        pass
    return info


def collect() -> dict:
    status = _git("status", "--porcelain")
    return {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "git_commit": _git("rev-parse", "HEAD"),
        "git_dirty": bool(status) if status is not None else None,
        "python": sys.version.split()[0],
        "packages": {p: _version(p) for p in ("vllm", "torch", "transformers", "huggingface_hub", "pytest", "numpy", "emoji", "validators", "inflect")},
        "host": platform.node(),
        "platform": platform.platform(),
        "slurm": {k: os.environ[k] for k in ("SLURM_JOB_ID", "SLURM_JOB_PARTITION", "SLURM_JOB_GPUS", "SLURM_JOB_NODELIST")
                  if k in os.environ},
        "gpu": _gpu(),
    }
