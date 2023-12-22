from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        """
        Initialize the Ball object.

        Attributes:
        - xam (int): X-axis movement speed.
        - yam (int): Y-axis movement speed.
        """
        super().__init__()
        self.shape("circle")  # Set the shape of the ball
        self.color("white")  # Set the color of the ball
        self.penup()  # Lift the pen to prevent drawing while moving
        self.xam = 10  # Initialize X-axis movement speed
        self.yam = 10  # Initialize Y-axis movement speed

    def move_ball(self):
        """
        Move the ball based on its current speed in the X and Y directions.
        """
        new_x = self.xcor() + self.xam
        new_y = self.ycor() + self.yam
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Reverse the Y-axis movement direction when the ball hits the top or bottom.
        """
        self.yam *= -1

    def bounce_x(self):
        """
        Reverse the X-axis movement direction when the ball hits a paddle.
        """
        self.xam *= -10

    def reset_direction(self, direction):
        """
        Reset the ball's position and X-axis movement direction when it scores a point.

        Parameters:
        - direction (int): The direction to set for the X and Y-axis movement speed.

        Returns:
        None
        """
        self.goto(0, 0)  # Move the ball to the center
        self.bounce_x()  # Reverse the X-axis movement direction
        self.yam = direction  # Reset Y-axis movement speed
        self.xam = direction  # Reset X-axis movement speed

    def speedy(self):
        """
        Increase the speed of the ball in both X and Y directions.
        """
        if self.yam == 10:
            self.yam += 10
        if self.xam == 10:
            self.xam += 10
        if self.yam == -10:
            self.yam -= 10
        if self.xam == -10:
            self.xam -= 10


