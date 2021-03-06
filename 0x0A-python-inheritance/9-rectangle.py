#!/usr/bin/python3
"""
9 - Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle """

    def __init__(self, width, height):
        """ init method """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Area """
        return self.__width * self.__height

    def __repr__(self):
        """ Representation of the instance """
        print("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __str__(self):
        """ String representation """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
