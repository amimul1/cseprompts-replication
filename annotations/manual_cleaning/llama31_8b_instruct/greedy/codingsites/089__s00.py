# ================= CSEPrompts manual cleaning =================
# task: codingsites/089 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   The tools inner and outer return the inner and outer product of two arrays.
# ---- model response below: edit from here ----

import numpy as np

def inner(arr1, arr2):
    """
    Calculate the inner product of two arrays.

    Args:
        arr1 (list or numpy array): The first array.
        arr2 (list or numpy array): The second array.

    Returns:
        float: The inner product of the two arrays.
    """
    return np.dot(arr1, arr2)

def outer(arr1, arr2):
    """
    Calculate the outer product of two arrays.

    Args:
        arr1 (list or numpy array): The first array.
        arr2 (list or numpy array): The second array.

    Returns:
        numpy array: The outer product of the two arrays.
    """
    return np.outer(arr1, arr2)
