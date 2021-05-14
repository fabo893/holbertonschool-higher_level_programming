#!/usr/bin/python3
"""
    10-Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class documentation"""

    def __init__(self, size):
        """init method"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Area """
        return self.__size * self.__size

    def __repr__(self):
        """ Representation of the instance """
        print("[Square] {}/{}".format(self.__size, self.__size))

    def __str__(self):
        """ String representation """
        return "[Square] {}/{}".format(self.__size, self.__size)
