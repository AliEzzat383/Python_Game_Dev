###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
tim = Turtle()
tim.shape("classic")
tim.color("black")
tim.speed("fastest")
colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123),
          (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
          (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
          (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208),
          (168, 99, 102)]

def hirst_painting(size, step, sqr_len,color_list):
    tim.ht()
    tim.penup()
    tim.goto(100, 100)
    tim.pendown()
    tim.speed("fastest")
    for j in range(sqr_len):
        tim.penup()
        new_y = tim.ycor() - step
        tim.bk(step * sqr_len)
        tim.goto(tim.xcor(), new_y)
        for i in range(sqr_len):
            tim.dot(size, random.choice(color_list))
            tim.fd(step)


hirst_painting(10, 20, 10,colors)
my_screen = Screen()
my_screen.exitonclick()
