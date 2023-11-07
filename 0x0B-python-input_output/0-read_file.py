#!/usr/bin/python3

def read_file(filename=""):
    """function read file and print it"""
    with open(filename, 'r', encoding="utf-8") as f:
        x = f.read()
        print(x)
