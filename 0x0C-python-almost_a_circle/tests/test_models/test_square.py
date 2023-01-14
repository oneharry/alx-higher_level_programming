#!/usr/bin/python3

import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_area(self):
        self.a = Square(2)
        self.assertEqual(self.a.area, 4)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display(self):
        self.a = Square(4)
        disp = "####\n####\n####\n####\n"
        self.a.display()
        self.assertEqual(stdout.getvalue(), disp)
