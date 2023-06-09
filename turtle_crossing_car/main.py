import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carManager.create_cars()
    carManager.move()
    for car in carManager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect a successful crossing
    if player.is_at_finish_line():
        player.starting_position()
        carManager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
