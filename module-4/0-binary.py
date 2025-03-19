#!/usr/bin/python3
"""A function that convert decimal values to binary"""

def binary(num):
    rem =[]
    while num / 2 > 0:
        rem. append (str(num %2 ))
        num //= 2
    return ''.join(rem[::-1])
        
    
print (binary(8))
    
