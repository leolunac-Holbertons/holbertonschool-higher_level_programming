#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if type(my_list) is list:
        copy = my_list.copy()
    else:
        return
    if idx < 0:
        return copy
    if idx >= len(my_list):
        return copy
    copy[idx] = element
    return copy
