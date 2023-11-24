from turtle import Screen, Turtle
import turtle
import pandas as pd

FONT = ("Courier", 10, "normal")

class StateName(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()

#Screen setup
screen = Screen()
screen.title("U.S State game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
show_state = StateName()

#get the coordinates
# def click_cor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(click_cor)
# turtle.mainloop()

#Read data
data = pd.read_csv('50_states.csv')
data["state"]= data["state"].str.title()
all_state = data.state.to_list()
total_state = len(all_state)

guessed_state = []

#Start the game
play = True
while len(guessed_state) < total_state:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/{len(all_state)} States Correct",
                                    prompt="What's another state?").title()

    if answer_state in all_state:
        if answer_state not in guessed_state:
            guessed_state.append(answer_state)

    for _ in range(total_state):
        name = data[data.state == answer_state]
        coordinate = (int(name.x.iloc[0]), int(name.y.iloc[0]))
    show_state.goto(coordinate)
    show_state.write(arg=answer_state, font=FONT)

    #generating csv file for missing state
    if answer_state == 'Exit':
        data_file = set(guessed_state).symmetric_difference(all_state)
        remain_state = pd.DataFrame(data_file)
        remain_state.to_csv('remain_state.csv')
        break

screen.exitonclick()
