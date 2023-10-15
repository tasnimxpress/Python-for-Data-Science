from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self, body_color):
        self.snake_color = body_color
        self.snake = []
        self.x_cod = 0.0
        self.y_cod = 0.0

        self.body()
        self.head = self.snake[0]

# snake body
    def body(self):
        for _ in range(3):
            snake_body = Turtle(shape='square')
            snake_body.penup()
            snake_body.color(self.snake_color)
            snake_body.goto(self.x_cod, self.y_cod)
            self.x_cod += -20
            self.snake.append(snake_body)

# forward
    def move(self):
        for part in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[part - 1].xcor()
            new_y = self.snake[part - 1].ycor()
            self.snake[part].goto(new_x, new_y)
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
