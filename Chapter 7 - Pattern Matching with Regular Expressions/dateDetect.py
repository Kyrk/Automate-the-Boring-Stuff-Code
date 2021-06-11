#!/usr/bin/env python3
'''Program with regex that can detect dates in the DD/MM/YYYY format.
- Days range from 01-31, months range from 01-12, years range from 1000-2999
- Single digit days/months must have a leading zero
Program will then check for other factors such as the number of days a certain
month has, as well as leap years'''
import re

def validDate(date):
    dateRegex = re.compile(r'''
            (0[1-9]|[1-2]\d|3[0-1])/    # Day 01-09, 10-29, 30-31
            (0[1-9]|1[0-2])/            # Month 01-09, 10-12
            ([1-2]\d{3})                # Year 1000-2999
            ''', re.VERBOSE)
    datemo = dateRegex.search(date)

    # Invalid if no match
    if datemo == None:
        print('{} is not a valid date'.format(date))
        return

    # Store regex groups into integer date variables
    day, month, year = [int(i) for i in datemo.groups()]

    # Determine if leap year
    if year % 4 == 0 and not (year % 100 == 0 and year % 400 > 0):
        leapyear = True
        # print('Leap year!')
    else:
        leapyear = False

    # Invalid if date has 31 days in a month with 30 days
    days30 = [4, 6, 9, 11]
    if month in days30 and day > 30:
        print('{} is not a valid date'.format(date))
        return

    # Invalid if month of February has more than 28 days, 29 if leap year
    if month == 2 and ((day > 28 and leapyear == False) or (day > 29 and
        leapyear == True)):
        print('{} is not a valid date'.format(date))
        return

    print('{} is a valid date.'.format(date))

# Test cases
validDate('1/02/2020')
validDate('01/02/2020')

validDate('00/02/2020')
validDate('15/00/2020')

validDate('11/2/2020')
validDate('11/02/2020')

validDate('29/02/2020')
validDate('29/02/2021')
validDate('31/02/2020')

validDate('09/06/2020')
validDate('31/04/2021')
validDate('31/03/2020')
