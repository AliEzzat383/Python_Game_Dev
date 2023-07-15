# Imports
from turtle import Screen
from scoreboard import ScoreBoard
from cars import Car
from player import Player
from traffic import Traffic
import time

# Control Constants
WIDTH = 600
HEIGHT = 600
OFFSET = 60  # based on player loc of -270 in case of editing,edit player as well
TOP = int((HEIGHT / 2) - OFFSET)
BOTTOM = - TOP
RIGHT = TOP
LEFT = BOTTOM

# Screen Setup
screen = Screen()
screen.colormode(255)
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)
screen.title("Turtle Crossing")
# Objects
user = Player()
# block = Car()
# block.goto(100, -200)
jam = Traffic()
score = ScoreBoard()

# Game function
in_game = True
while in_game:
    screen.update()
    time.sleep(0.1)
    jam.move_traffic()
    # jam.unique_loc()
    for x in jam.batch:
        if user.distance(x) < 20:
            score.game_over()
            in_game = False
            time.sleep(0.5)
            if screen.textinput("Restart Game", "would you like to go again ?") is not None:
                score.clear()
                score = ScoreBoard()
                user.origin_reset()
                jam.more_cars()
                in_game = True
    # block.moving()
    # if user.is_collide(block):
    #     print("yay")
    screen.listen()
    screen.onkeypress(user.move, "space")
    screen.onkeyrelease(user.stop, "space")
    if user.ycor() == TOP:
        score.add_score()
        user.origin_reset()

screen.exitonclick()
