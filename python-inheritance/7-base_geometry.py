#!/usr/bin/python3
'''he bele bele isler'''


class BaseGeometry:
    '''smoooothh operatoorr'''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):

        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value < 0 or value == 0:
            raise ValueError(f"{name} must be greater than 0")
