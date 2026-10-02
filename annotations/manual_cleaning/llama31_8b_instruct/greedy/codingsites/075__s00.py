# ================= CSEPrompts manual cleaning =================
# task: codingsites/075 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a generator function that generates the Fibonacci sequence up to n.
# ---- model response below: edit from here ----
def fibonacci(n):
    """
    Generator function to generate the Fibonacci sequence up to the nth number.

    Args:
        n (int): The number of Fibonacci numbers to generate.

    Yields:
        int: The next Fibonacci number in the sequence.
    """
    if n <= 0:
        return
    elif n == 1:
        yield 0
    elif n == 2:
        yield 0
        yield 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            yield a
            a, b = b, a + b