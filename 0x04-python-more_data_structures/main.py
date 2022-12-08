#!/usr/bin/python3
""" Roman to Integer test file
"""
roman_to_int = __import__('12-roman_to_int').roman_to_int

roman_number = "IV"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XL"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CD"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "XC"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "CM"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
