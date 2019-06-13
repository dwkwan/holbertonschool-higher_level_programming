#!/usr/bin/python3
"""Unittest for Rectangle class"""


import unittest
from models.rectangle import Rectangle
from models.base import Base
import io
import contextlib


class TestBaseClass(unittest.TestCase):
    """This class allows for testing of Base class"""

    def test_Rectangleinheritance(self):
        """This function tests that rectangle inherits from Base"""
        Rectangle.reset_objects()
        self.assertEqual(issubclass(Rectangle, Base), True)

    def test_objectinheritance(self):
        """This function tests that rectangle inherits from Base"""
        Rectangle.reset_objects()
        r1 = Rectangle(1, 1)
        self.assertEqual(isinstance(r1, Rectangle), True)

    def test_errorfornoarguments(self):
        """This function tests that Typeerror is thrown when 0 arguments"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle()
        self.assertEqual(
            str(e.exception),
            "__init__() missing 2 required positional arguments: 'width' and" +
            " 'height'")

    def test_errorfor1argument(self):
        """This function tests that Typeerror is thrown when 1 argument"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1)
        self.assertEqual(
            str(e.exception),
            "__init__() missing 1 required positional argument: 'height'")

    def test_errorfortoomanyarguments(self):
        """This function tests that Valueerror is thrown when extra args"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, 3, 4, 5, 7)
        self.assertEqual(
            str(e.exception),
            "'__init__() takes from 3 to 6" +
            "positional arguments but 7 were given'")

    def test_singlerectanglecreation(self):
        """This function tests for single instance creation"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_multiplerectanglecreation(self):
        """This function tests for multiple instance creation"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 3)

    def test_rectanglecreationwith1and2(self):
        """This function tests for ereationwithtwoattributesset"""
        Rectangle.reset_objects()
        r1 = Rectangle(1, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_rectanglecreationwithheight0(self):
        """This function tests for height set to 0"""
        Rectangle.reset_objects()
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(1, 0)
        self.assertEqual(str(e.exception), 'height must be > 0')

    def test_singlerectanglecreationwithallvalues(self):
        """This function tests for single instance creati\
on"""
        Rectangle.reset_objects()
        s1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 10)
        self.assertEqual(s1.id, 10)

    def test_duplicateid(self):
        """This function tests for multiple instance creation"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 5)
        r2 = Rectangle(10, 10, 10, 10, 5)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r2.id, 5)

    def test_badwidthvaluewithstring(self):
        """This function tests for bad size value with string"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle("foo", 1, 2, 3)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badheightvaluewithstring(self):
        """This function tests for bad size value with string"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, "foo", 1, 2, 3)
        self.assertEqual(str(e.exception), 'height must be an integer')

    def test_badxvaluewithstring(self):
        """This function tests for bad x value with string"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, "foo", 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithstring(self):
        """This function tests for bad y value with string"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, 3, "foo", 2)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_badwidthvaluewithtuple(self):
        """This function tests for bad width value with tuple"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle((1, 2), 1, 2, 3)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badheightvaluewithtuple(self):
        """This function tests for bad width value with tuple"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, (1, 2), 1, 2, 3)
        self.assertEqual(str(e.exception), 'height must be an integer')

    def test_badxvaluewithtuple(self):
        """This function tests for bad x value with tuple"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(5, 1, (1, 2), 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithtuple(self):
        """This function tests for bad y value with tuple"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(5, 1, 2, (1, 2), 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_badwidthvaluelists(self):
        """This function tests for bad width value with list"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle([1, 2], 1, 2, 3, 5)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badheightvaluelists(self):
        """This function tests for bad width value with list"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, [1, 2], 1, 2, 3)
        self.assertEqual(str(e.exception), 'height must be an integer')

    def test_badxvaluewithlist(self):
        """This function tests for bad x value with list"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(2, 1, [1, 2], 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithlist(self):
        """This function tests for bad y value with list"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, 3, [1, 2], 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_badwidthvaluebool(self):
        """This function tests for bad width value with bools"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(True, 1, 2, 3, 4)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badheightvaluebool(self):
        """This function tests for bad width value with bools"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, True, 1, 2, 3)
        self.assertEqual(str(e.exception), 'height must be an integer')

    def test_badxvaluewithbools(self):
        """This function tests for bad x value with bools"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(3, 1, False, 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithbools(self):
        """This function tests for bad y value with bools"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(2, 1, 2, True, 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_badwidthvaluefloats(self):
        """This function tests for bad width value with floats"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(float(1), 1, 2, 3, 5)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badheightvaluefloats(self):
        """This function tests for bad width value with floats"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, float(1), 1, 2, 3)
        self.assertEqual(str(e.exception), 'height must be an integer')

    def test_badxvaluewithfloats(self):
        """This function tests for bad x value with floats"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, float(1), 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithfloats(self):
        """This function tests for bad y value with floats"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, 4, float(1), 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_badwidthvaluesets(self):
        """This function tests for bad width value with sets"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle({1, 2, 3}, 1, 2, 3, 5)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badheightvaluesets(self):
        """This function tests for bad width value with sets"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, {1, 2, 3}, 1, 2, 5)
        self.assertEqual(str(e.exception), 'height must be an integer')

    def test_badxvaluewithsets(self):
        """This function tests for bad x value with sets"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, {1, 2, 3}, 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithsets(self):
        """This function tests for bad y value with sets"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, 2, {1, 2, 3}, 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_badwidthvaluedicts(self):
        """This function tests for bad size value with sets"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle({"foo": 1}, 1, 2, 3, 7)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badheightvaluedicts(self):
        """This function tests for bad size value with sets"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, {"foo": 1}, 1, 2, 7)
        self.assertEqual(str(e.exception), 'height must be an integer')

    def test_badxvaluewithdicts(self):
        """This function tests for bad x value with dicts"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, {"foo": 1}, 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithdicts(self):
        """This function tests for bad y value with dicts"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(2, 1, 2, {"foo": 1}, 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_badwidthvaluefuncs(self):
        """This function tests for bad size value with funcs"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(print(), 2, 1, 2, 3)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badheightvaluefuncs(self):
        """This function tests for bad size value with funcs"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, print(), 1, 2, 3)
        self.assertEqual(str(e.exception), 'height must be an integer')

    def test_badxvaluewithfuncs(self):
        """This function tests for bad x value with funcs"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(2, 1, print(), 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithfuncs(self):
        """This function tests for bad y value with funcs"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(2, 1, 2, print(), 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_allbadvalues(self):
        """This function tests for bad width value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(False, "foo", {"str": 7}, ("hello", ), True)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_NaNwidth(self):
        """This function tests for NaN x value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(float('nan'), 10, 5, 7, 7)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_NaNheight(self):
        """This function tests for NaN height value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(10, float('nan'), 5, 7, 7)
        self.assertEqual(str(e.exception), 'height must be an integer')

    def test_NaNx(self):
        """This function tests for NaN x value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(10, 10, float('nan'), 5, 7)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_NaNy(self):
        """This function tests for NaN y value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(10, 10, 5, float('nan'), 7)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_NaNall(self):
        """This function tests for all NaN values"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(
                float('nan'), float('nan'),  float('nan'), float('nan'),
                float('nan'))
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_infwidth(self):
        """This function tests for NaN height value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(float('Inf'), 10, 5, 7, 7)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_infheight(self):
        """This function tests for inf height value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(10, float('Inf'), 5, 7, 7)
        self.assertEqual(str(e.exception), 'height must be an integer')

    def test_infx(self):
        """This function tests for inf x value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(10, 10, float('Inf'), 5, 7)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_infy(self):
        """This function tests for inf y value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(10, 10, 5, float('Inf'), 7)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_infall(self):
        """This function tests for all inf value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(float('Inf'), float('Inf'),  float('Inf'),
                           float('Inf'),  float('Inf'))
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_inf(self):
        """This function tests for NaN"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(float('inf'), 10, 10, 5, 7)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_noidgiven(self):
        """This function tests that id is auto-set when none is given"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_recNoneid(self):
        """This function tests for None argument"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, None)
        self.assertEqual(r1.id, 1)

    def test_widthgetter(self):
        """This function tests for getting width"""
        Rectangle.reset_objects()
        r1 = Rectangle(25, 20, 30, 35, 100)
        self.assertEqual(r1.width, 25)

    def test_heightgetter(self):
        """This function tests for getting height"""
        Rectangle.reset_objects()
        r1 = Rectangle(25, 20, 30, 35, 100)
        self.assertEqual(r1.height, 20)

    def test_xgetter(self):
        """This function tests for getting x"""
        Rectangle.reset_objects()
        r1 = Rectangle(25, 20, 30, 35, 100)
        self.assertEqual(r1.x, 30)

    def test_ygetter(self):
        """This function tests for getting y"""
        Rectangle.reset_objects()
        r1 = Rectangle(25, 20, 30, 35, 100)
        self.assertEqual(r1.y, 35)

    def test_widthsetter(self):
        """This function tests the width setter"""
        Rectangle.reset_objects()
        r1 = Rectangle(25, 20, 30, 35, 100)
        r1.width = 45
        self.assertEqual(r1.width, 45)

    def test_heightsetter(self):
        """This function tests the height setter"""
        Rectangle.reset_objects()
        r1 = Rectangle(25, 20, 30, 35, 100)
        r1.height = 40
        self.assertEqual(r1.height, 40)

    def test_xsetter(self):
        """This function tests the x setter"""
        Rectangle.reset_objects()
        r1 = Rectangle(25, 20, 30, 35, 100)
        r1.x = 50
        self.assertEqual(r1.x, 50)

    def test_ysetter(self):
        """This function tests the y setter"""
        Rectangle.reset_objects()
        r1 = Rectangle(25, 20, 30, 35, 100)
        r1.y = 55
        self.assertEqual(r1.y, 55)

    def test_widthsettervalidation(self):
        """This function tests width setter validation"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(25, 20, 30, 35, 100)
            r1.width = "foo"
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_heightsettervalidation(self):
        """This function tests height setter validation"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(25, 20, 30, 35, 100)
            r1.height = "foo"
        self.assertEqual(str(e.exception), 'height must be an integer')

    def test_xsettervalidation(self):
        """This function tests x setter validation"""
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(25, 20, 30, 35, 100)
            r1.x = "foo"
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_ysettervalidation(self):
        """This function tests y setter validation"""
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(25, 20, 30, 35, 100)
            r1.y = "foo"
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_widthsettervalidationfor0(self):
        """This function tests width setter validation for 0"""
        Rectangle.reset_objects()
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(25, 20, 30, 35, 100)
            r1.width = 0
        self.assertEqual(str(e.exception), 'width must be > 0')

    def test_heightsettervalidationfor0(self):
        """This function tests height setter validation for 0"""
        Rectangle.reset_objects()
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(25, 20, 30, 35, 100)
            r1.height = 0
        self.assertEqual(str(e.exception), 'height must be > 0')

    def test_widthsettervalidationfornegative(self):
        """This function tests width setter validation for 0"""
        Rectangle.reset_objects()
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(25, 20, 30, 35, 100)
            r1.width = -1
        self.assertEqual(str(e.exception), 'width must be > 0')

    def test_heightsettervalidationfornegative(self):
        """This function tests height setter validation for 0"""
        Rectangle.reset_objects()
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(25, 20, 30, 35, 100)
            r1.height = -1
        self.assertEqual(str(e.exception), 'height must be > 0')

    def test_xsettervalidationfornegative(self):
        """This function tests width setter validation for 0"""
        Rectangle.reset_objects()
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(25, 20, 30, 35, 100)
            r1.x = -1
        self.assertEqual(str(e.exception), 'x must be >= 0')

    def test_ysettervalidationfornegative(self):
        """This function tests width setter validation for 0"""
        Rectangle.reset_objects()
        with self.assertRaises(ValueError) as e:
            r1 = Rectangle(25, 20, 30, 35, 100)
            r1.y = -1
        self.assertEqual(str(e.exception), 'y must be >= 0')

    def test_recprivateclassvariable(self):
        """This function tests __nb_objects being private"""
        Rectangle.reset_objects()
        with self.assertRaises(AttributeError) as e:
            print(Rectangle.__nb_objects)
        self.assertEqual(
            str(e.exception),
            "type object \'Rectangle\' has no attribute \'_TestBaseClass__n" +
            "b_objects\'")

    def test_recprivatewidthvariable(self):
        """This function tests width being private"""
        Rectangle.reset_objects()
        r1 = Rectangle(25, 20, 30, 35, 100)
        with self.assertRaises(AttributeError) as e:
            print(r1.__width)
        self.assertEqual(
            str(e.exception),
            "\'Rectangle\' object has no attribute \'_TestBaseClass__width\'")

    def test_recprivateheightvariable(self):
        """This function tests height being private"""
        Rectangle.reset_objects()
        r1 = Rectangle(25, 20, 30, 35, 100)
        with self.assertRaises(AttributeError) as e:
            print(r1.__height)
        self.assertEqual(
            str(e.exception),
            "\'Rectangle\' object has no attribute \'_TestBaseClass__height\'")

    def test_recprivatexvariable(self):
        """This function tests width being private"""
        Rectangle.reset_objects()
        r1 = Rectangle(25, 20, 30, 35, 100)
        with self.assertRaises(AttributeError) as e:
            print(r1.__x)
        self.assertEqual(
            str(e.exception),
            "\'Rectangle\' object has no attribute \'_TestBaseClass__x\'")

    def test_recprivateyvariable(self):
        """This function tests width being private"""
        Rectangle.reset_objects()
        r1 = Rectangle(25, 20, 30, 35, 100)
        with self.assertRaises(AttributeError) as e:
            print(r1.__y)
        self.assertEqual(
            str(e.exception),
            "\'Rectangle\' object has no attribute \'_TestBaseClass__y\'")

    def test_publicareamethod(self):
        """This function tests the public area method"""
        Rectangle.reset_objects()
        r1 = Rectangle(5, 10, 7, 9, 100)
        self.assertEqual(r1.area(), 50)

    def test_area_methodwithargthrowerror(self):
        s3 = Rectangle(3, 1, 3)
        with self.assertRaises(TypeError) as e:
            s3.area(9)
        self.assertEqual(str(e.exception),
                         "area() takes 1 positional argument but 2 were given")

    def test_updateid(self):
        """This function tests the public area method"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r1.id, 10)
        r1.update(89)
        self.assertEqual(r1.id, 89)

    def test_updatewidth(self):
        """This function tests updating width"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r1.width, 10)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)

    def test_updateheight(self):
        """This function tests updating height"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r1.height, 10)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)

    def test_updatex(self):
        """This function tests updating x"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r1.x, 10)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)

    def test_updatey(self):
        """This function tests updating y"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        self.assertEqual(r1.y, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

    def test_updateall(self):
        """This function tests updating all attributes"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.x, 10)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

    def test_updatewidthbadvalue(self):
        """This function tests updating width with bad value"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError) as e:
            r1.update(89, "foo")
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_updateheightbadvalue(self):
        """This function tests updating width with bad value"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError) as e:
            r1.update(89, 15, "foo")
        self.assertEqual(str(e.exception), "height must be an integer")

    def test_updatexbadvalue(self):
        """This function tests updating width with bad value"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError) as e:
            r1.update(89, 15, 20, "foo")
        self.assertEqual(str(e.exception), "x must be an integer")

    def test_updateybadvalue(self):
        """This function tests updating width with bad value"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        with self.assertRaises(TypeError) as e:
            r1.update(89, 15, 20, 25, "foo")
        self.assertEqual(str(e.exception), "y must be an integer")

    def test_updatekwargswidth(self):
        """This function tests updating width with kwargs"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(width=1)
        self.assertEqual(r1.width, 1)

    def test_updatekwargsheight(self):
        """This function tests updating height with kwargs"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(height=2)
        self.assertEqual(r1.height, 2)

    def test_updatekwargsx(self):
        """This function tests updating x with kwargs"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(x=3)
        self.assertEqual(r1.x, 3)

    def test_updatekwargsy(self):
        """This function tests updating y with kwargs"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(y=4)
        self.assertEqual(r1.y, 4)

    def test_updatekwargsid(self):
        """This function tests updating id with kwargs"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(id=5)
        self.assertEqual(r1.id, 5)

    def test_updatekwargsall(self):
        """This function tests updating all attrs with kwargs"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(width=5, height=5, x=5, y=5, id=5)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 5)
        self.assertEqual(r1.x, 5)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 5)

    def test_kwargsskipped(self):
        """This function tests updating args with kwargs"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(1, 2, 3, 4, 5, id=10)
        self.assertEqual(r1.id, 1)

    def test_badkeyignored(self):
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update(1, 2, 3, 4, 5, foo=20)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_fornoargumentstoupdate(self):
        """This function tests that update accepts 0 arguments"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 10, 10, 10, 10)
        r1.update()
        self.assertEqual(r1.id, 10)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

    def test_errorfortoomanyarguments(self):
        """This function tests that Valueerror is thrown when extra args"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Rectangle(1, 2, 3, 4, 5, 6)
        self.assertEqual(
            str(e.exception),
            "__init__() takes from 3 to 6 positional " +
            "arguments but 7 were given")

    def test_to_dictionary(self):
        """This function tests the to_dictionary function"""
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        self.assertEqual(r1_dictionary, {'x': 1, 'y': 9, 'id': 1, 'height': 2,
                                         'width': 10})

    def test_updatewithdict(self):
        """This function tests the to_dictionary function"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 2, 3, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 3)
        self.assertEqual(r2.y, 9)

    def test_updatewithdictionarybycomparingdictionaries(self):
        """This function tests the to_dictionary function"""
        Rectangle.reset_objects()
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)
        self.assertEqual(r1.__dict__, r2.__dict__)

    def test__str__method(self):
        """This function tests the str function"""
        Rectangle.reset_objects()
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")
        r2 = Rectangle(5, 5, 1)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

    def test_display__method(self):
        """This function tests the display function"""
        Rectangle.reset_objects()
        r1 = Rectangle(2, 3, 2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r1.display()
        self.assertEqual(f.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_display__method2(self):
        """This function tests the display function"""
        Rectangle.reset_objects()
        r2 = Rectangle(3, 2, 1, 0)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            r2.display()
        self.assertEqual(f.getvalue(), " ###\n ###\n")
