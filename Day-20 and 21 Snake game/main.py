from turtle import Screen
from snake import Snake
from food import Food
from score import Scorecard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('dim grey')
screen.title('Snake game version 1.0')
screen.tracer(0)


snake = Snake("white")
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
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scores.game_over()
        game_is_on = False
    screen.listen()


    #detect of collision with tail
    for tail in snake.segment[1:]:
        if snake.head.distance(tail) < 10:
            game_is_on = False
            scores.game_over()


    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")

    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


screen.exitonclick()
