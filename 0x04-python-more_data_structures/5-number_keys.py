#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    my_list = list(a_dictionary.keys())

    for i in my_list:
        count += 1

    return (count)
