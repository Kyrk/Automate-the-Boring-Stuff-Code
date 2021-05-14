#!/usr/bin/env python3
"""
Notes/tidbits of code
"""
# Escape characters:
# \'    Single quote
# \"    Double quote
# \t    Tab
# \n    Newline/line break
# \\    Backslash
print("EX 1")
print("Hello there!\nHow are you?\nI\'m doing fine.")

# Raw strings ignore escape characters
print("\nEX 2")
print(r'That is Carol\'s cat.')

# Multiline strings with triple quotes
print("\nEX 3")
print('''Dear Alice,
        Eve's cat has been arrested for catnapping, cat burglary, and extortion
        Sincerely,
        Bob''')
# Equivalent string
print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat \
burglary, and extortion.\n\nSincerely,\nBob')

"""Multiline comments.
Self-explanatory."""

# Indexing/slicing strings
print("\nEX 4")
spam = 'Hello, world!'
print(spam[0])
print(spam[4])
print(spam[-1])
print(spam[0:5])
print(spam[:5])
print(spam[7:])

fizz = spam[0:5]
print(fizz)

# in and not in operators
print("\nEX 5")
print('Hello' in 'Hello, World')        # True
print('Hello' in 'Hello')               # True
print('HELLO' in 'Hello, World')        # False
print('' in 'spam')                     # True
print('cats' not in 'cats and dogs')    # False

# Strings inside other strings
print("\nEX 6")
name = 'Al'
age = 4000
print('Hello, my name is ' + name + '. I am ' + str(age) + ' years old.')
# % operator
print('My name is %s. I am %s years old.' % (name, age))
# .format
print('My name is {}. I am {} years old'.format(name, str(age)))
# f-string (prefix string with 'f')
print(f'My name is {name}. Next year I will be {age + 1}.')

# Common string methods
print('\nEX 7')
print(spam.islower())               # False
print(spam.isupper())               # False
print('HELLO'.isupper())            # True
print('abc12345'.islower())         # True
print('12345'.islower())            # False
print('12345'.isupper())            # False
print('Hello'.upper())
print('Hello'.upper().lower())
print('Hello'.upper().lower().upper()) # Why would you do this
print('HELLO'.lower())
print('HELLO'.lower().islower())    # True
