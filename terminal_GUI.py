from functions import *

import msvcrt
import copy

BOARD_SIZE = 4

# Creating New board
board = getNewBoard(BOARD_SIZE)

prevScore = 0
score = 0
print(f'Score: {score}')
displayBoard(board)
prevBoard = copy.deepcopy(board)
ans = b'R'

#Main Loop (PRESS L TO LEAVE)
while ans.upper() != b'L':
    #Variable to keep track of score (and check if a move is valid)
    addScore = 0

    # Wait for users input
    ans = msvcrt.getch()

    #Direction has been chosen (Store previous postion)
    if ans.upper() == b'A' or ans.upper() == b'D' or ans.upper() == b'S':
        prevScore = score
        prevBoard = copy.deepcopy(board)

    #Different movement options (4 space directions)
    if ans.upper() == b'A':
        addScore = boardLeft(board)
    elif ans.upper() == b'D':
        addScore = boardRight(board)
    elif ans.upper() == b'W':
        addScore = boardUp(board)
    elif ans.upper() == b'S':
        addScore = boardDown(board)
    # Move was valid
    if addScore != -1:
        score += addScore
    #Move was not valid
    else:
        score = score # (Do something here if u want)
    #Return to previous board
    if ans.upper() == b'E' or ans.upper() == b'Q':
        board = copy.deepcopy(prevBoard)
        score = prevScore

    #Update board
    print(f'Score: {score}')
    displayBoard(board)


