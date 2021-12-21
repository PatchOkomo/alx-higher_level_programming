#!/usr/bin/python3
"""
Module 9-add_item
Contains function that adds and saves to Python obj to JSON file; loads objects
#Add all arguments to a Python list and save them to a file.
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    existing_content = load_from_json_file(filename)
except FileNotFoundError:
    existing_content = []
