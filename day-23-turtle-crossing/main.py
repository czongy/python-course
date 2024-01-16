import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "w")
screen.onkeypress(player.move_down, "s")
screen.onkeypress(player.move_left, "a")
screen.onkeypress(player.move_right, "d")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car(scoreboard.level)

    for car in car_manager.collection:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() == 280:
        player.reset_player()
        scoreboard.increase_level()


screen.exitonclick()
