#!/usr/bin/python3
"""i am vengeance"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """i am the night"""
    def __init__(self, size):
        """i am  batman"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2
