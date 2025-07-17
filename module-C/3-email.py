#/usr/bin/python3
"""a  module that validate a simple email address"""
import re

pattern = r"^\w+@\w+\.\w{2,}$"
text = "adeayo1144@gmail.com"

if re.match(pattern, text):
    print("Valid email format")
else:
    print("Invalid email format")