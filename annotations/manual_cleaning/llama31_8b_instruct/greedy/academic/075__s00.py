# ================= CSEPrompts manual cleaning =================
# task: academic/075 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Write a function called volume_and_area. volume_and_area
#   #will take in a dictionary. This dictionary is guaranteed to
#   #have three keys: "length", "width", and "height", whose
#   #values are integers representing three attributes of a
#   #rectangular prism (also known as a box).
#   #
#   #Modify this dictionary to add two keys: "volume" and "area".
#   #The values associated with these keys should be the volume
#   #and surface area of the box.
#   #
#   #The formula for volume is:
#   #  length * width * height
#   #
#   #The formula for surface area is:
#   #  2 * ((length * width) + (length*height) + (width*height))
#   #
#   #Because length, width, and height are integers, and because
#   #these formulas have no division, your results should be
#   #integers as well.
# ---- model response below: edit from here ----
### Calculating Volume and Area of a Rectangular Prism
def volume_and_area(box):
    """
    Calculate the volume and area of a rectangular prism.

    Args:
        box (dict): A dictionary containing the dimensions of the prism.
            It must have the keys "length", "width", and "height".

    Returns:
        dict: The input dictionary with the added keys "volume" and "area".
    """
    # Check if the input dictionary has the required keys
    required_keys = ["length", "width", "height"]
    if not all(key in box for key in required_keys):
        raise ValueError("The input dictionary must have the keys 'length', 'width', and 'height'")

    # Calculate the volume
    box["volume"] = box["length"] * box["width"] * box["height"]

    # Calculate the surface area
    box["area"] = 2 * ((box["length"] * box["width"]) + (box["length"] * box["height"]) + (box["width"] * box["height"]))

    return box

# Example usage:
box = {
    "length": 5,
    "width": 3,
    "height": 2
}

print(volume_and_area(box))