#!/usr/bin/python3
"""This module defines the to_json_string function"""


import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)
    Args:
    my_obj (str): object to return JSON representation of

    """
    return json.dumps(my_obj)
