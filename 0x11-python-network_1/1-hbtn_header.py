#!/usr/bin/python3
""" Send request to URL = displays X-Request-Id variable in the header response"""


import urllib.request
import sys
if __name__ == '__main__':
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as res:
            response = res.read()
            print("{}".format(res.headers["X-Request-Id"]))
    except URLError as err:
        pass
