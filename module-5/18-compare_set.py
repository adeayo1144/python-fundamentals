def set_operations(set_A, set_B):
    """
    Returns a dictionary with the results of set operations.

    Args:
        set_A (set): The first set.
        set_B (set): The second set.

    Returns:
        dict: A dictionary with the union, intersection, difference_A_B, and difference_B_A of the sets.
    """
    result = {
        "union": set_A.union(set_B),
        "intersection": set_A.intersection(set_B),
        "difference_A_B": set_A.difference(set_B),
        "difference_B_A": set_B.difference(set_A)
    }
    return result

set_A = {1, 2, 3, 4}
set_B = {3, 4, 5, 6}
print(set_operations(set_A, set_B))
