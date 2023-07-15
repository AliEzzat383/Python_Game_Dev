from turtle import Turtle
INIT_POS = (0, -270)
STEP = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(INIT_POS)

    def move(self):
        self.forward(STEP)

    def stop(self):
        self.goto(self.xcor(), self.ycor())

    def origin_reset(self):
        self.goto(INIT_POS)
