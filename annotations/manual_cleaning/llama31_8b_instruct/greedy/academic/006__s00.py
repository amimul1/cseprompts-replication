# ================= CSEPrompts manual cleaning =================
# task: academic/006 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   In some languages, it’s common to use camel case (otherwise known as “mixed case”) for
#   variables’ names when those names comprise multiple words, whereby the first letter of the first
#   word is lowercase but the first letter of each subsequent word is uppercase. For instance,
#   whereas a variable for a user’s name might be called name, a variable for a user’s first name
#   might be called firstName, and a variable for a user’s preferred first name (e.g., nickname)
#   might be called preferredFirstName.
#   
#   Python, by contrast, recommends snake case, whereby words are instead separated by underscores
#   (_), with all letters in lowercase. For instance, those same variables would be called name,
#   first_name, and preferred_first_name, respectively, in Python.
#   
#   Implement a program that prompts the user for the name of a variable in camel case and outputs
#   the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.
# ---- model response below: edit from here ----
def camel_to_snake_case(camel_case_str):
    """
    Convert a camel case string to snake case.

    Args:
        camel_case_str (str): The camel case string to convert.

    Returns:
        str: The equivalent snake case string.
    """
    snake_case_str = ''
    for i, char in enumerate(camel_case_str):
        if char.isupper() and i != 0:
            snake_case_str += '_' + char.lower()
        else:
            snake_case_str += char.lower()
    return snake_case_str

# Example usage:
variable_name = input("Enter a variable name in camel case: ")
print("Snake case equivalent:", camel_to_snake_case(variable_name))