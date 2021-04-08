#!/usr/bin/env python3
"""Program with function that divides 42 by passed integer argument, gives
exception if 0 is passed."""
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
