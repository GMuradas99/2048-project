from functions import *
from time import sleep

import keyboard

BOARD_SIZE = 4

board = getNewBoard(BOARD_SIZE)

displayBoard(board)
print()
boardUp(board)
displayBoard(board)

ans = ""

while ans != "q":
    ans = input("Direction: ")
    if ans == "a":
        boardLeft(board)
    if ans == "d":
        boardRight(board)
    if ans == "w":
        boardUp(board)
    if ans == "s":
        boardDown(board)
    
    displayBoard(board)