from turtle import Turtle

FONT = ("Arial", 16, "normal")
ALIGNMENT = "right"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.score = 0
        self.penup()
        self.color("black")
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(250, 250)
        self.write("score: ", False, ALIGNMENT, FONT)
        self.goto(260, 250)
        self.write(self.score, False, ALIGNMENT, FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.score = 0
        self.update_score()
        self.goto(70, 0)
        self.color("red")
        self.write("GAME OVER", False, ALIGNMENT, FONT)
