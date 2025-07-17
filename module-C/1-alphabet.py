#/usr/bin/python3
"""a module that handles regex for alphabetic characters"""
import re

pattern = r"[a-zA-Z]+"
text = "Hello World 123"
match = re.search(pattern, text)

if match:
    print("Found an alphabet:", match.group())
