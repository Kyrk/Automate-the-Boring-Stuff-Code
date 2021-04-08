#!/usr/bin/env python3
# Guess the number game that gives a player 6 tries
# to guess a random number between 1 and 20
import random

secretNumber = random.randint(1,20)
print("I am thinking of a number between 1 and 20.")
# Ask player to guess up to 6 times.
for guessesTaken in range(1, 7):
    print("Take a guess.")
    guess = int(input()) # Get input for number
    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break   # This condition is correct guess

if guess == secretNumber:
    print("Good job! You guessed my number in " + str(guessesTaken)
    + " guesses!")
else:
    print("Nope. The number I was thinking of was" + str(secretNumber))