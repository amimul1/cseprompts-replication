"""Prompt templates copied from the CSEPrompts 2.0 paper (Figs. 1 and 2).

Each figure shows three parts: "a system prompt, the task description, and the
instruction".  The paper does not say how the parts were joined or which chat
roles were used, so ``paper_messages`` follows the figure literally: part 1 is
the system message and parts 2 and 3 form the user message.  How each model
actually receives that (chat template, merged user turn, or plain text for base
models) is decided in ``render`` and recorded with every generation.
"""

from __future__ import annotations

CODE_SYSTEM = "You are a helpful AI assistant. You are given the following problem : "
CODE_INSTRUCTION = "Please write a Python code snippet to solve the problem. Thanks."

MCQ_SYSTEM = "You are a helpful AI assistant. You are given a Multiple Choice Question. "
MCQ_INSTRUCTION = "You need to pick one or multiple correct answers from the given ones. Thanks."


def paper_messages(body: str, kind: str) -> list[dict]:
    system, instruction = (CODE_SYSTEM, CODE_INSTRUCTION) if kind == "code" else (MCQ_SYSTEM, MCQ_INSTRUCTION)
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": f"{body}\n{instruction}"},
    ]


def flatten(messages: list[dict]) -> str:
    """All three parts as one text, in the figure's order, one per line."""
    return "\n".join(m["content"] for m in messages)


def paper_code_prompt(task: str) -> str:
    return flatten(paper_messages(task, "code"))


def paper_mcq_prompt(question: str) -> str:
    return flatten(paper_messages(question, "mcq"))


def render(messages: list[dict], tokenizer, mode: str = "auto") -> tuple[str, str]:
    """Turn the paper's messages into the exact string the model sees.

    Modes:
      chat-system  model's chat template, paper part 1 as the system message
      chat-user    model's chat template, all three parts in one user message
      plain        no template: the three parts as plain text (base/completion models)
      auto         chat-system; if the template rejects a system role -> chat-user;
                   if the model has no chat template -> plain
    Returns (rendered_text, mode_used).
    """
    if mode == "plain" or (mode == "auto" and not getattr(tokenizer, "chat_template", None)):
        return flatten(messages), "plain"

    def apply(msgs):
        return tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)

    merged = [{"role": "user", "content": flatten(messages)}]
    if mode == "chat-user":
        return apply(merged), "chat-user"
    try:
        return apply(messages), "chat-system"
    except Exception:
        if mode == "chat-system":
            raise
        return apply(merged), "chat-user"
