#!/usr/bin/env python3
# Program that autonomously simulates the game Zombie Dice using different bots
# that perform with different algorithms and compare the results of wins/ties.
import zombiedice
import random

class MyZombie:
    def __init__(self, name):
        # All zombies must have a name:
        self.name = name
    def turn(self, gameState):
        # gameState is a dict with info about the current state of the game.
        # You can choose to ignore it in code.
        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains, 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the exact roll
        # result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        # 'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        #           ('green', 'shotgun')]}
        # REPLACE THIS ZOMBIE CODE WITH YOURS:
        brains = 0
        shotguns = 0
        maxRolls = random.randrange(1, 5)
        numRolls = 0

        # Different bot pattern depending on name of class instance
        while diceRollResults is not None:
            # Stops rolling after bot rolls two brains
            if self.name == 'Two Brains Bot':
                brains += diceRollResults['brains']
                if brains < 2:
                    diceRollResults = zombiedice.roll() # roll again
                else:
                    break
            # Stops rolling after bot rolls two shotguns
            elif self.name == 'Two Shotguns Bot':
                shotguns += diceRollResults['shotgun']
                if shotguns < 2:
                    diceRollResults = zombiedice.roll() # roll again
                else:
                    break
            # Randomly decides if bot will continue or stop
            elif self.name == 'Random Bot':
                if random.randrange(1) == 1:
                    diceRollResults = zombiedice.roll() # roll again
                else:
                    break
            # Initially decides if bot will roll dice one to four times, but will
            # stop early if it rolls two shotguns
            elif self.name == 'Indecisive Bot':
                if numRolls <= maxRolls:
                    numRolls += 1
                    shotguns += diceRollResults['shotgun']
                    if shotguns < 2:
                        diceRollResults = zombiedice.roll() # roll again
                    else:
                        break
                else:
                    break
            # Stops rolling after bot rolls more shotguns than brains
            # TODO: Figure out if never winning a game is intentional or not
            elif self.name == 'More Shotguns Bot':
                brains += diceRollResults['brains']
                shotguns += diceRollResults['shotgun']
                if shotguns <= brains:
                    diceRollResults = zombiedice.roll() # roll again
                else:
                    break

zombies = (
        # Example bots.
        #zombiedice.examples.RandomCoinFlipZombie(name='Random'),
        #zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
        #zombiedice.examples.MinNumShotgunsThenStopsZombie(name=
        #    'Stop at 2 Shotguns', minShotguns=2),
        #zombiedice.examples.MinNumShotgunsThenStopsZombie(name=
        #    'Stop at 1 Shotgun', minShotguns=1),
        #MyZombie(name='My Zombie Bot'),
        # Add any other zombie players here.
        MyZombie(name='Two Brains Bot'),
        MyZombie(name='Two Shotguns Bot'),
        MyZombie(name='Random Bot'),
        MyZombie(name='Indecisive Bot'),
        MyZombie(name='More Shotguns Bot'),
)
# Uncomment one of the following lines to run in CLI or Web GUI mode:
zombiedice.runTournament(zombies=zombies, numGames=10)
#zombiedice.runWebGui(zombies=zombies, numGames=1000)
