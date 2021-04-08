#!/usr/bin/env python3
"""Example Tic-Tac-Toe program."""

# Print TTT board
def printBoard(board):
    print(
        " | " + board[0] + " | " + board[1] + " | " + board[2] + " |\n",
        "| " + board[3] + " | " + board[4] + " | " + board[5] + " |\n",
        "| " + board[6] + " | " + board[7] + " | " + board[8] + " |\n")

# Check if a valid play was made
def isValid(board, move, player):
    if move >= 0 and move <= 8 and board[move] == " ":
        return True
    else:
        print("INVALID MOVE")
        return False

# Checks if game-ending move is made and declares game results
def gameOver(board, player):
    if (board[0] == board[1] and board[1] == board[2] and board[0] == player) or \
        (board[3] == board[4] and board[4] == board[5] and board[3] == player) or \
        (board[6] == board[7] and board[7] == board[8] and board[6] == player) or \
        (board[0] == board[3] and board[3] == board[6] and board[0] == player) or \
        (board[1] == board[4] and board[4] == board[7] and board[1] == player) or \
        (board[2] == board[5] and board[5] == board[8] and board[2] == player) or \
        (board[0] == board[4] and board[4] == board[8] and board[0] == player) or \
        (board[6] == board[4] and board[4] == board[2] and board[6] == player):
        print("PLAYER {} WINS".format(player))
        return True
    elif " " not in board:
        print("THE GAME IS A DRAW")
        return True
    else:
        return False

# Self-explanatory
def changePlayers(player):
    if player == "X":
        return "O"
    elif player == "O":
        return "X"

def main():
    board = []
    player = "X"
    game = True

    # Initialize board with empty values
    for i in range(0, 9):
        board.append(" ")

    # Play game
    while game == True:
        print("PLAYER {}'S TURN".format(player))
        printBoard(board)

        # Get input
        move = int(input("ENTER POSITION [1-9]: ")) - 1

        # Make move and check if game is completed if valid
        if isValid(board, move, player):
            print("PLAYER {} MOVES TO POSITION {}\n".format(player, move + 1))
            board[move] = player
            # Check if game is complete, declare result
            if gameOver(board, player):
                printBoard(board)
                print("GAME OVER")
                game = False # End game
            else: # Switch players to continue game otherwise
                player = changePlayers(player)

main()
