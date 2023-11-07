#!/usr/bin/python3
"""
Contains the read_file function
"""

def read_file(filename=""):
    """read file and print it """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
