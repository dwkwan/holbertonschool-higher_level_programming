#!/usr/bin/python3
"""This module defines the write_file function"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns number of characters written
    Args:
    filename (str): File to write to
    text (str): text to write

    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
