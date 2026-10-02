# ================= CSEPrompts manual cleaning =================
# task: academic/079 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #It's a well-known and indisputable fact that if you want
#   #to make your name sound fancy, you should list it as only
#   #your first two initials followed by your last name. For
#   #example, my full name is David Andrew Joyner, and therefore
#   #my fancy name is D. A. Joyner. (If you have two middle names,
#   #it's even better, but we'll assume we have only one -- we're
#   #C. S. Lewis, not J. R. R. Tolkien).
#   #
#   #Write a function called fancy_me. fancy_me should take as
#   #input a list of strings, each representing a full name (e.g.
#   #"David Andrew Joyner" or "First Middle Last". fancy_me should
#   #return a single string, formatting that list of names in this
#   #fancy style, like this:
#   #
#   #  F. M. Last, D. A. Joyner, G. P. Burdell
#   #
#   #Each individual name is the first initial, then a period, then
#   #a space, then the second initial, then a period, then a space,
#   #then the last name, then a comma. There is no comma after the
#   #last name in the list.
#   #
#   #For example:
#   #
#   #  fancy_me(["First Middle Last", "David Andrew Joyner", "George P Burdell"])
#   #
#   #...would return "F. M. Last, D. A. Joyner, G. P. Burdell"
# ---- model response below: edit from here ----
def fancy_me(names):
    """
    Format a list of full names into a string with fancy style.

    Args:
        names (list): A list of strings, each representing a full name.

    Returns:
        str: A string with the list of names formatted in fancy style.
    """
    return ', '.join(' '.join([name.split()[0][0] + '. ' + name.split()[1][0] + '. ' + name.split()[-1] for name in names])