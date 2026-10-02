# ================= CSEPrompts manual cleaning =================
# task: codingsites/088 | model: llama31_8b_instruct | run: greedy | sample: 0
# PROGRAM task: keep the whole program the model wrote (input, processing, printing).
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   The tools dot and cross returns the dot and cross product of two arrays respectively.
# ---- model response below: edit from here ----
import numpy as np

def dot_product(vector1, vector2):
    """
    Calculate the dot product of two vectors.

    Args:
        vector1 (list or numpy array): The first vector.
        vector2 (list or numpy array): The second vector.

    Returns:
        float: The dot product of the two vectors.
    """
    return np.dot(vector1, vector2)

def cross_product(vector1, vector2):
    """
    Calculate the cross product of two vectors.

    Args:
        vector1 (list or numpy array): The first vector.
        vector2 (list or numpy array): The second vector.

    Returns:
        numpy array: The cross product of the two vectors.
    """
    return np.cross(vector1, vector2)
