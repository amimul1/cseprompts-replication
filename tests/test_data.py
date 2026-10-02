from cseprompts.data import load_coding, load_mcq, parse_test_cases
from cseprompts.prompts import CODE_SYSTEM, paper_code_prompt, paper_messages, render


def test_split_sizes_match_paper():
    assert len(load_coding("codingsites")) == 118
    assert len(load_coding("academic")) == 101
    assert len(load_mcq()) == 100


def test_inline_and_multiline_test_cases_parse():
    inline = parse_test_cases('Test Case 1:\nInput: "hello"\nOutput: "l"')
    multiline = parse_test_cases("Test Case 1:\nFunction Call:\nf(1)\nExpected Output:\n2")
    assert (inline[0].input, inline[0].expected_output) == ('"hello"', '"l"')
    assert (multiline[0].input, multiline[0].expected_output) == ("f(1)", "2")


def test_most_tests_parse():
    tests = [t for s in ("codingsites", "academic") for p in load_coding(s) for t in p.tests]
    assert sum(t.parsed for t in tests) / len(tests) > 0.98


def test_paper_prompt_format():
    p = paper_code_prompt("Write f.")
    assert p.startswith("You are a helpful AI assistant.") and p.endswith("Thanks.")


class _NoTemplate:  # like bigcode/starcoder2-7b, WizardCoder-15B
    chat_template = None


class _SystemOK:  # like CodeLlama / Magicoder
    chat_template = "..."

    def apply_chat_template(self, msgs, tokenize, add_generation_prompt):
        return "|".join(f"{m['role']}:{m['content']}" for m in msgs)


class _NoSystem(_SystemOK):  # like Mistral-7B-Instruct-v0.1, which raises on a system role
    def apply_chat_template(self, msgs, tokenize, add_generation_prompt):
        if msgs[0]["role"] == "system":
            raise ValueError("roles must alternate user/assistant")
        return super().apply_chat_template(msgs, tokenize, add_generation_prompt)


def test_paper_messages_follow_figure_1():
    msgs = paper_messages("Write f.", "code")
    assert msgs[0] == {"role": "system", "content": CODE_SYSTEM}
    assert msgs[1]["content"] == "Write f.\nPlease write a Python code snippet to solve the problem. Thanks."


def test_render_modes():
    msgs = paper_messages("Write f.", "code")
    assert render(msgs, _NoTemplate())[1] == "plain"
    assert render(msgs, _SystemOK())[1] == "chat-system"
    text, mode = render(msgs, _NoSystem())
    assert mode == "chat-user" and text.startswith("user:" + CODE_SYSTEM)
