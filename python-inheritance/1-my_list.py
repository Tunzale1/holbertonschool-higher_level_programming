#!/usr/bin/python3
'''valuable message'''


class MyList(list):
    '''my pretty list'''
    def print_sorted(self):
        sorted_copy = sorted(self)
        print(sorted_copy)
