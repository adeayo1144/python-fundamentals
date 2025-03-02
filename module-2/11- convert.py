#/usr/bin/python3
name= input ("Enter any  name")
new_text = ""
for char in name:
    if char.islower():
        new_text += char.upper()
    else:
        new_text += char
print(new_text)