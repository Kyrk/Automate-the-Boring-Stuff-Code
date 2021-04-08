#!/usr/bin/env python3
"""Example program that checks if pet name is in list, either from default or
user-inputted values"""
myPets = ['Zophie', 'Pooka', 'Fat-tail']
print('Enter a pet name:')
name = input()
if name not in myPets:
    print('I do not have a pet named ' + name)
else:
    print(name + ' is my pet.')
