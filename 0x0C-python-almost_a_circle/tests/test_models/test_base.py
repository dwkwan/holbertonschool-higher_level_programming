#!/usr/bin/python3
"""Unittest for Base class"""

import json
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBaseClass(unittest.TestCase):
    """This class allows for testing of Base class"""
    def test_singleinstancecreationwithoutid(self):
        """This function tests for multiple instance creation"""
        Base.reset_objects()
        b1 = Base( )
        self.assertEqual(b1.id, 1)
    def test_multipleinstancecreationwithoutid(self):
        """This function tests for multiple instance creation"""
        Base.reset_objects()
        b1 = Base( )
        b2 = Base( )
        b3 = Base( )
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
    def test_instancecreationwithid(self):
        """This function tests for one instance creation with id"""
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
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_duplicateid(self):
        """Test that duplicate ids are allowed"""
        Base.reset_objects()
        b1 = Base(1)
        b2 = Base(1)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 1)
"""
    def test_to_json_string(self):

        Base.reset_objects()
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, json.dumps(r1.__dict__))
"""
