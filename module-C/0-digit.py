#/usr/bin/python3
"""a module that handle regex for digit"""
import re

pattern = r"\d+"
text = "There are 123 apples"
match = re.search(pattern, text)

if match:
    print("Found a digit:", match.group())
