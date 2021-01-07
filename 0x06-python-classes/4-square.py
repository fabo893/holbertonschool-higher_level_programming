#!/usr/bin/python3
"""4-square.py
This is a module documentation
"""


class Square:
    """This is a class documentation"""
    def __init__(self, size=0):
        """Method __init__"""
        self.size = size

    def area(self):
        """Method that return the area"""
        x = (self.__size * self.__size)
        return x

    @property
    def size(self):
        """Getter method for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Args:
             value (int): new int to be set
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
