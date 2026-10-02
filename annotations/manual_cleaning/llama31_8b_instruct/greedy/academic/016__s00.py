# ================= CSEPrompts manual cleaning =================
# task: academic/016 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these
#   lyrics, wherein “adieu” means “goodbye” in French:
#   
#   Adieu, adieu, to yieu and yieu and yieu
#   
#   Of course, the line isn’t grammatically correct, since it would typically be written (with an
#   Oxford comma) as:
#   
#   Adieu, adieu, to yieu, yieu, and yieu
#   
#   To be fair, “yieu” isn’t even a word; it just rhymes with “you”!
#   
#   In a file called adieu.py, implement a program that prompts the user for names, one per line,
#   until the user inputs control-d. Assume that the user will input at least one name. Then bid
#   adieu to those names, separating two names with one and, three names with two commas and one
#   and, and
#    names with
#    commas and one and, as in the below:
#   
#   Adieu, adieu, to Liesl
#   Adieu, adieu, to Liesl and Friedrich
#   Adieu, adieu, to Liesl, Friedrich, and Louisa
#   Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
#   Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
#   Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
#   Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
# ---- model response below: edit from here ----
def bid_adieu(names):
    """
    Bid adieu to a list of names, following the pattern of The Sound of Music song.
    
    Args:
        names (list): A list of names to bid adieu to.
    
    Returns:
        str: A string with the bid adieu message.
    """
    if len(names) == 1:
        return f"Adieu, adieu, to {names[0]}."
    elif len(names) == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}."
    elif len(names) == 3:
        return f"Adieu, adieu, to {names[0]}, {names[1]}, and {names[2]}."
    else:
        # For 4 or more names, we need to add commas and "and" accordingly
        result = f"Adieu, adieu, to {', '.join(names[:-1])} and {names[-1]}."
        return result

def main():
    # Prompt the user for names until they input control-d
    names = []
    while True:
        try:
            name = input("Enter a name (or press Ctrl+D to finish): ")
            if name:
                names.append(name)
        except EOFError:
            break

    # Bid adieu to the names
    if names:
        print(bid_adieu(names))
    else:
        print("No names entered.")

if __name__ == "__main__":
    main()