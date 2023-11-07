#!/usr/bin/python3
"""Defines a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """function writes an Object by json form"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
