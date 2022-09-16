from turtle import Turtle
import random

XRAND_LIMIT = 250
YRAND_LIMIT = 250


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        rand_x = random.randint(- XRAND_LIMIT, XRAND_LIMIT)
        rand_y = random.randint(- YRAND_LIMIT, YRAND_LIMIT)
        self.goto(rand_x, rand_y)

    def refresh(self):
        rand_x = random.randint(- XRAND_LIMIT, XRAND_LIMIT)
        rand_y = random.randint(- YRAND_LIMIT, YRAND_LIMIT)
        self.goto(rand_x, rand_y)
