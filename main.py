# Import necessary modules
from turtle import Turtle, Screen
from pad import Paddy
from Score import ScoreBoard
from Ball import Ball
import time

# Initialize screen
screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off automatic screen updates

# Create paddles and ball objects
r_paddy = Paddy((350, 0))
l_paddy = Paddy((-350, 0))
ball = Ball()

# Set up keyboard bindings
screen.listen()
screen.onkey(fun=r_paddy.go_up, key="Up")
screen.onkey(fun=r_paddy.go_down, key="Down")
screen.onkey(fun=l_paddy.go_up, key="w")
screen.onkey(fun=l_paddy.go_down, key="s")

# Create a ScoreBoard object to keep track of scores
score = ScoreBoard()

flag = True
while flag:
    screen.update()  # Update the screen manually
    time.sleep(0.1)  # Pause to control the speed of the game
    ball.move_ball()  # Move the ball in each iteration

    # Check for collisions with the top and bottom walls
    if ball.ycor() > 290 or ball.ycor() < -289:
        ball.bounce_y()

    # Check for collisions with paddles
    if (ball.distance(r_paddy) < 50 and ball.xcor() > 330) or (ball.distance(l_paddy) < 50 and ball.xcor() < -330):
        ball.bounce_x()
        ball.speedy()

    # Check if the ball has passed the right boundary
    if ball.xcor() > 380:
        score.left_score_add()
        ball.reset_direction(direction=10)

    # Check if the ball has passed the left boundary
    if ball.xcor() < -380:
        score.right_score_add()
        ball.reset_direction(direction=-10)

# Close the game window when clicked
screen.exitonclick()


