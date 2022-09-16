import random
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
color_list = ["red", "green", "blue", "dark orange", "teal", "deep pink", "black", "saddle brown"]
tim = Turtle()
tim.shape("classic")
tim.color("black")
directions = [0, 90, 180, 270]
# tim.pensize(15)
tim.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def draw_spirograph(no_of_circles, offset):
    for x in range(0, 360, offset):
        if x != no_of_circles:
            tim.color(random_color())
            tim.circle(100)
            tim.setheading(x)


# def draw_spiral(offset):
#     for x in range(int(360 / offset)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + offset)
#
#
# draw_spiral(5)

draw_spirograph(100,5)

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# def draw_shape(n):
#     angle = 360 / n
#     tim.pencolor(random.choice(color_list))
#     for k in range(n):
#         tim.right(angle)
#         tim.forward(100)
#
#
# for j in range(3, 11):
#     draw_shape(j)

# for _ in range(4):
#     for a in range(10):
#         tim.fd(10)
#         tim.penup()
#         tim.fd(10)
#         tim.pendown()
#     tim.rt(90)

# for _ in range(4):
#     tim.fd(100)
#     tim.rt(90)
screen = Screen()
screen.exitonclick()
