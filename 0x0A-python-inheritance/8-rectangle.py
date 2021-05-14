#!/usr/bin/python3
"""
8 - Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle """

    def __init__(self, width, height):
        """ init method """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
