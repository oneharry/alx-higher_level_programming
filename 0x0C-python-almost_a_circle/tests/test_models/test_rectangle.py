#!/usr/bin/python3
import unittest
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

    def test_string_args(self):
        self.a = Rectangle(9, 3)
        with self.assertRaises(TypeError) as exc:
            self.b = Rectangle(2, 5, 0, "one")
        self.c = Rectangle(8, 4)
        self.assertEqual(self.a.id, self.c.id - 1)

    def test_negative_int(self):
        with self.assertRaises(TypeError) as exc:
            self.a = Rectangle(3, -6)

    def test_incomplete_pos_arg(self):
        with self.assertRaises(TypeError):
            self.a = Rectangle(7)

    def test_None(self):
        with self.assertRaises(ValueError):
            self.a = Rectangle(3, None, 7, 5, 10)
