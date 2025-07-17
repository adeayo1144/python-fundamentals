#/usr/bin/python3
import re

text = "Call me at 123-456-7890 or 987.654.3210 or (555) 123-4567"
pattern = r"(?:\(\d{3}\)\s*|\d{3}[-.])\d{3}[-.]\d{4}"

phone_numbers = re.findall(pattern, text)
print(phone_numbers)
