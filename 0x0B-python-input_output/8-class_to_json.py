#!/usr/bin/python3
"""
    8-class_to_json

    This module is for return dictionary description
"""


def class_to_json(obj):
    """Return the dictionary description
    """
    return obj.__dict__
