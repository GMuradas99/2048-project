from abc import ABC, abstractmethod
import tkinter as tk
from typing import Optional


class View(ABC):
    @abstractmethod
    def setup(self, model: object) -> object:
        """
        Binding method of GameGrid UI. Implements view class and connects the initial Model to View.
        The model object must be passed because it allows the UI to access
        the game matrix.

        :param model: Model instance.
        """
        pass

    @abstractmethod
    def init_grid(self, background: Optional[tk.Misc]) -> Optional[tk.Misc]:
        """
        UI initialization method.

        :param background: tkinter grid.
        """
        pass

    @abstractmethod
    def update_grid_cells(self, controller: object) -> object:
        """
        Updates grid after user action.

        The controller object must be passed because it allows the UI to access
        the game Matrix held by the Model.

        :param controller: Controller instance.
        """
        pass

    @abstractmethod
    def start_main_loop(self) -> object:
        pass
