#!/usr/bin/python3
'''reaching a fever pitch'''


import json


def save_to_json_file(my_obj, filename):
    '''remind me of us'''
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
