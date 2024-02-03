#!/usr/bin/python3
'''saam eleykim'''


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
        if (
                isinstance(value, tuple) and len(value) == 2
                and all(isinstance(v, int) and v >= 0 for v in value)
        ):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                if self.__position[1] > 0:
                    print("#" * self.__size)
                else:
                    print(" " * self.__position[0] + "#" * self.__size)
