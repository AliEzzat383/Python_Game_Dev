from turtle import Turtle
import time

ORIGIN = (0, 0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(ORIGIN)
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed = 10
        self.dx = self.speed
        self.dy = self.speed

        # self.speed("fastest")

    def move(self, direction=""):
        """type x for dx or y for dy , default is dx & dy"""
        if direction == "x":
            self.goto(self.xcor() + self.dx, self.ycor())
        elif direction == "y":
            self.goto(self.xcor(), self.ycor() + self.dy)
        else:
            self.goto(self.xcor() + self.dx, self.ycor() + self.dy)
        time.sleep(0.05)

    def bounce(self, direction=''):
        """type x for dx or y for dy , default is dx & dy"""
        if direction == 'x':
            self.dx *= -1
            self.move()
        elif direction == 'y':
            self.dy *= -1
            self.move()
        else:
            self.dx *= -1
            self.dy *= -1
            self.move()