#!/usr/bin/python3
"""
Send POST request to http://0.0.0.0:5000/search_user with letter as a param
displays id and name of body
"""


import requests
import sys
if __name__ == '__main__':
    val = ""
    if len(sys.argv) > 1:
        val = sys.argv[1]
    dat = {'q': val}
    res = requests.post('http://0.0.0.0:5000/search_user', data=dat)
    try:
        r = res.json()
        if len(r) == 0 or not r.get("id") or not r.get("name"):
            print("No result")
        else:
            print("[{}] {}".format(r.get("id"), r.get("name")))
    except ValueError:
        print("Not a valid JSON")
