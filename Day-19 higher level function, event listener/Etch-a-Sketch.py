from turtle import Turtle, Screen, colormode

colormode(255)
tim = Turtle()
screen = Screen()

def clockwise():
    tim.setheading(tim.heading() - 10)

def anticlockwise():
    tim.setheading(tim.heading() + 10)

def forward():
    tim.forward(10)

def backward():
    tim.backward(10)

def clean():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(forward, 'w')
screen.onkey(backward, 's')

screen.onkey(clockwise, "d")
screen.onkey(anticlockwise, "a")

screen.onkey(clean, "c")

screen.exitonclick()
