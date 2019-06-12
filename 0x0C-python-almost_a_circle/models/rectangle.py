#!/usr/bin/python3
"""This module creates the Rectangle class that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """A class named Rectangle

    Attributes:
    attr1(id): id of object
    attr2(width): rectangle width
    attr3(height): rectangle height
    attr4(x): number of spaces before rectangle
    attr5(y): number of newlines before rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instance of Rectangle class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """Prints in stdout the instance with the character #"""
        for row in range(self.__y):
            print()
        for row in range(self.__height):
            for column in range(self.__x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns the informal representation of the object"""
        return"[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Updates attributes"""
        attrs = ["id", "width", "height", "x", "y"]
        count = len(args)

        if not args or count < 1:
            for key, value in kwargs.items():
                for i in range(len(attrs)):
                    if key == attrs[i]:
                        setattr(self, attrs[i], value)
        elif args:
            for i in range(count):
                setattr(self, attrs[i], args[i])

    def to_dictionary(self):
        """Returns the dictionary representation of the Rectangle"""
        olddict = self.__dict__.copy()
        newdict = {}
        for i in olddict:
            newkey = i.replace('_Rectangle__', "")
            newdict[newkey] = self.__dict__[i]
        return newdict

    @property
    def width(self):
        """Returns width of instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of class instance"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Returns height of instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of class instance"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Returns x of instance"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets x of class instance"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Returns y of instance"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets y of class instance"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
