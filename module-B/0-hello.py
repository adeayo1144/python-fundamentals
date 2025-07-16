#!/usr/bin/python3
"""A module that explains the decorator function"""

def decorator(func):

    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")

    return wrapper

@decorator
def greet():
    print(f"Hello,Alice!")


if __name__ == "__main__":
    greet()
