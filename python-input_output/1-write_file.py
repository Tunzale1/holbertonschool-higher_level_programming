#!/usr/bin/python3
'''delve into python'''


def write_file(filename="", text=""):
    '''maraqli hekayet'''
    with open(filename, "w", encoding="utf-8") as f:
        count = f.write(text)
        return count
