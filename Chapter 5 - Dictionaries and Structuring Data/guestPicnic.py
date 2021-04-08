#!/usr/bin/env python3
"""Example program listing total number of items from all guests in dictionary.
Uses .get() method to provide fallback value if key does not contain called
value."""
allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
        'Bob': {'ham sandwiches': 3, 'apples': 2},
        'Carol': {'cups': 3, 'apple pies': 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of things being brought:')
print(' - Apples    ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups      ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes     ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))
