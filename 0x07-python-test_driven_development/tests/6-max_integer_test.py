#!/usr/bin/python3
""" Test module using unittest module """
import unittest


class TestMax(unittest.TestCase):
    """ Class definition of test cases
        Developed different test cases
    """
    def setUp(self):
        """ Method runs before every test case runs """
        self.max_integer = __import__('6-max_integer').max_integer

    def test_number(self):
        """ Test that function return the max number in a list"""
        self.assertEqual(self.max_integer([2, 1, 0, 5]), 5)
        self.assertEqual(self.max_integer([-2, -3, -1, -6]), -1)
        self.assertEqual(self.max_integer([2]), 2)
        self.assertEqual(self.max_integer([3.0, 1, 0, 1.0]), 3)
        self.assertEqual(self.max_integer([3.1, 3.6, 2.3]), 3.6)
    def test_string(self):
        """ Test cases for non iinteger float"""
        self.assertEqual(self.max_integer("Hello"), "o")

    def test_None(self):
        """ test case for none value """
        self.assertEqual(self.max_integer([]), None)
