def unique_sorted_list(numbers):
    """
    Returns a sorted list of unique numbers.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: A sorted list of unique numbers.
    """
    # Convert the list to a set to remove duplicates
    unique_numbers = set(numbers)
    
    # Convert the set back to a list and sort it in ascending order
    sorted_list = sorted(list(unique_numbers))
    
    return sorted_list
numbers = [5, 2, 3, 5, 2, 1]
result = unique_sorted_list(numbers)
print(result)
