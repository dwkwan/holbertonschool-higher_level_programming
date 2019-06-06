#!/usr/bin/python3
"""This module creates a Rectangle class that inherts from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class named BaseGeometry

    Attributes:
    attr1(width): width of rectangle
    attr2(height): height of rectangle
    """
    def __init__(self, width, height):
        """initializes an instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """returns area of instance"""
        return self.__width * self.__height

    def __str__(self):
        """returns string representation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
