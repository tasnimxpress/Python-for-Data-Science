from turtle import Screen
from screendivider import Divider
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time

HEIGHT = 500
WIDTH = 1000
COLOR = "black"
TARGET_SCORE = 10

# Screen Look:
screen = Screen()
screen.bgcolor(COLOR)
screen.setup(height=HEIGHT, width=WIDTH)
screen.title('Pong Arcade')
screen.tracer(False)

divider = Divider()
player_1_paddle = Paddle(x=-450, y=0)
player_2_paddle = Paddle(x=450, y=0)
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(fun=player_1_paddle.up, key='a')
screen.onkey(fun=player_1_paddle.down, key='d')

screen.onkey(fun=player_2_paddle.up, key='Up')
screen.onkey(fun=player_2_paddle.down, key='Down')


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # ball collision with up and down wall
    if ball.ycor() > 220 or ball.ycor() < -220:
        ball.bounce_y()

    # Ball collision with paddle
    if ball.distance(player_2_paddle) < 42 and ball.xcor() > 340 or ball.distance(player_1_paddle) < 42 and ball.xcor() <-340:
        ball.bounce_x()

    # right/Player_1 paddle miss
    if ball.xcor() > 510:
        ball.reset_position()
        score.increase_computer_score()

    # left/Player_2 paddle miss
    if ball.xcor() < -510:
        ball.reset_position()
        score.increase_player_score()

    if score.player_1_score == TARGET_SCORE or score.player_2_score == TARGET_SCORE:
        score.game_over()
        game_on = False


screen.exitonclick()
