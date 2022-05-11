STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle,Screen
from car_manager import CarManager
screen = Screen()
import time

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def move_forward(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def game_ends(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

