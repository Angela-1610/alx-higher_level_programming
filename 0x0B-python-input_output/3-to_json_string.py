#!/usr/bin/python3
"""Defines a string-to-JSON function."""
import json


def to_json_string(my_obj):
    """function returns JSON representation of object"""
    x = json.dumps(my_obj)
    return x
