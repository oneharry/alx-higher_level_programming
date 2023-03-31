#!/usr/bin/python3
""" Send POST request to URL with eamail as parameter, displays response body"""


from urllib.request import Request, urlopen
import urllib.parse
import sys
if __name__ == '__main__':
    values = {'email' : sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = Request(sys.argv[1], data)
    with urlopen(req) as res:
        response = res.read()
        print("{}".format(response))
