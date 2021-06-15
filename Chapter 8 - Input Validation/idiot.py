#!/usr/bin/env python3
# Example program that uses PyInputPlus to ask the user if they'd like to know
# how to keep an idiot busy for hours. If the user answers 'no', quit. If the
# user answers 'yes', go to the previous step.
import pyinputplus as pyip

# Infinite loop that runs until 'no' is entered to encounter break statement
while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt) # Will only accept 'yes' or 'no'
    if response == 'no':
        break

print('Thank you. Have a nice day.')
