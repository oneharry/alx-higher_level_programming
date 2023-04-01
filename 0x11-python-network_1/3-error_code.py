#!/usr/bin/python3
""" Send request to URL = displays X-Request-Id variable
in the header response"""


from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys
if __name__ == '__main__':
    try:
        req = Request(sys.argv[1])
        with urlopen(req) as res:
            print("{}".format(res.read().decode('utf-8')))
    except HTTPError as err:
        if hasattr(err, 'code'):
            print("Error code: {}".format(err.code))
