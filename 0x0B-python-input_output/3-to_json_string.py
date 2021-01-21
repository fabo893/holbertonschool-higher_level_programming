#!/usr/bin/python3
"""
    3-to_json_string

    This module is to return the JSON representation
"""


def to_json_string(my_obj):
    """JSON representation of an object(string)

        Args:
            my_obj - object to be represented

        Return - the JSON representation
    """
    import json
    pythontojson = json.dumps(my_obj)
    return pythontojson
