# ================= CSEPrompts manual cleaning =================
# task: academic/090 | model: llama31_8b_instruct | run: greedy | sample: 0
# CLASS/FUNCTION task: keep the definitions (and imports/helpers they need); remove example usage.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Create a class called RightTriangle. RightTriangle should
#   #have two attributes (instance variables): opposite and
#   #adjacent. Make sure the variable names match those words.
#   #Both will be floats.
#   #
#   #RightTriangle should have a constructor with two required
#   #parameters, one for each of those attributes (opposite and
#   #adjacent, in that order).
#   #
#   #RightTriangle should also have a method called
#   #find_hypotenuse. find_hypotenuse should calculate the
#   #hypotenuse of the triangle based on the current values for
#   #opposite and adjacent.
#   #
#   #hypotenuse should NOT be an attribute of the class;
#   #instead, hypotenuse should be calculated and returned live
#   #when the method find_hypotenuse is called.
#   #
#   #The find_hypotenuse method should have NO parameters
#   #besides self. Instead, it should calculate the hypotenuse
#   #based on the current values for the opposite and adjacent
#   #attributes.
#   #
#   #Hint: In other words: opposite and adjacent will be
#   #attributes similar to guacamole and cheese in the Burrito
#   #class from Problem Set 5.1. find_hypotenuse will be a
#   #method similar to the get_cost method from the Burrito
#   #class.
#   #
#   #Hint 2: The formula for hypotenuse is the square root of
#   #opposite squared plus adjacent squared. The easiest way to
#   #find the square root is to use the exponent operator to
#   #raise the sum to the 0.5 power (e.g. sum**0.5).
# ---- model response below: edit from here ----
import math

class RightTriangle:
    """
    A class representing a right triangle with attributes for opposite and adjacent sides.
    """

    def __init__(self, opposite, adjacent):
        """
        Initializes a RightTriangle object with the given opposite and adjacent sides.

        Args:
            opposite (float): The length of the opposite side.
            adjacent (float): The length of the adjacent side.
        """
        self.opposite = opposite
        self.adjacent = adjacent

    def find_hypotenuse(self):
        """
        Calculates the length of the hypotenuse of the triangle based on the current values for opposite and adjacent sides.

        Returns:
            float: The length of the hypotenuse.
        """
        # Calculate the sum of the squares of the opposite and adjacent sides
        sum_of_squares = self.opposite ** 2 + self.adjacent ** 2
        
        # Calculate the square root of the sum to find the hypotenuse
        hypotenuse = math.sqrt(sum_of_squares)
        
        return hypotenuse