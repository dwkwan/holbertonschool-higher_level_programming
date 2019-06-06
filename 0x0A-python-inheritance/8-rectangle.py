#!/usr/bin/python3
"""This module creates a Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class named BaseGeometry

    Attributes:
    attr1(width): width of rectangle
    attr2(height): height of rectangle
    """
    def __init__(self, width, height):
        """initializes instance"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
