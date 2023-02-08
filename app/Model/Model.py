import copy
from typing import List, Tuple, Any
from random import choices, randrange
from app.Model.Playable2048 import Playable2048


class Model(Playable2048):
    def __init__(self, side_length: int):
        """
        Logic for 2048 game. Implements Playable2048.
        It is manipulated by the Controller class, and it updates the View class.

        At initialization, it creates a new board with two randomly positioned tiles.

        :param side_length: Number of cells on the side of the board.
        """
        self.matrix = [[0] * side_length for i in range(side_length)]
        self.init_matrix()
        self.size = side_length

    def get_new_tile_number(self, pop=(2, 4), w=(0.9, 0.1)) -> int:
        result = choices(population=pop, weights=w, k=1)

        return result[0]

    def get_empty_tile(self):
        x, y = 0, 0
        size = len(self.matrix)
        while True:
            x, y = randrange(size), randrange(size)
            if self.matrix[x][y] == 0:
                break
        return x, y

    def init_matrix(self):
        tile = self.get_empty_tile()
        self.matrix[tile[0]][tile[1]] = self.get_new_tile_number()

        tile = self.get_empty_tile()
        self.matrix[tile[0]][tile[1]] = self.get_new_tile_number()

    def get_matrix(self) -> List[List[int]]:
        return self.matrix

    @staticmethod
    def transpose(mat: List[List[int]]):
        new = []
        for i in range(len(mat[0])):
            new.append([])
            for j in range(len(mat)):
                new[i].append(mat[j][i])
        return new

    @staticmethod
    def compare(mat_1: List[List[int]], mat_2: List[List[int]]) -> bool:
        for i in range(len(mat_1)):
            for j in range(len(mat_1[0])):
                if mat_1[i][j] != mat_2[i][j]:
                    return False
        return True

    def insert_new_tile(self):
        new_tile = self.get_empty_tile()
        self.matrix[new_tile[0]][new_tile[1]] = self.get_new_tile_number()

    def move_up(self):
        self.matrix = self.transpose(self.matrix)
        self.move_left()
        self.matrix = self.transpose(self.matrix)

    def move_left(self):
        prev_matrix = copy.deepcopy(self.matrix)

        for row in self.matrix:
            self.zeros_right(row)
            self.sum_left(row)
            self.zeros_right(row)

        if not self.game_over(prev_matrix):
            pass

    def move_down(self):
        self.matrix = self.transpose(self.matrix)
        self.move_right()
        self.matrix = self.transpose(self.matrix)

    def move_right(self):
        prev_matrix = copy.deepcopy(self.matrix)

        for row in self.matrix:
            self.zeros_left(row)
            self.sum_right(row)
            self.zeros_left(row)

        if not self.game_over(prev_matrix):
            pass

    def zeros_right(self, row: List[int]):
        result = []
        for i in range(self.size):
            j = self.size - 1 - i
            if row[j] == 0:
                result.append(row[j])
            else:
                result.insert(0, row[j])

        for i in range(self.size):
            row[i] = result[i]

    def zeros_left(self, row: List[int]):
        result = []
        for tile in row:
            if tile == 0:
                result.insert(0, tile)
            else:
                result.append(tile)

        for i in range(self.size):
            row[i] = result[i]

    def sum_right(self, row: List[int]):
        for i in range(self.size - 1):
            j = self.size - 1 - i
            if row[j] == row[j - 1]:
                row[j - 1] = 0
                row[j] = row[j] * 2

    def sum_left(self, row: List[int]):
        for i in range(self.size - 1):
            if row[i] == row[i + 1]:
                row[i + 1] = 0
                row[i] = row[i] * 2

    def game_over(self, prev_matrix) -> bool:
        """
        In this implementation, the method is also responsible for inserting
        new tiles when allowed by compare method.

        :param prev_matrix: matrix state before move.

        """
        if self.compare(prev_matrix, self.matrix):
            # if board hasn't changed after move attempt,
            # check for zeroes:
            if not self.has_zeros(self.matrix):
                # check if next move is possible: in any of the 4 directions
                if not self.next_move_possible()[0]:
                    print("GAME OVER")
                    return True
        else:
            self.insert_new_tile()

        return False

    def next_move_possible(self) -> Tuple[bool, List[Any]]:
        """
        Possible example of a 3x3 cell grid. Assume we want to check if the cell at position 1,2
        can be added to adjacent cells:

        2   2   2
        4   2   8
        16  64  2
               ...
        the i,j indexes are:

        0,0 0,1 0,2
        1,0 1,1 1,2
        2,0 2,1 2,2

        the indexes to be checked are (i-1,j-1), (i-1,j), (i-1,j+1)
                                       (i,j-1),    (i,j),  (i,j+1)
                                      (i+1,j-1), (i+1,j), (i+1,j+1)
        For every cell in range it must check the adjacent cells to see if they are equal.
        If any of the neighbouring cells are the same, then a move is possible
        """
        offsets = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        directions = ["up", "left", "right", "down"]
        options = []

        grid_limits = [0, self.size - 1]

        for i in range(self.size):
            for j in range(self.size):
                # for every tile in the grid, check all offsets until an addition
                # can be performed
                for offset, direction in zip(offsets, directions):
                    m, n = offset[0] + i, offset[1] + j
                    if m in grid_limits and n in grid_limits:
                        # if a neighbouring tile has the same number as the tile being
                        # evaluated, a move is possible in that direction.
                        if self.matrix[m][n] == self.matrix[i][j]:

                            if direction not in options:
                                options.append(direction)

                            if options == directions:
                                return True, options
        if len(options) > 0:
            return True, options

        return False, options

    @staticmethod
    def has_zeros(mat: List[List[int]]):
        for _ in mat:
            if 0 in mat:
                return True

        return False
