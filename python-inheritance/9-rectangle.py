#!/usr/bin/python3
'''full rectangle'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''no need to ask'''

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return f"[Rectangle] {self.__width}/ {self.__height}"
