#!/usr/bin/env python3
'''
Example program where the user enters a series of digits that adds up to 10.
This function passes a custom validation function to inputCustom():
    - Accepts a single string argument of what the user entered
    - Raises an exception if the string fails validation
    - Returns None (or has no return statement) if inputCustom() should return
      the string unchanged
    - Returns a non-None value if inputCustom() should return a different
      string from the one the user entered
    - Function passes as first argument to inputCustom()
'''
import pyinputplus as pyip

def addsUpToTen(numbers):
    numbersList = list(numbers) # Convert string to list of numbers
    for i, digit in enumerate(numbersList): # Add up each number in string
        numbersList[i] = int(digit)
    if sum(numbersList) != 10: # Raise exception if string fails validation
        raise Exception('The digits must add up to 10, not %s.' %
                (sum(numbersList)))
    return int(numbers) # Return an int form of numbers

response = pyip.inputCustom(addsUpToTen)    # No parenthesis after
print(response)
