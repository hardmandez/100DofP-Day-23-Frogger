from turtle import Screen
from player import Player
from car_management import Car, Carmanagement
import time

#Main variables
game_on = True

#Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.title("Turtler")
screen.tracer(0)
screen.listen()

#Create objects
player = Player()
carmanagement = Car()


#Screen controls setup
screen.onkey(player.move_player, "q")

while game_on:
    time.sleep(0.2)
    for i in len(lane1_cars):
        lane1_cars[i].move_car()
        lane1_cars[i].reset_car()
    screen.update()