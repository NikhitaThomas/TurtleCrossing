COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(x=280, y=(random.randint(-200,260)))
        self.left(180)
        

    def move_car(self):
        self.forward(20)

    def destroy_car(self):
        self.reset()

