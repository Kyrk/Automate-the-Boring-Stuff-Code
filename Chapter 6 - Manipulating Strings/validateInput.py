#!/usr/bin/env python3
"""
Example program that repeatedly asks users for their age and a password until
they provide valid input.
"""
while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal(): # Proceeds to next input if input is a decimal
        break
    print('Please enter a number for your age.')

while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum(): # Exits loop if input is letters and/or nums only
        break
    print('Password can only have letters and numbers.')
