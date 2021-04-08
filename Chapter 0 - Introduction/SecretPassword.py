#!/usr/bin/env python3

# Open text file with password
passwordFile = open('SecretPasswordFile.txt')
# Store content of text file into variable
secretPassword = passwordFile.read()

# Prompt to enter password
print('Enter your password: ')
typedPassword = input()

# If a dumb password
if typedPassword == '12345':
    print('That password is one that an idiot puts on their luggage.')

# Check if entered password matches
if typedPassword == secretPassword:
    print('Access granted.')
else:
    print('Access denied.')
    