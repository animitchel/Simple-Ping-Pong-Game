from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xam = 10
        self.yam = 10

    def move_ball(self):
        new_x = self.xcor() + self.xam
        new_y = self.ycor() + self.yam
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.yam *= -1

    def bounce_x(self):
        self.xam *= -1
       

    def reset_direction(self):
        self.goto(0, 0)
        self.bounce_x()
        self.yam = 10
        self.xam = 10

    def speedy(self):
        if self.yam == 10:
            self.yam += 10
        if self.xam == 10:
            self.xam += 10
        if self.yam == -10:
            self.yam -= 10
        if self.xam == -10:
            self.xam -= 10