#/usr/bin/python3
""" A program that takes the age of the person and displays double of that age if its greater than 18"""
age = int (input("enter your age"))
if age >= 18:
    print(age * 2)
else:
    print(age)