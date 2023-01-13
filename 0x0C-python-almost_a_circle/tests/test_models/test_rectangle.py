#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_all_args(self):
        self.a = Rectangle(10, 2, 0, 0)
        self.b = Rectangle(12, 5, 1, 3)
        self.assertEqual(self.a.id, self.b.id - 1)

    def test_positional_arg(self):
        self.a = Rectangle(3, 8)
        self.b = Rectangle(15, 10)
        self.assertEqual(self.a.id, self.b.id - 1)

    def test_set_width(self):
        self.a = Rectangle(4, 2, 2, 1, 17)
        self.a.width = 6
        self.assertEqual(self.a.width, 6)

    def test_set_height(self):
        self.a = Rectangle(6, 3)
        self.a.height = 4
        self.assertEqual(self.a.height, 4)

    def test_set_x(self):
        self.a = Rectangle(10, 8)
        self.a.x = 5
        self.assertEqual(self.a.x, 5)

    def test_set_y(self):
        self.a = Rectangle(2, 4, 10, 17)
        self.a.y = 15
        self.assertEqual(self.a.y, 15)

    def test_width_instatiation_valid(self):
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle("a", 1)
        self.assertEqual("width must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(3.6, 3)
        self.assertEqual("width must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(None, 4,)
        self.assertEqual("width must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle([2, 4], 9)
        self.assertEqual("width must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle({"a": 3, "d": 0}, 5)
        self.assertEqual("width must be an integer", str(exc.exception))
        with self.assertRaises(ValueError) as exc:
            self.a = Rectangle(-5, 9)
        self.assertEqual("width must be > 0", str(exc.exception))

    def test_width_setter_valid(self):
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(7, 1)
            self.a.width = "a"
        self.assertEqual("width must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(6, 3)
            self.a.width = 5.3
        self.assertEqual("width must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(9, 4,)
            self.a.width = None
        self.assertEqual("width must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(2, 9)
            self.a.width = [7, 10]
        self.assertEqual("width must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(10, 5)
            self.a.width = {"1": "one"}
        self.assertEqual("width must be an integer", str(exc.exception))
        with self.assertRaises(ValueError) as exc:
            self.a = Rectangle(10, 5)
            self.a.width = -4
        self.assertEqual("width must be > 0", str(exc.exception))

    def test_height_instatiation_valid(self):
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(4, "a")
        self.assertEqual("height must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(6, 1.3)
        self.assertEqual("height must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(6, None)
        self.assertEqual("height must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(5, [2, 4])
        self.assertEqual("height must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(9, {"a": 3, "d": 0})
        self.assertEqual("height must be an integer", str(exc.exception))
        with self.assertRaises(ValueError) as exc:
            self.a = Rectangle(10, -5)
        self.assertEqual("height must be > 0", str(exc.exception))

    def test_height_setter_valid(self):
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(7, 1)
            self.a.height = "a"
        self.assertEqual("height must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(6, 3)
            self.a.height = 8.4
        self.assertEqual("height must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(9, 4,)
            self.a.height = None
        self.assertEqual("height must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(2, 9)
            self.a.height = [7, 10]
        self.assertEqual("height must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(10, 5)
            self.a.height = {"1": "one"}
        self.assertEqual("height must be an integer", str(exc.exception))
        with self.assertRaises(ValueError) as exc:
            self.a = Rectangle(10, 5)
            self.a.height = 0
        self.assertEqual("height must be > 0", str(exc.exception))

    def test_x_instatiation_valid(self):
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(3, 1, "a")
        self.assertEqual("x must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(4, 3, 4.6)
        self.assertEqual("x must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(3, 4, None)
        self.assertEqual("x must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(8, 4, [2, 4])
        self.assertEqual("x must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(2, 10, {"a": 3, "d": 0})
        self.assertEqual("x must be an integer", str(exc.exception))
        with self.assertRaises(ValueError) as exc:
            self.a = Rectangle(8, 2, -4)

    def test_x_setter_valid(self):
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(7, 1)
            self.a.x = "a"
        self.assertEqual("x must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(6, 3)
            self.a.x = 3.9
        self.assertEqual("x must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(9, 4)
            self.a.x = None
        self.assertEqual("x must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(2, 9)
            self.a.x = [7, 10]
        self.assertEqual("x must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(10, 5)
            self.a.x = {"1": "one"}
        self.assertEqual("x must be an integer", str(exc.exception))
        with self.assertRaises(ValueError) as exc:
            self.a = Rectangle(10, 5)
            self.a.x = -9
        self.assertEqual("x must be >= 0", str(exc.exception))

    def test_y_instatiation_valid(self):
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(3, 2, 5, "a")
        self.assertEqual("y must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(8, 4, 1, 3.6)
        self.assertEqual("y must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(9, 4, 9, None)
        self.assertEqual("y must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(9, 4, 7, [2, 4])
        self.assertEqual("y must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(4, 2, 7, {"a": 3, "d": 0})
        self.assertEqual("y must be an integer", str(exc.exception))
        with self.assertRaises(ValueError) as exc:
            self.a = Rectangle(4, 7, 1, -10)
        self.assertEqual("y must be >= 0", str(exc.exception))

    def test_y_setter_valid(self):
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(7, 1)
            self.a.y = "a"
        self.assertEqual("y must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(6, 3)
            self.a.y = 8.6
        self.assertEqual("y must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(9, 4,)
            self.a.y = None
        self.assertEqual("y must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(2, 9)
            self.a.y = [7, 10]
        self.assertEqual("y must be an integer", str(exc.exception))
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(10, 5)
            self.a.y = {"1": "one"}
        self.assertEqual("y must be an integer", str(exc.exception))
        with self.assertRaises(ValueError) as exc:
            self.a = Rectangle(10, 5)
            self.a.y = -3
        self.assertEqual("y must be >= 0", str(exc.exception))

    def test_incomplete_pos_arg(self):
        with self.assertRaises(TypeError):
            self.a = Rectangle(7)

    def test_area(self):
        self.a = Rectangle(3, 2)
        self.assertEqual(self.a.area(), 6)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self, stdout):
        disp = "####\n####\n####\n"
        self.a = Rectangle(4, 3)
        self.a.display()
        self.assertEqual(stdout.getvalue(), disp)

    def test_str(self):
        self.a = Rectangle(3, 1, 8, 2, 11)
