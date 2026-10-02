# ================= CSEPrompts manual cleaning =================
# task: codingsites/104 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Create a function that takes an object and returns the keys and values as separate arrays.
# ---- model response below: edit from here ----
def separate_keys_values(input_dict):
    """
    Separate keys and values from a dictionary.

    Args:
        input_dict (dict): The input dictionary.

    Returns:
        tuple: A tuple containing two lists, the first for keys and the second for values.
    """
    keys = list(input_dict.keys())
    values = list(input_dict.values())
    return keys, values