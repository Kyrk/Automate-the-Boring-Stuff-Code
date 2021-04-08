#!/usr/bin/env python3
"""
Program that takes a list value and returns a string with all the items
separated by a comma and a space, with `and` inserted before the last item.

Example:
Passing list [1, 2, 3, 4, 5] will return "1, 2, 3, 4, and 5"
"""

def comma(list):
    newstring = ''
    for index, value in enumerate(list):
        if index == len(list) - 1:
            newstring += 'and '
        newstring += str(value)
        if index < len(list) - 1:
            newstring += ', '
    return newstring

print(comma([1, 2, 3, 4, 5]))
print(comma(['a', 'e', 'i', 'o', 'u']))
print(comma('mario'))
