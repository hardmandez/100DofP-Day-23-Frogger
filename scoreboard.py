from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.lives=3
        self.level=1
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(-260, 290)
        self.write(f"Lives: {self.lives}", align="center", font=("Arial", 10, "bold"))
        self.goto(-110, 290)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 10, "bold"))
        self.goto(110, 290)
        self.write(f"High Score: {self.high_score}", align="center", font=("Arial", 10, "bold"))
        self.goto(260, 290)
        self.write(f"Level: {self.level}", align="center", font=("Arial", 10, "bold"))

    def check_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial", 10, "bold"))
        self.goto(0, -20)
        self.write("Press ""r"" to play again", align="center", font=("Arial", 10, "bold"))

    def reset_lives(self):
        self.lives=3
        self.score=0
        self.level=1
        self.display_score()

# class PlayerLives(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.lives=3
#         self.penup()
#         self.hideturtle()
#         self.color("white")
#         self.display_lives()
#
#     def display_lives(self):
#         self.clear()
#         self.goto(-260, 290)
#         self.write(f"Lives: {self.lives}", align="center", font=("Arial", 10, "bold"))
#
#     def reset_lives(self):
#         self.lives=3
#         self.display_lives()



# class Level(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.penup()
#         self.hideturtle()
#         self.level = 1
#         self.color("white")
#         self.display_level()
#
#     def display_level(self):
#         self.clear()
#         self.goto(260, 290)
#         self.write(f"Level: {self.level}",align="left",font=("Arial",10, "bold"))
