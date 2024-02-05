#!/usr/bin/python3
'''saalamm'''


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"
    ''' rectangle'''
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        """sm"""
        return self.__height

    @height.setter
    def height(self, value):
        """private att"""
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """sm"""
        return self.__width

    @width.setter
    def width(self, value):
        """private att"""
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            print()
        else:
            result = ""
            for _ in range(self.__height):
                for _ in range(self.__width):
                    result += str(self.print_symbol)
                result += "\n"
            return result.rstrip()

    def __repr__(self):
        """Returns a string representation for recreation"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Custom behavior when the rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
