from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
# control constants
WIDTH = 800
HEIGHT = 600
PAD_LOC = (HEIGHT+WIDTH)/4
R_PAD_LOC = (PAD_LOC, 0)
L_PAD_LOC = (-PAD_LOC, 0)
OFFSET = 20
TOP = (HEIGHT / 2) - OFFSET  # subtract offset for viewing
BOTTOM = - TOP
RIGHT = (WIDTH / 2) - (3*OFFSET)
LEFT = - RIGHT
# screen initials
screen = Screen()
screen.title("Pong")
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.tracer(0)
# objects
r_paddle = Paddle(R_PAD_LOC)
l_paddle = Paddle(L_PAD_LOC)
ball = Ball()
scores = ScoreBoard()

in_game = True
while in_game:
    screen.update()

    screen.listen()
    screen.onkeypress(r_paddle.up, "Up")
    screen.onkeypress(r_paddle.down, "Down")
    screen.onkeyrelease(r_paddle.stop, "Up")
    screen.onkeyrelease(r_paddle.stop, "Down")

    screen.onkeypress(l_paddle.up, 'w')
    screen.onkeypress(l_paddle.down, 's')
    screen.onkeyrelease(l_paddle.stop, 'w')
    screen.onkeyrelease(l_paddle.stop, 's')

    if BOTTOM < ball.ycor() < TOP:
        ball.move()
    else:
        ball.bounce('y')
    if ball.distance(r_paddle) < 50:
        ball.bounce('x')
        ball.speed *= 10
    if ball.distance(l_paddle) < 50:
        ball.bounce('x')
        ball.speed *= 10
    if ball.xcor() > (PAD_LOC+30):
        scores.add_scores('r')
        ball.goto(0, 0)
        ball.bounce('x')
    if ball.xcor() < -(PAD_LOC+30):
        scores.add_scores('l')
        ball.goto(0, 0)
        ball.bounce('x')


screen.exitonclick()
