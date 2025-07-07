#!/usr/bin/python3
def symmetric_difference(set1, set2):
    """
    Returns the symmetric difference of two sets.

    The symmetric difference of two sets is a set of elements that are in exactly one of the sets.
    It is calculated as (set1 - set2) ∪ (set2 - set1), where '-' denotes set difference and '∪' denotes set union.

    Args:
        set1 (set): The first set.
        set2 (set): The second set.

    Returns:
        set: The symmetric difference of set1 and set2.
    """
    return set1.symmetric_difference(set2)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(symmetric_difference(set1, set2))
