# ================= CSEPrompts manual cleaning =================
# task: academic/015 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Because emoji aren’t quite as easy to type as text, at least on laptops and desktops, some
#   programs support “codes,” whereby you can type, for instance, :thumbs_up:, which will be
#   automatically converted to 👍. Some programs additionally support aliases, whereby you can more
#   succinctly type, for instance, :thumbsup:, which will also be automatically converted to 👍.
#   
#   See carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a list of codes with
#   aliases.
#   
#   Implement a program that prompts the user for a str in English and then outputs the “emojized”
#   version of that str, converting any codes (or aliases) therein to their corresponding emoji.
# ---- model response below: edit from here ----
import re

# Dictionary mapping codes and aliases to their corresponding emojis
emoji_map = {
    "thumbs_up": "👍",
    "thumbsup": "👍",
    # Add more mappings as needed
}

def emojize(text):
    """
    Replace codes and aliases in the input text with their corresponding emojis.
    
    Args:
        text (str): The input text to be emojized.
    
    Returns:
        str: The emojized text.
    """
    for code, emoji in emoji_map.items():
        # Use regular expression to find the code or alias in the text
        # The '\b' is a word boundary to prevent matching parts of other words
        text = re.sub(r'\b' + re.escape(code) + r'\b', emoji, text, flags=re.IGNORECASE)
    return text

def main():
    # Prompt the user for input
    text = input("Enter a string: ")
    
    # Emojize the input text
    emojized_text = emojize(text)
    
    # Print the emojized text
    print(emojized_text)

if __name__ == "__main__":
    main()