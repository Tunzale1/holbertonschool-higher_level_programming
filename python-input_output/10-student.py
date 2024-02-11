#!/usr/bin/python3
'''Student to JSON with filter'''


class Student:
    '''student class'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        student_dict = {}
        for attr in (attrs or dir(self)):
            if not attr.startswith('_'):  # Exclude private attributes
                value = getattr(self, attr)
                if not callable(value):  # Exclude methods
                    student_dict[attr] = value

        return student_dict
    return self.__dict__
