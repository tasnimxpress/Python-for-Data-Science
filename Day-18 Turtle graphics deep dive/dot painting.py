from turtle import Screen, colormode
import turtle as t
import colorgram
import random

colormode(255)
t.speed(0)
t.penup()
t.setx(-250)
t.sety(-225)

colors = colorgram.extract('image.jpeg', 50)
def random_color():
    first_color = random.choice(colors)
    rgb = first_color.rgb
    t.color(rgb)

def dot_art(number_of_dot, dot_size, xcor_gap):
    for _ in range(number_of_dot):
        random_color()
        t.dot(dot_size)
        t.penup()
        t.forward(xcor_gap)
        t.pendown()
        t.dot(dot_size)

def y_position(ycor_gap):
    t.penup()
    t.setx(-250)
    t.sety(t.ycor() + ycor_gap)

for _ in range(10):
    dot_art(10, 20, 50)
    y_position(ycor_gap=50)


t.hideturtle()
screen = Screen()
screen.exitonclick()
