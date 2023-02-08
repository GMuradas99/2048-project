from abc import ABC, abstractmethod
from typing import Tuple, List


class Playable2048(ABC):

    @abstractmethod
    def init_matrix(self):
        """
        Creates a new board with two randomly positioned tiles.
        (?) All boards must be squares and the side dimensions must be a multiple of two (?).

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
    def get_empty_tile(self) -> Tuple[int, int]:
        """
        Searches the matrix and returns
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

    @abstractmethod
    def game_over(self, prev_mat: List[List[int]]) -> bool:
        """
        If all tiles are non-empty and no movements are possible, it returns true.
        Otherwise false.

        :rtype: bool
        """
        pass