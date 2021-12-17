from turtle import Turtle

HEIGHT = 600
WIDTH = 800
SCORE_XCOR = int(round(WIDTH / 4))
SCORE_YCOR = int(round(HEIGHT / 2) - 120)


class Score(Turtle):
    def __init__(self, side):
        super().__init__()
        self.score: int = 0
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.speed(0)
        if side == "left":
            self.goto(-SCORE_XCOR, SCORE_YCOR)
        else:
            self.goto(SCORE_XCOR, SCORE_YCOR)

        self.print_score()

    def increase_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"{self.score}", move=False, align='center', font=('Courier', 80, 'bold'))

    def restart(self):
        self.score = 0
        self.clear()
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER \nClick to restart.", move=False, align='center', font=('Arial', 20, 'normal'))
