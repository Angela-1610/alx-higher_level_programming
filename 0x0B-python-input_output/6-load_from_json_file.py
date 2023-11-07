#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """function creates an Object from JSON file"""
    with open(filename) as f:
        return json.loads(f)
