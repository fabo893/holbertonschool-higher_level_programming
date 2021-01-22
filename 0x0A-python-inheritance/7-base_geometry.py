#!/usr/bin/python3
"""
    7-base_geometry

    This module is for Base Geometry class
"""


class BaseGeometry:
    """Base Geometry Class"""

    def area(self):
        """Area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Integer validator method"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.__name = str(name)
        self.__value = int(value)
