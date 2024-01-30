#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for i in my_list:
        if i % 2 != 0:
            total += int(i)
    return(total)
