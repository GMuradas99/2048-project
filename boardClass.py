import sys

sys.path.pop()

from functions import *

# Class to represent the Board object
class Board(object):
    # Constructor
    def __init__(self, boardSize, mode = 'power'):
        self.board = getNewBoard(boardSize)
        self.score = 0
        self.prevBoard = copy.deepcopy(self.board)
        self.prevScore = 0
        self.weightVector = getWeightMap(boardSize,mode)

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
    # Returns one dimensional vector of the row (power of 2)
    def getPowerVector(self):
        return getPV(self.board)
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
    # Returns the position score of the board at the current position
    def positionScore(self):
        return boardPositionScore(self.getLogarithmicVector(), self.weightVector)

    ### Setters ###
    # Sets the board as the input one
    def setBoard(self,newBoard):
        self.board = newBoard

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
    # Performs the move indicated by the String
    def moveString(self, string):
        addition = 0
        if string == 'Right':
            addition = self.right()
        elif string == 'Left':
            addition = self.left()
        elif string == 'Up':
            addition = self.up()
        elif string == 'Down':
            addition = self.down()
        elif string == 'Undo':
            addition = self.undo()
        return addition


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
    # Returns ordered list of tuples with the potential possible positional scores
    def potentialPositionalScores(self):
        result = []
        moves = self.getPossibleMoves()
        for move in moves:
            # Undo not included (YET)
            if move == 'Right':
                temp = copy.deepcopy(self.board)
                boardRight(temp)
                result.append((move,boardPositionScore(getLV(temp),self.weightVector)))
            if move == 'Left':
                temp = copy.deepcopy(self.board)
                boardLeft(temp)
                result.append((move,boardPositionScore(getLV(temp),self.weightVector)))
            if move == 'Up':
                temp = copy.deepcopy(self.board)
                boardUp(temp)
                result.append((move,boardPositionScore(getLV(temp),self.weightVector)))
            if move == 'Down':
                temp = copy.deepcopy(self.board)
                boardDown(temp)
                result.append((move,boardPositionScore(getLV(temp),self.weightVector)))

        return sorted(result, reverse = True, key = lambda x :x[1])