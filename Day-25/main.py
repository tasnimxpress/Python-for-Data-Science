import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('Division Games')

image = 'E:/GitHub/100DaysOfPython/Day-25/gifs/ezgif.gif'
screen.addshape(image)
turtle.shape(image)

# get corrdinate
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

df = pd.read_csv("E:/GitHub/100DaysOfPython/Day-25/division.csv")


def division(answer):
    corrdinate = df[df['division'] == answer]
    X = corrdinate['x'].iloc[0]
    Y = corrdinate['y'].iloc[0]
    return (X, Y)


all_division = df['division'].values
score = 0
length = len(df)
all_answer = []
t = turtle.Turtle()
t.hideturtle()
t.penup()

while score != length:
    answer = screen.textinput(title=f"{score}/{length} Guess the Division",
                              prompt="Enter your guess?").capitalize()

    if answer == 'Exit':
        missing_div = []
        for division in all_division:
            if division not in all_answer:
                missing_div.append(division)
        missing_data = pd.DataFrame(missing_div)
        missing_data.to_csv(
            'E:/GitHub/100DaysOfPython/Day-25/missing_division.csv')
        break
    elif answer in all_division and answer not in all_answer:
        position = division(answer)
        t.goto(position)
        all_answer.append(answer)
        score += 1
        t.write(answer)
