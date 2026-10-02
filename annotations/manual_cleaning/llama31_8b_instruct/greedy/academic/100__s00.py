# ================= CSEPrompts manual cleaning =================
# task: academic/100 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Pig Latin is a fictitious language. To translate a word into
#   #Pig Latin, you would take the consonants up until the first
#   #vowel, move them to the end, and add "ay" to the end.
#   #
#   #For example:
#   #
#   # pig -> igpay
#   # david -> avidday
#   # trash -> ashtray
#   # scram -> amscray
#   # translate -> anslatetray
#   #
#   #Write a function called to_pig_latin. to_pig_latin will take
#   #as input a single word, and return the Pig Latin version of
#   #the word.
#   #
#   #For the purposes of this problem, only a, e, i, o, and u are
#   #vowels: y is a consonant. You may assume that the word will
#   #start with at least one consonant, that the letters to move to
#   #the end will always be the consonants until the first vowel,
#   #and that the string will be all lower-case.
# ---- model response below: edit from here ----
### Pig Latin Translator Function
def to_pig_latin(word):
    """
    Translate a word into Pig Latin.

    Args:
        word (str): The word to translate.

    Returns:
        str: The Pig Latin version of the word.
    """
    # Define the vowels
    vowels = 'aeiou'

    # Find the index of the first vowel in the word
    for i, char in enumerate(word):
        if char in vowels:
            # Move the consonants to the end and add 'ay'
            return word[i:] + word[:i] + 'ay'

