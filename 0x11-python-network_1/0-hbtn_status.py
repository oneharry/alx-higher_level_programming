#!/usr/bin/python3
""" Fetches from URL = https://alx-intranet.hbtn.io/status """


import urllib.request
if __name__ == '__main__':
    try:
        req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
        with urllib.request.urlopen(req) as res:
            response = res.read()
            print("Body response:")
            print("\t - {}: {}".format("type", type(response)))
            print("\t - {}: {}".format("content", response))
            print("\t - utf8 content: {}".format(response.decode('utf-8')))
    except URLError as err:
        pass
