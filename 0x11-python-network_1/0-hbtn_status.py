#!/usr/bin/python3
""" Fetches from URL = https://alx-intranet.hbtn.io/status """


import urllib.request
if __name__ == '__main__':
    try:
        url = "https://alx-intranet.hbtn.io/status"
        with urllib.request.urlopen(url) as res:
            response = res.read()
            print("Body response:")
            print("\t - {}: {}".format("type", type(response)))
            print("\t - {}: {}".format("content", response))
            print("\t - {}: {}".format("utf8 content", res.msg))
    except URLError as err:
        pass
