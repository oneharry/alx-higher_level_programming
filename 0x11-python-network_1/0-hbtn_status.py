#!/usr/bin/python3
""" Fetches from URL = https://alx-intranet.hbtn.io/status """


from urllib.request import Request, urlopen
if __name__ == '__main__':
    req = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(req) as res:
        response = res.read()
        print("Body response:")
        print("\t- {}: {}".format("type", type(response)))
        print("\t- {}: {}".format("content", response))
        print("\t- utf8 content: {}".format(response.decode('utf-8')))
