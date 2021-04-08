#!/usr/bin/wnv python3
"""Example program using user input to be annoying."""
name = ''
while name.lower() != 'your name':
    print('Please type your name.')
    name = input()

while True:
    print('Please type your name.')
    name = input()
    if name.lower() == 'cody':
        break

print('Thank you!')
