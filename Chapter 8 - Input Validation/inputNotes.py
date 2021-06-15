#!/usr/bin/env python3
# Notes/code snippets
# Module for input validation, abbreviated to pyip
import pyinputplus as pyip

# inputNum() ensures user enters number and return int/float
# inputInt() '' int
# inputFloat() '' float
#response = pyip.inputNum()
#print(response)

# Provide prompt by passing string to 'prompt' keyword as function argument
response = pyip.inputNum(prompt='Enter a number: ')
print(response)

# inputNum()/Int()/Float() keyword arguments
response = pyip.inputNum('Enter num (at least 4): ', min=4)
print(response)
response = pyip.inputNum('Enter num (up to 6): ', max=6)
print(response)
response = pyip.inputNum('Enter num (greater than 4): ', greaterThan=4)
print(response)
print('Enter num (at least 4, but less than 6):')
response = pyip.inputNum('>', min=4, lessThan=6)
print(response)

# Allow blank input with blank keyword
response = pyip.inputNum('Enter num (blank values accepted): ', blank=True)
print(response)

# Stop asking user for input after a number of tries with limit keyword
response = pyip.inputNum('Enter num (2 attempts):', limit=2)
print(response)

# Stop asking user for input after a given amount of time with timeout keyword
response = pyip.inputNum('Enter num (10 seconds to complete): ', timeout=10)
print(response)

# Use default value if user fails limit or timeout with default keyword
response = pyip.inputNum('Enter num (2 attempts): ', limit=2, default='N/A')
print(response)

# Use regexes as keywords to specify whether an input is allowed or not
response = pyip.inputNum('Enter num (Roman nums allowed): ',
        allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'])
print(response)
response = pyip.inputNum('Enter num (Roman nums allowed): ',
        allowRegexes=[r'(i|v|x|l|c|d|m)+', r'zero'])
print(response)

response = pyip.inputNum('Enter num (No even numbers): ',
        blockRegexes=[r'[02468]$'])
print(response)

# Allow and blockRegexes are usable at same time, but allow overrides block
response = pyip.inputStr('Enter string (no cat but caterpillar and category): '
        , allowRegexes=[r'caterpillar', r'category'], blockRegexes=[r'cat'])
print(response)
