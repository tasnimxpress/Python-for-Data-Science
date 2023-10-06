from turtle import Turtle, Screen

#moving turtle
turtle_tur = Turtle()
turtle_tur.shape("turtle")
turtle_tur.color("green")
turtle_tur.forward(200)
turtle_tur.left(90)
turtle_tur.forward(150)
turtle_tur.left(90)
turtle_tur.forward(200)
turtle_tur.left(90)
turtle_tur.forward(150)


turtle_screen = Screen()

print(turtle_screen.canvheight)
turtle_screen.exitonclick()
