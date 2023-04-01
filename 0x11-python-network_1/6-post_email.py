#!/usr/bin/python3
""" Sends a POST request - url with email address as a parameter"""


import requests
import sys
if __name__ == '__main__':
    res = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print("{}".format(res.text))
