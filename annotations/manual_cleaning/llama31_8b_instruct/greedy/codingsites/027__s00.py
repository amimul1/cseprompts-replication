# ================= CSEPrompts manual cleaning =================
# task: codingsites/027 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are
#   on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep
#   in.
# ---- model response below: edit from here ----
def can_sleep_in(weekday, vacation):
    """
    Returns True if we sleep in, False otherwise.

    Parameters:
    weekday (bool): Whether it is a weekday.
    vacation (bool): Whether we are on vacation.

    Returns:
    bool: Whether we sleep in.
    """
    return not weekday or vacation