# turtle graphics
from turtle import Turtle, Screen

square = Turtle()


def create_square(distance, r_angle):
    square.forward(distance)
    square.right(r_angle)


for i in range(4):
    create_square(300, 90)

screen = Screen()
screen.exitonclick()
