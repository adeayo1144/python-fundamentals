#/usr/bin/python3
def safe_divide(a, b):
    try:
        result = a / b
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print(safe_divide(num1, num2))
except ValueError:
    print("Invalid input. Please enter numeric values.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
