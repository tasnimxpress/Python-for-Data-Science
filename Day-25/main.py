import turtle

screen = turtle.Screen()
screen.title('District Games')

# image = 'E:/GitHub/100DaysOfPython/Day-25/gifs/gifgit.gif'
image = 'E:/GitHub/100DaysOfPython/Day-25/gifs/us_states_img.gif'
screen.addshape(image)

# screen.screensize(canvwidth=346, canvheight=470)
screen.screensize(canvwidth=725, canvheight=491)


turtle.shape(image)
screen.exitonclick()
