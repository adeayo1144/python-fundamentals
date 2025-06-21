#!/usr/bin/python3
def swap_keys_values(dictionary):
    """
    Returns a new dictionary with keys and values swapped.

    Args:
        dictionary (dict): The input dictionary.

    Returns:
        dict: A new dictionary with keys and values swapped.

    Raises:
        ValueError: If the input dictionary has non-unique values.
    """
    if len(dictionary.values()) != len(set(dictionary.values())):
        raise ValueError("Input dictionary has non-unique values.")

    return {v: k for k, v in dictionary.items()}

original_dict = {'a': 1, 'b': 2, 'c': 3}
print(swap_keys_values(original_dict))
