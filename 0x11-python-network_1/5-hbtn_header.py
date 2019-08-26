#!/usr/bin/python3
"""sends a request to the URL and displays the value of X-Request-Id"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('x-request-id'))
