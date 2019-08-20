#!/usr/bin/python3
"""This module contains a script that finds a peak in a list of unsorted
integers"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    if list_of_integers == []:
        return None
    return max(list_of_integers)
