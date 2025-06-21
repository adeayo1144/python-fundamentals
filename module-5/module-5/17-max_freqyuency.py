def most_frequent_string(strings):
    """
    Returns the string that appears most frequently in the list along with its count.

    Args:
        strings (list): A list of strings.

    Returns:
        tuple: A tuple containing the most frequent string and its count.
    """
    frequency = {}
    for string in strings:
        frequency[string] = frequency.get(string, 0) + 1
    
    most_frequent = max(frequency, key=frequency.get)
    return most_frequent, frequency[most_frequent]

strings = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(most_frequent_string(strings))  