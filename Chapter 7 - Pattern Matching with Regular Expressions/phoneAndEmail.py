#!/usr/bin/env python3
# Example project that extracts all phone numbers and email addresses from the
# current contents in the clipboard.
import pyperclip, re

#TODO: Make variations that finds website URLs that begin with http:// or
# https://
# Clean up dates in different date formats by replacing with a single standard
# format.
# Remove sensitive information like SSN or CCNs
# Find common typos (e.g. multiple spaces, accidentally repeated words,
# multiple exclamation marks)

# Create phone number regex.
phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?      # Optional area code
        (\s|-|\.)?              # Optional separator
        (\d{3})                 # First 3 digits
        (\s|-|\.)               # Separator
        (\d{4})                 # Last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?  # Optional extension
        )''', re.VERBOSE)

# Create email regex
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+       # Username
    @                       # @ symbol
    [a-zA-Z0-9.-]+          # Domain name
    (\.[a-zA-Z]{2,4})       # Dot-something
    )''', re.VERBOSE)

# Find all matches from both regexes
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
