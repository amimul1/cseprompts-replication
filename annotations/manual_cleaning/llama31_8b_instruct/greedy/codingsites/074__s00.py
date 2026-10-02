# ================= CSEPrompts manual cleaning =================
# task: codingsites/074 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Return True if the given string contains an appearance of "xyz" where the xyz is not directly
#   preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
# ---- model response below: edit from here ----
def check_xyz(s):
    """
    Returns True if the given string contains an appearance of "xyz" 
    where the xyz is not directly preceeded by a period (.).
    
    Parameters:
    s (str): The input string to check.
    
    Returns:
    bool: True if "xyz" appears without a preceding period, False otherwise.
    """
    return "xyz" in s and s.find("xyz") != s.rfind("xyz")