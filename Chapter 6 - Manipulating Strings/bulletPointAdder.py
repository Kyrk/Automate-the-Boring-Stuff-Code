#!/usr/bin/env python3
# bulletPointAdder.py - Adds Wikipedia bullet points at the start of each line
# of text on the clipboard.
import pyperclip
text = pyperclip.paste() # Store text from clipboard as one string.

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): # Loop through all indexes in "lines" list
    lines[i] = '* ' + lines[i] # Add star to each string in "lines" list

text = '\n'.join(lines) # Merge list into single string

pyperclip.copy(text) # Add modified text to clipboard
