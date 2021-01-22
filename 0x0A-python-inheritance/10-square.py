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
        Rectangle.__init__(self, size, size)
        self.__size = size
