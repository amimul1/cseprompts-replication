# ================= CSEPrompts manual cleaning =================
# task: codingsites/097 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Create a function that takes two arguments: the original price and the discount percentage as
#   integers and returns the final price after the discount.
# ---- model response below: edit from here ----
def calculate_final_price(original_price, discount_percentage):
    """
    Calculate the final price after applying a discount.

    Args:
        original_price (int): The original price of the item.
        discount_percentage (int): The discount percentage.

    Returns:
        float: The final price after the discount.
    """
    # Ensure the discount percentage is not greater than 100
    if discount_percentage > 100:
        raise ValueError("Discount percentage cannot be greater than 100")

    # Calculate the discount amount
    discount_amount = (discount_percentage / 100) * original_price

    # Calculate the final price
    final_price = original_price - discount_amount

    return final_price