# ================= CSEPrompts manual cleaning =================
# task: codingsites/003 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   The aim of this challenge is, given a dictionary of people's online status, to count the number
#   of people who are online.
# ---- model response below: edit from here ----
def count_online_users(status_dict):
    """
    Counts the number of people who are online.

    Args:
        status_dict (dict): A dictionary where keys are user names and values are their online status (True or False).

    Returns:
        int: The number of people who are online.
    """
    return sum(1 for status in status_dict.values() if status)

# Example usage:
status_dict = {
    'Alice': True,
    'Bob': False,
    'Charlie': True,
    'David': False,
    'Eve': True
}

online_count = count_online_users(status_dict)
print(f"Number of people online: {online_count}")