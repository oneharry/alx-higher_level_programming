#!/usr/bin/python3
def roman_to_int(roman_string):
    d = dict({'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000})
    if not isinstance(roman_string, str) or None:
        return 0
    temp = ""
    tot = 0
    for i in roman_string:
        for k, v in d.items():
            if i == k:
                if temp + k == "IV" or temp + k == "IX" or temp + k == "XL":
                    tot -= d[temp]
                    tot += d[k] - d[temp]
                elif temp + k == "XC" or temp + k == "CD" or temp + k == "CM":
                    tot -= d[temp]
                    tot += d[k] - d[temp]
                else:
                    tot += d[k]
                temp = k
    return tot
