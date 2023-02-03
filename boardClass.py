from functions import *

# Class to represent the Board object
class Board(object):
    # Constructor
    def __init__(self, boardSize):
        self.board = getNewBoard(boardSize)
        self.score = 0
        self.prevBoard = None
        self.prevScore = 0

    #Displayer
    def display(self, displayScore = True):
        if not displayScore:
            displayBoard(self.board, -1)
        if displayScore:
            displayBoard(self.board, self.score)

    ### Getters ###
    # Returns the list of lists
    def getBoard(self):
        return self.board
    # Returns the number for the maximum tile
    def getMaximumTile(self):
        return getMaxTile(self.board)
    # Returns the current score of the Board
    def getScore(self):
        return self.score
    # Returns a one dimensional vector with the logarithm in base 2 of the tiles
    def getLogarithmicVector(self):
        return getLV(self.board)
    # Returns a list with the possible moves
    def getPossibleMoves (self):
        result = []
        if possibleRight(self.board):
            result.append('Right')
        if possibleLeft(self.board):
            result.append('Left')
        if possibleUp(self.board):
            result.append('Up')
        if possibleDown(self.board):
            result.append('Down')
        if not sameBoard(self.board, self.prevBoard):
            result.append('Undo')
        
        return result

    ### Checks ###
    #Returns true if the board is full
    def isFull(self):
        return boardFull(self.board)
    #Returns true if both boards are the same
    def equals(self,board2):
        return sameBoard(self.board, board2)

    ### Moves ###
    # Four directions of space
    def left(self):
        # Saving state
        self.prevScore = self.score
        self.prevBoard = copy.deepcopy(self.board)
        # Performing the move
        addition =  boardLeft(self.board)
        # Valid moves 
        if addition != -1:
            self.score += addition
        return addition
    def right(self):
        # Saving state
        self.prevScore = self.score
        self.prevBoard = copy.deepcopy(self.board)
        # Performing the move
        addition =  boardRight(self.board)
        # Valid moves 
        if addition != -1:
            self.score += addition
        return addition
    def up(self):
        # Saving state
        self.prevScore = self.score
        self.prevBoard = copy.deepcopy(self.board)
        # Performing the move
        addition =  boardUp(self.board)
        # Valid moves 
        if addition != -1:
            self.score += addition
        return addition
    def down(self):
        # Saving state
        self.prevScore = self.score
        self.prevBoard = copy.deepcopy(self.board)
        # Performing the move
        addition =  boardDown(self.board)
        # Valid moves 
        if addition != -1:
            self.score += addition
        return addition
    # Returns to the previous board, returns the difference in score
    def undo(self):
        difference = self.score - self.prevScore
        self.board = copy.deepcopy(self.prevBoard)
        self.score = self.prevScore
        return difference

    ### Reinforcement Learning Functions ###
    # Returns the potential score gain by moving the board sideways
    def potentialGainSideways(self):
        return getPotentialGainSideways(self.board)
    # Returns the potential score gain by moving the board vertically
    def potentialGainVertically(self):
        return getPotentialGainVertically(self.board)
    # Returns the potential score gain by undoing the last move
    def potentialGainUndo(self):
        return self.prevScore - self.score