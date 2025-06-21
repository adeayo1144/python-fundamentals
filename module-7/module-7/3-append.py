#!/usr/bin/python3
""" A program to append information in a file"""
with open("newfile.txt", "a+") as f:
    f.write("\n The information inside this document is"\
    "classified, you can only see this when you 're"\
    "taking a python course")