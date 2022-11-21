STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.shape('turtle')
        self.left(90)
        self.penup()
        self.goto_start()

    def goto_start(self):
        self.goto(STARTING_POSITION)

    def move_turtle(self):
        self.forward(MOVE_DISTANCE)

    def finish_line(self):
        self.goto_start()
