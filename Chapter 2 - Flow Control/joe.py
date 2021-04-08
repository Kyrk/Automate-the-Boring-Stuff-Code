#!/usr/bin/env python3
"""Example program that loops until the correct user and password is
inputted."""
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break

print('Access granted.')
