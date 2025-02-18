#/usr/bin/python3
""""" a progam for calculator"""
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
op = input("Enter your operator")


if op == "+":
    print(num1 + num2)
elif op =="-":
    print(num1 - num2)
elif op =="*":
    print(num1 * num2)
elif op =="/":
    print(num1 / num2)
else:
    print("undefined o6perator")


