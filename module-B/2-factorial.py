#!/usr/bin/python3
"""A function that creates a recursive/recursion functions of a factorials"""

def memoize(func):
    cache = {}

    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return wrapper


@memoize
def factorial(n):
        
        if n == 0 or n == 1:
              return 1
        else:

            return n * factorial(n - 1)
        
if __name__ =="__main__":
        print(factorial(2))
        print(factorial(8))
       