from turtle import Screen
from player import Player

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

#Screen controls setup
screen.onkey(player.move_player, "q")


while game_on:
    screen.update()