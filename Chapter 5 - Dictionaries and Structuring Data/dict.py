#!/usr/bin/env python3
"""Notes/tidbits from chapter"""
# Dictionaries are unordered
print("EX 1")
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon) # False, lists are ordered

eggs = {'name':'Zophie', 'species':'cat', 'age':'8'}
ham = {'species':'cat', 'age':'8', 'name':'Zophie'}
print(eggs == ham) # True

# Dictionary values
print("\nEX 2")
spam = {'color':'red', 'age':42}
for v in spam.values():
    print(v)

# Dictionary keys
print("\nEX 3")
for k in spam.keys():
    print(k)

print(spam.keys())
print(list(spam.keys()))

# Dictionary items: keys + values
print("\nEX 4")
for i in spam.items():
    print(i)

for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))

# Check if keys or values exist in dictionary
print('\nEX 5')
print('color' in spam.keys())
print('red' in spam.values())
print('name' in spam.keys())
print('name' not in spam.keys())
print('color' in spam)

# get() to check value and return fallback value
print('\nEX 6')
picnicItems = {'apples':5, 'cups':2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

# Set default values
print('\nEX 7')
spam = {'name':'Pooka', 'age': 5}
spam.setdefault('color', 'black') # Value added since dict had no 'color' value
print(spam)
spam.setdefault('color', 'white') # Value same since dict now has 'color' value
print(spam)
