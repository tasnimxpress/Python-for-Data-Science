from turtle import Turtle

REACHED_SCORE = 10
class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_1_score = 0
        self.player_2_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=-100, y=120)
        self.write(self.player_2_score, align="center", font=('courier', 80, 'normal'))
        self.goto(x=100, y=120)
        self.write(self.player_1_score, align="center", font=('courier', 80, 'normal'))


    def game_over(self):
        self.goto(x=0, y=0)
        if self.player_1_score == REACHED_SCORE:
            self.write("Game Over\n You Win", align="center", font=('courier', 25, 'normal'))
        else:
            self.write("Game Over\nYou Loose", align="center", font=('courier', 25, 'normal'))

    def increase_player_score(self):
        self.player_1_score += 1
        self.update_score()

    def increase_computer_score(self):
        self.player_2_score += 1
        self.update_score()
