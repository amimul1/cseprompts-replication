# ================= CSEPrompts manual cleaning =================
# task: academic/027 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   It’s not uncommon, in English, at least, to say “um” when trying to, um, think of a word. The
#   more you do it, though, the more noticeable it tends to be!
#   
#   In a file called um.py, implement a function called count that expects a line of text as input
#   as a str and returns, as an int, the number of times that “um” appears in that text, case-
#   insensitively, as a word unto itself, not as a substring of some other word. For instance, given
#   text like hello, um, world, the function should return 1. Given text like yummy, though, the
#   function should return 0.
# ---- model response below: edit from here ----
import re

def count_um(text: str) -> int:
    """
    Counts the number of times "um" appears in a given text, case-insensitively, as a whole word.

    Args:
        text (str): The input text to search for "um".

    Returns:
        int: The number of times "um" appears in the text.
    """
    # Convert the text to lowercase to make the search case-insensitive
    text = text.lower()
    
    # Use regular expression to find all occurrences of "um" as a whole word
    # The pattern '\bum\b' matches "um" as a whole word, where '\b' is a word boundary
    um_count = len(re.findall(r'\bum\b', text))
    
    return um_count

# Example usage:
print(count_um("hello, um, world"))  # Output: 1
print(count_um("yummy"))  # Output: 0
print(count_um("um, um, um, um"))  # Output: 3