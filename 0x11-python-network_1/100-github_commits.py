#!/usr/bin/python3
""" Solve interview challenge: Please list 10 commits
(from the most recent to oldest)
of the repository “rails” by the user “rails”
"""


import sys
import requests
if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    res = requests.get("https://api.github.com/repos/{}/{}/commits"
                       .format(owner, repo))
    r = res.json()
    for i in r[0:10]:
        print("{}: {}".format(i.get("sha"), i.get("commit").get("author")
              .get("name")))
