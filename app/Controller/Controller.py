from app.Model.Model import Model
from app.View.GameGrid import GameGrid


class Controller:
    def __init__(self, model: object, view: object):
        """
        Controller for 2048 game.
        It manipulates the model according to the keys pressed and updates the view.

        :param model: game logic
        :param view: game UI
        """
        self.model = model
        self.view = view

    def start(self):
        self.view.setup(self.model)
        self.view.update_grid_cells(self.model)

        self.view.master.bind('<KeyPress>', self.key_pressed)

        self.view.start_main_loop()

    def key_pressed(self, event):
        if event.char == "r":
            self.reset()

        elif event.char == "w":
            self.move_up()

        elif event.char == "a":
            self.move_left()

        elif event.char == "s":
            self.move_down()

        elif event.char == "d":
            self.move_right()

    def reset(self):
        self.view.destroy()
        self.model = Model(self.model.size)
        self.start()

    def move_up(self):
        self.model.move_up()
        # todo: maybe this update call should happen from Model instance
        self.view.update_grid_cells(self.model)

    def move_left(self):
        self.model.move_left()
        # todo: maybe this update call should happen from Model instance
        self.view.update_grid_cells(self.model)

    def move_down(self):
        self.model.move_down()
        # todo: maybe this update call should happen from Model instance
        self.view.update_grid_cells(self.model)

    def move_right(self):
        self.model.move_right()
        # todo: maybe this update call should happen from Model instance
        self.view.update_grid_cells(self.model)

