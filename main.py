from turtle import Screen
from player import Player
from car_management import CarManagement
from scoreboard import Scoreboard
import time

#Main variables
game_on = True
game_speed = 0.2

#Setup screen
screen = Screen()
# screen.screensize(530, 530)
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.title("Turtler")
screen.tracer(0)
screen.listen()

#Create objects
player = Player()
player.draw_lanes()
carmanagement = CarManagement()
scoreboard = Scoreboard()
# playerlives = PlayerLives()
# playerlevel = Level()

#Screen controls setup
screen.onkey(player.move_player, "q")
screen.onkey(scoreboard.reset_lives, "r")


while game_on:
    screen.update()
    #Move each car forward.
    carmanagement.move_car()

    #Check collision.
    for car in carmanagement.cars:
        if player.ycor() == car.ycor() and (player.xcor() >= car.xcor() and player.xcor() <= car.xcor()+40):
        # if player.distance(car) < 20:
            scoreboard.lives -= 1
            player.player_reset()
            scoreboard.display_score()
            # playerlives.display_lives()
        print(f"Player X:{player.xcor()}, Y:{player.ycor()}")


    #Check for completion
    if player.ycor() > 270:
        player.move_size = 0
        time.sleep(2)
        scoreboard.score += 10
        scoreboard.display_score()
        scoreboard.level += 1
        scoreboard.display_score()
        player.player_reset()
        game_speed -= 0.01
        for i in range(0,2):
            carmanagement.create_cars()
        player.move_size = 20

    #Check lives
    if scoreboard.lives <= 0:
        carmanagement.car_speed=0
        scoreboard.check_high_score()
        scoreboard.game_over()
        scoreboard.display_score()
    else:
        carmanagement.car_speed=20

    time.sleep(game_speed)