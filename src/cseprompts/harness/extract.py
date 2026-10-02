"""Automatic code extraction ("cleaning") from a model response.

The paper cleaned responses by hand ("manually cleaned to isolate the code").
This is the automatic, deterministic counterpart, written to follow the same
rules as the manual guidelines (docs/MANUAL_CLEANING.md) so the two tracks can
be compared:

  1. Collect fenced code blocks (```python, ```py, ``` or ~~~). Blocks tagged as
     another language or as output (bash, text, console, output...) are ignored.
     Blocks that parse as Python are concatenated in order; if none parse, the
     longest block is kept (so the syntax error is reported, not hidden).
  2. With no fences, take every maximal run of lines that parses as Python and
     contains a real statement (def/class/import/assignment/call/loop...).
  3. For function tasks ("function"/"custom"), keep only imports, function and
     class definitions, and top-level constants those definitions use. Drop
     example usage, prints, input() calls, tests and `if __name__ == "__main__":`
     blocks. For program tasks ("program"/"vars") keep the whole program.

Bump EXTRACTOR_VERSION whenever these rules change; it is stored with every result.
"""

from __future__ import annotations

import ast
import re
from dataclasses import dataclass, field

EXTRACTOR_VERSION = "1.0"

_FENCE = re.compile(r"(?P<fence>```|~~~)[ \t]*(?P<lang>[\w+#.-]*)[^\n]*\n(?P<body>.*?)(?:\n[ \t]*(?P=fence)|\Z)", re.S)
_PY_TAGS = {"", "python", "py", "python3", "py3", "python3.10", "python3.11", "python3.12", "pycon", "ipython"}
_STRONG = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom, ast.Assign,
           ast.AugAssign, ast.For, ast.While, ast.If, ast.With, ast.Try, ast.Return)


@dataclass
class Extraction:
    code: str
    method: str                      # fenced | unfenced | none
    n_blocks: int = 0
    parses: bool = False
    dropped: list[str] = field(default_factory=list)
    version: str = EXTRACTOR_VERSION


def _parses(src: str) -> bool:
    try:
        ast.parse(src)
        return True
    except (SyntaxError, ValueError):
        return False


def _strip_repl(src: str) -> str:
    """Turn a >>> REPL transcript into code (drop output lines)."""
    if not re.search(r"^\s*>>> ", src, re.M):
        return src
    out = []
    for ln in src.splitlines():
        if ln.lstrip().startswith(">>> ") or ln.lstrip() == ">>>":
            out.append(ln.lstrip()[4:])
        elif ln.lstrip().startswith("... "):
            out.append(ln.lstrip()[4:])
    return "\n".join(out)


def _fenced_blocks(text: str) -> list[str]:
    blocks = []
    for mt in _FENCE.finditer(text):
        lang = mt.group("lang").lower()
        if lang in _PY_TAGS:
            blocks.append(_strip_repl(mt.group("body")))
    return blocks


def _is_real_code(tree: ast.Module) -> bool:
    for node in ast.walk(tree):
        if isinstance(node, _STRONG):
            return True
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            return True
    return False


def _unfenced_segments(text: str) -> list[str]:
    lines = text.splitlines()
    n, i, segs = len(lines), 0, []
    while i < n:
        if not lines[i].strip():
            i += 1
            continue
        best = None
        for j in range(n, i, -1):
            chunk = "\n".join(lines[i:j])
            if _parses(chunk):
                try:
                    tree = ast.parse(chunk)
                except (SyntaxError, ValueError):
                    continue
                if _is_real_code(tree):
                    best = j
                break
        if best:
            segs.append("\n".join(lines[i:best]))
            i = best
        else:
            i += 1
    return segs


def _node_source(lines: list[str], node) -> str:
    start = min([node.lineno] + [d.lineno for d in getattr(node, "decorator_list", [])])
    return "\n".join(lines[start - 1:node.end_lineno])


def _names_used(node) -> set[str]:
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name)}


def keep_definitions(code: str) -> tuple[str, list[str]]:
    """Function tasks: keep imports, defs, classes and constants the defs use."""
    tree = ast.parse(code)
    lines = code.splitlines()
    defs = [n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef))]
    def_names = {d.name for d in defs}
    used = set().union(*(_names_used(d) for d in defs)) if defs else set()
    kept, dropped = [], []
    for node in tree.body:
        if isinstance(node, (ast.Import, ast.ImportFrom, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            kept.append(node)
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            names = {t.id for t in targets if isinstance(t, ast.Name)}
            calls_input = any(isinstance(c, ast.Call) and isinstance(c.func, ast.Name) and c.func.id == "input"
                              for c in ast.walk(node))
            is_lambda = isinstance(node.value, ast.Lambda)
            if names and not (names & def_names) and not calls_input and (names & used or is_lambda):
                kept.append(node)
            else:
                dropped.append(f"line {node.lineno}: {type(node).__name__}")
        else:
            dropped.append(f"line {node.lineno}: {type(node).__name__}")
    return "\n\n".join(_node_source(lines, n) for n in kept), dropped


def extract(text: str, kind: str) -> Extraction:
    blocks = _fenced_blocks(text)
    if blocks:
        good = [b for b in blocks if _parses(b)]
        if good:
            code, method = "\n\n".join(good), "fenced"
        else:
            code, method = max(blocks, key=len), "fenced"
        n_blocks = len(blocks)
    else:
        segs = _unfenced_segments(text)
        code, method, n_blocks = "\n\n".join(segs), ("unfenced" if segs else "none"), len(segs)
    code = code.strip("\n")
    if not code.strip():
        return Extraction("", "none", n_blocks)
    parses = _parses(code)
    dropped: list[str] = []
    if parses and kind in ("function", "custom"):
        code, dropped = keep_definitions(code)
    return Extraction(code + "\n" if code else "", method, n_blocks, parses, dropped)
