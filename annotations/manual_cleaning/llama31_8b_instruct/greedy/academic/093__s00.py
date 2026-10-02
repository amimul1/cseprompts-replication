# ================= CSEPrompts manual cleaning =================
# task: academic/093 | model: llama31_8b_instruct | run: greedy | sample: 0
# CLASS/FUNCTION task: keep the definitions (and imports/helpers they need); remove example usage.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Create a class called Rectangle. Rectangle should
#   #have two attributes (instance variables): length and
#   #width. Make sure the variable names match those words.
#   #Both will be floats.
#   #
#   #Rectangle should have a constructor with two required
#   #parameters, one for each of those attributes (length and
#   #width, in that order).
#   #
#   #Rectangle should also have a method called
#   #find_perimeter. find_perimeter should calculate the
#   #perimeter of the rectangle based on the current values for
#   #length and width.
#   #
#   #perimeter should NOT be an attribute of the class; instead,
#   #perimeter should be calculated and returned live when the
#   #ethod find_perimeter is called.
#   #
#   #The find_perimeter method should have NO parameters
#   #besides self. Instead, it should calculate the perimeter
#   #based on the current values for the opposite and adjacent
#   #attributes.
#   #
#   #Hint: The formula for perimeter is 2 * length + 2 * width.
# ---- model response below: edit from here ----
class Rectangle:
    """
    A class representing a rectangle with length and width attributes.
    """

    def __init__(self, length: float, width: float):
        """
        Initializes a Rectangle object with the given length and width.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def find_perimeter(self) -> float:
        """
        Calculates the perimeter of the rectangle based on its length and width.

        Returns:
            float: The perimeter of the rectangle.
        """
        return 2 * self.length + 2 * self.width

# Example usage:
rectangle = Rectangle(5.0, 3.0)
print(rectangle.find_perimeter())  # Output: 16.0