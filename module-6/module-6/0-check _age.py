#!/usr/bin/python3
# Prompt the user to enter their age
age_input = input("Please enter your age: ")

# Convert the input to an integer
try:
    age = int(age_input)

    # Check voting eligibility using if, elif, else
    if age >= 18:
        print("You can vote!")
    elif age >= 0:
        print("Sorry, you're not eligible to vote yet.")
    else:
        print("Age can't be negative.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
