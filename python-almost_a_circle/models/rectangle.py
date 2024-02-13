#!/usr/bin/python3
'''first rectangle'''


from models.base import Base


class Rectangle(Base):
    """document"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get"""
        return self.__width

    @width.setter
    def width(self, value):
        '''set'''
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """get"""
        return self.__height

    @height.setter
    def height(self, value):
        """set"""
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """get"""
        return self.__x

    @x.setter
    def x(self, value):
        """set"""
        self.__x = value
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """prototype"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter"""
        self.__y = value
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout with the character #"""
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        '''str method'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
