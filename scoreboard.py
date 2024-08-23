from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.setposition(x= -100, y= 200)
        self.write(self.l_score, align ="center", font=("Courier", 60, "normal"))
        self.setposition(x=100, y=200)
        self.write(self.r_score, align="center", font=("Courier", 60, "normal"))

    def point_for_l(self):
        self.l_score += 1
        self.update_score()

    def point_for_r(self):
        self.r_score += 1
        self.update_score()