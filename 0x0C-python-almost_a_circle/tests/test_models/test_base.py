#!/usr/bin/python3
"""Unittest for Base class"""

import json
import os
from os import path
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    """This class allows for testing of Base class"""
    def test_singleinstancecreationwithoutid(self):
        """This function tests for multiple instance creation"""
        Base.reset_objects()
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_multipleinstancecreationwithoutid(self):
        """This function tests for multiple instance creation"""
        Base.reset_objects()
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_instancecreationwithid(self):
        """This function tests for 1 instance creation with id"""
        Base.reset_objects()
        b1 = Base(12)
        self.assertEqual(b1.id, 12)

    def test_instancecreationwithstringid(self):
        """This function tests for one instance creation with id"""
        Base.reset_objects()
        b1 = Base("foo")
        self.assertEqual(b1.id, "foo")

    def test_multipleinstancecreationwithid(self):
        """This function tests for multiple instance creation with id"""
        Base.reset_objects()
        b1 = Base(15)
        self.assertEqual(b1.id, 15)
        b2 = Base(20)
        self.assertEqual(b2.id, 20)

    def test_Noneid(self):
        """This function tests for None argument"""
        Base.reset_objects()
        b1 = Base(None)
        self.assertEqual(b1.id, 1)

    def test_privateclassvariable(self):
        """This function tests __nb_objects being private"""
        Base.reset_objects()
        with self.assertRaises(AttributeError) as e:
            print(Base.__nb_objects)
        self.assertEqual(str(e.exception), "type object 'Base' has no attrib" +
                         "ute '_TestBaseClass__nb_objects'")

    def test_duplicateid(self):
        """Test that duplicate ids are allowed"""
        Base.reset_objects()
        b1 = Base(1)
        b2 = Base(1)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 1)

    def test_to_json_string(self):
        """This function tests the to_json_string func"""
        Base.reset_objects()
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(
            len(json_dictionary),
            len('[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'))

    def test_to_json_string_withNonearg(self):
        """This function tests the to_json_string func with None argument"""
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")
        self.assertEqual(type(json_dictionary), str)

    def test_to_json_string_withNaN(self):
        """This function tests the to_json_string func with NaN argument"""
        with self.assertRaises(TypeError) as e:
            json_dictionary = Base.to_json_string(float('nan'))
        self.assertEqual(str(e.exception), "object of type \'float\'" +
                         " has no len()")

    def test_to_json_string_withinf(self):
        """This function tests the to_json_string func with inf argument"""
        with self.assertRaises(TypeError) as e:
            json_dictionary = Base.to_json_string(float('inf'))
        self.assertEqual(
            str(e.exception), 'object of type \'float\' has no len()')

    def test_save_to_filewithNonearg(self):
        """This function tests the save_to_file func with None argument"""
        Base.reset_objects()
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            str = file.read()
        self.assertEqual(len(str), len('[]'))

    def test_save_to_filewithNaNearg(self):
        """This function tests the save_to_file func with None argument"""
        with self.assertRaises(TypeError) as e:
            json_dictionary = Base.to_json_string(float('nan'))
        self.assertEqual(str(e.exception),
                         'object of type \'float\' has no len()')

    def test_from_json_string(self):
        """This function tests the from_json_string func"""
        Base.reset_objects()
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output,
                         [{"height": 4, "width": 10, "id": 89},
                          {"height": 7, "width": 1, "id": 7}])
        self.assertEqual(type(list_output), list)

    def test_from_json_stringwithemptyjsonstring(self):
        """This function tests the from_json_string func"""
        Base.reset_objects()
        list_input = []
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [])
        self.assertEqual(type(list_output), list)

    def test_from_json_stringwithNonearg(self):
        """This function tests the from_json_string func"""
        Base.reset_objects()
        list_output = Rectangle.from_json_string(None)
        self.assertEqual(list_output, [])
        self.assertEqual(type(list_output), list)

    def test_create(self):
        """This function tests the create func"""
        Base.reset_objects()
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 3/5")
        self.assertEqual(r1 is r2, False)
        self.assertEqual(r1 == r2, False)

    def test_loadfromfile(self):
        os.remove("Rectangle.json")
        Base.reset_objects()
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output[0].id,  r1.id)
        self.assertEqual(list_rectangles_output[0].width,  r1.width)
        self.assertEqual(list_rectangles_output[0].height,  r1.height)
        self.assertEqual(list_rectangles_output[0].x,  r1.x)
        self.assertEqual(list_rectangles_output[0].y,  r1.y)
        self.assertEqual(list_rectangles_output[1].id,  r2.id)
        self.assertEqual(list_rectangles_output[1].width,  r2.width)
        self.assertEqual(list_rectangles_output[1].height,  r2.height)
        self.assertEqual(list_rectangles_output[1].x,  r2.x)
        self.assertEqual(list_rectangles_output[1].y,  r2.y)

    def test_save_to_filewithsquare(self):
        """This function tests the save_to_file func with None argument"""
        Base.reset_objects()
        s1 = Square(10, 7, 2, 8)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            str = file.read()
        self.assertEqual(len(str), 77)

    def test_save_to_filewithrec(self):
        """This function tests the save_to_file func with None argument"""
        Base.reset_objects()
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            str = file.read()
        self.assertEqual(len(str), 105)

    def test_save_to_filewithemptylist(self):
        """This function tests the save_to_file func with empty"""
        Base.reset_objects()
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            str = file.read()
        self.assertEqual(len(str), 2)

    def test_save_to_filewithNoneargsquare(self):
        """This function tests the save_to_file func None"""
        os.remove("Square.json")
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            str = file.read()
        self.assertEqual(len(str), 2)

    def test_save_to_filewithemptylist(self):
        """This function tests the save_to_file func with empty list arg"""
        os.remove("Square.json")
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            str = file.read()
        self.assertEqual(len(str), 2)

    def test_save_to_filewith1object(self):
        """This function tests the save_to_file func with 1 object"""
        os.remove("Square.json")
        Square.save_to_file([Square(1)])
        with open("Square.json", "r") as file:
            str = file.read()
        self.assertEqual(len(str), 38)

    def test_to_json_stringwithmultipledicts(self):
        """This function tests the to_json_string func"""
        Base.reset_objects()
        list_dictionaries = []
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(9, 3, 1, 7)
        list_dictionaries.append(r1.to_dictionary())
        list_dictionaries.append(r2.to_dictionary())
        json_dictionary = Base.to_json_string(list_dictionaries)
        self.assertEqual(len(json_dictionary), 105)
        self.assertEqual(type(json_dictionary), str)

    def test_Squarecreatewithjustid(self):
        """This function tests the create func"""
        Base.reset_objects()
        s1 = Square.create(**{'id': 89})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_Squarecreatewithidandsize(self):
        """This function tests the create func"""
        Base.reset_objects()
        s1 = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)

    def test_Squarecreatewithidsize(self):
        """This function tests the create func"""
        Base.reset_objects()
        s1 = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 0)

    def test_Squarecreatewithidsizexy(self):
        """This function tests the create func"""
        Base.reset_objects()
        s1 = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
