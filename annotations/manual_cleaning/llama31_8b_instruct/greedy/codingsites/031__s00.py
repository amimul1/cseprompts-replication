# ================= CSEPrompts manual cleaning =================
# task: codingsites/031 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23.
#   We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if
#   we are in trouble.
# ---- model response below: edit from here ----
def is_troubled(hour: int) -> bool:
    """
    Returns True if we are in trouble with the parrot, False otherwise.

    We are in trouble if the parrot is talking and the hour is before 7 or after 20.
    """
    return 0 <= hour < 7 or 20 < hour <= 23