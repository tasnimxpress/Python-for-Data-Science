from turtle import Turtle

MOVE_DISTANCE = 20
X_COR = 0.0
Y_COR = 0.0
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.body = []
        self.snake_body()
        self.head = self.body[0]

    def snake_body(self):
        for _ in range(3):
            pices = Turtle()
            pices.up()
            pices.color('white')
            pices.shape('square')
            pices.goto(X_COR-20, Y_COR)
            NEW_X_COR = pices.xcor()
            pices.goto(NEW_X_COR, Y_COR)
            self.body.append(pices)

    def move(self):
        for segment in range(len(self.body) - 1, 0, -1):
            new_x = self.body[segment - 1].xcor()
            new_y = self.body[segment - 1].ycor()
            self.body[segment].goto(new_x, new_y)

        self.body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
