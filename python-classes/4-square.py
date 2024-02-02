#!/usr/bin/python3
'''square'''


class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """private size atribute"""
        return self.__size

    def area(self):
        """area"""
        return self.__size * self.__size

    @size.setter
    def size(self, value):
        """private size atrbtwith validation"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
