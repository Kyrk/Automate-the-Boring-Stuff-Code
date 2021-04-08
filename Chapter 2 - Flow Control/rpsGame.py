#!/usr/bin/env python3
# Game of rock, paper, scissors
import random, sys

print("ROCK, PAPER, SCISSORS")
# Variables to keep track of score
wins = 0
losses = 0
ties = 0

# Main game loop
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties)) # Print score

    # Player input loop:
    while True:
        # Get input
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        playerMove = input()
        # Quit program if 'q'
        if playerMove == 'q':
            sys.exit() # Quit the program
        # Exit loop if valid input is placed
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break # Break out of player loop
        print('Type one of r, p, s, or q.') # If user did not enter valid input

    # Display what player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    # Display what computer chose
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Display and record win/loss/tie
    if playerMove == computerMove: # Tie
        print('It is a tie!')
        ties += 1
    # Win conditions
    elif (playerMove == 'r' and computerMove == 's') \
        or (playerMove == 'p' and computerMove == 'r') \
        or (playerMove == 's' and computerMove == 'p'):
        print('You win!')
        wins += 1
    # Lose conditions
    elif (playerMove == 'r' and computerMove == 'p') \
        or (playerMove == 'p' and computerMove == 's') \
        or (playerMove == 's' and computerMove == 'r'):
        print('You lose!')
        losses += 1
