#!/usr/bin/python3
def remove_duplicate_values(dictionary):
    """
    Removes dictionary items with duplicate values, keeping only the first occurrence.

    Args:
        dictionary (dict): The input dictionary.

    Returns:
        dict: A new dictionary with duplicate values removed.
    """
    seen = set()
    return {key: value for key, value in dictionary.items() if not (value in seen or seen.add(value))}

my_dict = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
print(remove_duplicate_values(my_dict))
