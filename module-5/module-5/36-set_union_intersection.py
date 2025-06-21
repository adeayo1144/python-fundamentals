#!/usr/bin/python3
def set_operations(set_A, set_B):
    """
    Returns a tuple containing the union and intersection of two sets.

    Args:
        set_A (set): The first set.
        set_B (set): The second set.

    Returns:
        tuple: A tuple containing the union and intersection of the sets.
    """
    union = set_A.union(set_B)
    intersection = set_A.intersection(set_B)
    return union, intersection

set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}
union, intersection = set_operations(set_A, set_B)
print("Union:", union)  
print("Intersection:", intersection)  
