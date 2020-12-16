#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if type(my_list) is list:
        new_list = [True]*len(my_list)
        for i in range(len(my_list)):
            if my_list[i] % 2 is 1:
                new_list[i] = False
        return new_list
