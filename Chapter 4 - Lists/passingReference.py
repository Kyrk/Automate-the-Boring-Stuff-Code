#!/usr/bin/env python3
"""Example program that modifies list without return value due to modifying
the value of the list in place/memory."""
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)
