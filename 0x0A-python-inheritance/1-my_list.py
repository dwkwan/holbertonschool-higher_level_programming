#!/usr/bin/python3
"A module that defines a class named MyList"


class MyList(list):
    """A class named MyList
    Attributes:
    attr1(print_sorted): prints sorted list
    """
    def print_sorted(self):
        """Prints instance"""
        print(sorted(self))
