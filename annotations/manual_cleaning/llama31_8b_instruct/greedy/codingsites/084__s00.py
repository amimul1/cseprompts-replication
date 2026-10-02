# ================= CSEPrompts manual cleaning =================
# task: codingsites/084 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Consider a string, s="AABCAAADA" and an integer, k=3. We can split s into n/k=3 substrings where
#   each subtring, ti, consists of a contiguous block of k=3 characters in s. Then, use each ti to
#   create string ui such that: The characters in ui are a subsequence of the characters in ti. Any
#   repeat occurrence of a character is removed from the string such that each character in ui
#   occurs exactly once. In other words, if the character at some index j in ti occurs at a previous
#   index <j in ti, then do not include the character in string ui.
# ---- model response below: edit from here ----
def process_string(s, k):
    """
    Process a string s by splitting it into substrings of length k, 
    removing duplicates from each substring, and returning the resulting strings.

    Args:
        s (str): The input string.
        k (int): The length of each substring.

    Returns:
        list: A list of strings, each with unique characters from the corresponding substring.
    """
    # Calculate the number of substrings
    n = len(s) // k
    
    # Initialize an empty list to store the processed substrings
    processed_strings = []
    
    # Process each substring
    for i in range(n):
        # Extract the current substring
        substring = s[i*k:(i+1)*k]
        
        # Convert the substring to a set to remove duplicates and then convert it back to a list
        # This is because sets in Python cannot contain duplicate elements
        unique_chars = list(set(substring))
        
        # Sort the unique characters to maintain a consistent order
        unique_chars.sort()
        
        # Join the unique characters into a string and add it to the list
        processed_strings.append(''.join(unique_chars))
    
    return processed_strings
