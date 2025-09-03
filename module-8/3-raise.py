#!/usr/bin/python3
""" a progrma that divdes two number"""
try:
    number1= int(input("Enter number1: "))
    number2= int(input("Enter number2: "))
    if number2 == 0:
        raise ZeroDivisionError("it cannot be divided by 0")
    a = number1/number2
    print(a)
except Exception as e:
        print(e)