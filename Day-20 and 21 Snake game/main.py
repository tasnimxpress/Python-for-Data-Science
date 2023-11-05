from turtle import Screen
from snake import Snake
from food import Food
from score import Scorecard
import time

VERSION = 2.0

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title(f'Snake game {VERSION}')
screen.tracer(0)

snake = Snake()
food = Food()
scores = Scorecard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect of collision with food
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend()
        scores.track_score()

    #detect of collision with wall
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        snake.reset_snake()
        scores.reset_score()

    screen.listen()

    #detect of collision with tail
    for tail in snake.segment[1:]:
        if snake.head.distance(tail) < 10:
            snake.reset_snake()
            scores.reset_score()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")

    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

screen.exitonclick()
