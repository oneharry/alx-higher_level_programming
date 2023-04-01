#!/usr/bin/python3
""" Send POST request to URL with eamail as parameter
displays response body"""


from urllib.request import Request, urlopen
from urllib.parse import urlencode
import sys
if __name__ == '__main__':
    values = {'email': sys.argv[2]}
    data = urlencode(values)
    data = data.encode('ascii')
    url = sys.argv[1]
    req = Request(url, data=data)
    with urlopen(req) as res:
        print("{}".format(res.read().decode('utf-8')))
