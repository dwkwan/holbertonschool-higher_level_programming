#!/usr/bin/python3
def max_integer(my_list=[]):
    result = 0
    for i in my_list:
        if i > result:
            result = i
    return result
