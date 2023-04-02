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
    header = {
        "Accept": "application/vnd.github+json",
        # "Authorization": "Bearer <YOUR-TOKEN>",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    res = requests.get('https://api.github.com/repos/{owner}/{repo}/commits',
                       headers=header)
    r = res.json()
    print("{}: {}".format(r.get("sha"), r.get("commit").get("author")
          .get("name")))
