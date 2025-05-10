#/usr/bin/python3
"""a program that convert capital letter to small letters"""
name = input("Enter your name")
for letter in name:
    if ord(letter) >= 65 and ord(letter) <90:
        print(chr(ord(letter) + 32), end="")
    else:
        print(letter, end=" ")
