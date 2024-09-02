
from turtle import Turtle, Screen, colormode
import random

screen = Screen()
screen.setup(width=500, height=400)

finish_line = Turtle()
finish_line.speed(0)
finish_line.hideturtle()
finish_line.up()
finish_line.goto(220, 140)
finish_line.right(90)
finish_line.pendown()
finish_line.width(5)
finish_line.forward(260)
finish_line.up()

color = ['red', 'green', 'orange', 'yellow', 'blue', 'purple']
user_input = (screen.textinput(title='Make your bet',
              prompt='Which turtle will win? Enter a color: ')).lower()


turtle_list = []
x_pos = -230
y_pos = -140
for i in range(6):
    tim = Turtle(shape='turtle')
    tim.up()
    tim.color(color[i])
    new_pos = tim.goto(x_pos, y_pos + 40)
    y_pos = tim.ycor()
    turtle_list.append(tim)

race_start = True
while race_start:
    for turtle in turtle_list:
        distance = random.randint(1, 20)
        turtle.forward(distance)

        if turtle.xcor() >= 220.0:
            winner = turtle.pencolor()
            if user_input == winner:
                finish_line.goto(-50, 0)
                finish_line.write("You win", font=("Arial", 20, "bold"))

            else:
                finish_line.goto(-200, 0)
                finish_line.write(f"You lose. The winner is {
                                  turtle.pencolor()}", font=("Arial", 20, "bold"))

            race_start = False

screen.exitonclick()
