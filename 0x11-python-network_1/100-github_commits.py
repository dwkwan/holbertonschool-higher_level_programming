#!/usr/bin/python3
"""takes your Github credentials (username and password) and uses the Github
API to display your id
"""
import requests
from sys import argv

owner = argv[1]
repository_name = argv[2]

if __name__ == "__main__":
    r = requests.get(
        'https://api.github.com/repos/{:}/{:}/commits?per_page=10'.format(
            owner, repository_name)).json()
    for item in range(len(r)):
        print("{:}: {:}".format(r[item].get('sha'), r[item].get('commit').get(
            'committer').get('name')))
