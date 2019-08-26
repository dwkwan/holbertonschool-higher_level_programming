#!/usr/bin/python3
"""This module takes a string and sends a search request to Star Wars API"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get('https://swapi.co/api/people/?search={:}'.format(
        argv[1])).json()
    print("Number of results: {:}".format(r.get('count')))
    for i in range(len(r.get('results'))):
        print(r.get('results')[i].get('name'))
