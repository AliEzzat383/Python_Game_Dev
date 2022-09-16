from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

XEDGE = 280
YEDGE = 280
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
points = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

in_game = True
while in_game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # TODO: collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        points.update_score()
        snake.grow()
    # TODO: detect wall collision
    if not ((-280 < snake.head.xcor() < 280) and (-280 < snake.head.ycor() < 280)):
        # if (not (-280 < snake.head.xcor() < 280)) or (not (-280 < snake.head.ycor() < 280))
        in_game = False
        points.game_over()
    # TODO: detect tail collision
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            in_game = False
            points.game_over()

screen.exitonclick()
