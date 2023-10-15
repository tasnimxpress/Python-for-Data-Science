from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('sea green')
screen.title('Snake game version 1.0')
screen.tracer(0)


snake = Snake("white")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    screen.listen()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")

    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


screen.exitonclick()
