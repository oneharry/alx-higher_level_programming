#!/usr/bin/python3
""" Sends a POST request - url with email address as a parameter"""


import requests
import sys
if __name__ == '__main__':
    res = requests.get(sys.argv[1])
    if res.status_code < 400:
        print("{}".format(res.text))
    else:
        print("Error code: {}".format(res.status_code))
