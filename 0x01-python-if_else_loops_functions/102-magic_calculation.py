#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c
    else:
        if b > c:
            return a * b - c
        return a + b
print(magic_calculation(3, 1, 2))
