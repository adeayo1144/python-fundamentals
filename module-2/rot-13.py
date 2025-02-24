#/usr/bin/python3
"""a program for rot 13 cipher"""

encode =""
message = input("Enter a message")
for letter in message:
    if letter.isupper():
        if letter > + "A" and letter <= "M":
            encode += chr(ord(letter) + 13)
        else:
            encode += chr(ord(letter) - 13)
    else:
        if letter >= "a" and letter <= "m":
            encode += chr(ord(letter) + 13)
        else:
            encode += chr(ord(letter) - 13)
print(encode)
