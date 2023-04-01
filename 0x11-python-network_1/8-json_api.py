#!/usr/bin/python3
"""
Send POST request to http://0.0.0.0:5000/search_user with letter as a param
displays id and name of body
"""


import requests
import sys
import json
if __name__ == '__main__':
    val = ""
    try:
        if len(sys.argv) < 1 or type(eval(sys.argv[1])) != str:
            raise IndexError
        val = sys.argv[1]
        data = {'q': val}
        res = requests.post('http://0.0.0.0:5000/search_user', data)
        if json.load(res.text):
            res.raise_for_status()
        print(res.text)
    except json.decoder.JSONDecodeError as err:
        print("Not a valid JSON")
    except IndexError:
        print("No result")
