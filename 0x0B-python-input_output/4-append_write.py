#!/usr/bin/python3
"""This module defines the append_write function"""


def append_write(filename="", text=""):
    """Appends a string at end of a text file, returns # of characters written
    Args:
    filename (str): File to append to
    text (str): text to append

    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
