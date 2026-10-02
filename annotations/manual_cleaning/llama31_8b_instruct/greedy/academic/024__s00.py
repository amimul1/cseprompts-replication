# ================= CSEPrompts manual cleaning =================
# task: academic/024 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   In Season 5, Episode 23 of NUMB3RS, a supposed IP address appears on screen, 275.3.6.28, which
#   isn’t actually a valid IPv4 (or IPv6) address.
#   
#   An IPv4 address is a numeric identifier that a device (or, on TV, hacker) uses to communicate on
#   the internet, akin to a postal address in the real world, typically formatted in dot-decimal
#   notation as #.#.#.#. But each # should be a number between 0 and 255, inclusive. Suffice it to
#   say 275 is not in that range! If only NUMB3RS had validated the address in that scene!
#   
#   In a file called numb3rs.py, implement a function called validate that expects an IPv4 address
#   as input as a str and then returns True or False, respectively, if that input is a valid IPv4
#   address or not.
# ---- model response below: edit from here ----
def validate(ip_address: str) -> bool:
    """
    Validate an IPv4 address.

    Args:
    ip_address (str): The IP address to be validated.

    Returns:
    bool: True if the IP address is valid, False otherwise.
    """
    # Split the IP address into its four parts
    parts = ip_address.split('.')

    # An IPv4 address should have exactly four parts
    if len(parts) != 4:
        return False

    # Check each part of the IP address
    for part in parts:
        # A part should be a digit
        if not part.isdigit():
            return False

        # Convert the part to an integer
        num = int(part)

        # A part should be between 0 and 255 (inclusive)
        if num < 0 or num > 255:
            return False

        # A part should not have leading zeros
        if len(part) > 1 and part[0] == '0':
            return False

    # If all checks pass, the IP address is valid
    return True
