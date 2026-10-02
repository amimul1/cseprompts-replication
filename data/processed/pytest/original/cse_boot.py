"""Run one candidate *program* in a guarded child process.

Usage (by cse_runtime.run_program):  python cse_boot.py <candidate.py>

Before running the candidate as __main__ this:
  * limits CPU time, file size and (on Linux) memory;
  * sends input() prompt text to stderr, so stdout holds only what the program
    prints (CS50-style prompts like "Greeting: " must not break output checks);
  * optionally fixes random numbers (CSE_RANDOM_SEQ, a JSON list consumed in
    order by randint/randrange/choice) and today's date (CSE_TODAY=YYYY-MM-DD);
  * disables destructive/escaping calls (file deletion, process spawning,
    sockets) -- the same idea as HumanEval's reliability_guard. This is a
    safety net for model-written intro-CS code, not a security boundary.
"""

import builtins
import json
import os
import runpy
import sys


def _limits():
    try:
        import resource
    except ImportError:  # pragma: no cover
        return
    cpu = int(os.environ.get("CSE_CPU_SECONDS", "10"))
    resource.setrlimit(resource.RLIMIT_CPU, (cpu, cpu + 1))
    fsize = 16 * 1024 * 1024
    resource.setrlimit(resource.RLIMIT_FSIZE, (fsize, fsize))
    if sys.platform.startswith("linux"):
        mem = int(os.environ.get("CSE_MEMORY_MB", "2048")) * 1024 * 1024
        resource.setrlimit(resource.RLIMIT_AS, (mem, mem))


def _quiet_input(prompt=""):
    if prompt:
        sys.stderr.write(str(prompt))
        sys.stderr.flush()
    line = sys.stdin.readline()
    if line == "":
        raise EOFError("EOF when reading a line")
    return line[:-1] if line.endswith("\n") else line


def _fix_random():
    seq = os.environ.get("CSE_RANDOM_SEQ")
    if not seq:
        return
    values = json.loads(seq)
    import random

    it = iter(values)

    def nxt(*_a, **_k):
        try:
            return next(it)
        except StopIteration:
            raise RuntimeError("CSE_RANDOM_SEQ exhausted") from None

    random.randint = nxt
    random.randrange = nxt
    random.choice = lambda seq_: nxt()


def _fix_today():
    today = os.environ.get("CSE_TODAY")
    if not today:
        return
    import datetime as _dt

    y, m, d = (int(x) for x in today.split("-"))

    class _Date(_dt.date):
        @classmethod
        def today(cls):
            return cls(y, m, d)

    class _DateTime(_dt.datetime):
        @classmethod
        def now(cls, tz=None):
            return cls(y, m, d)

        @classmethod
        def today(cls):
            return cls(y, m, d)

    _dt.date = _Date
    _dt.datetime = _DateTime


def guard(inprocess: bool = False):
    """inprocess=True is used inside the pytest process (function tasks), where pytest
    itself still needs os.chdir and os.putenv; child program runs get the full guard."""
    import shutil
    import socket
    import subprocess

    def blocked(name):
        def _f(*_a, **_k):
            raise PermissionError(f"{name} is disabled in the evaluation sandbox")
        return _f

    for name in ("system", "remove", "unlink", "rmdir", "removedirs", "rename", "renames", "replace",
                 "truncate", "kill", "killpg", "fork", "forkpty", "execv", "execve", "execl", "execle",
                 "execlp", "execvp", "execvpe", "popen", "spawnl", "spawnv", "putenv", "chmod", "chown",
                 "setuid", "setgid", "chdir", "fchdir"):
        if inprocess and name in ("chdir", "fchdir", "putenv"):  # pytest needs these between tests
            continue
        if hasattr(os, name):
            setattr(os, name, blocked(f"os.{name}"))
    for name in ("rmtree", "move", "chown"):
        setattr(shutil, name, blocked(f"shutil.{name}"))
    for name in ("Popen", "run", "call", "check_call", "check_output", "getoutput", "getstatusoutput"):
        setattr(subprocess, name, blocked(f"subprocess.{name}"))
    socket.socket = blocked("socket.socket")
    socket.create_connection = blocked("socket.create_connection")


def main():
    path = sys.argv[1]
    _limits()
    builtins.input = _quiet_input
    _fix_random()
    _fix_today()
    guard()
    sys.argv = [path]
    runpy.run_path(path, run_name="__main__")


if __name__ == "__main__":
    main()
