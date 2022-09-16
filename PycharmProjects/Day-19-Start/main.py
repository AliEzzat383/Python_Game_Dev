import turtle
from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()


def move_forwards():
    tim.fd(10)


my_screen.listen()
my_screen.onkey(key="space", fun=move_forwards)
my_screen.exitonclick()
