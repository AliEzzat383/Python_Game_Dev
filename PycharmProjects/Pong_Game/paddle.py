from turtle import Turtle

PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_STEP = 40
PADDLE_CEILING = 225
PADDLE_FLOOR = -PADDLE_CEILING


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.goto(location)
        self.shape("square")
        self.shapesize(stretch_wid=(PADDLE_HEIGHT / 20), stretch_len=(PADDLE_WIDTH / 20))
        self.color("white")
        self.penup()

    def up(self):
        if self.ycor() < PADDLE_CEILING:
            self.sety(self.ycor() + PADDLE_STEP)

    def down(self):
        if self.ycor() > PADDLE_FLOOR:
            self.sety(self.ycor() - PADDLE_STEP)

    def stop(self):
        self.sety(self.ycor())
