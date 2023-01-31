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
        pass


class Model(Playable2048):
    def __init__(self, side_length: int):
        """
        Model for 2048 game. Implements Playable2048.
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
        matrix = [[0] * length for i in range(length)]

        tile_1 = self.get_empty_tile(matrix)
        tile_2 = self.get_empty_tile(matrix)

        matrix[tile_1[0]][tile_1[1]] = self.get_new_tile_number()
        matrix[tile_2[0]][tile_2[1]] = self.get_new_tile_number()

        return matrix


model = Model(4)
board = model.matrix

for row in board:
    print(row)