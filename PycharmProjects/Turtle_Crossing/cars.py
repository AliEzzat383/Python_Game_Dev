import random
from turtle import Turtle


# Control Constants
WIDTH = 600
HEIGHT = 600
OFFSET = 60  # based on player loc of -270 in case of editing,edit player as well

TOP = int((HEIGHT / 2) - OFFSET)
BOTTOM = - TOP
RIGHT = TOP
LEFT = BOTTOM


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.origin = (RIGHT, random.randrange(BOTTOM, TOP, 40))
        self.color((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.step = random.randint(10, 50)

    def moving(self):
        if self.xcor() <= LEFT:
            self.goto(self.origin)
        else:
            self.goto(self.xcor() - self.step, self.ycor())

    def update_origin(self):
        self.origin = (RIGHT, random.randrange(BOTTOM, TOP, 40))
        self.goto(self.origin)
