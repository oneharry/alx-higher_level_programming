#!/usr/bin/python3
""" Fetches from URL = https://alx-intranet.hbtn.io/status """


import urllib.request
if __name__ == '__main__':
    try:
        with urllib.request.urlopen('https://alx-intranet.hbtn.io/status')
        as res:
            response = res.read()
            print("\t - {}: {}".format("type", type(response)))
            print("\t - {}: {}".format("content", response))
            print("\t - {}: {}".format("utf8 content", res.msg))
    except URLError as err:
        pass
