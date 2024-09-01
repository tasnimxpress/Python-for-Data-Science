from turtle import Turtle as t, colormode, Screen
from random import randrange

shapes = t()
screen = Screen()
colormode(255)


def create_shape(distance, num_side):
    cone = 360 / num_side
    color = (randrange(255), randrange(255), randrange(255))
    shapes.pencolor(color)

    for _ in range(num_side):
        shapes.forward(distance)
        shapes.right(cone)


for i in range(3, 10):
    create_shape(100, i)

shapes.hideturtle()
screen.exitonclick()
