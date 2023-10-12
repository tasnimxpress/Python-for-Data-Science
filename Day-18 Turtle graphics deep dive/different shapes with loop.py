from turtle import Turtle, Screen, colormode
import random

screen = Screen()
colormode(255)

timmy = Turtle()

i = 3
on = True
while on:
    timmy.color(random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255))

    for _ in range(i):
        timmy.right(360/i)
        timmy.forward(100)
    timmy.home()

    if timmy.pos() == (0.00, 0.00):
        i += 1

    if i == 11:
        on = False

screen.exitonclick()
