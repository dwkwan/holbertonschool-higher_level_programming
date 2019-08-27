#!/usr/bin/python3
"""This module takes a string and sends a search request to Star Wars API"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get('https://swapi.co/api/people/?search={:}'.format(
        argv[1])).json()
    print("Number of results: {:}".format(r.get('count')))
    try:
        while r:
            for i in range(len(r.get('results'))):
                print(r.get('results')[i].get('name'))
                films = r.get('results')[i].get('films')
                for film in range(len(films)):
                    x = requests.get(films[film]).json()
                    print("\t{:}".format(x.get('title')))
            r = requests.get(r.get('next')).json()
    except:
        pass
