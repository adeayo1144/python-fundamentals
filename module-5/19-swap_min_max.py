def swap_min_max(numbers):
    """
    Swaps the smallest and largest numbers in a list.

    Args:
        numbers (list): A list of numbers.

    Returns:
        list: The list with the smallest and largest numbers swapped.
    """
    if len(numbers) < 2:
        return numbers  # or raise an error, depending on the desired behavior
    
    min_index = numbers.index(min(numbers))
    max_index = numbers.index(max(numbers))
    
    numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
    
    return numbers

numbers = [4, 9, 2, 7, 5]
print(swap_min_max(numbers))  
