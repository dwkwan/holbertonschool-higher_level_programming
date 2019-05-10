#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k, v in a_dictionary.items():
        if v == value:
            del a_dictionary[k]
            break
    for k, v in a_dictionary.items():
        if v == value:
            del a_dictionary[k]
            break
    for k, v in a_dictionary.items():
        if v == value:
            del a_dictionary[k]
            break
    return a_dictionary
