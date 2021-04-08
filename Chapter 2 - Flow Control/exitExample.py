#!/usr/bin/env python3
"""Example program that ends if user types 'exit'."""
import sys

while True:
    print("Type exit to exit.")
    response = input()
    if response == 'exit':
        sys.exit() # Ends program
    print('You typed {}.'.format(response))
