from Model import Model
from View import GameGrid


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start(self):
        self.view.setup(self)
        self.view.update_grid_cells()
        self.view.start_main_loop()


game = Controller(Model(4), GameGrid())
game.start()
