#!/usr/bin/env python3
"""
More notes/tidbits of code
"""
# isX() Methods
print('EX 1')
print('hello'.isalpha())    # True if only letters and not blank
print('hello123'.isalpha())

print('hello123'.isalnum()) # True if only letters and/or numbers
print('hello'.isalnum())

print('123'.isdecimal())    # True if only numbers

print('  '.isspace())       # True if spaces, tabs, and newlines and not blank

# True if only words beginning with uppercase letter followed by lowercase
# letters
print('This Is Title Case'.istitle())
print('This Is Title Case 123'.istitle())
print('This Is not Title Case'.istitle())
print('This Is NOT Title Case Either'.istitle())

# startswith() and endswith() Methods
print('\nEX 2')
# True if start of string matches with method argument
print('Hello, world!'.startswith('Hello'))
# True if end of string matches with method argument
print('Hello, world!'.endswith('world!'))
print('abc123'.startswith('abcdef'))
print('abc123'.endswith('12'))
print('Hello, world!'.startswith('Hello, world!'))
print('Hello, world!'.endswith('Hello, world!'))

# join() and split() Methods
print('\nEX 3')
# Returns string with string called upon in between each element in list
# argument
print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Simon'])) # My name is not actually Simon
print('ABC'.join(['My', 'name', 'is', 'Simon']))
# Splits string into list separated by string called upon
print('MyABCnameABCisABCSimon'.split('ABC'))
print('My name is Simon'.split('m'))
# Splits multiline string along newline characters
spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment."
Please do not drink it.
Sincerely,
Bob'''
print(spam.split('\n'))

# partition() Method
print('\nEX 4')
# Split string into text before and after a separator string
# Searches string for passed separator string and returns a tuple of three
# substrings for 'before', 'separator', and 'after'.
print('Hello, world!'.partition('w'))
print('Hello, world!'.partition('world'))
# Method splits string only in first instance
print('Hello, world!'.partition('o'))
# If separator string isn't found
print('Hello, world!'.partition('XYZ'))
# Uses multiple assignment trick to assign returned strings to three variables
before, sep, after = 'Hello, world'.partition(' ')
print(before)
print(after)

# Justifying text Methods
print('\nEX 5')
# Right-justify string with total string length 10
print('Hello'.rjust(10))
# " " 20
print('Hello'.rjust(20))
# Total string length will be same despite longer initial string
print('Hello, World'.rjust(20))
# Left-justify
print('Hello'.ljust(10))
# Optional second argument to specify a fill character instead of a space
print('Hello'.rjust(20, '*'))
print('Hello'.ljust(20, '-'))
# Center text with total string length 20
print('Hello'.center(20))
print('Hello'.center(20, '='))

# Remove whitespace with strip Methods
print('\nEX 6')
# Remove whitespace from beginning and/or end
spam = '   Hello, World   '
print(spam.strip())
# Remove whitespace from beginning
print(spam.lstrip())
# Remove from end
print(spam.rstrip())

# Numeric values of characters
# ord() function gets Unicode code point of one-character string
print(ord('A'))
print(ord('4'))
print(ord('!'))
# chr() function gets one-character string of an integer code point
print(chr(65))
# Ordering/operations on characters
print(ord('B'))
print(ord('A') < ord('B'))
print(chr(ord('A')))
print(chr(ord('A') + 1))
