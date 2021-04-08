#!/usr/bin/env python3
"""Example program of a magic 8 ball with a function that returns an answer via
switch statement depending on the random value passed to it."""
import random

# Function that returns fortune depending on number passed
def getAnswer(answerNumber):
    # Dictionary as a "switch statement"
    return {
        1: 'It is certain',
        2: 'It is decidedly so',
        3: 'Yes',
        4: 'Reply hazy try again',
        5: 'Ask again later',
        6: 'Concentrate and ask again',
        7: 'My reply is no',
        8: 'Outlook not so good',
        9: 'Very doubtful',
    }[answerNumber]

# # Get random number 1-9
# r = random.randint(1, 9)
# # Call function passing randomized number
# fortune = getAnswer(r)
# print(fortune)

# Call function
print(getAnswer(random.randint(1, 9)))
