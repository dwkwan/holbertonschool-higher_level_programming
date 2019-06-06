#!/usr/bin/python3
"""This module defines the is_same_class function"""


def is_same_class(obj, a_class):
    """returns True or False based on inheritance"""
    return type(obj) == a_class
