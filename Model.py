from abc import ABC, abstractmethod
from typing import List, Tuple
from random import choices, randrange
from tkinter import Frame, Label, CENTER
import constants as c


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
        m = [[0] * length for i in range(length)]

        tile_1 = self.get_empty_tile(m)
        tile_2 = self.get_empty_tile(m)

        m[tile_1[0]][tile_1[1]] = self.get_new_tile_number()
        m[tile_2[0]][tile_2[1]] = self.get_new_tile_number()

        return m

    def get_matrix(self) -> List[List[int]]:
        return self.matrix


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start(self):
        self.view.setup(self)
        self.view.start_main_loop()


# class TkView(View):
#     def setup(self, controller):
#         # setup tkinter
#         self.root = tk.Tk()
#         self.root.geometry("400x400")
#         self.root.title("UUIDGen")
#
#         # create the gui
#         self.frame = tk.Frame(self.root)
#         self.frame.pack(fill=tk.BOTH, expand=1)
#         self.label = tk.Label(self.frame, text="Result:")
#         self.label.pack()
#         self.list = tk.Listbox(self.frame)
#         self.list.pack(fill=tk.BOTH, expand=1)
#         self.generate_uuid_button = tk.Button(self.frame, text="Generate UUID",
#                                               command=controller.handle_click_generate_uuid)
#         self.generate_uuid_button.pack()
#         self.clear_button = tk.Button(self.frame, text="Clear list", command=controller.handle_click_clear_list)
#         self.clear_button.pack()
#
#     def start_main_loop(self):
#         # start the loop
#         self.root.mainloop()

class GameGrid(Frame):
    def __init__(self, m):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')

        self.commands = {
        }

        self.grid_cells = []
        self.init_grid()
        self.matrix = m
        self.history_matrixs = []
        self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=c.BACKGROUND_COLOR_GAME,width=c.SIZE, height=c.SIZE)
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = Frame(
                    background,
                    bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                    width=c.SIZE / c.GRID_LEN,
                    height=c.SIZE / c.GRID_LEN
                )
                cell.grid(
                    row=i,
                    column=j,
                    padx=c.GRID_PADDING,
                    pady=c.GRID_PADDING
                )
                t = Label(
                    master=cell,
                    text="",
                    bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                    justify=CENTER,
                    font=c.FONT,
                    width=5,
                    height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    def update_grid_cells(self):
        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="",bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(
                        text=str(new_number),
                        bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number]
                    )
        self.update_idletasks()


# class GameGrid(Frame):
#     def __init__(self, matrix):
#         Frame.__init__(self)
#         self.grid()
#         self.master.title('2048')
#
#         self.grid_cells = []
#         self.matrix = matrix
#         self.init_grid()
#         self.update_grid_cells()
#
#         self.mainloop()
#
#     def init_grid(self):
#         background = Frame(self, bg="white", width=500, height=500)
#         background.grid()
#
#         for i in range(len(self.matrix)):
#             grid_row = []
#             for j in range(len(self.matrix[0])):
#                 cell = Frame(
#                     background,
#                     bg="grey",
#                     width=500 / len(self.matrix),
#                     height=500 / len(self.matrix)
#                 )
#                 cell.grid(
#                     row=i,
#                     column=j,
#                     padx=5,
#                     pady=5
#                 )
#                 t = Label(
#                     master=cell,
#                     text="",
#                     bg="grey",
#                     justify=CENTER,
#                     font=("Verdana", 40, "bold"),
#                     width=5,
#                     height=2
#                 )
#                 t.grid()
#                 grid_row.append(t)
#             self.grid_cells.append(grid_row)
#
#     def update_grid_cells(self):
#         for i in range(len(self.matrix)):
#             for j in range(len(self.matrix[0])):
#                 number = self.matrix[i][j]
#                 if number == 0:
#                     self.grid_cells[i][j].configure(text="", bg="grey")
#                 else:
#                     self.grid_cells[i][j].configure(
#                         text=str(number),
#                         bg="red" if number % 2 == 0 else "blue",
#                         fg="white"
#                     )
#         self.update_idletasks()


# create the MVC & start the application
# c = Controller(Model(4), TkView())
# c.start()

game2048 = Model(8)
matrix = game2048.get_matrix()
GameGrid(matrix)

