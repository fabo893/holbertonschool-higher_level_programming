#!/usr/bin/python3
"""
    Base class

    This module is for the Base class
"""

import json


class Base:
    """Base class documentation"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init method"""
        if type(id) is int:
            self.id = int(id)
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """the to_json"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """the save file"""
        if list_objs is None:
            json_string = "[]"
        else:
            json_string = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs])
        with open(
                cls.__name__ + '.json',
                mode='w+', encoding='utf-8') as a_file:
            a_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """from json"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return(json.loads(json_string))

        @classmethod
        def create(cls, **dictionary):
            """dictionary to instance"""
            dummy = cls(3, 3, 3)
            dummy.update(**dictionary)
            return dummy
