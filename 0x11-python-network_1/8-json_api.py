#!/usr/bin/python3
"""takes in a letter, sends a POST request to
http://0.0.0.0:5000/search_user
"""
import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        json_dict = r.json()
        if len(json_dict.keys()) > 0:
            print("[{:}] {:}".format(json_dict.get('id'), json_dict.get(
                'name')))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
