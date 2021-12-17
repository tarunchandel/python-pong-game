from turtle import Turtle

HEIGHT = 600
WIDTH = 800
BAT_SPEED = 80
BAT_XCOR = int(round(WIDTH / 2)) - 20
BAT_MAX_MOVE = int(round(HEIGHT / 2)) - BAT_SPEED


class Bat(Turtle):
    def __init__(self, direction):
        super().__init__()
        self.penup()
        self.speed(0)
        self.shape("square")
        self.color("white")
        self.resizemode("user")
        self.shapesize(stretch_len=4, stretch_wid=1)
        self.setheading(90)
        if direction == "left":
            self.goto(-BAT_XCOR, 0)
        else:
            self.goto(BAT_XCOR, 0)

    def move_up(self):
        if self.ycor() < BAT_MAX_MOVE:
            self.forward(BAT_SPEED)

    def move_down(self):
        if self.ycor() > - BAT_MAX_MOVE:
            self.backward(BAT_SPEED)
