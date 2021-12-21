#!/usr/bin/python3
"""
Module 9-add_item
Contains function that adds and saves to Python obj to JSON file; loads objects
#Add all arguments to a Python list and save them to a file.
"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('8-load_from_json_file').load_from_json_file

    try:
        content = load_from_json_file("add_item.json")
    except FileNotFoundError:
        content = []
    content.extend(sys.argv[1:])
    save_to_json_file(content, "add_item.json")
