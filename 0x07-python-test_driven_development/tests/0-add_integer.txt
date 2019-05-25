This doctest checks a function that adds 2 integers.
Import the module
>>> add_integer = __import__('0-add_integer').add_integer

Add two integers
>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98
>>> add_integer(2)
100
>>> add_integer(100.3, -2)
98
>>> add_integer(-3, -2)
-5
>>> add_integer(-3, 2)
-1
>>> add_integer(0)
98

Test that the return type is an int
>>> add_integer(3.2, 4.1)
7

Correct error raised
>>> add_integer("Hello")
Traceback (most recent call last):
TypeError: a must be an integer

>>> add_integer(2,"Hello")
Traceback (most recent call last):
TypeError: b must be an integer

>>> add_integer(None)
Traceback (most recent call last):
TypeError: a must be an integer

>>> add_integer(float('nan'))
Traceback (most recent call last):
TypeError: a must be an integer

>>> add_integer(98, float('nan'))
Traceback (most recent call last):
TypeError: b must be an integer
