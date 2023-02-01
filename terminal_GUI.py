from functions import *
from boardClass import Board

import msvcrt

BOARD_SIZE = 3

# Creating New board
board = Board(BOARD_SIZE)

print(f'Score: {board.getScore()}')
board.display()
ans = b'R'

#Main Loop (PRESS L TO LEAVE)
while ans.upper() != b'L':
    #Variable to keep track of score (and check if a move is valid)

    # Wait for users input
    ans = msvcrt.getch()

    #Different movement options (4 space directions)
    if ans.upper() == b'A':
        addScore = board.left()
    elif ans.upper() == b'D':
        addScore = board.right()
    elif ans.upper() == b'W':
        addScore = board.up()
    elif ans.upper() == b'S':
        addScore = board.down()
    #Return to previous board
    if ans.upper() == b'E' or ans.upper() == b'Q':
        board.undo()

    #Update board
    print(f'Score: {board.getScore()}')
    board.display()


