#!/usr/bin/python3
'''inpout'''


def read_file(filename=""):
    '''read'''
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        print(content)
