import turtle
from turtle import Screen, colormode
import random

colormode(255)
def draw_shapes(num_of_line):
    angle = 360/num_of_line
    for _ in range(num_of_line):
        turtle.right(angle)
        turtle.forward(100)


for line in range(3, 11):
    turtle.color(random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255))
    draw_shapes(line)

screen = Screen()
screen.exitonclick()
