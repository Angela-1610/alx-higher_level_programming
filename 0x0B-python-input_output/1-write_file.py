#!/usr/bin/python3
"""Defines a file-writing function."""

def write_file(filename="", text=""):
    """write in file and return no of char

    Args:
        filename: file to write in
        text: to write it in file

    Returns:
        no of char written
    """

    with open(filename, 'w', encoding='utf=8') as x:
        y = x.write(text)
        return y
