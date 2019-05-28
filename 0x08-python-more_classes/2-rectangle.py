#!/usr/bin/python3
"""This module creates a class named Rectangle"""


class Rectangle:
    """A class named Rectangle

    Attributes:
    attr1(width): width of rectangle
    attr2(height): height of rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """Gets the height of the class instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the class instance"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Gets the width of the class instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the class instance"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returns the area of the class instance"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the permimeter of the class instance"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)
