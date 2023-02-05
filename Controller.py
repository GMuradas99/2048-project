from Model import Model
from View import GameGrid


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
        self.view.setup(self)
        self.view.update_grid_cells()

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

    def move_left(self):
        self.model.move_left()

    def move_down(self):
        self.model.move_down()

    def move_right(self):
        self.model.move_rigth()


game = Controller(Model(4), GameGrid())
game.start()
