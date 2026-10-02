"""The `original` suite reproduces the release as-is: every released expected value is kept."""

import json

from cseprompts.harness.build import SUITE_DIR
from cseprompts.harness.runner import evaluate

ORIGINAL = SUITE_DIR / "original"


def test_original_suite_covers_the_whole_release():
    tasks = [json.loads(line) for line in (ORIGINAL / "tasks.jsonl").read_text().splitlines() if line.strip()]
    assert len(tasks) == 219
    no_tests = [t["uid"] for t in tasks if t["n_tests"] == 0]
    assert no_tests == ["academic/090"]  # its released test field holds no test cases


def test_released_values_are_kept_even_when_they_contradict_the_prompt():
    # CodingSites #24: "return True if the sum is less than 100"; release test 1 expects False for 45 + 50
    assert "check(call(m, TASK, (45, 50), {}), False, 'eq')" in (ORIGINAL / "codingsites" / "test_024.py").read_text()
    prompt_correct = "def f(a, b):\n    return a + b < 100\n"
    res = evaluate(prompt_correct, ORIGINAL / "codingsites" / "test_024.py", "function")
    assert (res["label_name"], res["n_passed"], res["n_tests"]) == ("PARTIAL", 4, 5)


def test_a_correct_solution_passes_a_task_whose_released_tests_are_right():
    code = "def count_online(d):\n    return sum(1 for v in d.values() if v == 'online')\n"
    assert evaluate(code, ORIGINAL / "codingsites" / "test_003.py", "function")["label_name"] == "ALL_PASSED"
