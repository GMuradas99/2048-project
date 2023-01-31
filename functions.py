from random import randrange,choices

import copy


# Prints without newline
def printf(s):
    print(s,end="")

# Returns the maximum tile on the board
def getMaxTile(board):
    maxes = []
    for row in board:
        maxes.append(max(row))
    
    return max(maxes)

#Colors the numbers
def colored(fg_color, bg_color, text):
    r = fg_color
    result = f'\033[38;2;{r};{r};{r}m{text}'
    r = bg_color
    result = f'\033[48;2;{r};{r};{r}m{result}\033[0m'
    return result

# Displays the board
def displayBoard(board):
    print("__________________________")
    for id, row in enumerate(board):
        printf("|")
        for tile in row:
            number = colored(0,255,str(tile))

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
        printf("|")
        if id != len(board)-1: print("\n|                        |")
        else: print("")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

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

# Returns True if the board has no empty tiles
def isFull(board):
    for row in board:
        if 0 in board:
            return False
    
    return True

# Returns a number for a new tile with the set probability
def getNewTileNumber(pop = [2,4], w = [0.9,0.1]):
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

# Adds the same tiles to the Right
def sumRight(row):
    for i in range(len(row)-1):
        j = 3-i
        if row[j] == row[j-1]:
            row[j-1] = 0
            row[j] = row[j]*2

# Moves all zeros to the rigth
def zerosRight(row):
    result = []
    for i in range(len(row)):
        j = 3-i
        if row[j] == 0:
            result.append(row[j])
        else:
            result.insert(0,row[j])

    for i in range(len(row)):
        row[i] = result[i]

# Adds the same tiles to the Left
def sumLeft(row):
    for i in range(len(row)-1):
        if row[i] == row[i+1]:
            row[i+1] = 0
            row[i] = row[i]*2

# Move row to the right
def moveRight(row):
    zerosLeft(row)
    sumRight(row)
    zerosLeft(row)

# Move row to the left
def moveLeft(row):
    zerosRight(row)
    sumLeft(row)
    zerosRight(row)

# Moves board to the right
def boardRight(board):
    prevBoard = copy.deepcopy(board)
    for row in board:
        moveRight(row)
    newTile = getEmptyTile(board)

    if sameBoard(prevBoard,board):
        return False
    else:
        board[newTile[0]][newTile[1]] = getNewTileNumber()
        return True

# Moves board to the left
def boardLeft(board):
    prevBoard = copy.deepcopy(board)
    for row in board:
        moveLeft(row)
    newTile = getEmptyTile(board)
    
    if sameBoard(prevBoard,board):
        return False
    else:
        board[newTile[0]][newTile[1]] = getNewTileNumber()
        return True

# Moves board up
def boardUp(board):
    transposedBoard = list(map(list, zip(*board)))
    boardLeft(transposedBoard)
    changedBoard = list(map(list, zip(*transposedBoard)))
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = changedBoard[i][j]

# Moves board down
def boardDown(board):
    transposedBoard = list(map(list, zip(*board)))
    boardRight(transposedBoard)
    changedBoard = list(map(list, zip(*transposedBoard)))
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = changedBoard[i][j]


# Returns ture if the boards are the same
def sameBoard(b1,b2):
    for i in range(len(b1)):
        for j in range(len(b1[0])):
            if b1[i][j] != b2[i][j]:
                return False
    return True