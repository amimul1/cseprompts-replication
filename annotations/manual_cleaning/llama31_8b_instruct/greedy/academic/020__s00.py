# ================= CSEPrompts manual cleaning =================
# task: academic/020 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   implement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein
#   shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U)
#   omitted, whether inputted in uppercase or lowercase.
#   
#   here is the Setting up my twttr from Problem Set 2:
#   
#   When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by
#   omitting vowels, much like Twitter was originally called twttr. Implement a program that prompts
#   the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and
#   U) omitted, whether inputted in uppercase or lowercase.
# ---- model response below: edit from here ----
def shorten(text):
    """
    This function takes a string as input and returns the same string but with all vowels (A, E, I, O, and U) omitted, 
    whether inputted in uppercase or lowercase.
    
    Parameters:
    text (str): The input string to be shortened.
    
    Returns:
    str: The shortened string with vowels omitted.
    """
    vowels = 'AEIOUaeiou'
    return ''.join([char for char in text if char not in vowels])

def main():
    # Prompt the user for a string of text
    text = input("Please enter a string of text: ")
    
    # Call the shorten function and store the result
    shortened_text = shorten(text)
    
    # Print the shortened text
    print("The shortened text is: ", shortened_text)

if __name__ == "__main__":
    main()