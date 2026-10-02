# ================= CSEPrompts manual cleaning =================
# task: codingsites/060 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   The Josephus Problem is a theoretical problem related to a certain counting-out game. Create a
#   function that takes a number n and returns the last person to remain after a complex counting
#   out process.
# ---- model response below: edit from here ----
def josephus(n, k):
    """
    Returns the last person to remain after a Josephus process with n people and a step size of k.

    :param n: The number of people in the circle.
    :param k: The step size in the Josephus process.
    :return: The position of the last person to remain.
    """
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1