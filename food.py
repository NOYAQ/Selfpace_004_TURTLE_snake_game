""" 
calls Turtle class from turtle module
creates a Food object.
"""
from turtle import Turtle
from random import randint
class Food(Turtle):
    """
    A Food class is superclass of Turtle class
    """
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.new_food()

    def new_food(self):
        """
        A function changes coordinate of the food object randomly.
        """
        self.goto(randint(-460, 460),randint(-340, 340))
# End-Of-Line (EOL)