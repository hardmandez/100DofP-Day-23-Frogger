from turtle import Turtle
import random
LANE_POSITIONS(-285,-265,-245,-225,-205,-)

class car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.colour(random.randint(0,255),random.randint(0,255),random.randint(0,255))
