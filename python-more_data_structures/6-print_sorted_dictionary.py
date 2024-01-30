#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sett = sorted(a_dictionary.keys())
    for i in sett:
        print("{}: {}".format(i, a_dictionary[i]))
