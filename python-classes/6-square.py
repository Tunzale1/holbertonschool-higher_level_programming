#!/usr/bin/python3
'''square'''


class Square:
    '''square is documented'''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """private size atribute"""
        return self.__size

    @property
    def position(self):
        return self.__position

    def area(self):
        """area"""
        return self.__size * self.__size

    @position.setter
    def position(self, value):
        """private position atrb validation"""
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position[0] = value[0]
        self.__position[1] = value[1]

    @size.setter
    def size(self, value):
        """private size atrbtwith validation"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """ prints in stdout the square with the character #"""
        x, y = self.position
        for i in range(self.size):
            print(" " * x + "#" * self.size)
        if self.size == 0:
            print()
