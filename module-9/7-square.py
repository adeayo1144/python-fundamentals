#/usr/bin/python3
"""An empty class that define a square"""

class Square:
    def __init__(self, size = 0):
        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("SIZE MUST BE GREATER THAN OR EQUAL TO ZERO")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
          
my_square = Square(5)
"""print((my_square.__dict__))"""
print(my_square.area())






