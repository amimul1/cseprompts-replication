# ================= CSEPrompts manual cleaning =================
# task: codingsites/077 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE

def calculate_operations(a, b):
    """
    Calculate the sum, product, and difference of two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        tuple: A tuple containing the sum, product, and difference of a and b.
    """
    sum_result = a + b
    product_result = a * b
    difference_result = a - b

    return sum_result, product_result, difference_result