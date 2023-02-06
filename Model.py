import copy
from abc import ABC, abstractmethod
from typing import List, Tuple
from random import choices, randrange


class Playable2048(ABC):

    @abstractmethod
    def get_new_matrix(self, side_length: int) -> List[List[int]]:
        """
        Creates a new board with two randomly positioned tiles.
        (?) All boards must be squares and the side dimensions must be a multiple of two (?).

        :param side_length: Number of cells on the side of the board.
        Default value: 4
        :rtype: List[List[int]]
        :return board: A matrix of integers with two non-zero tiles
        """
        pass

    @abstractmethod
    def get_new_tile_number(self, pop: Tuple[int, int], w: Tuple[int, int]) -> int:
        """
        Returns a number for a new tile with the set probability.

        :param pop: Population. Default: 2,4
        :param w: Weights. Default: 0.9,0.1
        :rtype: int
        :return: Tile number
        """
        pass

    @abstractmethod
    def get_empty_tile(self, board: List[List[int]]) -> Tuple[int, int]:
        """

        :param board:
        """
        pass

    @abstractmethod
    def move_up(self):
        pass

    @abstractmethod
    def move_left(self):
        pass

    @abstractmethod
    def move_down(self):
        pass

    @abstractmethod
    def move_right(self):
        pass


class Model(Playable2048):
    def __init__(self, side_length: int):
        """
        Logic for 2048 game. Implements Playable2048.
        It is manipulated by the Controller class, and it updates the View class.

        At initialization, it creates a new board with two randomly positioned tiles.

        :param side_length: Number of cells on the side of the board.
        """
        self.matrix = self.get_new_matrix(side_length)
        self.size = side_length

    def get_new_tile_number(self, pop=(2, 4), w=(0.9, 0.1)) -> int:
        result = choices(population=pop, weights=w, k=1)

        return result[0]

    def get_empty_tile(self, matrix):
        x, y = 0, 0
        size = len(matrix)
        while True:
            x, y = randrange(size), randrange(size)
            if matrix[x][y] == 0:
                break
        return x, y

    def get_new_matrix(self, length) -> List[List[int]]:
        m = [[0] * length for i in range(length)]

        tile = self.get_empty_tile(m)
        m[tile[0]][tile[1]] = self.get_new_tile_number()

        tile = self.get_empty_tile(m)
        m[tile[0]][tile[1]] = self.get_new_tile_number()

        return m

    def get_matrix(self) -> List[List[int]]:
        return self.matrix

    @staticmethod
    def transpose(mat):
        new = []
        for i in range(len(mat[0])):
            new.append([])
            for j in range(len(mat)):
                new[i].append(mat[j][i])
        return new

    def move_up(self):
        self.matrix = self.transpose(self.matrix)
        self.move_left()
        self.matrix = self.transpose(self.matrix)

    def move_left(self):
        for row in self.matrix:
            self.zeros_right(row)
            self.sum_left(row)
            self.zeros_right(row)

        self.get_empty_tile(self.matrix)

    def move_down(self):
        pass

    def move_right(self):

        for row in self.matrix:
            self.zeros_left(row)
            self.sum_right(row)
            self.zeros_left(row)

        self.get_empty_tile(self.matrix)

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

    def zeros_up(self, row: List[int]):
        pass

    def zeros_down(self, row: List[int]):
        pass

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

    def sum_up(self, row: List[int]):
        pass

    def sum_down(self, row: List[int]):
        pass
