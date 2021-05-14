#!/usr/bin/env python3
"""
Example program that makes a case-insensitive comparison.
Slightly modified to serve as a function.
"""

def convertlowercase(feeling):
    # Use lower method to compare string fully lowercased
    if feeling.lower() == 'great':
        print('I feel great too.')
    else:
        print('I hope the rest of your day is good.')

print('How are you?')
feeling = input()

convertlowercase(feeling)

# Non-input test cases
convertlowercase('great')
convertlowercase('GREAT')
convertlowercase('''Why are we still here? Just to suffer? Every night, I can
feel my leg... and my arm... even my fingers. The body I've lost... won't stop
hurting... It's like they're still all there. You feel it, too, don't you?''')
convertlowercase('GrEat')
