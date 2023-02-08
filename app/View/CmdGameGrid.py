# todo: add cmd line ui option made by @gonzalo
from abc import ABC
from app.View.View import View


class CmdGameGrid(View, ABC):
    def setup(self, model: object) -> object:
        pass

    def init_grid(self, background):
        pass

    def update_grid_cells(self, controller: object) -> object:
        pass

    def start_main_loop(self) -> object:
        pass
