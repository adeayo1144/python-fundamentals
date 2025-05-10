#!/usr/bin/python3
def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in s.lower() if char in vowels)

result = count_vowels("programming")
print(result)

