#!/usr/bin/python3
def merge_dictionaries(dict1, dict2):
    """
    Merges two dictionaries. If a key exists in both, keeps the value from the second dictionary.

    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.

    Returns:
        dict: The merged dictionary.
    """
    return {**dict1, **dict2}

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dictionaries(dict1, dict2))  
