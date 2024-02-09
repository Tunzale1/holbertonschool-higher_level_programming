#!/usr/bin/python3
''' i'm vengeance '''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """I am the night"""
    def __init__(self, size):
        """ i am batman"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
