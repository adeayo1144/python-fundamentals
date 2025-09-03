#!/usr/bin/python3
""" a module that handles exception"""
try:
    with open("file.txt", "r") as f:
        print( f.read())
except Exception as e:
    print("file not found")

