#!/usr/bin/env python3
"""
Example Magic 8 ball program using a list to store possible messages.
"""
import random

messages = [
        'It is certain',
        'It is decidedly so',
        'Reply hazy try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook not so good',
        'Very doubtful',
        'Suck my dong',
        ]

print(messages[random.randint(0,len(messages)-1)])
