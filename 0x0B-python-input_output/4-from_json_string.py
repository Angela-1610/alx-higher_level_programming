#!/usr/bin/python3
import json

def from_json_string(my_str):
    """function return data structure represented by JSON"""

    x = json.loads(my_str)
    return x
