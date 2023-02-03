from random import randrange,choices

import copy

##### DISPLAY FUNCTIONS ####

# Prints without newline
def printf(s):
    print(s,end="")

#Colors the numbers
def colored(fg_color, bg_color, text):
    r = fg_color
    result = f'\033[38;2;{r};{r};{r}m{text}'
    r = bg_color
    result = f'\033[48;2;{r};{r};{r}m{result}\033[0m'
    return result

# Displays the board, input -1 into the score if it shoud be hidden
def displayBoard(board, score):
    if score != -1:
        print("\033[38;2;200;200;0mScore:\033[0m",score)
    printf("_")
    for _ in range(len(board)):
        printf("______")
    print("_")
    for id, row in enumerate(board):
        printf("|")
        for tile in row:
            number = colored(255,0,str(pow(2,tile)))

            if tile == 0:
                printf("  \033[38;2;75;75;0m"+str(tile)+"\033[0m  ")
            elif len(str(pow(2,tile))) == 1:
                printf("  "+number+"  ")
            elif len(str(pow(2,tile))) == 2:
                printf(" "+number+"  ")
            elif len(str(pow(2,tile))) == 3:
                printf(" "+number+" ")
            elif len(str(pow(2,tile))) == 4:
                printf(number+" ")
            elif len(str(pow(2,tile))) == 5:
                printf(number)
            printf(" ")
        printf("|")
        if id != len(board)-1: 
            printf("\n|")
            for _ in range(len(board)):
                printf("      ")
            print("|")
        else: print("")
    printf("‾")
    for _ in range(len(board)):
        printf("‾‾‾‾‾‾")
    print("‾")

#### GETTERS ####

# Returns the maximum tile on the board
def getMaxTile(board):
    maxes = []
    for row in board:
        maxes.append(max(row))
    
    return max(maxes)

# Returns coordinates for an empty tile
def getEmptyTile(board):
    x = 0
    y = 0
    while True:
        x = randrange(len(board))
        y = randrange(len(board))
        if board[x][y] == 0:
            break

    return x,y

# Returns a number for a new tile with the set probability
def getNewTileNumber(pop = [1,2], w = [0.9,0.1]):
    result = choices(population=pop, weights=w, k=1)

    return result[0]

# Creates a new board with two randomly positioned tiles
def getNewBoard(boardSize):
    r = [[0] * boardSize for i in range(boardSize)]
    tile1 = getEmptyTile(r)
    r[tile1[0]][tile1[1]] = getNewTileNumber()
    tile2 = getEmptyTile(r)
    r[tile2[0]][tile2[1]] = getNewTileNumber()

    return r

# Returns the potential score gain of moving a row
def getPotentialGain(row):
    result = 0
    pointer = row[0]
    for i in range(1, len(row)):
        if pointer == 0:
            pointer = row[i]
        elif pointer == row[i]:
            result += pow(2,pointer)*2
            pointer = 0
        elif pointer != row[i] and row[i] != 0: 
            pointer = row[i] 

    return result

# Returns the potential score gain of moving a board sideways
def getPotentialGainSideways(board):
    result = 0
    for row in board:
        result += getPotentialGain(row)
    
    return result

# Returns the potential score gain of moving a board vertically
def getPotentialGainVertically(board):
    transposedBoard = list(map(list, zip(*board)))
    return getPotentialGainSideways(transposedBoard)

# Returns one dimensional vector of the board with the logarithms in base 2 of the tiles
def getLV(board):
    flatList = [item for sublist in board for item in sublist]
    # for i in range(len(flatList)):
    #     if flatList[i] != 0:
    #         flatList[i] = int(math.log(flatList[i],2))
    return flatList

# Returns one dimensional vector of the row (power of 2)
def getPV(board):
    flatList = [item for sublist in board for item in sublist]
    for i in range(len(flatList)):
        if flatList[i] != 0:
            flatList[i] = pow(2,flatList[i])
    return flatList

#Returns weight map for specified board size modes => ['power', 'logarithm']
def getWeightMap(size, mode):
    if mode not in ['power','logarithm']:
        print('Error:',mode,'mode not supported.')
    perfectTiles = []
    if mode == 'power':
        for i in range(pow(size,2)):
            perfectTiles.append(pow(2,i+2))
    if mode == 'logarithm':
        for i in range(pow(size,2)):
            perfectTiles.append(i+2)
    # Normalization
    perfectTiles = [float(i)/sum(perfectTiles) for i in perfectTiles]

    firstRow = perfectTiles[:size]
    thirdRow = perfectTiles[size*2:size*3]
    firstRow.reverse()
    thirdRow.reverse()

    adjustedPositions = firstRow + perfectTiles[size:size*2] + thirdRow + perfectTiles[size*3:]

    return adjustedPositions

# Returns a list with the possible moves
def getPossibleMovesOfBoard(board, prevBoard):
    result = []
    
    if possibleRight(board):
        result.append('Right')
    if possibleLeft(board):
        result.append('Left')
    if possibleUp(board):
        result.append('Up')
    if possibleDown(board):
        result.append('Down')
    if not sameBoard(board, prevBoard):
        result.append('Undo')
    
    return result
        
 # Returns ordered list of tuples with the potential possible positional scores
def getPotentialPositionalScores(board, prevBoard, weightVector):
    result = []
    moves = getPossibleMovesOfBoard(board, prevBoard)
    for move in moves:
        # Undo not included (YET)
        if move == 'Right':
            temp = copy.deepcopy(board)
            boardRight(temp)
            result.append([move,boardPositionScore(getLV(temp), weightVector)])
        if move == 'Left':
            temp = copy.deepcopy(board)
            boardLeft(temp)
            result.append([move,boardPositionScore(getLV(temp), weightVector)])
        if move == 'Up':
            temp = copy.deepcopy(board)
            boardUp(temp)
            result.append([move,boardPositionScore(getLV(temp), weightVector)])
        if move == 'Down':
            temp = copy.deepcopy(board)
            boardDown(temp)
            result.append([move,boardPositionScore(getLV(temp), weightVector)])

    return sorted(result, reverse = True, key = lambda x :x[1])

#### CALCULATIONS ####

# Returns the score of the current board position:
def boardPositionScore(boardVector, weightMap):
    result = 0
    for i,tile in enumerate(boardVector):
        result += tile * weightMap[i]

    return result

# Performs search of specified depth to get the best move
def performSearch(depth,board,prevBoard,weightVector, debug = False):
    if depth == 1:
        moves = getPotentialPositionalScores(board,prevBoard,weightVector)
        if len(moves) == 0:
            return []
        s = moves[0]

        if debug:
            print(s[0])

        return s
    else: 
        moves = getPotentialPositionalScores(board,prevBoard,weightVector)
        if len(moves) == 0:
            return []
        for move in moves:
            temp = copy.deepcopy(board)
            moveBoardWithString(temp, move[0])
            tempPrev = copy.deepcopy(board)
            next = performSearch(depth-1, temp, tempPrev, weightVector, debug)
            if len(next) != 0:
                move[1] += next[1]
        s = sorted(moves, reverse = True, key = lambda x :x[1])

        if debug:
            for _ in range(depth):
                print("-",end='')
            print(s[0][0])

        return s[0]

#### MOVEMENT FUNCTIONS ####

# Moves all zeros to the left
def zerosLeft(row):
    result = []
    for tile in row:
        if tile == 0:
            result.insert(0,tile)
        else:
            result.append(tile)

    for i in range(len(row)):
        row[i] = result[i]

# Adds the same tiles to the Right returns the puntuation gained from the sums
def sumRight(row):
    result = 0
    for i in range(len(row)-1):
        j = len(row)-1-i
        if row[j] == row[j-1] and row[j] > 0:
            row[j-1] = 0
            result += pow(2,row[j])*2
            row[j] += 1
    return result

# Moves all zeros to the rigth
def zerosRight(row):
    result = []
    for i in range(len(row)):
        j = len(row)-1-i
        if row[j] == 0:
            result.append(row[j])
        else:
            result.insert(0,row[j])

    for i in range(len(row)):
        row[i] = result[i]

# Adds the same tiles to the Left returns the puntuation gained from the sums
def sumLeft(row):
    result = 0
    for i in range(len(row)-1):
        if row[i] == row[i+1] and row[i] > 0:
            row[i+1] = 0
            result += pow(2,row[i])*2
            row[i] += 1
    return result

# Move row to the right returns the puntuation gained from the move 
def moveRight(row):
    zerosLeft(row)
    r = sumRight(row)
    zerosLeft(row)
    return r

# Move row to the left returns the puntuation gained from the move
def moveLeft(row):
    zerosRight(row)
    r = sumLeft(row)
    zerosRight(row)
    return r

# Moves board to the right and spawn new tile returns the puntuation gained from the move (-1 if the move is not possible)
def boardRight(board):
    result = 0
    prevBoard = copy.deepcopy(board)
    for row in board:
        result += moveRight(row)

    if sameBoard(prevBoard,board):
        return -1
    
    newTile = getEmptyTile(board)

    if sameBoard(prevBoard,board):
        return -1
    else:
        board[newTile[0]][newTile[1]] = getNewTileNumber()
        return result

# Moves board to the left and spawn new tile returns the puntuation gained from the move (-1 if the move is not possible)
def boardLeft(board):
    result = 0
    prevBoard = copy.deepcopy(board)
    for row in board:
        result += moveLeft(row)

    if sameBoard(prevBoard,board):
        return -1

    newTile = getEmptyTile(board)
    
    if sameBoard(prevBoard,board):
        return -1
    else:
        board[newTile[0]][newTile[1]] = getNewTileNumber()
        return result

# Moves board up and spawn new tile returns the puntuation gained from the move (-1 if the move is not possible)
def boardUp(board):
    transposedBoard = list(map(list, zip(*board)))
    r = boardLeft(transposedBoard)
    changedBoard = list(map(list, zip(*transposedBoard)))
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = changedBoard[i][j]
    return r

# Moves board down and spawn new tile returns the puntuation gained from the move (-1 if the move is not possible)
def boardDown(board):
    transposedBoard = list(map(list, zip(*board)))
    r = boardRight(transposedBoard)
    changedBoard = list(map(list, zip(*transposedBoard)))
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = changedBoard[i][j]
    return r

# Moves board in specified direction
def moveBoardWithString(board, string):
    if string == "Right":
        boardRight(board)
    if string == "Left":
        boardLeft(board)
    if string == "Up":
        boardUp(board)
    if string == "Down":
        boardDown(board)

#### CHECKERS #### 

# Returns ture if the boards are the same
def sameBoard(b1,b2):
    for i in range(len(b1)):
        for j in range(len(b1[0])):
            if b1[i][j] != b2[i][j]:
                return False
    return True

# Returns True if the board has no empty tiles
def boardFull(board):
    for _ in board:
        if 0 in board:
            return False
    
    return True

#Returns true if a move to the right is possible
def possibleRight(board):
    nextBoard = copy.deepcopy(board)


    boardRight(nextBoard)

    return not sameBoard(board,nextBoard)

#Returns true if a move to the left is possible
def possibleLeft(board):
    nextBoard = copy.deepcopy(board)
    boardLeft(nextBoard)

    return not sameBoard(board,nextBoard)

#Returns true if a move Up is possible
def possibleUp(board):
    nextBoard = copy.deepcopy(board)
    boardUp(nextBoard)

    return not sameBoard(board,nextBoard)

#Returns true if a move Down is possible
def possibleDown(board):
    nextBoard = copy.deepcopy(board)
    boardDown(nextBoard)

    return not sameBoard(board,nextBoard)