#!/usr/bin/python3
"""This module creates a class named Square"""


class Square:
    """A class named Square

    Attributes:
    attr1 (size): size of square
    """
    def __init__(self, size=0):
        """
        Args:
        size (int): size for __size attribute of class instance
        """
        self.__size = size

    def area(self):
        """Calculates the area based on size of square
        Returns:
        int: The return value. Returns the area
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Gets the size of the class instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the class instance"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """
        Args:
        other (obj): other object of type square for comparison
        Returns:
        int: Boolean value. Returns True or False
        """
        return(self.area() == other.area())

    def __ne__(self, other):
        """
        Args:
        other (obj): other object of type square for comparison
        Returns:
        int: Boolean value. Returns True or False
        """
        return(self.area() != other.area())

    def __lt__(self, other):
        """
        Args:
        other (obj): other object of type square for comparison
        Returns:
        int: Boolean value. Returns True or False
        """
        return(self.area() < other.area())

    def __le__(self, other):
        """
        Args:
        other (obj): other object of type square for comparison
        Returns:
        int: Boolean value. Returns True or False
        """
        return(self.area() <= other.area())

    def __gt__(self, other):
        """
        Args:
        other (obj): other object of type square for comparison
        Returns:
        int: Boolean value. Returns True or False
        """
        return(self.area() > other.area())

    def __ge__(self, other):
        """
        Args:
        other (obj): other object of type square for comparison
        Returns:
        int: Boolean value. Returns True or False
        """
        return(self.area() >= other.area())
