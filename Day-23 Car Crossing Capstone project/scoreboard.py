from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.start_level = 1
        self.update_level()

    def update_level(self):
        self.goto(-200, 250)
        self.write(f'Level: {self.start_level}', True, 'Center', FONT)

    def current_level(self):
        self.start_level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', True, 'Center', FONT)
