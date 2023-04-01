#!/usr/bin/python3
""" Fetches URL using request and get value of X-Request-Id"""


import requests
import sys
if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    print("{}".format(res.headers.get('X-Request-Id')))
