from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position: tuple):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position: tuple):
        self.speed('fastest')
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=5)
        self.left(90)
        self.goto(position)
        self.color('white')

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.back(20)
