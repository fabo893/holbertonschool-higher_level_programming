#!/usr/bin/python3
"""
    2-is_same_class

    This module is to check an instance
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of the specified class

        Args:
            obj - object to be verified
            a_class - class to check the object

            Return - If is instance return True, otherwise False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
