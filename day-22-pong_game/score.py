from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.l_score = 0
        self.r_score = 0
        self.print_score()

    def print_score(self):
        self.write(arg=f"{self.l_score}          {self.r_score}", align="center", font=("arial", 20, "normal"))

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.print_score()

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.print_score()


class Centerline(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        self.draw_line()

    def draw_line(self):
        while self.ycor() > -300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)