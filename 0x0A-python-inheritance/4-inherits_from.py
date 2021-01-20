#!/usr/bin/python3
"""
    4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """Documentation"""
    if a_class is not bool and isinstance(obj, a_class):
            return True
    else:
        return False
