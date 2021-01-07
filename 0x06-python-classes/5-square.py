#!/usr/bin/python3
"""5-square.py
This is a module documentation
"""


class Square:
    """This is a class documentation"""
    def __init__(self, size=0):
        """Method __init__"""
        self.size = size

    def area(self):
        """Method that return the area"""
        return self.__size ** 2

    def my_print(self):
        """Print the square"""
        if self.__size == 0:
            print()
        else:
            for x in range(0, self.__size):
                for i in range(0, self.__size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
