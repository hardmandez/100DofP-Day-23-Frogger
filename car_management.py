from turtle import Turtle
import random

LANE_POSITIONS=(270,250,230,210,190,170,150,130,110,90,70,50,30,10,-10,-30,-50,-70,-90,-110,-130,-150,-170,-190,-210,-230,-250,-270)
CAR_SIZE=(20,40)
COLOURS=("RED","GREEN","BLUE","BLACK","WHITE")

class Carmanagement(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(COLOURS[random.randint(0, 4)])
        self.setheading(180)
        self.shapesize(1, 2, 1)
        self.create_cars()

    def create_cars(self):
        for lane in LANE_POSITIONS:
            new_car = car(lane)
            self.car_lanes.append(new_car)

    def move_car(self):
        self.forward(20)

    def reset_car(self):
        if self.xcor() < -310:
            new_x = 310
            new_y = self.ycor()
            self.goto(new_x,new_y)

class Car()