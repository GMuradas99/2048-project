from functions import *
from time import sleep

import copy
import keyboard

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