#!/usr/bin/env python3
'''Program with function that uses regular expressions to make sure the
password string passed as a parameter is strong.
A 'strong' password contains the following:
    - At least 8 characters long
    - Contains both uppercase and lowercase characters
    - Contains at least one digit
'''
import re

def pwStrength(pw):
    # Regexs
    lenRegex = re.compile(r'\w{8,}')
    upperRegex = re.compile(r'[a-z]')
    lowerRegex = re.compile(r'[A-Z]')
    numRegex = re.compile(r'\d')
    strength = 0

    # Check password length
    if lenRegex.search(pw) == None:
        print('Password should be at least 8 characters long.')
    else:
        strength += 1

    # Check for both uppercase and lowercase characters
    if upperRegex.search(pw) == None or lowerRegex.search(pw) == None:
        print('Password should contain both uppercase and lowercase',
                'characters.')
    else:
        strength += 1

    # Check for at least one digit
    if numRegex.search(pw) == None:
        print('Password should contain at least one digit.')
    else:
        strength += 1

    # Print strength results
    if strength == 0:
        print('Your password sucks.')
    elif strength == 1:
        print('Your password is weak.')
    elif strength == 2:
        print('Your password is okay.')
    elif strength == 3:
        print('Your password is strong.')

    print()

# Test cases
pwStrength('witch')     # 0
pwStrength('witch1')    # 1
pwStrength('Witch')     # 1
pwStrength('witchbby')  # 1
pwStrength('witch123')  # 2
pwStrength('Witch1')    # 2
pwStrength('Witchbby')  # 2
pwStrength('Witch123')  # 3
pwStrength('Witch1234')  # 3
