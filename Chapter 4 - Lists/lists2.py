#!/usr/bin/env python3
"""More notes/tidbits from chapter"""
# Sequence data
print("EX 1")
name = 'Zophie'
print(name[0])
print(name[-2])
print(name[:4])

print('Zo' in name)
print('z' in name)
print('p' not in name)

for i in name:
    print('*** {} ***'.format(i))

# Tuples
print("\nEX 2")
eggs = ('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))
# eggs[1] = 99 Will fail, tuples cannot be modified

# Convert list and tuple types
print("\nEX 3")
print(type(tuple(['cat', 'dog', 5]))) # list to tuple
print(type(list(('cat', 'dog', 5)))) # tuple to list
print(list('hello'))
print(tuple('hello'))

# List references
print("\nEX 4")
spam = [0, 1, 2, 3, 4, 5]
cheese = spam # Reference is being copied, not the list
cheese[1] = 'Hello!' # This changes the list value
print(spam)
print(cheese) # The cheese variable refers to the same list.

# Memory address
print("\nEX 5")
print(id('Howdy'))

# Copy lists/dictionaries
print("\nEX 6")
import copy
print(id(spam))
cheese = copy.copy(spam)
print(id(cheese)) # Different list with different identity
cheese[1] = 42
print(spam)
print(cheese)
