#!/usr/bin/env python3
'''
Program with function that takes a string and does the same thing as the
strip() string method: if no arguments are passed other than the string to
strip, then whitespace characters will be removed from the beginning and end of
the string. Otherwise, characters specified in second argument to function will
be removed from the string.
'''
import re

def stripString(strarg, stripchars = ''):
    # Regex to get string from first non-whitespace character to last
    stripRegex = re.compile(r'\w.*\w')
    stripmo = stripRegex.search(strarg)

    # Remove whitespace if no second argument passed
    if stripchars == '':
        print(stripmo.group())
        return

    # Regex with char(s) to be stripped
    charRegex = re.compile(stripchars)
    # Substitute all instances of char(s) with empty strings
    print(charRegex.sub('', strarg))

# Test cases
stripString('  ayy lmao  ')
stripString('  ayy lmao  ', 'a')
stripString('star, guitar, reservoir, zanzibar', 'ar')
