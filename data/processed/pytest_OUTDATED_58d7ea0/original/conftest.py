"""pytest plumbing for the generated CSEPrompts suites.

Environment (set by the runner, cseprompts.harness.runner):
  CSE_CANDIDATE     path to the candidate .py file under test (required)
  CSE_RESULT        where to write the JSON report (optional)
  CSE_TEST_TIMEOUT  seconds per test (default 10)

Fixtures:
  m               the candidate imported as a module (function/class tasks), loaded
                  once, under the guard, with a time limit; if loading fails every
                  test that uses it errors and the report says why
  candidate_path  the candidate file (program tasks run it via cse_runtime.run_program)
"""

import importlib.util
import os
import signal
import sys
import time
import traceback

import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cse_boot  # noqa: E402
import cse_runtime  # noqa: E402

TIMEOUT = int(os.environ.get("CSE_TEST_TIMEOUT", "10"))
REPORT = {"load": None, "tests": {}, "resolved_entry": {}}


class TestTimeout(Exception):
    pass


def _alarm(_signum, _frame):
    raise TestTimeout(f"test exceeded {TIMEOUT}s")


@pytest.fixture(scope="session")
def candidate_path():
    path = os.environ.get("CSE_CANDIDATE")
    if not path or not os.path.exists(path):
        pytest.fail("CSE_CANDIDATE is not set or does not exist")
    return path


@pytest.fixture(scope="session")
def m(candidate_path):
    if REPORT["load"] is not None and not REPORT["load"]["ok"]:
        pytest.fail(f"candidate failed to load: {REPORT['load']['error']}")
    spec = importlib.util.spec_from_file_location("candidate", candidate_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["candidate"] = module
    old = signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(TIMEOUT)
    t0 = time.time()
    try:
        cse_boot.guard(inprocess=True)
        spec.loader.exec_module(module)
    except BaseException as exc:  # SyntaxError, NameError, EOFError from input(), SystemExit, timeout...
        REPORT["load"] = {"ok": False, "error": type(exc).__name__, "detail": "".join(
            traceback.format_exception_only(type(exc), exc)).strip()[-500:]}
        pytest.fail(f"candidate failed to load: {type(exc).__name__}")
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, old)
    REPORT["load"] = {"ok": True, "seconds": round(time.time() - t0, 3)}
    return module


@pytest.fixture(autouse=True)
def _per_test_timeout():
    old = signal.signal(signal.SIGALRM, _alarm)
    signal.alarm(TIMEOUT)
    yield
    signal.alarm(0)
    signal.signal(signal.SIGALRM, old)


def pytest_runtest_logreport(report):
    name = report.nodeid.split("::")[-1]
    entry = REPORT["tests"].setdefault(name, {"outcome": "passed", "error": None})
    if report.failed:
        entry["outcome"] = "error" if report.when != "call" else "failed"
        exc = getattr(report, "longrepr", None)
        etype = None
        if exc is not None and hasattr(exc, "reprcrash") and exc.reprcrash is not None:
            etype = exc.reprcrash.message.split(":")[0].strip()
        entry["error"] = etype
        entry["message"] = str(getattr(exc, "reprcrash", exc))[-400:] if exc is not None else None
    elif report.skipped and report.when in ("setup", "call"):
        entry["outcome"] = "skipped"


def pytest_sessionfinish(session, exitstatus):
    out = os.environ.get("CSE_RESULT")
    if out:
        REPORT["resolved_entry"] = cse_runtime.RESOLVED
        REPORT["exitstatus"] = int(exitstatus)
        cse_runtime.dump_json(out, REPORT)
