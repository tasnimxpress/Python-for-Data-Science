import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
stage = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(fun=player.move, key="Up")
    cars.car()
    cars.move_car()

    #collision with car
    for each_car in cars.all_car:
        if each_car.distance(player) < 20:
            game_is_on = False
            stage.game_over()

        #win and level up
        if player.win():
            player.start_again()
            cars.level_up()
            stage.current_level()

screen.exitonclick()
