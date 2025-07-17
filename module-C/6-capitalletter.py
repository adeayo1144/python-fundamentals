#/usr/bin/python3
import re

text = "Alice went to Wonderland with Bob and Charlie."
pattern = r"\b[A-Z][a-zA-Z]*\b"

capitalized_words = re.findall(pattern, text)
print(capitalized_words)
