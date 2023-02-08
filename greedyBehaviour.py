from time import sleep
from boardClass import Board
from functions import *
from tqdm import tqdm
bar = tqdm()

# VARIABLES TO TEST
WAITTIME = 0.0
DEPTH = 4

board = Board(4)

move = performSearch(DEPTH, board.getBoard(), board.getBoard(), board.getWeightVector())
while len(move) != 0:
    board.moveString(move[0])
    # board.display()
    move = performSearch(DEPTH, board.getBoard(), board.getBoard(), board.getWeightVector())
    # print(move)

    # Display
    bar.update(1)  
    bar.set_description_str(desc=f'Max {pow(2,board.getMaximumTile())}')

    sleep(WAITTIME)

board.display()
print("GAME OVER")
