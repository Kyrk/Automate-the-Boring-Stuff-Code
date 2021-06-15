#!/usr/bin/env python3
'''
Program that asks users for their sandwich preferences:
    - Bread type
    - Protein type
    - Option to add cheese
    - Cheese type if 'yes' to previous preference
    - Option to add mayo, mustard, lettuce, or tomato
    - Number of sandwiches (minimum of 1 sandwich)
Program will have prices for each option and display total cost after user
enters their selection.
'''
import pyinputplus as pyip

cost = 0

# Select type of sandwich bread
response = pyip.inputMenu(['Wheat', 'White', 'Sourdough'],
        prompt='Select a type of sandwich bread:\n')

# Add selected bread to cost
if response == 'wheat' or response == 'white':
    cost += 0.50
else:
    cost += 0.75

# Select type of protein
response = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'],
        prompt='Select a protein:\n')

# Add selected protein to cost
if response == 'chicken' or response == 'ham':
    cost += 2.00
elif response == 'turkey':
    cost += 2.50
else:
    cost -= 1.00

# Ask for cheese
response = pyip.inputYesNo('Do you want cheese?\n')

# Select type of cheese if user selects 'yes'
if response == 'yes':
    response = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'],
            prompt='Select a type of cheese:\n')

    # Add selected cheese to cost
    if response == 'cheddar':
        cost += 0.25
    elif response == 'Swiss':
        cost += 0.75
    else:
        cost += 0.50

# Ask for condiments and add to cost if user selects 'yes'
response = pyip.inputYesNo('Do you want mayo?\n')

if response == 'yes':
    cost += 0.25

response = pyip.inputYesNo('Do you want mustard?\n')

if response == 'yes':
    cost += 0.25

response = pyip.inputYesNo('Do you want lettuce?\n')

if response == 'yes':
    cost += 0.25

response = pyip.inputYesNo('Do you want tomato?\n')

if response == 'yes':
    cost += 0.25

response = pyip.inputInt('Enter number of sandwiches: ', min=1)
cost *= response

print('Your total is ${:.2f}.'.format(cost))
