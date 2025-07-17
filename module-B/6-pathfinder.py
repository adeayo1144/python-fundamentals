#!/usr/bin/python3
from functools import lru_cache
def grid_paths(m, n):
    @lru_cache(maxsize=None)  # memoization
    def dp(i, j):
        # Base case: only one way if row=1 or col=1
        if i == 1 or j == 1:
            return 1
        # Recursive case: move down or right
        return dp(i - 1, j) + dp(i, j - 1)
    
    return dp(m, n)

print(grid_paths(3, 3))  
