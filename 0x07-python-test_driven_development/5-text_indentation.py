#!/usr/bin/python3
"""
This module provides an indentation function to be tested using
docstring testing.
"""


def text_indentation(text):
    """
    Function to print two new lines after . ? and : characters, and
    takes out spaces at beginning or end of lines

    Args:
        text: string to change
    """
    if isinstance(text, str):
        new_string = ""
        flag = False

        for i in text:
            if flag is False:
                spaces = 0
                if i == ' ' or i == '\t':
                    continue
            flag = True

            if i == '.' or i == '?' or i == ':':
                new_string += (' ' * spaces) + i + "\n" + "\n"
                flag = False
                continue

            if i == '\n':
                flag = False
            if i != ' ' and i != '\t':
                new_string += (' ' * spaces) + i
                spaces = 0
            else:
                spaces += 1

        print(new_string, end='')

    else:
        raise TypeError('text must be a string')
