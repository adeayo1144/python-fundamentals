#/usr/bin/python3
import re

text = "This is is a test test sentence."
pattern = r"\b(\w+)\s+\1\b"

matches = re.findall(pattern, text)
print("Repeated words:", matches)

# Optional: Highlight repeated words by surrounding them with **
highlighted = re.sub(pattern, r"**\1 \1**", text)
print("Highlighted:", highlighted)
