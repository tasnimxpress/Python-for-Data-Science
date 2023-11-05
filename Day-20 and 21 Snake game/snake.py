from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
COLOR = 'white'
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    # snake body
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_body(position)

    def add_body(self, position):
        snake_body = Turtle(shape='square')
        snake_body.penup()
        snake_body.color(COLOR)
        snake_body.goto(position)
        self.segment.append(snake_body)

    def extend(self):
        self.add_body(self.segment[-1].position())

    def reset_snake(self):
        for each in self.segment:
            each.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    # forward
    def move(self):
        for part in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[part - 1].xcor()
            new_y = self.segment[part - 1].ycor()
            self.segment[part].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # UP
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    # DOWN
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    # LEFT
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    # RIGHT
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
