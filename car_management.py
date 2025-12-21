from turtle import Turtle
import random

LANE_POSITIONS=(270,250,230,210,190,170,150,130,110,90,70,50,30,10,-10,-30,-50,-70,-90,-110,-130,-150,-170,-190,-210,-230,-250,-270)
# CAR_SIZE=((1.0,2.0,1.0),(1.0,1.0,1.0))
CAR_FORWARD=20
COLOURS=("RED","GREEN","BLUE","BLACK","WHITE")

class CarManagement():
    def __init__(self):
        self.cars=[]
        self.no_of_cars=10
        self.car_speed=20

        for i in range(self.no_of_cars):
            self.create_cars()

    def create_cars(self):
        # for lane in LANE_POSITIONS:
        new_car = Car()
        new_car_x = random.randint(-280,280)
        new_car_y = random.choice(LANE_POSITIONS)
        # new_car.goto(new_car_x, lane)
        new_car.goto(new_car_x, new_car_y)
        self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            if car.xcor() <= -270:
                new_car_x = 280
                new_car_y = random.choice(LANE_POSITIONS)
                car.goto(new_car_x, new_car_y)
            car.forward(self.car_speed)

    def reset_car(self):
        if self.xcor() < -310:
            new_x = 310
            new_y = self.ycor()
            self.goto(new_x,new_y)

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("black")
        self.fillcolor(COLOURS[random.randint(0, 4)])
        self.setheading(180)
        self.shapesize(1,2,1)
