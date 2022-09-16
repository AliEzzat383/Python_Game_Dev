import turtle
from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()


def move_forwards():
    tim.fd(10)


def move_backwards():
    tim.bk(10)


def cw():
    tim.rt(10)


def ccw():
    tim.lt(10)


def key_motion():
    my_screen.listen()
    my_screen.onkey(key="Up", fun=move_forwards)
    my_screen.onkey(key="Down", fun=move_backwards)
    my_screen.onkey(key="Right", fun=cw)
    my_screen.onkey(key="Left", fun=ccw)
    my_screen.onkey(key="c", fun=tim.reset)


key_motion()
my_screen.exitonclick()
