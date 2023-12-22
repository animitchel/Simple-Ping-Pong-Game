from turtle import Turtle


class Paddy(Turtle):
    def __init__(self, positions):
        """
        Initialize a Paddy object.

        Parameters:
        - positions: Tuple, initial (x, y) coordinates for the paddle.
        """
        super().__init__()
        self.new_pads = []  # This variable doesn't seem to be used; you might want to remove it
        self.shape("square")  # Set the shape of the paddle
        self.color("white")  # Set the color of the paddle
        self.shapesize(stretch_wid=5, stretch_len=1)  # Stretch the paddle vertically
        self.penup()  # Lift the pen to prevent drawing while moving the paddle
        self.goto(positions)  # Set the initial position of the paddle

    def go_up(self):
        """
        Move the paddle up by a fixed distance.
        """
        new_y = self.ycor() + 20  # Increase the y-coordinate to move the paddle up
        self.goto(self.xcor(), new_y)  # Move the paddle to the new position

    def go_down(self):
        """
        Move the paddle down by a fixed distance.
        """
        new_y = self.ycor() - 20  # Decrease the y-coordinate to move the paddle down
        self.goto(self.xcor(), new_y)  # Move the paddle to the new position
