#!/usr/bin/python3
"""
    4-from_json_string

    This module is for return an object
"""


def from_json_string(my_str):
    """Return an object represented by a JSON string

        Args:
            my_str - the string represented by JSON

        Return - an object
    """
    import json
    json_to_py = json.loads(my_str)
    return json_to_py
