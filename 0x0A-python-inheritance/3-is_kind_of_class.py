#!/usr/bin/python3
"""
    3-is_kind_of_class

    Module to check an instance
"""
def is_kind_of_class(obj, a_class):
    """Check if the object is an instance of

        Args:
            obj - object to be verified
            a_class - class to check

            Return - On success, True
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
