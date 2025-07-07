#!/usr/bin/python3
from collections import Counter

def count_items(item_list):
    Returns a dictionary with the count of each item in the list.

    Args:
        item_list (list): A list of items.

    Returns:
        dict: A dictionary where keys are unique items and values are their counts.
    """
    return dict(Counter(item_list))

# Example usageitems = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']
print(count_items(items))
```
