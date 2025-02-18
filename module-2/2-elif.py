#/usr/bin/python3
""" A program in python that can differenciate between even and odd values"""
num = int(input("enter any number"))
if num % 2 == 1:
    print("this is odd ")
elif num % 2 == 0:
    print("this is even")
else:
    print("undefined")