# ================= CSEPrompts manual cleaning =================
# task: codingsites/009 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a function that counts how many different countries are represented in a list of country
#   IDs.
# ---- model response below: edit from here ----
def count_unique_countries(country_ids):
    """
    Counts the number of unique countries in a list of country IDs.

    Args:
        country_ids (list): A list of country IDs.

    Returns:
        int: The number of unique countries.
    """
    return len(set(country_ids))