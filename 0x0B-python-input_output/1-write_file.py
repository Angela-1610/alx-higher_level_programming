#!/usr/bin/python3
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """write in file and return no of char"""
    with open(filename, 'w', encoding='utf=8') as x:
        return x.write(text)
