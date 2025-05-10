#!/usr/bin/python3
""" main for calculator"""
add = __import__("cal").add
sub = __import__("cal").sub
mul = __import__("cal").mul
div= __import__("cal").div

operator  = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

num1 = float(input("Enter any number of your choice"))
num2 = float(input("Enter any number of your choice"))
op = input("Enter your operators")
if op not in operator:
    print ("invalid operation, try again")
    exit(1)

for key,value in operator.items():
    if op == key:
        result = operator.get(op)(num1,num2)
        print (result)
        break






