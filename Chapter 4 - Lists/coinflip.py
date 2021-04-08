#!/usr/bin/env python3
"""
Program that calculates how often a streak of 6 heads or 6 tails comes up
in a randomly generated list of coin flips.

Generates a list of 100 randomly selected 'heads' and 'tails' values.
Checks if there's a streak of 6 heads or tails in this list.
Repeats this experiment 10000 times to calculate the percentage of coin flips
containing a streak.
"""
import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values
    flips = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            flips.append('heads')
        else:
            flips.append('tails')

    # Code that checks if there's a streak of 6 heads or tails in a row
    streak = 0
    lastFlip = '' # Used to compare current coin flip with previous flip
    for flip in flips:
        if flip == lastFlip:
            streak += 1
        else:
            streak = 1 # Reset streak if broken
        if streak == 6: # Add to main streak counter and break loop if 6 streak
            numberOfStreaks += 1
            break
        lastFlip = flip

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
