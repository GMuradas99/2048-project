from abc import ABC, abstractmethod
import tkinter as tk
from typing import Optional
import constants as c


class View(ABC):
    @abstractmethod
    def setup(self, controller: object) -> object:
        """

        :param controller:
        """
        pass

    @abstractmethod
    def init_grid(self, background: Optional[tk.Misc]) -> Optional[tk.Misc]:
        """

        :param background:
        """
        pass

    @abstractmethod
    def update_grid_cells(self, controller: object) -> object:
        """

        """
        pass

    @abstractmethod
    def start_main_loop(self) -> object:
        pass


class GameGrid(tk.Frame, View):

    def setup(self, controller: object):
        tk.Frame.__init__(self)

        self.grid()
        self.master.title('2048')

        self.master.frame = tk.Frame(self, bg=c.BACKGROUND_COLOR_GAME, width=c.SIZE, height=c.SIZE)
        self.grid_cells = []
        self.init_grid(self.master.frame)

        self.matrix = controller.model.get_matrix()
        self.history_matrixs = []

    def init_grid(self, background):
        background.grid()

        for i in range(c.GRID_LEN):
            grid_row = []
            for j in range(c.GRID_LEN):
                cell = tk.Frame(
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
                t = tk.Label(
                    master=cell,
                    text="",
                    bg=c.BACKGROUND_COLOR_CELL_EMPTY,
                    justify=tk.CENTER,
                    font=c.FONT,
                    width=5,
                    height=2)
                t.grid()
                grid_row.append(t)
            self.grid_cells.append(grid_row)

    def update_grid_cells(self, controller):
        self.matrix = controller.model.get_matrix()

        for i in range(c.GRID_LEN):
            for j in range(c.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(text="", bg=c.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(
                        text=str(new_number),
                        bg=c.BACKGROUND_COLOR_DICT[new_number],
                        fg=c.CELL_COLOR_DICT[new_number]
                    )
        self.update_idletasks()

    def start_main_loop(self):
        self.mainloop()
