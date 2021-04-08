#!/usr/bin/env python3
"""
Program with isValidChessBoard() function that takes a dictionary argument and
returns True or False depending on if the board is valid.

A valid board:
    - Exactly 1 black king and 1 white king
    - At most 16 pieces per player:
        - At most 8 pawns
        - Default:
            - 8 pawns
            - 2 rooks
            - 2 bishops
            - 2 knights
            - 1 queen
            - 1 king
        - If there are more than the default rooks, bishops, knights, or queen,
          the sum of the number of pawns and additional pieces must not exceed
          8
    - Pieces must be on a valid space from '1a' to '8h'
        - First string character must be between 1 and 8
        - Second string character must be between 'a' and 'h'
        - String length must be exactly 2 characters
        - Space cannot contain more than 1 piece
    - Piece names must begin with 'w' or 'b' to represent white or black,
      followed by name of the piece
    - e.g. {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen',
      '3e': 'wking'}
"""

def isValidChessBoard(board):
    """ Function that takes a dictionary argument and returns True or False
    depending on if the board is valid."""
    # list of pieces allowed on the chessboard
    validPieces = ['bking', 'bqueen', 'bknight', 'bbishop', 'brook', 'bpawn',
             'wking', 'wqueen', 'wknight', 'wbishop', 'wrook', 'wpawn']
    pieceCount = {'bking': 0, 'bqueen': 0, 'bknight': 0, 'bbishop': 0, 'brook':
            0, 'bpawn': 0, 'wking': 0, 'wqueen': 0, 'wknight': 0, 'wbishop': 0,
            'wrook': 0, 'wpawn': 0}
    spaceCount = {} # Counter for spaces on board
    bPawnCount = 0 # To store pawns + promoted pawns
    wPawnCount = 0

    # Get frequency of chess pieces from dictionary
    for piece in board.values():
        # Return False if invalid piece name
        if piece not in pieceCount:
            print(piece + " is not a valid piece")
            return False
        pieceCount[piece] += 1
    #print(pieceCount)

    # Check validity/frequency of board spaces
    for space in board.keys():
        # Return False for invalid board values
        if len(space) > 2 or int(space[0]) < 1 or int(space[0]) > 8 or space[1] > 'h':
            print(space + " is not a valid board space")
            return False
        # Return False for duplicate board spaces
        # TODO: Get program to recognize duplicate keys of board spaces, may
        # try to create reverse dictionary to convert keys into values
        spaceCount.setdefault(space, 0)
        if spaceCount[space] + 1 > 1:
            print(space + " contains more than 1 value")
            return False
        spaceCount[space] += 1
    #print(spaceCount)

    # Add pawns to total pawn count
    bPawnCount += pieceCount['bpawn']
    wPawnCount += pieceCount['wpawn']

    # Add promoted pawns to total pawn count
    for piece, value in pieceCount.items():
        # Extra knights, bishops, and brooks
        if (piece == 'bknight' or piece == 'bbishop' or piece == 'bbrook') \
                and value > 2:
            bPawnCount += value - 2
        if (piece == 'wknight' or piece == 'wbishop' or piece == 'wbrook') \
                and value > 2:
            wPawnCount += value - 2
        # Extra queens
        if piece == 'bqueen' and value > 1:
            bPawnCount += value - 1
        if piece == 'wqueen' and value > 1:
            wPawnCount += value - 1

    # Return False if sum of pawns and promoted pawns exceed 8 pieces
    if bPawnCount > 8 or wPawnCount > 8:
        print("Invalid pawn count")
        return False

    # Return False if there is not exactly 1 king on both sides
    if pieceCount['bking'] != 1 or pieceCount['wking'] != 1:
        print("Invalid king pieces")
        return False

    print("Board is valid")
    return True
    # pieceCount = countPieces(board)

isValidChessBoard({'1h': 'bking', '7h': 'wqueen', '2g': 'wking'})
isValidChessBoard({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
    '5h': 'bqueen', '3e': 'wking'})
isValidChessBoard({'1h': 'bking', '2g': 'wqueen'})
isValidChessBoard({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
    '5h': 'bqueen', '3e': 'wking', '4f': 'bking'})
isValidChessBoard({'1j': 'bking', '6c': 'wqueen', '2g': 'bbishop',
    '5h': 'bqueen', '3e': 'wking'})
isValidChessBoard({'1hh': 'bking', '6c': 'wqueen', '2g': 'bbishop',
    '5h': 'bqueen', '3e': 'wking'})
isValidChessBoard({'0h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
    '5h': 'bqueen', '3e': 'wking'})
isValidChessBoard({'9h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
    '5h': 'bqueen', '3e': 'wking'})
isValidChessBoard({'1h': 'bking', '6c': 'dqueen', '2g': 'bbishop',
    '5h': 'bqueen', '3e': 'wking'})
isValidChessBoard({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
    '5h': 'bqueen', '3e': 'wking', '1a': 'bpawn', '2a': 'bpawn', '3a': 'bpawn',
    '4a': 'bpawn', '5a': 'bpawn', '6a': 'bpawn', '7a': 'bpawn', '8a': 'bpawn',
    '2b': 'bpawn'})
isValidChessBoard({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
    '5h': 'bqueen', '3e': 'wking', '1a': 'bpawn', '2a': 'bpawn', '3a': 'bpawn',
    '4a': 'bpawn', '5a': 'bpawn', '6a': 'bpawn', '7a': 'bpawn', '8a': 'bpawn',
    '2b': 'bqueen'})
isValidChessBoard({'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
    '5h': 'bqueen', '3e': 'wking', '1a': 'bpawn', '2a': 'bpawn', '3a': 'bpawn',
    '4a': 'bpawn', '5a': 'bpawn', '6a': 'bpawn', '7a': 'bpawn', '8a':
    'bqueen'})
