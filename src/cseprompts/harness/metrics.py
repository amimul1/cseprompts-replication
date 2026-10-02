"""pass@k (Chen et al., 2021; Eq. 1 of the CSEPrompts 2.0 paper) and simple uncertainty estimates."""

from __future__ import annotations

import random
from math import comb


def pass_at_k(n: int, c: int, k: int) -> float:
    """Unbiased estimator 1 - C(n-c, k) / C(n, k) for one task with n samples, c correct."""
    if n - c < k:
        return 1.0
    return 1.0 - comb(n - c, k) / comb(n, k)


def mean(xs) -> float:
    xs = list(xs)
    return sum(xs) / len(xs) if xs else float("nan")


def bootstrap_ci(per_task: list[float], iters: int = 2000, seed: int = 0, alpha: float = 0.05) -> tuple[float, float]:
    """Percentile bootstrap over tasks for the mean of per-task scores."""
    if not per_task:
        return float("nan"), float("nan")
    rng = random.Random(seed)
    n = len(per_task)
    means = sorted(sum(per_task[rng.randrange(n)] for _ in range(n)) / n for _ in range(iters))
    lo = means[int(alpha / 2 * iters)]
    hi = means[min(iters - 1, int((1 - alpha / 2) * iters))]
    return lo, hi
