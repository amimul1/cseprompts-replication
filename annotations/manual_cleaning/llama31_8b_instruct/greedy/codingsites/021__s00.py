# ================= CSEPrompts manual cleaning =================
# task: codingsites/021 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a function that takes an integer minutes and converts it to seconds.
# ---- model response below: edit from here ----
def minutes_to_seconds(minutes: int) -> int:
    """
    Converts minutes to seconds.

    Args:
        minutes (int): The number of minutes to convert.

    Returns:
        int: The equivalent number of seconds.
    """
    return minutes * 60
