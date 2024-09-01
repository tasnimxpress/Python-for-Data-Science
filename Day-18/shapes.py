# create triangle, square, polygons using turtle graphics


import turtle as t
from turtle import colormode
from random import randrange

polygon = t.Turtle()
screen = t.Screen()

colormode(255)


def create_shapes(distance, angle, limit):
    random_color()
    for _ in range(limit):
        polygon.forward(distance)
        polygon.right(angle)


def random_color():
    R = randrange(255)
    G = randrange(255)
    B = randrange(255)
    polygon.pencolor(R, G, B)


# triangle: range(3)
create_shapes(100, 120, 3)

# square: range(4)
create_shapes(100, 90, 4)

# pentagon: range(4)
create_shapes(100, 72, 5)

# hexagon: range(6):
create_shapes(100, 60, 6)

# heptagon: range(7)
create_shapes(100, 51.43, 7)

# octagon: range(8)
create_shapes(100, 45, 8)

# nonagon: range(9):
create_shapes(100, 40, 9)

# decogon: range(10):
create_shapes(100, 36, 10)


polygon.hideturtle()
screen.exitonclick()
