#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = ()
    for i in range(2):
        a = b = 0
        if len(tuple_a) > i:
            a = tuple_a[i]
        if len(tuple_b) > i:
            b = tuple_b[i]
        tuple_c = tuple_c + (a + b,)
    return (tuple_c)
