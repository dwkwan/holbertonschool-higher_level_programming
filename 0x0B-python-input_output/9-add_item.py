#!/usr/bin/python3
"""This module creates a script that adds args to Python list and saves them"""

from os import path
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if path.exists("add_item.json") is False:
    save_to_json_file([], "add_item.json")
my_list = load_from_json_file("add_item.json")
for i in range(1, len(argv)):
    my_list.append(argv[i])
save_to_json_file(my_list, "add_item.json")
