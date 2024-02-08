#!/usr/bin/python3
'''salam elykim'''


def inherits_from(obj, a_class):
    '''inherited (directly or indirectly) from the specified class'''
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
