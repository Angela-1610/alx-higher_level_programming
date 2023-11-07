#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """function append text in file and return char no"""
    with open(filename, 'a', encoding='utf=8') as x:
        y = x.write(text)
        return y
