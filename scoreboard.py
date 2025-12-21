from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,290)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 10, "bold"))


class PlayerLives(Turtle):
    def __init__(self):
        super().__init__()
        self.lives=3
        self.penup()
        self.hideturtle()
        self.color("white")
        self.display_lives()

    def display_lives(self):
        self.clear()
        self.goto(-260, 290)
        self.write(f"Lives: {self.lives}", align="center", font=("Arial", 10, "bold"))

    def reset_lives(self):
        self.lives=3
        self.display_lives()

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.color("white")
        self.display_level()

    def display_level(self):
        self.clear()
        self.goto(260, 290)
        self.write(f"Level: {self.level}",align="left",font=("Arial",10, "bold"))
