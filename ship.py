from turtle import Turtle

MOVE_DISTANCE = 20


class Ship(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('./images/player.gif')
        self.penup()
        self.goto(x, y)

    # Move to the left
    def side_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    # Move to the right
    def side_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x, self.ycor())

