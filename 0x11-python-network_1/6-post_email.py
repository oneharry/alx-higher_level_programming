#!/usr/bin/python3
""" Sends a POST request - url with email address as a parameter"""


import requests
import sys
if __name__ == '__main__':
    res = requests.get(sys.argv[1], {'email': sys.argv[2]})
    print("{}".format(res.text))
