#/usr/bin/python3

# utils/greetings.py

def say_hello(name):
    return f"Hello, {name}! Welcome to Python."
from utils.greetings import say_hello

# Call the function with any name
message = say_hello("Alex")
print(message)
