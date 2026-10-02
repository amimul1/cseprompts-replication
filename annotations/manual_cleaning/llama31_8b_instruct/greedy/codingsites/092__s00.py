# ================= CSEPrompts manual cleaning =================
# task: codingsites/092 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Define a function named count that takes a single parameter. The parameter is a string. The
#   string will contain a single word divided into syllables by hyphens, such as these: "ho-tel",
#   "cat"
# ---- model response below: edit from here ----
def count(s):
    """
    Counts the number of syllables in a word.

    Args:
        s (str): A string containing a single word divided into syllables by hyphens.

    Returns:
        int: The number of syllables in the word.
    """
    # Remove any leading or trailing whitespace from the input string
    s = s.strip()
    
    # If the string is empty, return 0
    if not s:
        return 0
    
    # Split the string into syllables based on hyphens
    syllables = s.split('-')
    
    # Return the number of syllables
    return len(syllables)
