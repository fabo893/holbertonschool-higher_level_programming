#!/usr/bin/python3
"""
    9-student

    This module is to define the class Student
"""


class Student:
    """Defining class Student"""
    def __init__(self, first_name, last_name, age):
        """Method __init__"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary representation

            Args:
                self - the Student instance

            Return - a dictionary
        """
        return self.__dict__
