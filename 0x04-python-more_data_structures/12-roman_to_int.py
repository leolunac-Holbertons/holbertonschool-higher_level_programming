#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) is False or roman_string is None:
        return 0
    rn_dict = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    s_dict = {
        "IV": -2,
        "IX": -2,
        "XL": -20,
        "XC": -20,
        "CD": -200,
        "CM": -200
    }
    # if (value < valueofnextletter then value is negative
    value = sum(list(rn_dict[x] for x in roman_string))
    for (k, v) in s_dict.items():
        if k in roman_string:
            value += s_dict[k]
    return value
