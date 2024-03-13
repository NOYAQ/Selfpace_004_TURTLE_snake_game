""" 
calls Turtle class from Turtle module
creates a Score object.
"""
from turtle import Turtle
class Score(Turtle):
    """
    A Score class is the superclass of Turtle class, writes 'Score:0' initial, on top of the screen
    """
    def __init__(self) -> None:
        super().__init__()
        self.color("blue")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.high_score = self.get_high_score()
        self.goto(0,350)
        self.write(arg = f"Your score: {self.score}, High score: {self.high_score}",\
                   align="center", font=("Arial", 18, "bold"))  
    def update(self):
        """
        A function increaes the score +1 whenever it is called.
        """
        self.clear()
        self.score += 1
        self.write(arg = f"Your score: {self.score},  High score: {self.high_score}",\
                   align="center", font=("Arial", 18, "bold"))
    def gameover(self):
        """
        A function writes 'Game Over' in the middle of the screen
        """
        # compares the user score and the high score, if the score is higher than
        # the high score, changes the high score and calls the update function.
        # The update function adds 1 to the user score so before calls the function subtracts 1
        # from the user score
        if self.score > self.high_score:
            self.high_score = self.score
            self.score -= 1
            self.set_high_score()
            self.update()
        self.goto(0,0)
        self.write(arg = "GAME OVER", align="center", font=("Arial", 18, "bold"))
    def get_high_score(self):
        with open("high_score.txt", mode="r") as file:
            high_score = file.read()
            high_score = int(high_score)
        return high_score
    def set_high_score(self):
         with open("high_score.txt", mode="w") as file:
            high_score = file.write(f"{self.high_score}")
