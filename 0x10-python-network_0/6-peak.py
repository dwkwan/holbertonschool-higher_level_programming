#!/usr/bin/python3
"""This module contains a script that finds a peak in a list of unsorted
integers"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers"""
    length = len(list_of_integers)
    if length == 0:
        return None
    peak = re_peak(list_of_integers, 0, length - 1)
    return peak


def re_peak(int_list, start, end):
    if start == end:
        return int_list[start]
    mid = int((start + end) // 2)
    if int_list[mid] > int_list[mid + 1] and int_list[mid] > int_list[mid - 1]:
        return int_list[mid]
    if int_list[mid + 1] > int_list[mid]:
        return re_peak(int_list, mid + 1, end)
    else:
        return re_peak(int_list, 0, mid - 1)
