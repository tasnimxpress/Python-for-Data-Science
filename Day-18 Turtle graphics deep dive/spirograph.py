from turtle import Screen, colormode
import turtle as t
import random

colormode(255)
t.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.color(r, g, b)

def spirograph(gap):
    for _ in range(int(360/gap)):
        random_color()
        t.setheading(t.heading() + gap)
        t.circle(100)

spirograph(5)
t.hideturtle()

screen = Screen()
screen.exitonclick()
