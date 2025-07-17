#/usr/bin/python3
""" a module that splits a sentence into words"""
import re

pattern = r"\b\w+\b"
text = "Hello, world!How are you?"

words = re.findall(pattern, text)
print(words)