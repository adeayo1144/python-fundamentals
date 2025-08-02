#usr/bin/python3
class Square:
    def __init__(self, size = 0):
        self.size = size

    @property
    def size(self):
        return self.__size
        
    def area(self):
        return self.__size**2
    
    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("Size must be greater than or equal to Zero")
        else:
            self.__size = size

my_square = Square(5)
print(my_square.__dict__)
print (my_square.size)
