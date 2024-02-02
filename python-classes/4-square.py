#!/usr/bin/python3
'''square'''


class Square:
    def __init__(self, size=0):
        '''init'''
        self.__size = size

    @property
    def size(self):
        '''self'''
        return self.__size

    def area(self):
        '''area'''
        return self.__size * self.__size

    @size.setter
    def size(self, value):
        '''size'''
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
