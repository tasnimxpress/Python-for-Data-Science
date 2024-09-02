from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()


def move_forward():
    pen.forward(20)


def move_backward():
    pen.backward(20)


def counter_clockwise():
    # pen.setheading(90)
    pen.left(10)


def clockwise():
    pen.right(10)


def clear_screen():
    pen.clear()
    pen.reset()


screen.listen()
screen.onkey(fun=move_forward, key='w')
screen.onkey(fun=move_backward, key='s')
screen.onkey(fun=counter_clockwise, key='a')
screen.onkey(fun=clockwise, key='d')
screen.onkey(fun=clear_screen, key='c')


screen.exitonclick()
