from turtle import Turtle, Screen


timmy = Turtle()
timmy.shape('arrow')

# triangle
for _ in range(3):
    timmy.right(360/3)
    timmy.forward(100)

# square
for _ in range(4):
    timmy.right(360/4)
    timmy.forward(100)

# pentagon
for _ in range(5):
    timmy.right(360/5)
    timmy.forward(100)

# hexagon
for _ in range(6):
    timmy.right(360/6)
    timmy.forward(100)

# heptagon
for _ in range(7):
    timmy.right(360/7)
    timmy.forward(100)

# octagon
for _ in range(8):
    timmy.right(360/8)
    timmy.forward(100)

# nonagon
for _ in range(9):
    timmy.right(360/9)
    timmy.forward(100)

# decagon
for _ in range(10):
    timmy.right(360/10)
    timmy.forward(100)


timmy.penup()
timmy.goto(-300, 0)

# dashed line
for _ in range(25):
    timmy.penup()
    timmy.forward(10)

    timmy.pendown()
    timmy.forward(10)

screen = Screen()
screen.exitonclick()

