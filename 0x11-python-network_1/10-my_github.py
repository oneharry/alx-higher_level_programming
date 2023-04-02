#!/usr/bin/python3
""" Using github username and password """


import requests
import sys
if __name__ == '__main__':
    username = sys.argv[1]
    token = sys.argv[2]
    header = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    res = requests.get(f'https://api.github.com/users/{username}',
                       headers=header)
    r = res.json()
    print("{}".format(r.get("id")))
