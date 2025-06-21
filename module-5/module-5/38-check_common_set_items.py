#!/usr/bin/python3
def have_common_items(set_A, set_B):
    """
    Checks if two sets have any common items.

    Args:
        set_A (set): The first set.
        set_B (set): The second set.

    Returns:
        bool: True if the sets have common items, False otherwise.
    """
    return bool(set_A & set_B)

set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}
print(have_common_items(set_A, set_B))  

set_A = {1, 2, 3}
set_B = {4, 5, 6}
print(have_common_items(set_A, set_B))  
