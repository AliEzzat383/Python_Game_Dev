from turtle import Turtle

FONT = ("Courier", 88, "normal")
ALIGNMENT = "center"
R_LOC = (100, 200)
L_LOC = (-100, 200)


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.l_score = 0
        self.r_score = 0
        self.update_scores()

    def update_scores(self):
        self.clear()
        self.goto(L_LOC)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(R_LOC)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def add_scores(self, winner=''):
        if winner == 'r':
            self.r_score += 1
            self.update_scores()
        elif winner == 'l':
            self.l_score += 1
            self.update_scores()
