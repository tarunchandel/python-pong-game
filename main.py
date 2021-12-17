from turtle import Screen, Turtle

from ball import Ball
from bat import Bat
from score import Score

HEIGHT = 600
WIDTH = 800

BALL_MAX_XCOR = int(round(WIDTH / 2)) - 20
BALL_MAX_YCOR = int(round(HEIGHT / 2)) - 20

BALL_ANGLE_INCREASE = 90

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

divider = Turtle()
divider.color("white")
divider.hideturtle()
divider.penup()
divider.pensize(5)
divider.speed(0)
divider.shape("square")
divider.left(270)
divider.goto(0, HEIGHT / 2)
for i in range(int(HEIGHT / 20)):
    if divider.isdown():
        divider.penup()
    else:
        divider.pendown()
    divider.forward(20)

left_bat = Bat("left")
right_bat = Bat("right")

screen.listen()
screen.onkey(right_bat.move_up, "Up")
screen.onkey(right_bat.move_down, "Down")
screen.onkey(left_bat.move_up, "a")
screen.onkey(left_bat.move_down, "z")

# TODO: make the bats move while the key is pressed
# TODO: add an option to make it a 1 player game, the left bat moves on its own

ball = Ball()
current_ball_angle = 45
ball.setheading(current_ball_angle)
hit = False
left_score = Score("left")
right_score = Score("right")

while True:

    if ball.distance(left_bat) < 50 and ball.xcor() < -(BALL_MAX_XCOR - 20) \
            or ball.distance(right_bat) < 50 and ball.xcor() > (BALL_MAX_XCOR - 20) \
            or ball.ycor() < -BALL_MAX_YCOR \
            or ball.ycor() > BALL_MAX_YCOR:
        hit = True
    elif ball.xcor() > BALL_MAX_XCOR:
        left_score.increase_score()
        ball.goto(0, 0)
        current_ball_angle += BALL_ANGLE_INCREASE
        hit = True
    elif ball.xcor() < -BALL_MAX_XCOR:
        right_score.increase_score()
        ball.goto(0, 0)
        current_ball_angle += BALL_ANGLE_INCREASE
        hit = True

    if hit:
        current_ball_angle += BALL_ANGLE_INCREASE
        ball.setheading(current_ball_angle)
        hit = False
    screen.update()
    ball.move()

screen.exitonclick()
