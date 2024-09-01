# create a spirograph using turtle module

from turtle import Turtle as t, Screen, colormode
from random import randrange

screen = Screen()
graph = t()
colormode(255)
graph.speed(0)

circle_continue = True
while circle_continue:

    random_color = (randrange(255), randrange(255), randrange(255))
    graph.color(random_color)
    graph.circle(100)
    graph.setheading(graph.heading() + 10)

    if graph.heading() == 0.0:
        circle_continue = False


screen.exitonclick()
