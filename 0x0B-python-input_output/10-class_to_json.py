#!/usr/bin/python3
"""This module creates a func that returns the dict for JSON serialization"""


def class_to_json(obj):
    """Returns the dictionary description of object
    Args:
    obj (object): object to return dictionary description  of
    """
    return obj.__dict__
