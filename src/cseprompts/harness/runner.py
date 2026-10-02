"""Run one candidate against one task's generated pytest file and label the result.

Labels follow the paper's rubric (Guidelines.csv) and the column names of its
Results/Comparison.csv:

  0 NO_CODE        nothing to run (empty after cleaning)
  1 NOT_EXECUTED   the code cannot run: syntax error; for function/class tasks the
                   module fails (or times out) while loading; for program tasks every
                   test run crashes or times out
  2 ALL_FAILED     ran, but no test passed
  3 PARTIAL        some but not all tests passed
  4 ALL_PASSED     every test passed      <- what pass@1 counts

Candidates run in a fresh temporary directory, in a separate process, with a
minimal environment (no HF token or other secrets), a per-test time limit and the
cse_boot guard. See src/cseprompts/harness/runtime/.
"""

from __future__ import annotations

import ast
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

LABELS = {0: "NO_CODE", 1: "NOT_EXECUTED", 2: "ALL_FAILED", 3: "PARTIAL", 4: "ALL_PASSED"}


def _has_code(code: str) -> bool:
    try:
        tree = ast.parse(code)
    except SyntaxError:
        return bool(code.strip())
    return bool(tree.body) and not all(
        isinstance(n, ast.Expr) and isinstance(getattr(n, "value", None), ast.Constant) for n in tree.body)


def evaluate(code: str, test_file: Path, kind: str, *, test_timeout: int = 10, total_timeout: int = 180,
             extra_env: dict | None = None) -> dict:
    """Evaluate candidate source `code` with the pytest file `test_file`."""
    result = {"label": None, "label_name": None, "n_tests": None, "n_passed": 0, "reason": None,
              "load_error": None, "tests": {}, "resolved_entry": {}}
    if not _has_code(code):
        result.update(label=0, label_name=LABELS[0], reason="no_code")
        return result
    try:
        compile(code, "candidate.py", "exec")
    except (SyntaxError, ValueError) as exc:
        result.update(label=1, label_name=LABELS[1], reason="syntax_error", load_error=type(exc).__name__)
        return result

    suite_root = test_file.parents[1]
    with tempfile.TemporaryDirectory(prefix="cse_") as tmp:
        cand = Path(tmp) / "candidate.py"
        cand.write_text(code, encoding="utf-8")
        report_path = Path(tmp) / "report.json"
        env = {"PATH": os.environ.get("PATH", ""), "PYTHONHASHSEED": "0", "PYTHONDONTWRITEBYTECODE": "1",
               "PYTHONIOENCODING": "utf-8", "LANG": "C.UTF-8", "HOME": tmp,
               "CSE_CANDIDATE": str(cand), "CSE_RESULT": str(report_path), "CSE_TEST_TIMEOUT": str(test_timeout)}
        env.update(extra_env or {})
        cmd = [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider",
               "--rootdir", str(suite_root), "-c", str(suite_root / "pytest.ini"), str(test_file)]
        try:
            proc = subprocess.run(cmd, cwd=tmp, env=env, capture_output=True, text=True, timeout=total_timeout,
                                  stdin=subprocess.DEVNULL)
            timed_out = False
        except subprocess.TimeoutExpired:
            proc, timed_out = None, True
        report = json.loads(report_path.read_text()) if report_path.exists() else None

    if report is None:
        result.update(label=1, label_name=LABELS[1], reason="timeout" if timed_out else "harness_crash",
                      load_error="Timeout" if timed_out else None,
                      harness_stderr=(proc.stderr[-1500:] if proc is not None else None))
        return result

    tests = report.get("tests", {})
    n_tests = len(tests)
    n_passed = sum(1 for t in tests.values() if t["outcome"] == "passed")
    result.update(tests=tests, n_tests=n_tests, n_passed=n_passed, resolved_entry=report.get("resolved_entry", {}))
    load = report.get("load")
    if load is not None and not load.get("ok"):
        result.update(label=1, label_name=LABELS[1], reason="load_error", load_error=load.get("error"),
                      load_detail=load.get("detail"))
        return result
    if kind in ("program", "vars") and n_tests and n_passed == 0 and all(
            (t.get("message") or "").find("program crashed") >= 0 or (t.get("message") or "").find("timed out") >= 0
            for t in tests.values()):
        result.update(label=1, label_name=LABELS[1], reason="crashed_on_all_tests")
        return result
    if n_tests == 0:
        result.update(label=None, label_name="NO_TESTS", reason="task_has_no_tests")
        return result
    label = 4 if n_passed == n_tests else (2 if n_passed == 0 else 3)
    result.update(label=label, label_name=LABELS[label])
    return result
