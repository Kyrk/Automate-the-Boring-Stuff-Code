#!/usr/bin/env python3
"""Example program printing list of cat names based on how many names are
inputted by user."""
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
    ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation

print('The cat names are:')
for name in catNames:
    print(' ' + name)
