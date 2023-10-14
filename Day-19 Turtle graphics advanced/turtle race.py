from turtle import Turtle, Screen
import random

screen = Screen()

# width = x coordinate, height = y coordinate
screen.setup(height=400, width=800)

colors = ["red", "blue", "yellow", "orange", "purple", "green"]
all_turtle = []

user_bet = screen.textinput(title="Make your bet", prompt=f'Who will win?\nParticipants are: {colors}\nEnter a color: ')

distance = -100
i = 0
for _ in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-350.0, y=distance)
    i += 1
    distance += 40
    all_turtle.append(new_turtle)

wrap = Turtle()
wrap.speed(0)
wrap.penup()
wrap.goto(350, 150)
wrap.pendown()
wrap.pensize(10)
wrap.color("light sky blue")
wrap.right(90)
wrap.forward(300)

if user_bet:
    race_on = True

    while race_on:
        for turtle in all_turtle:
            if turtle.xcor() > 350:
                race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print('You win')
                else:
                    print(f'You loose. The winner is {winning_color}. ')
            turtle.forward(random.randint(1, 9))

screen.exitonclick()
