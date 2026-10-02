# ================= CSEPrompts manual cleaning =================
# task: academic/081 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   #Imagine you are trying to choose what restaurant to visit.
#   #You have a list of restaurants, each with a collection of
#   #star ratings. You also have a minimum standard; you will
#   #only go to a restaurant whose star rating is at least your
#   #minimum standard.
#   #
#   #Write a function called restaurant_rating. restaurant_rating
#   #has two parameters. The first is a dictionary, where the keys
#   #are restaurant names and the values are lists of ratings. The
#   #second parameter is your minimum rating. If a restaurant's
#   #average rating is above your minimum rating, you might visit
#   #it. If it is not, you won't.
#   #
#   #restaurant_rating should return a list of restaurants eligible
#   #for you to visit. That is, it should return a list of
#   #restaurant names from the dictionary whose average ratings
#   #(the average of the ratings in their lists) is greater than or
#   #equal to your minimum rating.
#   #
#   #For example:
#   #rest_and_rating = {'burger king':[4,5,3,4,3], 'moes':[4,5,5,5,5], 'taco bell':[1,2,3,4,5]}
#   #value = 4.5
#   #restaurant_rating(rest_and_rating, value) -> ['moes']
# ---- model response below: edit from here ----
def restaurant_rating(restaurants, min_rating):
    """
    Returns a list of restaurant names whose average rating is greater than or equal to the minimum rating.

    Args:
        restaurants (dict): A dictionary where keys are restaurant names and values are lists of ratings.
        min_rating (float): The minimum rating required for a restaurant to be considered.

    Returns:
        list: A list of restaurant names that meet the minimum rating requirement.
    """
    eligible_restaurants = []

    for restaurant, ratings in restaurants.items():
        # Calculate the average rating for the current restaurant
        average_rating = sum(ratings) / len(ratings)
        
        # Check if the average rating is greater than or equal to the minimum rating
        if average_rating >= min_rating:
            eligible_restaurants.append(restaurant)

    return eligible_restaurants