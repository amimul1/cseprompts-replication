# ================= CSEPrompts manual cleaning =================
# task: codingsites/081 | model: llama31_8b_instruct | run: greedy | sample: 0
# CLASS/FUNCTION task: keep the definitions (and imports/helpers they need); remove example usage.
# Rules (docs/MANUAL_CLEANING.md): delete everything that is not the model's code; keep the
# code EXACTLY as written (no bug fixes, renames or additions); if there is no code, delete it
# all and set NO_CODE. When finished, change TODO below to DONE (or NO_CODE).
# MANUAL_STATUS: DONE
# ---- task prompt (reference only) ----
#   Write a function that takes a function and some arguments, and returns a new function that can
#   be called with additional arguments.
# ---- model response below: edit from here ----
def partial(func, *args, **kwargs):
    """
    Returns a new function that can be called with additional arguments.

    Args:
        func (function): The function to be partially applied.
        *args: The positional arguments to be passed to the function.
        **kwargs: The keyword arguments to be passed to the function.

    Returns:
        function: A new function that can be called with additional arguments.
    """
    def new_func(*new_args, **new_kwargs):
        return func(*(args + new_args), **{**kwargs, **new_kwargs})
    return new_func
