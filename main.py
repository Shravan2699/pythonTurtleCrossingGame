import random
import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
scoreboard = Scoreboard()
screen.listen()
car_manager = CarManager()


# print(len(my_cars))
my_turtle = Player()
screen.onkey(my_turtle.move_forward,"Up")
game_is_on = True
print(car_manager)
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # Turtle collides with cars
    for car in car_manager.all_cars:
        if my_turtle.distance(car) < 25:
            print("game Over")
            scoreboard.final_scoreboard()
            screen.exitonclick()

    #turtle crosses the road,we level up,cars speed up
    if my_turtle.game_ends():
        my_turtle.go_to_start()
        car_manager.speed_up()
        scoreboard.level_up()






