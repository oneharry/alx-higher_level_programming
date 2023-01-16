#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_size(self):
        self.a = Square(3)
        self.assertEqual(self.a.size, 3)

    def test_set_size(self):
        self.a = Square(1)
        self.a.size = 9
        self.assertEqual(self.a.size, 9)
