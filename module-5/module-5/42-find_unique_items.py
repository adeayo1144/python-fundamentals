#!/usr/bin/python3
def unique_items(list1, list2):
    """
    Returns a set of items that appear in only one list.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        set: A set of items that appear in only one list.
    """
    set1 = set(list1)
    set2 = set(list2)
    return set1.symmetric_difference(set2)

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(unique_items(list1, list2))
