#!/usr/bin/python3
"""
    Base class

    This module is for the Base class
"""


class Base:
    """Base class documentation"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init method"""
        if type(id) is int:
            self.id = int(id)
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
