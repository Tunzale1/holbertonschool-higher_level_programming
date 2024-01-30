#!/usr/bin/python3
def uniq_add(my_list=[]):
    seen = set()
    total = 0
    for i in my_list:
        if i not in seen:
            total += int(i)
            seen.add(i)
    return(total)
