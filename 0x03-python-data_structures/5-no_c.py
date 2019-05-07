#!/usr/bin/python3
def no_c(my_string):
    my_newstring = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            my_newstring += i
    my_string = my_newstring
    return my_string
