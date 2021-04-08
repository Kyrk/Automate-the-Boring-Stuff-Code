#!/usr/bin/env python3
# Prints 'Hello' if 1 is stored in spam, 'Howdy' if 2,
# and 'Greetings!' if anything else
spam = input()

if spam == '1':
    print('Hello')
elif spam == '2':
    print('Howdy')
else:
    print('Greetings!')