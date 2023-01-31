from functions import *
import msvcrt

import copy

BOARD_SIZE = 4

board = getNewBoard(BOARD_SIZE)

displayBoard(board)
prevBoard = copy.deepcopy(board)
ans = b'R'

while ans.upper() != b'L':
    ans = msvcrt.getch()

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
    elif ans.upper() == b'E' or ans.upper() == b'Q':
        board = copy.deepcopy(prevBoard)

    displayBoard(board)


