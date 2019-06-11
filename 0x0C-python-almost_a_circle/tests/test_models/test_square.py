#!/usr/bin/python3
"""Unittest for Base class"""


import unittest
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle
class TestBaseClass(unittest.TestCase):
    """This class allows for testing of Base class"""
    def test_SquareinheritancefromBase(self):
        """This function tests that square inherits from Base"""
        Square.reset_objects()
        self.assertEqual(issubclass(Square, Base), True)

    def test_SquareinheritancefromRectangle(self):
        """This function tests that square inherits from Base"""
        Square.reset_objects()
        self.assertEqual(issubclass(Square, Rectangle), True)

    def test_objectinheritance(self):
        """This function tests that object is of type Rectangle"""
        Square.reset_objects()
        s1 = Square(5)
        self.assertEqual(isinstance(s1, Square), True)

    def test_errorfornoarguments(self):
        """This function tests that Typeerror is thrown when 0 arguments"""
        Square.reset_objects()
        with self.assertRaises(TypeError) as e:
            s1 = Square()
        self.assertEqual(str(e.exception), "__init__() missing 1 required positional argument: 'size'")

    def test_errorfortoomanyarguments(self):
        """This function tests that Typeerror is thrown when 0 arguments"""
        Square.reset_objects()
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 2, 3, 4, 5)
        self.assertEqual(str(e.exception), "__init__() takes from 2 to 5 positional arguments but 6 were given")

    def test_singlesquarecreation(self):
        """This function tests for single instance creation"""
        Square.reset_objects()
        s1 = Square(10)
        self.assertEqual(s1.id, 1)

    def test_multiplesquarecreation(self):
        """This function tests for single instance creation"""
        Square.reset_objects()
        s1 = Square(10)
        s2 = Square(2)
        s3 = Square(3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 3)

    def test_singlesquarecreationwithallvalues(self):
        """This function tests for single instance creation"""
        Square.reset_objects()
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 10)
        self.assertEqual(s1.id, 10)

    def test_badsizevalue(self):
        """This function tests for bad size value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square("foo", 1, 2, 3)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badxvalue(self):
        """This function tests for bad x value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, "foo", 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvalue(self):
        """This function tests for bad y value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, "foo", 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_sizegetter(self):
        """This function tests the size getter"""
        Rectangle.reset_objects()
        r1 = Square(1, 2, 2, 3)
        self.assertEqual(r1.size, 1)

    def test_sizesetter(self):
        """This function tests the size setter"""
        Rectangle.reset_objects()
        r1 = Square(1, 2, 2, 3)
        self.assertEqual(r1.size, 1)
        r1.size = 100
        self.assertEqual(r1.size, 100)

    def test_sizesetterwithstring(self):
        """This function tests the size setter with string"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, 2, 3)
            self.assertEqual(r1.size, 1)
            r1.size = "foo"
        self.assertEqual(str(e.exception), "width must be an integer")


    def test_updatebadsizevalue(self):
        """This function tests for bad size value"""
        Square.reset_objects()
        r1 = Square(1, 2, 3, 4)
        r1.update(1, "foo")
        self.assertEqual(r1.size, 1)

    def test_updatebadxvalue(self):
        """This function tests for bad size value"""
        Square.reset_objects()
        r1 = Square(1, 2, 3, 4)
        r1.update(1, 2, "foo")
        self.assertEqual(r1.x, 2)

    def test_updatebadyvalue(self):
        """This function tests for bad size value"""
        Square.reset_objects()
        r1 = Square(1, 2, 3, 4)
        r1.update(1, 2, 3, "foo")
        self.assertEqual(r1.y, 3)

    def test_updateallbadvalues(self):
        """This function tests for all bad values"""
        Square.reset_objects()
        r1 = Square(1, 2, 3, 4)
        r1.update([1], (9, ), True, "foo")
        self.assertEqual(r1.size, 1)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 4)

    def test_to_dict(self):
        """This function tests the to_dictionary function"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 1, 'x': 2, 'size': 10, 'y': 1})

    def test_updatewithdict(self):
        """This function tests the update function with to_dict"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 1)

    def test_updatewithdictionarybycomparingdictionaries(self):
        """This function tests the to_dictionary function"""
        s1 = Square(10, 2, 1, 9)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(s1.__dict__, s2.__dict__)
