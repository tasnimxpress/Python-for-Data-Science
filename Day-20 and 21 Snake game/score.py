from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scorecard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 270)
        self.color('white')

        self.score = 0
        self.hideturtle()
        self.speed(0)
        self.update_board()

    def update_board(self):
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def track_score(self):
        self.clear()
        self.score += 1
        self.update_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over.", False, ALIGNMENT, FONT)
