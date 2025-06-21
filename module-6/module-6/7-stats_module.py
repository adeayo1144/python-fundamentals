#/usr/bin/python3

# stats.py

def average(lst):
    """Returns the average of numbers in a list."""
    if not lst:
        return 0
    return sum(lst) / len(lst)

def maximum(lst):
    """Returns the highest number in a list."""
    if not lst:
        return None
    return max(lst)
# main.py

import stats  # Import your custom module

# Sample list of integers
numbers = [10, 20, 30, 40, 50]

# Use functions from the stats module
avg = stats.average(numbers)
max_value = stats.maximum(numbers)

# Print the results
print("Numbers:", numbers)
print("Average:", avg)
print("Maximum:", max_value)
