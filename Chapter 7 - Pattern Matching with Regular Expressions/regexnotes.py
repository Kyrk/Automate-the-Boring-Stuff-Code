#!/usr/bin/env python3
# Notes/code bits for regexes
import re   # Used for all regex functions

# Create regex object with re.compile(r'expression')
# \d - any digit character
print('EXAMPLE 1')
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Matching regex objects with re.search('string')
# mo - generic name for Match object
mo = phoneNumRegex.search('My number is 415-555-4242')
# Return string of matched text with .group()
print('Phone number found: ' + mo.group())

# Grouping with Parenthesis
print('\nEXAMPLE 2')
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242')
# Call groups with .group(#)
print(mo.group(1))
print(mo.group(2))
print(mo.group(0)) # Return entire matched text like .group()

print(mo.groups()) # Returns tuple of all groups
areaCode, mainNumber = mo.groups() # Multiple assignments to groups
print(areaCode) # mo.group(1)
print(mainNumber) # mo.group(2)

# Use \ to ignore special characters like parenthesis
print('\nEXAMPLE 3')
phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print(mo.group(1))
print(mo.group(2))
# Special characters:
# . ^ $ * + ? { } [ ] \ | ( )

# Use | pipe to match one of multiple expressions
print('\nEXAMPLE 4')
heroRegex = re.compile(r'Batman|Tina Fey') # Match either Batman or Tina Fey
# If both expressions match, first occurrence of match will be returned as mo
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

# Use pipes and parenthesis to match multiple patterns with same prefix
print('\nEXAMPLE 5')
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

# Use '?' to optionally match
print('\nEXAMPLE 6')
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
# Looking for phone numbers that do or do not have an area code
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

# Use '*' to match zero or more instances of a match
print('\nEXAMPLE 7')
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowowoman')
print(mo3.group())

# Use '+' to match one or more instances of a match
print('\nEXAMPLE 8')
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batman') # No match
print(mo3 == None)

# Match repititions of instances using braces {}
print('\nEXAMPLE 9')
haRegex = re.compile(r'(Ha){3}') # Match 3 instances of 'Ha'
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha') # No match
print(mo2 == None)
haRegex = re.compile(r'(Ha){3,5}') # Match 3-5 instances of 'Ha'
mo3 = haRegex.search('HaHaHaHa')
print(mo3.group())
haRegex = re.compile(r'(Ha){,3}') # Match 0-3 instances of 'Ha'
mo4 = haRegex.search('Batman') # Match is True, even with no instances
print(mo4.group())

# Greedy vs Non-Greedy Matching
print('\nEXAMPLE 10')
greedyHaRegex = re.compile(r'(Ha){3,5}')
# Regexs are greedy by default, matching the longest string possible
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
# Non-Greedy/lazy matches shortest string possible using '?' after {}
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

# Return strings of every match using findall() method
print('\nEXAMPLE 11')
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group()) # First instance of matching text
# List of instances of matching text
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))
# List of instances of matching text in groups listed as tuples
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
print(phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000'))

# Shorthand Character Classes:
# \d - Digit 0-9
# \D - Any character not a digit 0-9
# \w - Any letter, number, or underscore
# \W - Any character not a letter, digit, or underscore
# \s - Space, tab, or newline
# \S - Not a space, tab, or newline

print('\nEXAMPLE 12')
# Regex containing any-sized number, a space/tab/newline, and any-sized
# combination of letters/digits/underscores
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids,'
    ' swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge'))

# Create own character classes using square brackets []
print('\nEXAMPLE 13')
vowelRegex = re.compile(r'[aeiouAEIOU]') # Returns all vowels
print(vowelRegex.findall('Robocop eats baby food. BABY FOOD.'))
# Caret ^ after [ matches characters not in character class
consonantRegex = re.compile(r'[^aeiouAEIOU]') # Returns all consonants
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))

# Get matches at beginning or end of string with caret ^ or dollar sign $
print('\nEXAMPLE 14')
# Caret ^ means match must occur at beginning of searched text
beginsWithHello = re.compile(r'^Hello') # Starts with 'Hello'
print(beginsWithHello.search('Hello, world!'))
print(beginsWithHello.search('He said hello.') == False) # Returns True
# Dollar sign $ means match must occur at end of searched text
endsWithNumber = re.compile(r'\d$') # Ends with a decimal
print(endsWithNumber.search('Your number is 42'))
print(endsWithNumber.search('Your number is forty two.')) # Returns True
wholeStringIsNum = re.compile(r'^\d+$') # Starts and ends with 1+ decimals
print(wholeStringIsNum.search('1234567890'))
print(wholeStringIsNum.search('12345xyz67890') == False) # Returns True
print(wholeStringIsNum.search('12 34567890') == False) # Returns True

# Match everything but newlines with the wildcard character '.'
print('\nEXAMPLE 15')
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat at the'
    'frathouse'))

# Match everything with dot-star .*
print('\nEXAMPLE 16')
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))
print(mo.group(2))
# Dot-star is a greedy algorithm
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
# Add question mark .*? to stop matching text at the first instance of its end
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())

# Make case-insensitive regex with re.compile('regex', re.I)
print('\nEXAMPLE 17')
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search('Al, why does your programming book talk about robocop so'
    'much?').group())

# Substitute strings with sub() method
print('\nEXAMPLE 18')
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice have the secret documents to '
    'Agent Bob'))
# Substitute groups
agentNamesRegex = re.compile(r'Agent (\w)\w*')
# Replace agent names with first letter of name followed by ****
print(agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent'
    ' Eve knew Agent Bob was a double agent.'))

# Make complex regexes easier to read with re.VERBOSE to ignore whitespace and
# comments.
print('\nEXAMPLE 20')
phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?  # Area code
        (\s|-|\.)?          # Separator
        \d{3}               # First 3 digits
        (\s|-|\.)           # Separator
        \d{4}               # Last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?    # Extension
        )''',re.VERBOSE)

# Use multiple function arguments using pipe character |
print('\nEXAMPLE 21')
# Regex that's both case-insensitive and includes newlines matching '.' character
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
