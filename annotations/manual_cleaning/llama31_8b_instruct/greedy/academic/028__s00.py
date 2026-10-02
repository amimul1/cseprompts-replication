# ================= CSEPrompts manual cleaning =================
# task: academic/028 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   When creating a Google Form that prompts users for a short answer (or paragraph), it’s possible
#   to enable response validation and require that the user’s input match a regular expression. For
#   instance, you could require that a user input an email address with a regex like this one:
#   
#   ^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-
#   9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$
#   In a file called response.py, using either validator-collection or validators from PyPI,
#   implement a program that prompts the user for an email address via input and then prints Valid
#   or Invalid, respectively, if the input is a syntatically valid email address. You may not use
#   re. And do not validate whether the email address’s domain name actually exists.
# ---- model response below: edit from here ----
# response.py
from validator_collection import validators

def validate_email():
    """Prompt the user for an email address and print whether it's valid or not."""
    email = input("Please enter an email address: ")
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    validate_email()
