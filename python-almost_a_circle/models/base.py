#!/usr/bin/python3
'''base class'''


import json


class Base:
    '''yikilmadim ayaktayim'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as file:
            if list_objs is None:
                return file.write("[]")
            else:
                new_list = [obj.to_dictionary() for obj in list_objs]
                file.write(cls.to_json_string(new_list))
