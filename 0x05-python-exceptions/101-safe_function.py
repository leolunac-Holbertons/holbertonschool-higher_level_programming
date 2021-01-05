#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except:
        sys.stderr.write("Exception: {}\n".format(sys.exc_info()[1]))
        return None
