#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if type(my_list) is not list:
        return
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list[:idx] + my_list[idx + 1:]
    my_list.clear()
    for i in new_list:
        my_list.append(i)
    return my_list
