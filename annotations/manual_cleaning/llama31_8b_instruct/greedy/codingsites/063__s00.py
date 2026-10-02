# ================= CSEPrompts manual cleaning =================
# task: codingsites/063 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given a list of cities and the distances between each pair of cities, what is the shortest
#   possible route that visits each city and returns to the origin city?
# ---- model response below: edit from here ----
import numpy as np

def nearest_neighbor_tsp(distances, start_city):
    """
    Nearest Neighbor algorithm for solving TSP.

    Parameters:
    distances (numpy array): Matrix of distances between cities.
    start_city (int): Index of the starting city.

    Returns:
    route (list): Shortest possible route that visits each city and returns to the origin city.
    """
    num_cities = len(distances)
    visited = [False] * num_cities
    route = [start_city]
    visited[start_city] = True

    for _ in range(num_cities - 1):
        current_city = route[-1]
        next_city = None
        min_distance = float('inf')

        for i in range(num_cities):
            if not visited[i] and distances[current_city, i] < min_distance:
                next_city = i
                min_distance = distances[current_city, i]

        route.append(next_city)
        visited[next_city] = True

    # Return to the starting city
    route.append(start_city)

    return route

def print_route(route, distances):
    """
    Print the shortest possible route and its total distance.

    Parameters:
    route (list): Shortest possible route that visits each city and returns to the origin city.
    distances (numpy array): Matrix of distances between cities.
    """
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distances[route[i], route[i + 1]]

    print("Route:", route)
    print("Total distance:", total_distance)

