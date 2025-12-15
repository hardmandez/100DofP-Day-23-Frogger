from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.shapesize()
        self.setheading(90)
        self.goto(0,-290)

    def move_player(self):
        self.forward(20)
        print(f"Up")
