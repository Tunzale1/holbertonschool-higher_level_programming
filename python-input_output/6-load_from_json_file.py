#!/usr/bin/python3
'''i am just a freak'''


import json


def load_from_json_file(filename):
    '''surf curse'''
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
