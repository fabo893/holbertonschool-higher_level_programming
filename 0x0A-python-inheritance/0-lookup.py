#!/usr/bin/python3
"""
    0-lookup

    This module is for return the available attributes and methods
"""


def lookup(obj):
    """View list of available attributes and methods

        Args:
            obj - the object to be analyzed

            Return - a list
    """
    return list(dir(obj))
