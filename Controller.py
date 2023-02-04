from time import sleep

from Model import Model
from View import GameGrid


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def start(self):
        self.view.setup(self)
        self.view.update_grid_cells()

        self.view.master.bind('<KeyPress>', self.key_pressed)

        self.view.start_main_loop()

    def key_pressed(self, event):
        if event.char == "r":
            self.reset()

    def reset(self):
        self.view.destroy()
        self.model = Model(4)  # todo: avoid hardcoded length
        self.start()


game = Controller(Model(4), GameGrid())
game.start()
