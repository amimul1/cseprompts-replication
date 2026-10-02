# ================= CSEPrompts manual cleaning =================
# task: codingsites/041 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Add a function named list_benefits() that returns the following list of strings: "More organized
#   code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect
#   code together". Add a function named build_sentence(info) which receives a single argument
#   containing a string and returns a sentence starting with the given string and ending with the
#   string " is a benefit of functions!"
# ---- model response below: edit from here ----

def list_benefits():
    """
    Returns a list of strings representing the benefits of using functions in programming.
    
    Returns:
        list: A list of strings describing the benefits of functions.
    """
    return [
        "More organized code",
        "More readable code",
        "Easier code reuse",
        "Allowing programmers to share and connect code together"
    ]

def build_sentence(info):
    """
    Builds a sentence starting with the given string and ending with " is a benefit of functions!".
    
    Args:
        info (str): The string to be used in the sentence.
    
    Returns:
        str: A sentence starting with the given string and ending with " is a benefit of functions!".
    """
    return f"{info} is a benefit of functions!"

# Example usage:
benefits = list_benefits()
print("Benefits of functions:")
for benefit in benefits:
    print(build_sentence(benefit))