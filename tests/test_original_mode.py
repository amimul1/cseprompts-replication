"""The `original` suites reproduce each release as-is: every released expected value is kept.

The current release is 57275c2 (data/processed/pytest/original/); the OUTDATED release 58d7ea0, used by
the paper, is kept in data/processed/pytest_OUTDATED_58d7ea0/original/.
"""

import json

from cseprompts.data import load_coding, load_mcq
from cseprompts.harness.build import SUITE_DIRS
from cseprompts.harness.runner import evaluate

CURRENT = SUITE_DIRS["57275c2"] / "original"
OUTDATED = SUITE_DIRS["58d7ea0"] / "original"


def manifest(suite):
    return [json.loads(line) for line in (suite / "tasks.jsonl").read_text().splitlines() if line.strip()]


def test_current_suite_covers_the_whole_release_with_every_released_test():
    tasks = manifest(CURRENT)
    assert len(tasks) == 219
    assert [t["uid"] for t in tasks if t["n_tests"] == 0] == []  # Academic #90 now has tests
    released = {p.uid: len(p.tests) for split in ("codingsites", "academic") for p in load_coding(split, "57275c2")}
    for t in tasks:  # each released test is a test, except release header lines that are not tests
        assert t["n_tests"] + len(t["skipped_release_fragments"]) == released[t["uid"]], t["uid"]


def test_current_release_values_are_used_as_released():
    # CodingSites #24 test 1 is True in 57275c2 (it was False in 58d7ea0)
    assert "check(call(m, TASK, (45, 50), {}), True, 'eq')" in (CURRENT / "codingsites" / "test_024.py").read_text()
    prompt_correct = "def f(a, b):\n    return a + b < 100\n"
    res = evaluate(prompt_correct, CURRENT / "codingsites" / "test_024.py", "function")
    assert (res["label_name"], res["n_passed"], res["n_tests"]) == ("ALL_PASSED", 5, 5)
    # Academic #13 test 4 still says "4 POTATOES" in 57275c2 and is kept as released
    assert "4 POTATOES" in (CURRENT / "academic" / "test_013.py").read_text()


def test_current_release_mcq_has_100_distinct_questions():
    qs = load_mcq("57275c2")
    assert len(qs) == 100 and len({q.prompt for q in qs}) == 100


def test_outdated_suite_covers_the_old_release():
    tasks = manifest(OUTDATED)
    assert len(tasks) == 219
    no_tests = [t["uid"] for t in tasks if t["n_tests"] == 0]
    assert no_tests == ["academic/090"]  # its released test field held no test cases


def test_outdated_released_values_are_kept_even_when_they_contradict_the_prompt():
    # CodingSites #24: "return True if the sum is less than 100"; 58d7ea0 test 1 expects False for 45 + 50
    assert "check(call(m, TASK, (45, 50), {}), False, 'eq')" in (OUTDATED / "codingsites" / "test_024.py").read_text()
    prompt_correct = "def f(a, b):\n    return a + b < 100\n"
    res = evaluate(prompt_correct, OUTDATED / "codingsites" / "test_024.py", "function")
    assert (res["label_name"], res["n_passed"], res["n_tests"]) == ("PARTIAL", 4, 5)


def test_a_correct_solution_passes_a_task_whose_released_tests_are_right():
    code = "def count_online(d):\n    return sum(1 for v in d.values() if v == 'online')\n"
    for suite in (CURRENT, OUTDATED):
        assert evaluate(code, suite / "codingsites" / "test_003.py", "function")["label_name"] == "ALL_PASSED"
