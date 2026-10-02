# ================= CSEPrompts manual cleaning =================
# task: academic/008 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by
#   omitting vowels, much like Twitter was originally called twttr. Implement a program that prompts
#   the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and
#   U) omitted, whether inputted in uppercase or lowercase.
# ---- model response below: edit from here ----
def omit_vowels(text):
    """
    Omit all vowels (A, E, I, O, and U) from the input text.

    Args:
        text (str): The input text.

    Returns:
        str: The text with all vowels omitted.
    """
    vowels = 'AEIOUaeiou'
    return ''.join([char for char in text if char not in vowels])

def main():
    # Prompt the user for a string of text
    text = input("Please enter a string of text: ")

    # Omit vowels from the text
    text_without_vowels = omit_vowels(text)

    # Print the result
    print("Text without vowels:", text_without_vowels)

if __name__ == "__main__":
    main()