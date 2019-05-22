#!/usr/bin/python3
"""This module creates a class named Square"""


class Square:
    """A class named Square

    Attributes:
    attr1 (size): size of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
        size (int): size for __size attribute of class instance
        """
        self.size = size
        self.position = position

    def area(self):
        """Calculates the area based on size of square
        Returns:
        int: The return value. Returns the area
        """
        return self.__size ** 2

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

    def my_print(self):
        """Prints in stdout the square with the # character"""
        if self.__size > 0:
            for row in range(self.__position[1]):
                print()
            for row in range(self.__size):
                for column in range(self.__position[0]):
                    print(" ", end="")
                for column in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()

    @property
    def position(self):
        """Gets the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def __repr__(self):
        """Prints the value of an instance of the Square class"""
        newstring = ""
        if self.__size > 0:
            for row in range(self.__position[1]):
                newstring += "\n"
            for row in range(self.__size):
                for column in range(self.__position[0]):
                    newstring += " "
                for column in range(self.__size):
                    newstring += "#"
                newstring += "\n"
        else:
            newstring += '\n'
        return newstring[:-1]
