#!/usr/bin/python3
"""This module defines the to_json_string function"""


import json


def from_json_string(my_str):
    """Returns the JSON representation of an object (string)
    Args:
    my_obj (str): object to return JSON representation of

    """
    return json.loads(my_str)
