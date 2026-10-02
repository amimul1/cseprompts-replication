# ================= CSEPrompts manual cleaning =================
# task: codingsites/080 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a function that takes a Python object, serializes it to JSON, and returns the JSON string.
# ---- model response below: edit from here ----
import json

def serialize_to_json(obj):
    """
    Serialize a Python object to a JSON string.

    Args:
        obj (object): The Python object to serialize.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(obj, indent=4)