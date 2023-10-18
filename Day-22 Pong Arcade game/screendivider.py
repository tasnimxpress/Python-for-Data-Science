from turtle import Turtle

HEIGHT = 500
WIDTH = 1000
DIVIDER_UPPER_BOUND = (HEIGHT/2) - 20
DIVIDER_LOWER_BOUND = (-HEIGHT/2) + 20

class Divider:
    def __init__(self):
        self.divider = []
        self.wall()


    def wall(self):
        brick = Turtle()
        brick.hideturtle()
        brick.penup()
        brick.goto(0, DIVIDER_LOWER_BOUND)
        brick.pencolor('white')
        brick.pensize(5)
        brick.setheading(90)

        set_brick = True
        while set_brick:
            if brick.ycor() > DIVIDER_UPPER_BOUND:
                set_brick = False
            else:
                brick.speed(0)
                brick.pendown()
                brick.forward(20)
                brick.penup()
                brick.forward(20)
            self.divider.append(brick)
