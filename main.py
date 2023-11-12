from turtle import Turtle, Screen
from pad import Paddy
from Score import ScoreBoard
from Ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)

r_paddy = Paddy((350, 0))
l_paddy = Paddy((-350, 0))
ball = Ball()

screen.listen()

screen.onkey(fun=r_paddy.go_up, key="Up")
screen.onkey(fun=r_paddy.go_down, key="Down")
screen.onkey(fun=l_paddy.go_up, key="w")
screen.onkey(fun=l_paddy.go_down, key="s")
score = ScoreBoard()

flag = True
while flag:
    screen.update()
    time.sleep(0.1)
    ball.move_ball()

    if ball.ycor() > 290 or ball.ycor() < -289:
        ball.bounce_y()

    if ball.distance(r_paddy) < 50 and ball.xcor() > 330 or ball.distance(l_paddy) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        ball.speedy()

    if ball.xcor() > 380:
        score.left_score_add()

        ball.reset_direction()

    if ball.xcor() < -380:
        score.right_score_add()
        ball.reset_direction()

screen.exitonclick()
