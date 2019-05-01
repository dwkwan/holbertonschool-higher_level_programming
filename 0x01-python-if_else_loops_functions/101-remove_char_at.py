#!/usr/bin/python3
def remove_char_at(str, n):
    newstring = ""
    for count, c in enumerate(str):
        if (count != n):
            newstring += c
    return (newstring)
