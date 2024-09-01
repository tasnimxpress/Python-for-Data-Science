# create a dashed line using turtle graphics

import turtle as t

dash = t.Turtle()
screen = t.Screen()


def create_dash(distance, line):
    dash.up()
    dash.hideturtle()
    dash.goto(-300, 0)
    dash.showturtle()

    for i in range(line):
        dash.forward(distance)
        dash.up()
        dash.forward(distance)
        dash.down()


create_dash(10, 30)

screen.exitonclick()
