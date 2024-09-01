from colors import color_list
import random
from turtle import Turtle as t, Screen, colormode

tod = t()
screen = Screen()
colormode(255)
tod.hideturtle()


def spot_art(dot_size, x_position, y_position, number_of_dots, number_of_line, row_space, column_space):
    tod.speed(0)
    tod.up()
    x_cor = x_position
    y_cor = y_position
    tod.goto(x_cor, y_cor)

    for _ in range(number_of_line):
        for _ in range(number_of_dots):
            random_color = random.choice(color_list)
            tod.color(random_color)
            tod.dot(dot_size)
            tod.up()
            tod.forward(column_space)
            tod.down()
            current_position = tod.ycor() + row_space
        tod.up()
        tod.goto(x_cor, current_position)


spot_art(dot_size=30, x_position=-245, y_position=-220, number_of_dots=10,
         number_of_line=10, row_space=50, column_space=50)

screen.exitonclick()
