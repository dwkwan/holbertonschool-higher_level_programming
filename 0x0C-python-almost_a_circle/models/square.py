#!/usr/bin/python3
"""This module creates the Square class that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """A class named Square

    Attributes:
    attr1(id): id of object
    attr2(width): square width
    attr3(height): square height
    attr4(x): number of spaces before square
    attr5(y): number of spaces before square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes instance of Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of Square class"""
        return"[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Returns the size of the object"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the object"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes"""
        attrs = ["id", "size", "x", "y"]
        count = len(args)
        if not args or count < 1:
            for key, value in kwargs.items():
                for i in range(len(attrs)):
                    if key == attrs[i] and type(value) == int:
                        setattr(self, attrs[i], value)
        elif args and all(type(x) is int for x in args):
            for i in range(count):
                setattr(self, attrs[i], args[i])

    def to_dictionary(self):
        """Returns the dictionary representation of the Square"""
        newdict = {}
        olddict = self.__dict__.copy()
        for i in olddict:
            newkey = i.replace('_Rectangle__', "")
            if newkey == "width" or newkey == "height":
                newkey = "size"
            newdict[newkey] = self.__dict__[i]
        return newdict
