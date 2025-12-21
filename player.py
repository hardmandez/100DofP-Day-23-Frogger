from turtle import Turtle

LANE_POSITIONS=(270,250,230,210,190,170,150,130,110,90,70,50,30,10,-10,-30,-50,-70,-90,-110,-130,-150,-170,-190,-210,-230,-250,-270)

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("green")
        self.shapesize()
        # self.goto(300,300)
        # self.pendown()
        # self.goto(-300,300)
        # self.goto(-300,-300)
        # self.goto(300,-300)
        # self.goto(300, 300)
        self.penup()
        self.setheading(90)
        self.goto(0,-280)
        # print(self.shapesize())

    def move_player(self):
        self.forward(20)
        print(f"Up")

    def player_reset(self):
        self.goto(0, -290)


    def draw_lanes(self):
        for lane in LANE_POSITIONS:
            new_y=lane-10
            self.penup()
            self.goto(280,new_y)
            self.pendown()
            self.goto(-280,new_y)
            self.penup()
        self.goto(0, -290)

