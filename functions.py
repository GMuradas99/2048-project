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

# Displays the board
def displayBoard(board):
    printf("_")
    for _ in range(len(board)):
        printf("______")
    print("_")
    for id, row in enumerate(board):
        printf("|")
        for tile in row:
            number = colored(255,0,str(tile))

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
        if row[j] == row[j-1]:
            row[j-1] = 0
            result += row[j]*2
            row[j] = row[j]*2
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
        if row[i] == row[i+1]:
            row[i+1] = 0
            result += row[i]*2
            row[i] = row[i]*2
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