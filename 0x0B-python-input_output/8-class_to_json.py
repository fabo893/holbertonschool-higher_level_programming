#!/usr/bin/python3
"""
    8-class_to_json

    This module is for return dictionary description
"""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization

        Args:
            obj - object

        Return - a dictionary
    """
    return obj.__dict__
