from time import sleep
from boardClass import Board

WAITTIME = 0.5

board = Board(4)
board.display()

moves = board.potentialPositionalScores()

while len(moves) != 0:
    board.moveString(moves[0][0])
    board.display()
    moves = board.potentialPositionalScores()
    print(board.potentialPositionalScores())
    sleep(WAITTIME)

print("GAME OVER")
