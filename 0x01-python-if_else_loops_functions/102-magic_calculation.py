#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        if b > c:
            return a * b
        else:
            return c
    else:
        return a + b
