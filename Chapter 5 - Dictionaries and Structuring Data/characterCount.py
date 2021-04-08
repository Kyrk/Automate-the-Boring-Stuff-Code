#!/usr/bin/env python3
"""Example program that prints the character frequency of a string."""
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)
