from functions import *
from time import sleep

import copy
import keyboard

# Returns the maximum tile on the board
def getMaxTile(board):
    maxes = []
    for row in board:
        maxes.append(max(row))
    
    return max(maxes)

# Displays the board
def displayBoard(board):
    for row in board:
        for tile in row:

            number = "\033[38;2;255;255;255m"+str(tile)+"\033[0m"

            if tile == 0:
                printf("  \033[38;2;75;75;0m"+str(tile)+"\033[0m  ")
            elif len(str(tile)) == 1:
                printf("  "+number+"  ")
            elif len(str(tile)) == 2:
                printf(" "+number+"  ")
            elif len(str(tile)) == 3:
                printf(" "+number+" ")
            elif len(str(tile)) == 4:
                printf(number+" ")
            elif len(str(tile)) == 5:
                printf(number)
            printf(" ")
        print("\n")

BOARD_SIZE = 4

board = getNewBoard(BOARD_SIZE)

displayBoard(board)
prevBoard = copy.deepcopy(board)
ans = ""

while ans != "q":
    ans = input("Direction: ")
    if ans == "a":
        prevBoard = copy.deepcopy(board)
        boardLeft(board)
    if ans == "d":
        prevBoard = copy.deepcopy(board)
        boardRight(board)
    if ans == "w":
        prevBoard = copy.deepcopy(board)
        boardUp(board)
    if ans == "s":
        prevBoard = copy.deepcopy(board)
        boardDown(board)
    if ans == "e":
        board = copy.deepcopy(prevBoard)
    
    displayBoard(board)


