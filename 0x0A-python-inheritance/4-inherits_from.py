#!/usr/bin/python3
"""
    4-inherits_from.py
"""


def inherits_from(obj, a_class):
    """Documentation"""
    if type(obj) is a_class:
            return False
    if issubclass(type(obj), a_class):
        return True
