from turtle import Turtle, Screen
screen = Screen()
screen.listen()


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)
        # self.move_speed = 0.1

    def move_up(self):
        if self.ycor() < 260:
            y_cor = self.ycor() + 20
            self.goto(x=self.xcor(), y=y_cor)

    def move_down(self):
        if self.ycor() > -260:
            y_cor = self.ycor() - 20
            self.goto(x=self.xcor(), y=y_cor)

    def move_paddle(self, up_key, down_key):
        screen.onkeypress(self.move_up, up_key)
        screen.onkeypress(self.move_down, down_key)
