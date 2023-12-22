from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        """
        Initialize the ScoreBoard object.

        Attributes:
        - l_score (int): Left player's score.
        - r_score (int): Right player's score.
        """
        super().__init__()
        self.color("white")  # Set the color of the score display
        self.penup()  # Lift the pen to prevent drawing while moving
        self.hideturtle()  # Hide the turtle icon
        self.l_score = 0  # Initialize left player's score
        self.r_score = 0  # Initialize right player's score
        self.update_score()  # Update the score display initially

    def update_score(self):
        """
        Update the score display on the screen.
        """
        self.clear()  # Clear previous score display
        # Display left player's score
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Times New Roman", 50, "bold"))
        # Display right player's score
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Times New Roman", 50, "bold"))

    def right_score_add(self):
        """
        Increment the right player's score and update the display.
        """
        self.r_score += 1  # Increment right player's score
        self.update_score()  # Update the score display

    def left_score_add(self):
        """
        Increment the left player's score and update the display.
        """
        self.l_score += 1  # Increment left player's score
        self.update_score()  # Update the score display
