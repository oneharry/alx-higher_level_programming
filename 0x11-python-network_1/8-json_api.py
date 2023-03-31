#!/usr/bin/python3
""" 
Send POST request to http://0.0.0.0:5000/search_user with letter as a param
displays id and name of body
"""


import requests
import sys
if __name__ == '__main__':
    val = ""
    if sys.argv[1]:
        val = sys.argv[1]
    data = {'q': val}
    res = requests.get('http://0.0.0.0:5000/search_user', data)
    
    
