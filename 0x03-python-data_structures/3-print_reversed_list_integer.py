#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        reversedlist = reversed(my_list)
        for i in reversedlist:
            print("{:d}".format(i))
