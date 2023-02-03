from time import sleep
from boardClass import Board
from functions import *

# VARIABLES TO TEST
WAITTIME = 0.0
DEPTH = 5

board = Board(4)
board.display()

move = performSearch(DEPTH, board.getBoard(), board.getBoard(), board.getWeightVector())

while len(move) != 0:
    board.moveString(move[0])
    board.display()
    move = performSearch(DEPTH, board.getBoard(), board.getBoard(), board.getWeightVector())
    print(move)
    sleep(WAITTIME)

print("GAME OVER")
