from functions import *

import msvcrt
import copy

BOARD_SIZE = 4

# Creating New board
board = getNewBoard(BOARD_SIZE)

displayBoard(board)
prevBoard = copy.deepcopy(board)
ans = b'R'

#Main Loop (PRESS L TO LEAVE)
while ans.upper() != b'L':
    # Wait for users input
    ans = msvcrt.getch()

    #Different movement options (4 space directions)
    if ans.upper() == b'A':
        prevBoard = copy.deepcopy(board)
        boardLeft(board)
    elif ans.upper() == b'D':
        prevBoard = copy.deepcopy(board)
        boardRight(board)
    elif ans.upper() == b'W':
        prevBoard = copy.deepcopy(board)
        boardUp(board)
    elif ans.upper() == b'S':
        prevBoard = copy.deepcopy(board)
        boardDown(board)
    #Return to previous board
    elif ans.upper() == b'E' or ans.upper() == b'Q':
        board = copy.deepcopy(prevBoard)

    #Update board
    displayBoard(board)


