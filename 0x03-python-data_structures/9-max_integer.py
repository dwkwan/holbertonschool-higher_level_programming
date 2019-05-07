#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        result = my_list[0]
        for i in my_list[1:]:
            if i > result:
                result = i
        return result
