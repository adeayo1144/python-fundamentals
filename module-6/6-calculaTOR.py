#/usr/bin/python3

# Simple Calculator Program

# Ask the user to enter two numbers
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Ask the user to choose an operation
    print("Choose an operation: +, -, *, /")
    operation = input("Enter operation: ")

    # Perform the calculation based on the operation
    if operation == "+":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please choose +, -, *, or /.")
except ValueError:
    print("Invalid input. Please enter valid numbers.")
