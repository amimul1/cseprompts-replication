# ================= CSEPrompts manual cleaning =================
# task: academic/051 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Imagine you're writing a cash register application. To make
#   #interaction easier on the user, it doesn't have separate
#   #areas for passwords, PIN numbers, or cash totals --
#   #instead, it looks at what the cashier enters and infers
#   #whether it's their PIN number, their password, or the cash
#   #total for a transaction.
#   #
#   #The register makes this decision with the following rules:
#   #
#   # - If the cashier entered only digits, then it's a PIN
#   #   number.
#   # - If the cashier entered a decimal number, then it's the
#   #   transaction amount.
#   # - If the cashier entered anything else, then it's their
#   #   password.
#   #
#   #Write a function named interpretCashier. interpretCashier
#   #should take one parameter as input, which will always be
#   #a string initially.
#   #
#   # - If the string entered represents a PIN number, return
#   #   "PIN".
#   # - If the string entered represents a transaction amount,
#   #   return "Transaction".
#   # - If the string entered represents a password, return
#   #   "Password".
#   #
#   #Hint: There is a very easy way to do this, and a very hard
#   #way to do this. Remember, this test is on control
#   #structures, not strings.
# ---- model response below: edit from here ----
### Interpreting Cashier Input
def interpretCashier(input_str):
    """
    Determine the type of input based on the cashier's entry.

    Args:
        input_str (str): The input string from the cashier.

    Returns:
        str: The type of input ("PIN", "Transaction", or "Password").
    """
    if input_str.replace('.', '', 1).isdigit():  # Check if the string is a PIN or transaction amount
        return "PIN" if input_str.isdigit() else "Transaction"
    else:  # If the string is not a PIN or transaction amount, it's a password
        return "Password"
