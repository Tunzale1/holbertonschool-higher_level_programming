#!/usr/bin/python3
'''ordekler gedir yol ile'''

def append_write(filename="", text=""):
    '''cibi dolu pul ile'''
    with open(filename, "a", encoding="utf-8") as f:
        heri = f.write(text)
        return heri
