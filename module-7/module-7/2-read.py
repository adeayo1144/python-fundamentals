#/usr/bin/python3
"""A Program to read a file using context manager"""
with open("newfile.txt", "r") as f:
    file = f.read()
    print(file)