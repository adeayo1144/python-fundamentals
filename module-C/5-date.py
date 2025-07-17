#/usr/bin/python3
"""a module that extract date in DD-MM-YYY format"""
import re

pattern = r"\b\d{2}-\d{2}-\d{4}\b"
text = "Today's date is 22-08-2025 and tomorrow is 23-08-2025"

dates=re.findall(pattern, text)
print(dates)