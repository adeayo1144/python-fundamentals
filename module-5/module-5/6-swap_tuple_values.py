def swap_first_last(tup):
    # Check if the tuple has at least two elements
    if len(tup) < 2:
        return tup  # or raise an error, depending on the desired behavior
    
    # Swap the first and last elements
    swapped_tup = (tup[-1],) + tup[1:-1] + (tup[0],)
    
    return swapped_tup

tup = (1, 2, 3, 4)
result = swap_first_last(tup)
print(result)
