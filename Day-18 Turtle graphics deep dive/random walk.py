from turtle import Screen, colormode
import turtle as t
import random

colormode(255)
t.pensize(10)
t.speed(0)
walk_direction = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.color(r, g, b)


for line in range(200):
    random_color()
    t.forward(30)
    t.setheading(random.choice(walk_direction))
    
t.shape('circle')
t.shapesize(0.1)

screen = Screen()
screen.exitonclick()
