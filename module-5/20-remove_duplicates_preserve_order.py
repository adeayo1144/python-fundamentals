def remove_duplicates(input_list):
    """
    Removes duplicates from a list while preserving the original order.

    Args:
        input_list (list): The list from which to remove duplicates.

    Returns:
        list: The list with duplicates removed.
    """
    seen = set()
    output_list = [x for x in input_list if not (x in seen or seen.add(x))]
    return output_list

input_list = [1, 3, 2, 3, 1, 4, 2]
print(remove_duplicates(input_list))  
