from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_body()
        score.score_tracker()

    # detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 300 or snake.head.ycor() < -295:
        game_on = False
        score.game_over()

    # detect collision with tail
    for pices in snake.body[1:]:
        if snake.head.distance(pices) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()
