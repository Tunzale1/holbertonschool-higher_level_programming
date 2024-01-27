#!/usr/bin/python3
import hidden_4
import sys
if __name__ == "__main__":
    show = dir(hidden_4)
    for i in show:
        if i[0] != "_":
            print("{}".format(i))
