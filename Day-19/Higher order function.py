# Higher order function
# higher order function is a type of function that takes another function as an input

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(20)


screen.listen()
# onkey is behaving as higher order function; it takes move_forward function as function input
screen.onkey(fun=move_forward, key='right')


screen.exitonclick()
