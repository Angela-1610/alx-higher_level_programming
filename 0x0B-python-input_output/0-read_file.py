#!/usr/bin/python3

def read_file(filename=""):
    """read file and print it """

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
