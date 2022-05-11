FONT = ("Courier", 24, "normal")

from turtle import Turtle,Screen

screen1 = Screen()
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.level = 1
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-260,260)
        self.write(f"LEVEL {self.level}", font=FONT)


    def level_up(self):
        self.level += 1
        self.update_scoreboard()

    def final_scoreboard(self):
        self.goto(-100,0)
        self.write("GAME OVER", font=FONT)
