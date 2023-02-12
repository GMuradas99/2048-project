from app.Controller.Controller import Controller
from app.Model.Model import Model
from app.View.GameGrid import GameGrid


def main():
    game = Controller(Model(4), GameGrid())
    game.start()


if __name__ == '__main__':
    main()
