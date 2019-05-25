#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """This function tests for positive output"""
    def test_positiveoutput(self):
        list = [1, 2, 3, 4]
        self.assertEqual(max_integer(list), 4)
    """This function tests for negative output"""
    def test_max_negativeoutput(self):
        list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(list), -1)
    """This function tests for one number"""
    def test_max_onenumber(self):
        list = [3]
        self.assertEqual(max_integer(list), 3)
    """This function tests for one negative number"""
    def test_max_onenegativenumber(self):
        list = [-1]
        self.assertEqual(max_integer(list), -1)
    """This function tests for unordered list"""
    def test_max_unordered(self):
        list = [1, 4, 2, 3]
        self.assertEqual(max_integer(list), 4)
    """This function tests for identical values"""
    def test_max_identicalvalues(self):
        list = [3, 3, 3, 3]
        self.assertEqual(max_integer(list), 3)
    """This function tests for strings"""
    def test_max_strings(self):
        list = ['a', 'b', 'c', 'd']
        self.assertEqual(max_integer(list), 'd')
    """This function tests for raising error when None is passed"""
    def test_max_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)
    """This function tests for True"""
    def test_max_True(self):
        with self.assertRaises(TypeError):
            max_integer(True)

if __name__ == '__main__':
    unittest.main()
