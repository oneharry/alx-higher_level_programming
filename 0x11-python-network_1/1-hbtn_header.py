#!/usr/bin/python3
""" Send request to URL = displays X-Request-Id variable
in the header response"""


from urllib.request import Request, urlopen
import sys
if __name__ == '__main__':
    req = Request(sys.argv[1])
    with urlopen(req) as res:
        response = res.read()
        print("{}".format(res.headers["X-Request-Id"]))
