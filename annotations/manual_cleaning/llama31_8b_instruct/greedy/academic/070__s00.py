# ================= CSEPrompts manual cleaning =================
# task: academic/070 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #APA citation style cites author names like this:
#   #
#   #  Last, F., Joyner, D., Burdell, G.
#   #
#   #Note the following:
#   #
#   # - Each individual name is listed as the last name, then a
#   #   comma, then the first initial, then a period.
#   # - The names are separated by commas, including the last
#   #   two.
#   # - There is no space or comma following the last period.
#   #
#   #Write a function called names_to_apa. names_to_apa should
#   #take as input one string, and return a reformatted string
#   #according to the style given above. You can assume that
#   #the input string will be of the following format:
#   #
#   #  First Last, David Joyner, and George Burdell
#   #
#   #You may assume the following:
#   #
#   # - There will be at least three names, with "and" before
#   #   the last name.
#   # - Each name will have exactly two words.
#   # - There will be commas between each pair of names.
#   # - The word 'and' will precede the last name.
#   # - The names will only be letters (no punctuation, special
#   #   characters, etc.), and first and last name will both be
#   #   capitalized.
#   #
#   #Hint: You can use the string replace() method to delete
#   #text from a string. For example, a_string.replace("hi", "")
#   #will delete all instances of "hi". There are multiple ways
#   #you might choose to use this.
# ---- model response below: edit from here ----
def names_to_apa(s):
    """
    Reformat a string of names to APA citation style.

    Args:
        s (str): The input string of names.

    Returns:
        str: The reformatted string in APA citation style.
    """
    # Split the string into a list of names
    names = s.split(', ')

    # Remove the word 'and' from the last name
    if len(names) > 1:
        last_name = names.pop(-1)
        names[-1] = names[-1].replace('and', '')

    # Capitalize the first letter of each name
    names = [name.capitalize() for name in names]

    # Split each name into first and last names
    names = [name.split() for name in names]

    # Format each name as Last, F.
    names = [f"{last[0]}. {first[0]}. " for last, first in names]

    # Join the names with commas
    apa_string = ', '.join(names)

    # Remove the trailing space and period
    apa_string = apa_string.strip(' .')

    return apa_string

# Example usage:
print(names_to_apa("First Last, David Joyner, and George Burdell"))