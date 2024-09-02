# Higher order function
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


screen.listen()
screen.onkey(fun=move_forward, key='right')


screen.exitonclick()
