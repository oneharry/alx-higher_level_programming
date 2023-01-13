#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_create_Base(self):
        self.a = Base()
        self.assertIs(type(self.a), Base)

    def test_instance(self):
        self.a = Base()
        self.b = Base()
        self.assertIs(type(self.a), type(self.b))

    def test_id_without_arg(self):
        self.a = Base()
        self.b = Base()
        self.assertEqual(self.a.id, self.b.id - 1)

    def test_id_with_arg(self):
        self.a = Base()
        self.b = Base(13)
        self.assertEqual(self.b.id, 13)

    def test_id_float(self):
        self.a = Base()
        self.b = Base(4.5)
        self.assertEqual(self.b.id, 4)

    def test_id_string(self):
        self.a = Base()
        self.b = Base("Hello")
        self.assertEqual(self.a.id, self.b.id - 1)

    def test_neg_int(self):
        self.a = Base()
        self.b = Base(-3)
        self.assertEqual(self.a.id, self.b.id - 1)

    def test_multiple_args(self):
        with self.assertRaises(TypeError):
            self.b = Base(6, 3)
