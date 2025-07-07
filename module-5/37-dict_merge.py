#!/usr/bin/python3
def remove_key(dictionary, key):
    """
    Removes a key from a dictionary if it exists and returns the updated dictionary.

    Args:
        dictionary (dict): The dictionary from which to remove the key.
        key: The key to remove.

    Returns:
        dict: The updated dictionary.
    """
    dictionary.pop(key, None)
    return dictionary


my_dict = {"name": "Jayomide", "age": 30, "city": "abuja"}
print(remove_key(my_dict, "age"))  
