#!/usr/bin/python3
"""This module creates a class named Rectangle"""


class Rectangle:
    """A class named Rectangle

    Attributes:
    attr1(width): width of rectangle
    attr2(height): height of rectangle
    attr3(number_of_instances): number of instances
    attr4(print_symbol): symbol for representation
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

    def __str__(self):
        """Returns the string representation of the class instance"""
        stringrep = ""
        if self.__width == 0 or self.__height == 0:
            return stringrep
        for row in range(self.__height):
            for column in range(self.__width):
                stringrep += str(self.print_symbol)
            if row < self.__height - 1:
                stringrep += "\n"
        return stringrep

    def __repr__(self):
        """Returns the string representation of the class instance for
        recreation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Finalizer when instance is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger rectangle"""
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
