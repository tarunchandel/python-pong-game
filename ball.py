from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.speed(0)
        self.setheading(45)

    def move(self):
        self.forward(1)
