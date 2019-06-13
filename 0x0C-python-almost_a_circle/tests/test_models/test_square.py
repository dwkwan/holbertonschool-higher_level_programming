#!/usr/bin/python3
"""Unittest for Base class"""


import unittest
import io
import contextlib
from models.square import Square
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """This class allows for testing of Base class"""
    def test_SquareinheritancefromBase(self):
        """This function tests that square inherits from Base"""
        Square.reset_objects()
        self.assertEqual(issubclass(Square, Base), True)

    def test_SquareinheritancefromRectangle(self):
        """This function tests that square inherits from Base"""
        Square.reset_objects()
        self.assertEqual(issubclass(Square, Rectangle), True)

    def test_objectinheritance(self):
        """This function tests that object is of type Rectangle"""
        Square.reset_objects()
        s1 = Square(5)
        self.assertEqual(isinstance(s1, Square), True)

    def test_errorfornoarguments(self):
        """This function tests that Typeerror is thrown when 0 arguments"""
        Square.reset_objects()
        with self.assertRaises(TypeError) as e:
            s1 = Square()
        self.assertEqual(
            str(e.exception),
            "__init__() missing 1 required positional argument: 'size'")

    def test_errorfortoomanyarguments(self):
        """This function tests that Typeerror is thrown when 0 arguments"""
        Square.reset_objects()
        with self.assertRaises(TypeError) as e:
            s1 = Square(1, 2, 3, 4, 5)
        self.assertEqual(
            str(e.exception),
            "__init__() takes from 2 to 5 positional" +
            " arguments but 6 were given")

    def test_negativesize(self):
        """This function tests that Typeerror is thrown when 0 arguments"""
        Square.reset_objects()
        with self.assertRaises(ValueError) as e:
            s1 = Square(-1)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_negativexvalue(self):
        """This function tests that ValueError is thrown for - x value"""
        Square.reset_objects()
        with self.assertRaises(ValueError) as e:
            s1 = Square(1, -2)
        self.assertEqual(str(e.exception), "x must be >= 0")

    def test_negativeyvalue(self):
        """This function tests that ValueError is thrown for - y value"""
        Square.reset_objects()
        with self.assertRaises(ValueError) as e:
            s1 = Square(1, 2, -2)
        self.assertEqual(str(e.exception), "y must be >= 0")

    def test_0size(self):
        """This function tests that ValueError is thrown for 0 size value"""
        Square.reset_objects()
        with self.assertRaises(ValueError) as e:
            s1 = Square(0)
        self.assertEqual(str(e.exception), "width must be > 0")

    def test_singlesquarecreation(self):
        """This function tests for single instance creation"""
        Square.reset_objects()
        s1 = Square(10)
        self.assertEqual(s1.id, 1)

    def test_multiplesquarecreation(self):
        """This function tests for single instance creation"""
        Square.reset_objects()
        s1 = Square(10)
        s2 = Square(2)
        s3 = Square(3)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s3.id, 3)

    def test_singlesquarecreationwithallvalues(self):
        """This function tests for single instance creation"""
        Square.reset_objects()
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 10)
        self.assertEqual(s1.id, 10)
        s2 = Square(10, 10, 10, 10)
        self.assertEqual(s2.width, 10)
        self.assertEqual(s2.height, 10)
        self.assertEqual(s2.x, 10)
        self.assertEqual(s2.y, 10)
        self.assertEqual(s2.id, 10)

    def test_multiplesquarecreationwithallvalues(self):
        """This function tests for single instance creation"""
        Square.reset_objects()
        s1 = Square(10, 10, 10, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.height, 10)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 10)
        self.assertEqual(s1.id, 10)

    def test_badsizevaluewithstring(self):
        """This function tests for bad size value with string"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square("foo", 1, 2, 3)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badxvaluewithstring(self):
        """This function tests for bad x value with string"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, "foo", 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithstring(self):
        """This function tests for bad y value with string"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, "foo", 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_badsizevaluewithtuple(self):
        """This function tests for bad size value with tuple"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square((1, 2), 1, 2, 3)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badxvaluewithtuple(self):
        """This function tests for bad x value with tuple"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, (1, 2), 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithtuple(self):
        """This function tests for bad y value with tuple"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, (1, 2), 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_badsizevaluelists(self):
        """This function tests for bad size value with list"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square([1, 2], 1, 2, 3)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badxvaluewithlist(self):
        """This function tests for bad x value with list"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, [1, 2], 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithlist(self):
        """This function tests for bad y value with list"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, [1, 2], 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_badsizevaluebool(self):
        """This function tests for bad size value with bools"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(True, 1, 2, 3)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badxvaluewithbools(self):
        """This function tests for bad x value with bools"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, False, 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithbools(self):
        """This function tests for bad y value with bools"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, True, 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_badsizevaluefloats(self):
        """This function tests for bad size value with floats"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(float(1), 1, 2, 3)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badxvaluewithfloats(self):
        """This function tests for bad x value with floats"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, float(1), 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithfloats(self):
        """This function tests for bad y value with floats"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, float(1), 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_badsizevaluesets(self):
        """This function tests for bad size value with sets"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square({1, 2, 3}, 1, 2, 3)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badxvaluewithsets(self):
        """This function tests for bad x value with sets"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, {1, 2, 3}, 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithsets(self):
        """This function tests for bad y value with sets"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, {1, 2, 3}, 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_badsizevaluedicts(self):
        """This function tests for bad size value with sets"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square({"foo": 1}, 1, 2, 3)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badxvaluewithdicts(self):
        """This function tests for bad x value with dicts"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, {"foo": 1}, 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithdicts(self):
        """This function tests for bad y value with dicts"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, {"foo": 1}, 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_badsizevaluefuncs(self):
        """This function tests for bad size value with funcs"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(print(), 1, 2, 3)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_badxvaluewithfuncs(self):
        """This function tests for bad x value with funcs"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, print(), 2, 3)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_badyvaluewithfuncs(self):
        """This function tests for bad y value with funcs"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, print(), 3)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_NaNsize(self):
        """This function tests for NaN x value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(float('nan'), 10, 5, 7)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_NaNx(self):
        """This function tests for NaN x value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(10, float('nan'), 5, 7)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_NaNy(self):
        """This function tests for NaN y value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(10, 10, float('nan'), 7)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_NaNall(self):
        """This function tests for all NaN values"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(
                float('nan'), float('nan'),  float('nan'), float('nan'))
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_infsize(self):
        """This function tests for inf size value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(float('Inf'), 10, 5, 7)
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_infx(self):
        """This function tests for inf x value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(10, float('Inf'), 5, 7)
        self.assertEqual(str(e.exception), 'x must be an integer')

    def test_infy(self):
        """This function tests for inf y value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(10, 10, float('Inf'), 7)
        self.assertEqual(str(e.exception), 'y must be an integer')

    def test_infall(self):
        """This function tests for all inf value"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(
                float('Inf'), float('Inf'),  float('Inf'), float('Inf'))
        self.assertEqual(str(e.exception), 'width must be an integer')

    def test_sizegetter(self):
        """This function tests the size getter"""
        Rectangle.reset_objects()
        r1 = Square(1, 2, 2, 3)
        self.assertEqual(r1.size, 1)

    def test_sizesetter(self):
        """This function tests the size setter"""
        Rectangle.reset_objects()
        r1 = Square(1, 2, 2, 3)
        self.assertEqual(r1.size, 1)
        r1.size = 100
        self.assertEqual(r1.size, 100)

    def test_sizesetterwithstring(self):
        """This function tests the size setter with string"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, 2, 3)
            self.assertEqual(r1.size, 1)
            r1.size = "foo"
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_sizesetterwithtuple(self):
        """This function tests the size setter with string"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, 2, 3)
            self.assertEqual(r1.size, 1)
            r1.size = (1, 2)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_sizesetterwithlist(self):
        """This function tests the size setter with string"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, 2, 3)
            self.assertEqual(r1.size, 1)
            r1.size = [1, 2]
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_sizesetterwithdict(self):
        """This function tests the size setter with string"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, 2, 3)
            self.assertEqual(r1.size, 1)
            r1.size = {"foo": 2}
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_sizesetterwithset(self):
        """This function tests the size setter with string"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, 2, 3)
            self.assertEqual(r1.size, 1)
            r1.size = {"foo", 2}
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_sizesetterwithfunc(self):
        """This function tests the size setter with func"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, 2, 3)
            self.assertEqual(r1.size, 1)
            r1.size = print()
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_sizesetterwithfloat(self):
        """This function tests the size setter with func"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, 2, 3)
            self.assertEqual(r1.size, 1)
            r1.size = float(1)
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_sizesetterwithbool(self):
        """This function tests the size setter with func"""
        Rectangle.reset_objects()
        with self.assertRaises(TypeError) as e:
            r1 = Square(1, 2, 2, 3)
            self.assertEqual(r1.size, 1)
            r1.size = True
        self.assertEqual(str(e.exception), "width must be an integer")

    def test_update(self):
        """This function tests the update function"""
        Square.reset_objects()
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
        s1.update(x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/4 - 2")
        s1.update(size=7, y=1)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_kwargsskipped(self):
        """This function tests updating args with kwargs"""
        Rectangle.reset_objects()
        s1 = Square(10, 10, 10, 10)
        s1.update(1, 2, 3, 4, id=10)
        self.assertEqual(s1.id, 1)

    def test_updatebadsizevalue(self):
        """This function tests for bad size value"""
        Square.reset_objects()
        r1 = Square(1, 2, 3, 4)
        r1.update(1, "foo")
        self.assertEqual(r1.size, 1)

    def test_updatebadxvalue(self):
        """This function tests for bad size value"""
        Square.reset_objects()
        r1 = Square(1, 2, 3, 4)
        r1.update(1, 2, "foo")
        self.assertEqual(r1.x, 2)

    def test_updatebadyvalue(self):
        """This function tests for bad size value"""
        Square.reset_objects()
        r1 = Square(1, 2, 3, 4)
        r1.update(1, 2, 3, "foo")
        self.assertEqual(r1.y, 3)

    def test_updateallbadvalues(self):
        """This function tests for all bad values"""
        Square.reset_objects()
        r1 = Square(1, 2, 3, 4)
        r1.update([1], (9, ), True, "foo")
        self.assertEqual(r1.size, 1)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.id, 4)

    def test_to_dict(self):
        """This function tests the to_dictionary function"""
        Square.reset_objects()
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 1, 'x': 2, 'size': 10, 'y': 1})

    def test_updatewithdict(self):
        """This function tests the update function with to_dict"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 1)

    def test_updatewithdictionarybycomparingdictionaries(self):
        """This function tests the to_dictionary function"""
        s1 = Square(10, 2, 1, 9)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        self.assertEqual(s1.__dict__, s2.__dict__)

    def test__str__method(self):
        """This function tests the str function"""
        Rectangle.reset_objects()
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (2) 2/0 - 2")
        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (3) 1/3 - 3")

    def test_display__method(self):
        """This function tests the display function"""
        Rectangle.reset_objects()
        s1 = Square(5)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s1.display()
        self.assertEqual(f.getvalue(), "#####\n#####\n#####\n#####\n#####\n")

    def test_display__method2(self):
        """This function tests the display function"""
        Rectangle.reset_objects()
        s2 = Square(2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s2.display()
        self.assertEqual(f.getvalue(), "  ##\n  ##\n")

    def test_display__method3(self):
        """This function tests the display function"""
        Rectangle.reset_objects()
        s3 = Square(3, 1, 3)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s3.display()
        self.assertEqual(f.getvalue(), "\n\n\n ###\n ###\n ###\n")

    def test_area_method(self):
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 9)

    def test_area_methodwithargthrowerror(self):
        s3 = Square(3, 1, 3)
        with self.assertRaises(TypeError) as e:
            s3.area(9)
        self.assertEqual(str(e.exception),
                         "area() takes 1 positional argument but 2 were given")
