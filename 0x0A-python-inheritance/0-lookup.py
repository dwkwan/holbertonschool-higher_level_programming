#!/usr/bin/python3
"""This module defines the lookup function"""


def lookup(obj):
    """Returns a valid list of attributes of the object"""
    return dir(obj)
