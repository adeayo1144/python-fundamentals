#!/usr/bin/python3
"""A module that explains decorator with argument"""

def decorator(func):

    def wrapper(*args, **kwargs):
        print("Before the function call")
        func(*args, **kwargs)
        print("After the function call")
    return wrapper


@decorator
def greet(name):
    print(f"Hello, {name}!")


if __name__ == "__main__":
    greet("Alice")
