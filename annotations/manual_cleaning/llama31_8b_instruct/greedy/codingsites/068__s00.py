# ================= CSEPrompts manual cleaning =================
# task: codingsites/068 | model: llama31_8b_instruct | run: greedy | sample: 0
# FUNCTION task: keep the function/class definitions (and imports/helpers they need); remove example calls, prints and tests.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Given n items of different weights and bins each of capacity c, assign each item to a bin such
#   that number of total used bins is minimized.
# ---- model response below: edit from here ----
def first_fit_decreasing(weights, capacities):
    """
    First-Fit Decreasing algorithm for bin packing problem.

    Parameters:
    weights (list): List of item weights.
    capacities (list): List of bin capacities.

    Returns:
    list: List of bins, where each bin is a list of item weights.
    """
    # Sort items in decreasing order of weight
    weights.sort(reverse=True)

    # Initialize bins
    bins = [[] for _ in range(len(capacities))]

    # Assign items to bins
    for weight in weights:
        # Find the first bin that can accommodate the item
        for i, bin in enumerate(bins):
            if sum(bin) + weight <= capacities[i]:
                bins[i].append(weight)
                break
        else:
            # If no bin can accommodate the item, create a new bin
            bins.append([weight])

    return bins