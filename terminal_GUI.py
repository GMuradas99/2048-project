from functions import *
from boardClass import Board

# DELETE
from test import performSearch

import msvcrt

BOARD_SIZE = 4

# Creating New board
board = Board(BOARD_SIZE)

board.display()
ans = b'R'
#Main Loop (PRESS L TO LEAVE)
while ans.upper() != b'L':

    # Wait for users input
    ans = msvcrt.getch()

    #Different movement options (4 space directions)
    if ans.upper() == b'A':
        board.left()
    elif ans.upper() == b'D':
        board.right()
    elif ans.upper() == b'W':
        board.up()
    elif ans.upper() == b'S':
        board.down()
    #Return to previous boardd
    if ans.upper() == b'E' or ans.upper() == b'Q':
        board.undo()

    #Update board
    board.display()
    print("Best Move",performSearch(5, board.getBoard(), board.getBoard(), board.getWeightVector()))