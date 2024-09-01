from turtle import Turtle as t, Screen, colormode
import random

line = t()
screen = Screen()
colormode(255)

# 0 - east
# 90 - north
# 180 - west
# 270 - south

turn = [0, 90, 180, 270]
line.width(10)
line.speed(0)


def angle():
    return random.choice(turn)


def walk(limit):
    for _ in range(limit):
        rand_color = (random.randrange(255), random.randrange(
            255), random.randrange(255))
        line.pencolor(rand_color)
        to_angle = angle()
        line.setheading(to_angle)
        line.forward(40)


walk(100)


line.hideturtle()
screen.exitonclick()
