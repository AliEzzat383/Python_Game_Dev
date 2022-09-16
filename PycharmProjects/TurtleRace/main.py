from turtle import Turtle, Screen
import random

go = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race")
colors = ["red", "orange", "gold", "green", "blue", "purple"]
# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-230, y=-150)
turtles = []
for color in colors:
    tortoise = Turtle(shape="turtle")
    tortoise.color(color)
    tortoise.penup()
    turtles.append(tortoise)
for item in turtles:
    step = 50 * turtles.index(item) - 100
    item.goto(x=-230, y=step)
if user_bet:
    go = True
while go:
    for trtl in turtles:
        if trtl.xcor() >= 230:
            go = False
            winner = trtl.pencolor()
            if winner == user_bet:
                print(f"you've won the {winner} turtle is the winner")
                exit()
            else:
                print(f"you've lost the {winner} turtle is the winner")
                exit()

        rand_dist = random.randint(0, 10)
        trtl.forward(rand_dist)
screen.exitonclick()
