#!/usr/bin/env python3
# Example multi-clipboard project that stores multiple phrases to paste
import sys
import pyperclip

# Dictionary that associates piece of text with a key phrase
TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?""",
        'shebang': """#!/usr/bin/env python3"""}

# Takes 2 command line arguments: file name (mclip.py) and a dictionary phrase
if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

# Checks if keyphrase matches with dictionary key and copies text if true
keyphrase = sys.argv[1] # First command line arg is the keyphrase
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard.')
else:
    print('There is no text for ' + keyphrase)

# To run in Win-R Run:
# Create mclip.bat file in C:\Windows folder:
# @py.exe C:\path_to_file\mclip.py %*
# @pause
# Press Win-R and type mclip key phrase
