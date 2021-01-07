#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""4-square.py
This is a module documentation
"""


class Square:
    """This is a class documentation"""
    def __init__(self, size=0):
        """Method __init__"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method that return the area"""
        x = (self.__size * self.__size)
        return x

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
