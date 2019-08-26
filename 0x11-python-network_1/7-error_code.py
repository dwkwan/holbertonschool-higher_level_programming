#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the body"""
import requests
from sys import argv

if __name__ == "__main__":
        r = requests.get(argv[1])
        if r.status_code < 400:
                print(r.text)
        else:
                print("Error code: {:}".format(r.status_code))
