#/usr/bin/python3

def is_multiple(a, b):
    """Returns True if a is a multiple of b AND b is a multiple of a, otherwise False."""
    if a == 0 or b == 0:
        return False  # Avoid division by zero
    return a % b == 0 and b % a == 0

# Test the function with various values
test_cases = [
    (10, 5),    # False: 10 is a multiple of 5, but 5 is not a multiple of 10
    (4, 2),     # False
    (3, 3),     # True: both are multiples of each other
    (0, 5),     # False: 0 is a multiple of 5, but 5 is not a multiple of 0
    (5, 0),     # False: division by zero
    (12, 4),    # False
    (6, 3),     # False
]

for a, b in test_cases:
    result = is_multiple(a, b)
    print(f"is_multiple({a}, {b}) → {result}")
